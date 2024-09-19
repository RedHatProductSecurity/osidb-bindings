from enum import Enum


class OsidbApiV1FlawsCvssScoresListIssuer(str, Enum):
    CVEORG = "CVEORG"
    NIST = "NIST"
    OSV = "OSV"
    RH = "RH"

    def __str__(self) -> str:
        return str(self.value)
