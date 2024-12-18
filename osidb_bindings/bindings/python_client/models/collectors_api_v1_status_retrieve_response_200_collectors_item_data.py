from enum import Enum


class CollectorsApiV1StatusRetrieveResponse200CollectorsItemData(str, Enum):
    COMPLETE = "COMPLETE"
    EMPTY = "EMPTY"
    PARTIAL = "PARTIAL"

    def __str__(self) -> str:
        return str(self.value)
