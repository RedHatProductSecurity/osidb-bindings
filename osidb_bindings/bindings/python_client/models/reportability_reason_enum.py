from enum import Enum


class ReportabilityReasonEnum(str, Enum):
    JOINTLY_IDENTIFIED = "jointly_identified"
    MANUAL_OVERRIDE = "manual_override"
    RED_HAT_IDENTIFIED = "red_hat_identified"

    def __str__(self) -> str:
        return str(self.value)
