from enum import Enum


class MilestoneTypeEnum(str, Enum):
    ADDITIONAL_INFORMATION_RESPONSE = "additional_information_response"
    FINAL = "final"
    VALUE_0 = "24h"
    VALUE_1 = "72h"

    def __str__(self) -> str:
        return str(self.value)
