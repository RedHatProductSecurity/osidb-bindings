from enum import Enum


class OsidbApiV1FlawsListMitigatedBy(str, Enum):
    FORTIFY = "FORTIFY"
    SELINUX = "SELINUX"

    def __str__(self) -> str:
        return str(self.value)
