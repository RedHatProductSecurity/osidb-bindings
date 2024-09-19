from enum import Enum


class IssuerEnum(str, Enum):
    CVEORG = "CVEORG"
    RH = "RH"
    NIST = "NIST"
    OSV = "OSV"

    def __str__(self) -> str:
        return str(self.value)
