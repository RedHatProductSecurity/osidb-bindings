from enum import Enum


class KindEnum(str, Enum):
    EXPLOITS_KEV_REQUESTED = "EXPLOITS_KEV_REQUESTED"
    MAJOR_INCIDENT_REQUESTED = "MAJOR_INCIDENT_REQUESTED"
    MINOR_INCIDENT_REQUESTED = "MINOR_INCIDENT_REQUESTED"

    def __str__(self) -> str:
        return str(self.value)
