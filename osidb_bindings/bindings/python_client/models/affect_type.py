from enum import Enum


class AffectType(str, Enum):
    DEFAULT = "DEFAULT"

    def __str__(self) -> str:
        return str(self.value)
