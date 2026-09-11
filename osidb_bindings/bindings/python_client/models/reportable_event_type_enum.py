from enum import Enum


class ReportableEventTypeEnum(str, Enum):
    EXPLOITS_KEV_APPROVED = "EXPLOITS_KEV_APPROVED"
    MAJOR_INCIDENT_APPROVED = "MAJOR_INCIDENT_APPROVED"

    def __str__(self) -> str:
        return str(self.value)
