import importlib
import os

import httpx
from httpx_gssapi import HTTPSPNEGOAuth

from .bindings.python_client import AuthenticatedClient
from .bindings.python_client.api.auth import (
    auth_token_create,
    auth_token_refresh_create,
    auth_token_retrieve,
)
from .bindings.python_client.models import Flaw, TokenObtainPair, TokenRefresh
from .bindings.python_client.types import UNSET
from .constants import OSIDB_API_VERSION, OSIDB_BINDINGS_API_PATH, TRUSTED_CAS

# Import API modules via importlib so we can parametrize path and API version
osidb_flaws_list = importlib.import_module(
    f"{OSIDB_BINDINGS_API_PATH}.osidb_api_{OSIDB_API_VERSION}_flaws_list",
    package="osidb_bindings",
)
osidb_flaws_retrieve = importlib.import_module(
    f"{OSIDB_BINDINGS_API_PATH}.osidb_api_{OSIDB_API_VERSION}_flaws_retrieve",
    package="osidb_bindings",
)
osidb_flaws_create = importlib.import_module(
    f"{OSIDB_BINDINGS_API_PATH}.osidb_api_{OSIDB_API_VERSION}_flaws_create",
    package="osidb_bindings",
)
osidb_flaws_update = importlib.import_module(
    f"{OSIDB_BINDINGS_API_PATH}.osidb_api_{OSIDB_API_VERSION}_flaws_update",
    package="osidb_bindings",
)
osidb_status_retrieve = importlib.import_module(
    f"{OSIDB_BINDINGS_API_PATH}.osidb_api_{OSIDB_API_VERSION}_status_retrieve",
    package="osidb_bindings",
)


def new_session(
    osidb_server_uri,
    password=None,
    username=None,
    verify_ssl=None,
):
    """Create a new session for selected OSIDB URI"""

    if verify_ssl is None:

        # Use httpx/requests/cURL environment variables or set default trusted CAs
        verify_ssl = (
            os.getenv("SSL_CERT_FILE")
            or os.getenv("REQUESTS_CA_BUNDLE")
            or os.getenv("CURL_CA_BUNDLE")
            or TRUSTED_CAS
        )

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
            verify_ssl=verify_ssl,
        )

        self.refresh_token = self.__get_refresh_token()

    def __get_refresh_token(self) -> str:
        """Get resfresh token based on the auth type"""

        if isinstance(self.auth, tuple):
            response = auth_token_create.sync(
                client=self.__client,
                form_data=TokenObtainPair.from_dict(
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
                form_data=TokenRefresh.from_dict({"refresh": self.refresh_token}),
                multipart_data=UNSET,
                json_body=UNSET,
            )
        except httpx.HTTPStatusError:

            # expired refresh token, renew it and try again
            self.refresh_token = self.__get_refresh_token()
            response = auth_token_refresh_create.sync(
                client=self.__client,
                form_data=TokenRefresh.from_dict({"refresh": self.refresh_token}),
                multipart_data=UNSET,
                json_body=UNSET,
            )

        return response.access

    @property
    def __client_with_new_access_token(self) -> AuthenticatedClient:
        """Create a new client with refreshed access token"""

        return self.__client.with_headers(
            {"Authorization": f"Bearer {self.__get_access_token()}"}
        )

    def __get_sync_function(self, api_module):
        """
        Get 'sync' function from API module if available (response example is defined in schema)
        or get basic 'sync_detailed' function (response example is not defined in schema)
        """
        return getattr(api_module, "sync", getattr(api_module, "sync_detailed"))

    def status(self):
        status_fn = self.__get_sync_function(osidb_status_retrieve)
        return status_fn(client=self.__client_with_new_access_token)

    def retrieve(self, id, **kwargs):
        flaws_retrieve_fn = self.__get_sync_function(osidb_flaws_retrieve)
        return flaws_retrieve_fn(
            client=self.__client_with_new_access_token, id=id, **kwargs
        )

    def retrieve_list(self, **kwargs):
        flaws_list_retrieve_fn = self.__get_sync_function(osidb_flaws_list)
        return flaws_list_retrieve_fn(
            client=self.__client_with_new_access_token, **kwargs
        )

    def search(self, searched_text):
        flaws_list_retrieve_fn = self.__get_sync_function(osidb_flaws_list)
        return flaws_list_retrieve_fn(
            client=self.self.__client_with_new_access_token, search=searched_text
        )

    def create(self, form_data):
        flaw_data = Flaw.from_dict(form_data)

        flaws_create_fn = self.__get_sync_function(osidb_flaws_create)
        return flaws_create_fn(
            client=self.self.__client_with_new_access_token,
            form_data=flaw_data,
            json_body=UNSET,
            multipart_data=UNSET,
        )

    def update(self, id, form_data, **kwargs):
        flaw_data = Flaw.from_dict(form_data)

        flaws_update_fn = self.__get_sync_function(osidb_flaws_update)
        return flaws_update_fn(
            client=self.self.__client_with_new_access_token,
            id=id,
            form_data=flaw_data,
            json_body=UNSET,
            multipart_data=UNSET,
            **kwargs,
        )

    def delete(self):
        raise NotImplementedError("Flaw delete not implemented yet.")

    def reload_session(self):
        self.__client.reload_session()
