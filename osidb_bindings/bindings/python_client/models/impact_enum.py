from enum import Enum


class ImpactEnum(str, Enum):
    CRITICAL = "CRITICAL"
    IMPORTANT = "IMPORTANT"
    LOW = "LOW"
    MODERATE = "MODERATE"

    def __str__(self) -> str:
        return str(self.value)
