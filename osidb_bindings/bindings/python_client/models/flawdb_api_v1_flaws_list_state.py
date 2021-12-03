from enum import Enum


class FlawdbApiV1FlawsListState(str, Enum):
    ASSIGNED = "ASSIGNED"
    CLOSED = "CLOSED"
    DRAFT = "DRAFT"
    NEW = "NEW"
    OPEN = "OPEN"
    STUB = "STUB"
    VERIFIED = "VERIFIED"

    def __str__(self) -> str:
        return str(self.value)
