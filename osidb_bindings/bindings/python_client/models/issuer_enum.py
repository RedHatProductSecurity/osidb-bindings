from enum import Enum


class IssuerEnum(str, Enum):
    CISA = "CISA"
    CVEORG = "CVEORG"
    NIST = "NIST"
    OSV = "OSV"
    RH = "RH"

    def __str__(self) -> str:
        return str(self.value)
