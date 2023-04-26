from enum import Enum


class OsidbApiV1FlawsListAffectsResolution(str, Enum):
    VALUE_0 = ""
    DEFER = "DEFER"
    DELEGATED = "DELEGATED"
    FIX = "FIX"
    OOSS = "OOSS"
    WONTFIX = "WONTFIX"
    WONTREPORT = "WONTREPORT"

    def __str__(self) -> str:
        return str(self.value)
