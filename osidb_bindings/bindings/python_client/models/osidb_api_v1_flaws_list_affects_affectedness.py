from enum import Enum


class OsidbApiV1FlawsListAffectsAffectedness(str, Enum):
    VALUE_0 = ""
    AFFECTED = "AFFECTED"
    NEW = "NEW"
    NOTAFFECTED = "NOTAFFECTED"

    def __str__(self) -> str:
        return str(self.value)
