from enum import Enum


class Type5B2Enum(str, Enum):
    DEFAULT = "DEFAULT"

    def __str__(self) -> str:
        return str(self.value)
