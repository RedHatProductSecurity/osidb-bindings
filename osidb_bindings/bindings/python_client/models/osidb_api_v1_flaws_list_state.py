from enum import Enum


class OsidbApiV1FlawsListState(str, Enum):
    ASSIGNED = "ASSIGNED"
    CLOSED = "CLOSED"
    MODIFIED = "MODIFIED"
    NEW = "NEW"
    ON_QA = "ON_QA"
    POST = "POST"
    RELEASE_PENDING = "RELEASE_PENDING"
    VERIFIED = "VERIFIED"

    def __str__(self) -> str:
        return str(self.value)
