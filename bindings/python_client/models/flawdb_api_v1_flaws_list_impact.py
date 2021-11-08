from enum import Enum


class FlawdbApiV1FlawsListImpact(str, Enum):
    CRITICAL = "CRITICAL"
    IMPORTANT = "IMPORTANT"
    LOW = "LOW"
    MODERATE = "MODERATE"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
