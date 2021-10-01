from enum import Enum


class MitigatedByEnum(str, Enum):
    SELINUX = "SELINUX"
    FORTIFY = "FORTIFY"
    GRSEC = "GRSEC"

    def __str__(self) -> str:
        return str(self.value)
