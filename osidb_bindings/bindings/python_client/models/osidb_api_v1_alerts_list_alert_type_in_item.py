from enum import Enum


class OsidbApiV1AlertsListAlertTypeInItem(str, Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
