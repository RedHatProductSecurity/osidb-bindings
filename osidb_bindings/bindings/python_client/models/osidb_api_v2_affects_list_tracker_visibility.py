from enum import Enum


class OsidbApiV2AffectsListTrackerVisibility(str, Enum):
    EMBARGOED = "EMBARGOED"
    INTERNAL = "INTERNAL"
    PUBLIC = "PUBLIC"

    def __str__(self) -> str:
        return str(self.value)
