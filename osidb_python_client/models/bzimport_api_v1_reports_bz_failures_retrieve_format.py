from enum import Enum


class BzimportApiV1ReportsBzFailuresRetrieveFormat(str, Enum):
    CSV = "csv"
    JSON = "json"
    XML = "xml"

    def __str__(self) -> str:
        return str(self.value)
