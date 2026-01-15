from enum import Enum


class OsidbApiV1TrackersListAffectsFlawVisibility(str, Enum):
    EMBARGOED = "EMBARGOED"
    INTERNAL = "INTERNAL"
    PUBLIC = "PUBLIC"

    def __str__(self) -> str:
        return str(self.value)
