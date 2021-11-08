from enum import Enum


class OsimApiV1WorkflowsRetrieve2Format(str, Enum):
    CSV = "csv"
    JSON = "json"
    XML = "xml"

    def __str__(self) -> str:
        return str(self.value)
