from enum import Enum


class OsidbApiV1TrackersListAffectsAffectedness(str, Enum):
    VALUE_0 = ""
    AFFECTED = "AFFECTED"
    NEW = "NEW"
    NOTAFFECTED = "NOTAFFECTED"

    def __str__(self) -> str:
        return str(self.value)
