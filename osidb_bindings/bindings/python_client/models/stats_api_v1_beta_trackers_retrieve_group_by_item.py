from enum import Enum


class StatsApiV1BetaTrackersRetrieveGroupByItem(str, Enum):
    PS_PRODUCT = "ps_product"

    def __str__(self) -> str:
        return str(self.value)
