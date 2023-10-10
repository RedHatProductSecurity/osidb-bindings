from enum import Enum


class OsidbApiV1FlawsCvssScoresListIssuer(str, Enum):
    NIST = "NIST"
    RH = "RH"

    def __str__(self) -> str:
        return str(self.value)
