from enum import Enum


class FlawdbApiV1FlawsListMitigatedBy(str, Enum):
    FORTIFY = "FORTIFY"
    GRSEC = "GRSEC"
    SELINUX = "SELINUX"

    def __str__(self) -> str:
        return str(self.value)
