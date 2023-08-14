from enum import Enum


class OsidbApiV1FlawsListMajorIncidentState(str, Enum):
    VALUE_0 = ""
    APPROVED = "APPROVED"
    CISA_APPROVED = "CISA_APPROVED"
    INVALID = "INVALID"
    REJECTED = "REJECTED"
    REQUESTED = "REQUESTED"

    def __str__(self) -> str:
        return str(self.value)
