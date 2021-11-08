import importlib

from constants import (
    OSIDB_API_VERSION,
    OSIDB_BINDINGS_API_PATH,
    OSIDB_BINDINGS_USERAGENT,
)
from bindings.python_client import AuthenticatedClient

# TODO: Once FlawDB will be renamed to OSIDB, these paths need to be changed
osidb_flaws_list = importlib.import_module(
    f"{OSIDB_BINDINGS_API_PATH}.flawdb_api_{OSIDB_API_VERSION}_flaws_list"
)
osidb_flaws_retrieve = importlib.import_module(
    f"{OSIDB_BINDINGS_API_PATH}.flawdb_api_{OSIDB_API_VERSION}_flaws_retrieve"
)
osidb_status_retrieve = importlib.import_module(
    f"{OSIDB_BINDINGS_API_PATH}.flawdb_api_{OSIDB_API_VERSION}_status_retrieve"
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
            headers={"User-Agent": OSIDB_BINDINGS_USERAGENT, **headers},
            verify_ssl=verify_ssl,
        )

    def status(self):
        return osidb_status_retrieve.sync(client=self.__client)

    def retrieve(self, **kwargs):
        return osidb_flaws_retrieve.sync(client=self.__client, **kwargs)

    def retrieve_list(self, **kwargs):
        return osidb_flaws_list.sync(client=self.__client, **kwargs)

    def create(self):
        raise NotImplementedError("Flaw create not implemented yet.")

    def update(self):
        raise NotImplementedError("Flaw update not implemented yet")

    def delete(self):
        raise NotImplementedError("Flaw delete not implemented yet.")

    def reload_session(self):
        self.__client.reload_session()
