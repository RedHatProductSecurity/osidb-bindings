from enum import Enum


class AffectTypeEnum(str, Enum):
    DEFAULT = "DEFAULT"

    def __str__(self) -> str:
        return str(self.value)
