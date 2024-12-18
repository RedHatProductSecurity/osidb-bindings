from enum import Enum


class OsidbApiV1FlawsListAffectsImpact(str, Enum):
    CRITICAL = "CRITICAL"
    IMPORTANT = "IMPORTANT"
    LOW = "LOW"
    MODERATE = "MODERATE"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
