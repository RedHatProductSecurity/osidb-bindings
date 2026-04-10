"""
osidb-bindings constants
"""

from requests.utils import default_user_agent

OSIDB_BINDINGS_VERSION: str = "5.8.1"
OSIDB_BINDINGS_USERAGENT: str = (
    f"osidb-bindings/{OSIDB_BINDINGS_VERSION} ({default_user_agent()})"
)

# Placeholder keyword that gets replaced with the osidb-bindings identity in custom user-agent strings
USERAGENT_PLACEHOLDER: str = "{bindings-user-agent}"
OSIDB_BINDINGS_API_PATH: str = ".bindings.python_client.api"
OSIDB_BINDINGS_PLACEHOLDER_FIELD: str = (
    f'__placeholder_field{OSIDB_BINDINGS_VERSION.replace(".","")}'
)

DEFAULT_LIMIT: int = 50

# all available session operations
ALL_SESSION_OPERATIONS: list[str] = [
    "retrieve",
    "update",
    "list",
    "create",
    "destroy",
    "search",
]
