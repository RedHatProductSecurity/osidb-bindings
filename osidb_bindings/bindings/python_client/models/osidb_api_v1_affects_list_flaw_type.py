from enum import Enum


class OsidbApiV1AffectsListFlawType(str, Enum):
    VULNERABILITY = "VULNERABILITY"
    WEAKNESS = "WEAKNESS"

    def __str__(self) -> str:
        return str(self.value)
