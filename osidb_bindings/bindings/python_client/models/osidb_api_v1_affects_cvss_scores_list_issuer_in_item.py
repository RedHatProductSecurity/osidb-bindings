from enum import Enum


class OsidbApiV1AffectsCvssScoresListIssuerInItem(str, Enum):
    CISA = "CISA"
    CVEORG = "CVEORG"
    NIST = "NIST"
    OSV = "OSV"
    RH = "RH"

    def __str__(self) -> str:
        return str(self.value)
