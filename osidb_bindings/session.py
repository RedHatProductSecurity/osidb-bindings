"""
osidb-bindings session
"""

import asyncio
import importlib
from types import ModuleType
from typing import Any, Callable, Dict, List, Optional

import aiohttp
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
    DEFAULT_LIMIT,
    OSIDB_API_VERSION,
    OSIDB_BINDINGS_API_PATH,
    OSIDB_BINDINGS_PLACEHOLDER_FIELD,
    OSIDB_BINDINGS_USERAGENT,
)
from .exceptions import OperationUnsupported, UndefinedRequestBody
from .helpers import get_env
from .iterators import Paginator

osidb_status_retrieve = importlib.import_module(
    f"{OSIDB_BINDINGS_API_PATH}.osidb_api_{OSIDB_API_VERSION}_status_retrieve",
    package="osidb_bindings",
)

MAX_CONCURRENCY = get_env(
    "COMPONENT_REGISTRY_BINDINGS_MAX_CONCURRENCY", "10", is_int=True
)


def double_underscores_to_single_underscores(fn):
    """
    Function decorator which changes all the keyword arguments which include
    double underscore to use single underscore instead.

    eg. affect__affectedness -> affect_affectedness

    This change is needed because in OpenAPI schema query parameters might contain
    double underscore, howerver OpenAPI Python Client package converts all these
    double underscores into single ones and thus this creates a confusion as user
    tries to use query parameter from the OpenAPI schema specification unaware of
    the underscore change.
    """

    def inner(*args, **kwargs):
        new_kwargs = {name.replace("__", "_"): value for name, value in kwargs.items()}
        return fn(*args, **new_kwargs)

    return inner


def get_sync_function(api_module: ModuleType) -> Callable:
    """
    Get 'sync' function from API module if available (response example is defined in schema)
    or get basic 'sync_detailed' function (response example is not defined in schema)
    """
    return double_underscores_to_single_underscores(
        getattr(api_module, "sync", getattr(api_module, "sync_detailed"))
    )


def get_async_function(api_module: ModuleType) -> Callable:
    """
    Get 'sync' function from API module if available (response example is defined in schema)
    or get basic 'sync_detailed' function (response example is not defined in schema)
    """
    return double_underscores_to_single_underscores(
        getattr(api_module, "async_", getattr(api_module, "async_detailed"))
    )


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

    return Session(
        base_url=osidb_server_uri.strip("/"), auth=auth, verify_ssl=verify_ssl
    )


class Session:
    """Simple session wrapper which encapsulates the client"""

    def __init__(self, base_url, auth=None, verify_ssl=True):

        # Store auth for the refresh token acquirement
        self.auth = auth

        self.__client = AuthenticatedClient(
            base_url=base_url,
            headers={
                "User-Agent": OSIDB_BINDINGS_USERAGENT,
                "Bugzilla-Api-Key": get_env("BUGZILLA_API_KEY", ""),
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
            subresources={
                "comments": {"allowed_operations": ["retrieve", "list", "create"]},
                "references": {
                    "allowed_operations": [
                        "retrieve",
                        "update",
                        "list",
                        "create",
                        "destroy",
                    ]
                },
                "acknowledgments": {
                    "allowed_operations": [
                        "retrieve",
                        "update",
                        "list",
                        "create",
                        "destroy",
                    ]
                },
                "cvss_scores": {
                    "allowed_operations": [
                        "retrieve",
                        "update",
                        "list",
                        "create",
                        "destroy",
                    ]
                },
                "package_versions": {
                    "allowed_operations": [
                        "retrieve",
                        "update",
                        "list",
                        "create",
                        "destroy",
                    ]
                },
            },
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
            subresources={
                "cvss_scores": {
                    "allowed_operations": [
                        "retrieve",
                        "update",
                        "list",
                        "create",
                        "destroy",
                    ]
                },
            },
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
        subresources: Dict[str, dict] = None,
    ):
        self.client = client
        self.resource_name = resource_name
        self.allowed_operations = allowed_operations

        if subresources is None:
            subresources = {}

        # Create a session operation group for each subresource with respective
        # allowed session operations
        for subresource_name, subresource_metadata in subresources.items():
            setattr(
                self,
                subresource_name,
                SessionOperationsGroup(
                    client,
                    resource_name=f"{resource_name}_{subresource_name}",
                    **subresource_metadata,
                ),
            )

    def __raise_operation_unsupported(self, operation_name: str):
        """Operation unsupported exception shortcut"""

        raise OperationUnsupported(
            f'Operation "{operation_name}" is not supported for the '
            f'"{self.resource_name}" resource.'
        )

    def __raise_undefined_request_body(self, operation_name: str):
        """Undefined request body shortcut"""

        raise UndefinedRequestBody(
            f'The request body for the resource "{self.resource_name}" '
            f'and the operation "{operation_name}" is not defined.'
        )

    def __get_method_module(self, resource_name: str, method: str) -> ModuleType:
        # import endpoint module based on a method
        return importlib.import_module(
            f"{OSIDB_BINDINGS_API_PATH}.osidb_api_{OSIDB_API_VERSION}_{resource_name}_{method}",
            package="osidb_bindings",
        )

    # CRUD operations

    def retrieve(self, id, *args, **kwargs):
        if "retrieve" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="retrieve"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(id, *args, client=self.client(), **kwargs)
        else:
            self.__raise_operation_unsupported("retrieve")

    def retrieve_list(self, *args, **kwargs):
        if "list" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="list"
            )
            sync_fn = get_sync_function(method_module)
            response = sync_fn(*args, client=self.client(), **kwargs)
            return Paginator.make_response_iterable(
                response, self.retrieve_list, *args, **kwargs
            )
        else:
            self.__raise_operation_unsupported("retrieve_list")

    def create(self, form_data: Dict[str, Any], *args, **kwargs):
        if "create" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="create"
            )
            model = getattr(method_module, "REQUEST_BODY_TYPE", None)
            if model is None:
                self.__raise_undefined_request_body("create")

            transformed_data = model.from_dict(form_data)
            sync_fn = get_sync_function(method_module)
            return sync_fn(
                *args,
                client=self.client(),
                form_data=transformed_data,
                multipart_data=UNSET,
                json_body=UNSET,
                **kwargs,
            )
        else:
            self.__raise_operation_unsupported("create")

    def update(self, id, form_data: Dict[str, Any], *args, **kwargs):
        if "update" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="update"
            )
            model = getattr(method_module, "REQUEST_BODY_TYPE", None)
            if model is None:
                self.__raise_undefined_request_body("update")

            transformed_data = model.from_dict(form_data)
            sync_fn = get_sync_function(method_module)
            return sync_fn(
                id,
                *args,
                client=self.client(),
                form_data=transformed_data,
                multipart_data=UNSET,
                json_body=UNSET,
                **kwargs,
            )
        else:
            self.__raise_operation_unsupported("update")

    def delete(self, id, *args, **kwargs):
        if "destroy" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="destroy"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(
                id,
                *args,
                client=self.client(),
                **kwargs,
            )
        else:
            self.__raise_operation_unsupported("delete")

    # Extra operations

    def count(self, *args, **kwargs):
        if "list" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="list"
            )
            sync_fn = get_sync_function(method_module)
            kwargs.pop("offset", None)
            kwargs["limit"] = 1
            kwargs["include_fields"] = OSIDB_BINDINGS_PLACEHOLDER_FIELD

            response = sync_fn(*args, client=self.client(), **kwargs)
            return response.count
        else:
            self.__raise_operation_unsupported("retrieve_list")

    def search(self, searched_text: str):
        if "search" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="list"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(client=self.client(), search=searched_text)
        else:
            self.__raise_operation_unsupported("search")

    def retrieve_list_iterator(self, *args, **kwargs):
        if "list" in self.allowed_operations:
            paginator = Paginator(
                *args,
                retrieve_list_fn=self.retrieve_list,
                **kwargs,
            )

            for page in paginator:
                for resource in page.results:
                    yield resource
        else:
            self.__raise_operation_unsupported("retrieve_list")

    def retrieve_list_iterator_async(
        self, *args, max_results: Optional[int] = None, **kwargs
    ):
        if "list" in self.allowed_operations:
            for page in asyncio.run(
                self.__retrieve_list_async(*args, max_results=max_results, **kwargs)
            ):
                for resource in page.results:
                    yield resource
        else:
            self.__raise_operation_unsupported("retrieve_list")

    async def __retrieve_list_async(
        self, *args, max_results: Optional[int] = None, **kwargs
    ):
        if "list" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="list"
            )
            async_fn = get_async_function(method_module)

            kwargs.pop("offset", None)
            limit = kwargs.pop("limit", None) or DEFAULT_LIMIT

            results = []
            connector = aiohttp.TCPConnector(limit=MAX_CONCURRENCY)
            async with aiohttp.ClientSession(connector=connector) as async_session:
                client = self.client().with_async_session(async_session)

                # await first response page
                first_response = await async_fn(
                    *args, limit=limit, client=client, **kwargs
                )
                results.append(first_response)

                # no additional pages
                if first_response.next_ is None:
                    return results

                results_count = (
                    min(max_results, first_response.count)
                    if max_results is not None
                    else first_response.count
                )

                # retrieve rest of the pages
                tasks = [
                    async_fn(*args, limit=limit, offset=offset, client=client, **kwargs)
                    for offset in range(limit, results_count, limit)
                ]
                results.extend(await asyncio.gather(*tasks))

            return results
        else:
            self.__raise_operation_unsupported("retrieve_list")
