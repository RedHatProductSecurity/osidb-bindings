from enum import Enum


class OsidbApiV1FlawsListAffectsType(str, Enum):
    DEFAULT = "DEFAULT"

    def __str__(self) -> str:
        return str(self.value)
