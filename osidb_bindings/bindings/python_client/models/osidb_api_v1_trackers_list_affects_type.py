from enum import Enum


class OsidbApiV1TrackersListAffectsType(str, Enum):
    DEFAULT = "DEFAULT"

    def __str__(self) -> str:
        return str(self.value)
