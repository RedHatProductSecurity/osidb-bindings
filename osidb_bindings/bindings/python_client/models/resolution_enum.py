from enum import Enum


class ResolutionEnum(str, Enum):
    NONE = "NONE"
    FIX = "FIX"
    DEFER = "DEFER"
    WONTFIX = "WONTFIX"
    OOSS = "OOSS"
    DELEGATED = "DELEGATED"
    WONTREPORT = "WONTREPORT"

    def __str__(self) -> str:
        return str(self.value)
