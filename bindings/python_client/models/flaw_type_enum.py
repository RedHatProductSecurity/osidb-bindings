from enum import Enum


class FlawTypeEnum(str, Enum):
    VULNERABILITY = "VULNERABILITY"
    WEAKNESS = "WEAKNESS"

    def __str__(self) -> str:
        return str(self.value)
