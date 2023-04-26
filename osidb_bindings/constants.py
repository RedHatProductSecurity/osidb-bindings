from typing import Dict, List

OSIDB_API_VERSION: str = "v1"
OSIDB_BINDINGS_USERAGENT: str = "osidb-bindings-3.1.0"
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

# mapping for resources which model names are different from the endpoint name
RESOURCE_TO_MODEL_MAPPING: Dict[str, str] = {}
