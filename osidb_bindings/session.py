import importlib
import os
import re
from functools import partial
from types import ModuleType
from typing import Any, Callable, Dict, List

import requests
from requests_gssapi import HTTPSPNEGOAuth

from .bindings.python_client import AuthenticatedClient, models
from .bindings.python_client.api.auth import (
    auth_token_create,
    auth_token_refresh_create,
    auth_token_retrieve,
)
from .bindings.python_client.types import UNSET
from .constants import (
    ALL_SESSION_OPERATIONS,
    OSIDB_API_VERSION,
    OSIDB_BINDINGS_API_PATH,
    OSIDB_BINDINGS_USERAGENT,
    RESOURCE_TO_MODEL_MAPPING,
)

osidb_status_retrieve = importlib.import_module(
    f"{OSIDB_BINDINGS_API_PATH}.osidb_api_{OSIDB_API_VERSION}_status_retrieve",
    package="osidb_bindings",
)


class OperationUnsupported(Exception):
    """Session operation is unsupported exception"""


def get_sync_function(api_module: ModuleType) -> Callable:
    """
    Get 'sync' function from API module if available (response example is defined in schema)
    or get basic 'sync_detailed' function (response example is not defined in schema)
    """
    return getattr(api_module, "sync", getattr(api_module, "sync_detailed"))


def new_session(
    osidb_server_uri,
    password=None,
    username=None,
    verify_ssl=True,
):
    """Create a new session for selected OSIDB URI"""

    if username and password:

        # OSIDB instances with the username/password auth for token acquirement
        auth = (username, password)
    else:

        # OSIDB instances with the kerberos auth for token acquirement
        auth = "kerberos"

    return Session(base_url=osidb_server_uri, auth=auth, verify_ssl=verify_ssl)


class Session:
    """Simple session wrapper which encapsulates the client"""

    def __init__(self, base_url, auth=None, verify_ssl=True):

        # Store auth for the refresh token acquirement
        self.auth = auth

        self.__client = AuthenticatedClient(
            base_url=base_url,
            headers={
                "User-Agent": OSIDB_BINDINGS_USERAGENT,
                "Bugzilla-Api-Key": os.getenv("BUGZILLA_API_KEY"),
            },
            verify_ssl=verify_ssl,
        )

        self.flaws = SessionOperationsGroup(
            self.__get_client_with_new_access_token,
            "flaws",
            allowed_operations=(
                "retrieve",
                "update",
                "list",
                "create",
                "search",
            ),
        )
        self.affects = SessionOperationsGroup(
            self.__get_client_with_new_access_token,
            "affects",
            allowed_operations=(
                "retrieve",
                "update",
                "list",
                "create",
                "destroy",
            ),
        )
        self.trackers = SessionOperationsGroup(
            self.__get_client_with_new_access_token,
            "trackers",
            allowed_operations=(
                "retrieve",
                "list",
            ),
        )

        self.refresh_token = self.__get_refresh_token()

    def status(self):
        status_fn = get_sync_function(osidb_status_retrieve)
        return status_fn(client=self.__get_client_with_new_access_token())

    def __get_refresh_token(self) -> str:
        """Get resfresh token based on the auth type"""

        if isinstance(self.auth, tuple):
            response = auth_token_create.sync(
                client=self.__client,
                form_data=models.TokenObtainPair.from_dict(
                    {"username": self.auth[0], "password": self.auth[1]}
                ),
                multipart_data=UNSET,
                json_body=UNSET,
            )
        else:
            response = auth_token_retrieve.sync(
                client=self.__client.with_auth(HTTPSPNEGOAuth())
            )
        return response.refresh

    def __get_access_token(self) -> str:
        """Get new access token using the refresh token"""

        try:
            response = auth_token_refresh_create.sync(
                client=self.__client,
                form_data=models.TokenRefresh.from_dict(
                    {"refresh": self.refresh_token}
                ),
                multipart_data=UNSET,
                json_body=UNSET,
            )
        except requests.HTTPError:

            # expired refresh token, renew it and try again
            self.refresh_token = self.__get_refresh_token()
            response = auth_token_refresh_create.sync(
                client=self.__client,
                form_data=models.TokenRefresh.from_dict(
                    {"refresh": self.refresh_token}
                ),
                multipart_data=UNSET,
                json_body=UNSET,
            )

        return response.access

    def __get_client_with_new_access_token(self) -> AuthenticatedClient:
        """Create a new client with refreshed access token"""

        return self.__client.with_headers(
            {"Authorization": f"Bearer {self.__get_access_token()}"}
        )


class SessionOperationsGroup:
    """
    Group of the CRUD and extra operations for one specific resource
    """

    def __init__(
        self,
        client: Callable,
        resource_name: str,
        allowed_operations: List[str] = ALL_SESSION_OPERATIONS,
    ):
        self.client = client
        self.resource_name = resource_name
        self.allowed_operations = allowed_operations

    @property
    def model_name(self) -> str:
        if self.resource_name in RESOURCE_TO_MODEL_MAPPING:
            # from mapping
            return RESOURCE_TO_MODEL_MAPPING[self.resource_name]
        else:
            # parse it from the resource name
            name_components = self.resource_name.split("_")
            name_components[-1] = name_components[-1][:-1]
            return "".join(name_component.title() for name_component in name_components)

    @property
    def model(self):
        return getattr(models, self.model_name)

    def __get_method_module(self, resource_name: str, method: str) -> ModuleType:
        # import endpoint module based on a method
        return importlib.import_module(
            f"{OSIDB_BINDINGS_API_PATH}.osidb_api_{OSIDB_API_VERSION}_{resource_name}_{method}",
            package="osidb_bindings",
        )

    def __make_iterable(self, response, **kwargs):
        """
        Populate next, prev and iterator helper methods for paginated responses
        """

        response.iterator = Paginator(
            session_operation=self.retrieve_list, init_response=response
        )

        for param_name, func_name in (("next_", "next"), ("previous", "prev")):
            kwargs.pop("limit", None)
            kwargs.pop("offset", None)
            param = getattr(response, param_name, None)
            if param is None:
                setattr(response, func_name, lambda: None)
            else:
                limit = re.search("limit=(\d+)", param)
                if limit is not None:
                    kwargs["limit"] = limit.group(1)
                offset = re.search("offset=(\d+)", param)
                if offset is not None:
                    kwargs["offset"] = offset.group(1)

                setattr(response, func_name, partial(self.retrieve_list, **kwargs))

        return response

    # CRUD operations

    def retrieve(self, id, **kwargs):
        if "retrieve" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="retrieve"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(id, client=self.client(), **kwargs)
        else:
            raise OperationUnsupported(
                'Operation "update" is not supported for the '
                f'"{self.resource_name}" resource.'
            )

    def retrieve_list(self, **kwargs):
        if "list" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="list"
            )
            sync_fn = get_sync_function(method_module)
            return self.__make_iterable(
                sync_fn(client=self.client(), **kwargs), **kwargs
            )
        else:
            raise OperationUnsupported(
                'Operation "update" is not supported for the '
                f'"{self.resource_name}" resource.'
            )

    def create(self, form_data: Dict[str, Any]):
        if "create" in self.allowed_operations:
            model = getattr(models, self.model_name)
            transformed_data = model.from_dict(form_data)

            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="create"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(
                client=self.client(),
                form_data=transformed_data,
                multipart_data=UNSET,
                json_body=UNSET,
            )
        else:
            raise OperationUnsupported(
                'Operation "update" is not supported for the '
                f'"{self.resource_name}" resource.'
            )

    def update(self, id, form_data: Dict[str, Any]):
        if "update" in self.allowed_operations:
            transformed_data = self.model.from_dict(form_data)

            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="update"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(
                id,
                client=self.client(),
                form_data=transformed_data,
                multipart_data=UNSET,
                json_body=UNSET,
            )
        else:
            raise OperationUnsupported(
                'Operation "update" is not supported for the '
                f'"{self.resource_name}" resource.'
            )

    def delete(self, id):
        if "destroy" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="destroy"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(
                id,
                client=self.client(),
            )
        else:
            raise OperationUnsupported(
                'Operation "delete" is not supported for the '
                f'"{self.resource_name}" resource.'
            )

    # Extra operations

    def search(self, searched_text: str):
        if "search" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="list"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(client=self.client(), search=searched_text)
        else:
            raise OperationUnsupported(
                'Operation "search" is not supported for the '
                f'"{self.resource_name}" resource.'
            )


class Paginator:
    """
    Iterable for handling API pagination.

    Receives either starting limit and offset or already existing response from which
    it should continue.

    It keeps calling `.next()` response until pages are exhausted.
    """

    def __init__(
        self,
        session_operation: Callable,
        limit: int = 100,
        offset: int = 0,
        init_response=None,
        **kwargs,
    ):
        self.session_operation = session_operation
        self.__init_limit = limit
        self.__init_offset = offset
        self.__init_response = init_response
        self.current_response = init_response
        self.kwargs = kwargs

    def __iter__(self):
        self.current_response = self.__init_response
        return self

    def __next__(self):
        if self.current_response is None:
            response = self.session_operation(
                limit=self.__init_limit, offset=self.__init_offset, **self.kwargs
            )
            self.current_response = response
            return response
        else:
            response = self.current_response.next()
            if response is not None:
                self.current_response = response
                return response
            else:
                raise StopIteration
