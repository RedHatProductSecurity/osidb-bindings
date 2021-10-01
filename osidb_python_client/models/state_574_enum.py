from enum import Enum


class State574Enum(str, Enum):
    STUB = "STUB"
    DRAFT = "DRAFT"
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    VERIFIED = "VERIFIED"

    def __str__(self) -> str:
        return str(self.value)
