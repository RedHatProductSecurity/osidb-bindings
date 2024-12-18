from enum import Enum


class AlertTypeEnum(str, Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
