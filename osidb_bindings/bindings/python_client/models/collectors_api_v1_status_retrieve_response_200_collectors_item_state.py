from enum import Enum


class CollectorsApiV1StatusRetrieveResponse200CollectorsItemState(str, Enum):
    PENDING = "PENDING"
    BLOCKED = "BLOCKED"
    READY = "READY"
    RUNNING = "RUNNING"

    def __str__(self) -> str:
        return str(self.value)
