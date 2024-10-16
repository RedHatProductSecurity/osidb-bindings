from enum import Enum


class MajorIncidentStateEnum(str, Enum):
    REQUESTED = "REQUESTED"
    REJECTED = "REJECTED"
    APPROVED = "APPROVED"
    CISA_APPROVED = "CISA_APPROVED"
    MINOR = "MINOR"
    ZERO_DAY = "ZERO_DAY"
    INVALID = "INVALID"

    def __str__(self) -> str:
        return str(self.value)
