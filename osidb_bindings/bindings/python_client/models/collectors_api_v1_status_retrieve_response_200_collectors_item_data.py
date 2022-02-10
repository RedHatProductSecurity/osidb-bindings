from enum import Enum


class CollectorsApiV1StatusRetrieveResponse200CollectorsItemData(str, Enum):
    EMPTY = "EMPTY"
    PARTIAL = "PARTIAL"
    COMPLETE = "COMPLETE"

    def __str__(self) -> str:
        return str(self.value)
