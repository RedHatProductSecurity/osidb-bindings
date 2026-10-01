from enum import Enum


class MilestoneTypeEnum(str, Enum):
    FINAL = "final"
    VALUE_0 = "24h"
    VALUE_1 = "72h"

    def __str__(self) -> str:
        return str(self.value)
