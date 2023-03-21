from enum import Enum


class Resolution01FEnum(str, Enum):
    DUPLICATE = "DUPLICATE"
    WONTFIX = "WONTFIX"
    NOTABUG = "NOTABUG"
    ERRATA = "ERRATA"
    CANTFIX = "CANTFIX"
    DEFERRED = "DEFERRED"
    CURRENTRELEASE = "CURRENTRELEASE"
    UPSTREAM = "UPSTREAM"
    RAWHIDE = "RAWHIDE"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    NEXTRELEASE = "NEXTRELEASE"
    WORKSFORME = "WORKSFORME"
    EOL = "EOL"

    def __str__(self) -> str:
        return str(self.value)
