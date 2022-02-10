from enum import Enum


class MitigatedByEnum(str, Enum):
    SELINUX = "SELINUX"
    FORTIFY = "FORTIFY"

    def __str__(self) -> str:
        return str(self.value)
