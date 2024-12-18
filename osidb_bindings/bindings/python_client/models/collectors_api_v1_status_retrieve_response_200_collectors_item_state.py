from enum import Enum


class CollectorsApiV1StatusRetrieveResponse200CollectorsItemState(str, Enum):
    BLOCKED = "BLOCKED"
    PENDING = "PENDING"
    READY = "READY"
    RUNNING = "RUNNING"

    def __str__(self) -> str:
        return str(self.value)
