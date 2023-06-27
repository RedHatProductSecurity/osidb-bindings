from enum import Enum


class FlawType(str, Enum):
    VULNERABILITY = "VULNERABILITY"
    WEAKNESS = "WEAKNESS"

    def __str__(self) -> str:
        return str(self.value)
