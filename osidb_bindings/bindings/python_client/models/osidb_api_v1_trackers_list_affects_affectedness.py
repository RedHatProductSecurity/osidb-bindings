from enum import Enum


class OsidbApiV1TrackersListAffectsAffectedness(str, Enum):
    AFFECTED = "AFFECTED"
    NEW = "NEW"
    NOTAFFECTED = "NOTAFFECTED"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
