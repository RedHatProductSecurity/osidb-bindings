import importlib

from .bindings.python_client import AuthenticatedClient
from .bindings.python_client.models import Flaw
from .bindings.python_client.types import UNSET
from .constants import OSIDB_API_VERSION, OSIDB_BINDINGS_API_PATH

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
    osidb_server_uri, password=None, username=None, token=None, verify_ssl=True
):
    """Create a new session for selected OSIDB URI"""

    auth = None
    headers = {}

    if username and password:
        auth = (username, password)
    elif token:
        headers["Authorization"] = f"Token {token}"
    else:
        raise NotImplementedError("Kerberos authentication not implemented yet.")

    return Session(
        base_url=osidb_server_uri, auth=auth, headers=headers, verify_ssl=verify_ssl
    )


class Session:
    """Simple session wrapper which encapsulates the client"""

    def __init__(self, base_url, auth=None, headers=None, verify_ssl=None):

        if not headers:
            headers = {}

        self.__client = AuthenticatedClient(
            base_url=base_url,
            auth=auth,
            headers=headers,
            verify_ssl=verify_ssl,
        )

    def __get_sync_function(self, api_module):
        """
        Get 'sync' function from API module if available (response example is defined in schema)
        or get basic 'sync_detailed' function (response example is not defined in schema)
        """
        return getattr(api_module, "sync", getattr(api_module, "sync_detailed"))

    def status(self):
        status_fn = self.__get_sync_function(osidb_status_retrieve)
        return status_fn(client=self.__client)

    def retrieve(self, id, **kwargs):
        flaws_retrieve_fn = self.__get_sync_function(osidb_flaws_retrieve)
        return flaws_retrieve_fn(client=self.__client, id=id, **kwargs)

    def retrieve_list(self, **kwargs):
        flaws_list_retrieve_fn = self.__get_sync_function(osidb_flaws_list)
        return flaws_list_retrieve_fn(client=self.__client, **kwargs)

    def search(self, searched_text):
        flaws_list_retrieve_fn = self.__get_sync_function(osidb_flaws_list)
        return flaws_list_retrieve_fn(client=self.__client, search=searched_text)

    def create(self, form_data):
        flaw_data = Flaw.from_dict(form_data)

        flaws_create_fn = self.__get_sync_function(osidb_flaws_create)
        return flaws_create_fn(
            client=self.__client,
            form_data=flaw_data,
            json_body=UNSET,
            multipart_data=UNSET,
        )

    def update(self, id, form_data, **kwargs):
        flaw_data = Flaw.from_dict(form_data)

        flaws_update_fn = self.__get_sync_function(osidb_flaws_update)
        return flaws_update_fn(
            client=self.__client,
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
