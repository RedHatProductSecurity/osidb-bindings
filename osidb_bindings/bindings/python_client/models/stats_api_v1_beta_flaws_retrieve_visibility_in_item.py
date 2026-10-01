from enum import Enum


class StatsApiV1BetaFlawsRetrieveVisibilityInItem(str, Enum):
    EMBARGOED = "EMBARGOED"
    INTERNAL = "INTERNAL"
    PUBLIC = "PUBLIC"

    def __str__(self) -> str:
        return str(self.value)
