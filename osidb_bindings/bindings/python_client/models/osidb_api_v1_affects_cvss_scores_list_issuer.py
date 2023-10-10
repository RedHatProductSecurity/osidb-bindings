from enum import Enum


class OsidbApiV1AffectsCvssScoresListIssuer(str, Enum):
    NIST = "NIST"
    RH = "RH"

    def __str__(self) -> str:
        return str(self.value)
