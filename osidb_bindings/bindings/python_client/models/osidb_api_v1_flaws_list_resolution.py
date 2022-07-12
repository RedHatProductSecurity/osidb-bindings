from enum import Enum


class OsidbApiV1FlawsListResolution(str, Enum):
    VALUE_0 = ""
    CANTFIX = "CANTFIX"
    CURRENTRELEASE = "CURRENTRELEASE"
    DEFERRED = "DEFERRED"
    DUPLICATE = "DUPLICATE"
    EOL = "EOL"
    ERRATA = "ERRATA"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    NEXTRELEASE = "NEXTRELEASE"
    NOTABUG = "NOTABUG"
    RAWHIDE = "RAWHIDE"
    UPSTREAM = "UPSTREAM"
    WONTFIX = "WONTFIX"
    WORKSFORME = "WORKSFORME"

    def __str__(self) -> str:
        return str(self.value)
