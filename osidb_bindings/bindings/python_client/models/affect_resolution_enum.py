from enum import Enum


class AffectResolutionEnum(str, Enum):
    FIX = "FIX"
    DEFER = "DEFER"
    WONTFIX = "WONTFIX"
    OOSS = "OOSS"
    DELEGATED = "DELEGATED"
    WONTREPORT = "WONTREPORT"

    def __str__(self) -> str:
        return str(self.value)
