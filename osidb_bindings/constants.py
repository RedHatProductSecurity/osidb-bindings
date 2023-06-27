from typing import List

OSIDB_API_VERSION: str = "v1"
OSIDB_BINDINGS_VERSION: str = "3.1.0"
OSIDB_BINDINGS_USERAGENT: str = f"osidb-bindings-{OSIDB_BINDINGS_VERSION}"
OSIDB_BINDINGS_API_PATH: str = ".bindings.python_client.api.osidb"

# all available session operations
ALL_SESSION_OPERATIONS: List[str] = (
    "retrieve",
    "update",
    "list",
    "create",
    "destroy",
    "search",
)
