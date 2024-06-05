from enum import Enum


class AlertTypeEnum(str, Enum):
    WARNING = "WARNING"
    ERROR = "ERROR"

    def __str__(self) -> str:
        return str(self.value)
