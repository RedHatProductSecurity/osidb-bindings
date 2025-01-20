"""
osidb-bindings constants
"""

from typing import List

OSIDB_API_VERSION: str = "v1"
OSIDB_BINDINGS_VERSION: str = "4.6.2"
OSIDB_BINDINGS_USERAGENT: str = f"osidb-bindings-{OSIDB_BINDINGS_VERSION}"
OSIDB_BINDINGS_API_PATH: str = ".bindings.python_client.api.osidb"
OSIDB_BINDINGS_PLACEHOLDER_FIELD: str = (
    f'__placeholder_field{OSIDB_BINDINGS_VERSION.replace(".","")}'
)

DEFAULT_LIMIT: int = 50

# all available session operations
ALL_SESSION_OPERATIONS: List[str] = (
    "retrieve",
    "update",
    "list",
    "create",
    "destroy",
    "search",
)
