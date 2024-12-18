from enum import Enum


class ResolutionEnum(str, Enum):
    DEFER = "DEFER"
    DELEGATED = "DELEGATED"
    FIX = "FIX"
    OOSS = "OOSS"
    WONTFIX = "WONTFIX"
    WONTREPORT = "WONTREPORT"

    def __str__(self) -> str:
        return str(self.value)
