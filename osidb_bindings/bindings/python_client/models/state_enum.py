from enum import Enum


class StateEnum(str, Enum):
    DONE = "DONE"
    NEW = "NEW"
    REQ = "REQ"
    SKIP = "SKIP"

    def __str__(self) -> str:
        return str(self.value)
