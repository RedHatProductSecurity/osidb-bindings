from enum import Enum


class ResponsibilityScopeEnum(str, Enum):
    MANUFACTURER = "manufacturer"
    STEWARD = "steward"

    def __str__(self) -> str:
        return str(self.value)
