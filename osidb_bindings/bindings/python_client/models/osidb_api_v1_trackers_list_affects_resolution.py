from enum import Enum


class OsidbApiV1TrackersListAffectsResolution(str, Enum):
    DEFER = "DEFER"
    DELEGATED = "DELEGATED"
    FIX = "FIX"
    OOSS = "OOSS"
    VALUE_0 = ""
    WONTFIX = "WONTFIX"
    WONTREPORT = "WONTREPORT"

    def __str__(self) -> str:
        return str(self.value)
