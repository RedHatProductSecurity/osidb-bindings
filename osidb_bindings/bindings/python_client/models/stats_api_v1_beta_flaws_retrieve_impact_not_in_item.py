from enum import Enum


class StatsApiV1BetaFlawsRetrieveImpactNotInItem(str, Enum):
    CRITICAL = "CRITICAL"
    IMPORTANT = "IMPORTANT"
    LOW = "LOW"
    MODERATE = "MODERATE"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
