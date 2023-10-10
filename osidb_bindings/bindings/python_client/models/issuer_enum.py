from enum import Enum


class IssuerEnum(str, Enum):
    RH = "RH"
    NIST = "NIST"

    def __str__(self) -> str:
        return str(self.value)
