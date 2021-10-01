from enum import Enum


class Type824Enum(str, Enum):
    VULNERABILITY = "VULNERABILITY"
    WEAKNESS = "WEAKNESS"

    def __str__(self) -> str:
        return str(self.value)
