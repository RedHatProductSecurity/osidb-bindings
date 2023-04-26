from enum import Enum


class OsidbApiV1AffectsListFlawImpact(str, Enum):
    VALUE_0 = ""
    CRITICAL = "CRITICAL"
    IMPORTANT = "IMPORTANT"
    LOW = "LOW"
    MODERATE = "MODERATE"

    def __str__(self) -> str:
        return str(self.value)
