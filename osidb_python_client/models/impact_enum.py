from enum import Enum


class ImpactEnum(str, Enum):
    NONE = "NONE"
    LOW = "LOW"
    MODERATE = "MODERATE"
    IMPORTANT = "IMPORTANT"
    CRITICAL = "CRITICAL"

    def __str__(self) -> str:
        return str(self.value)
