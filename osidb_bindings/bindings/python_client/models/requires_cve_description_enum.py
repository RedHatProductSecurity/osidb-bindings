from enum import Enum


class RequiresCveDescriptionEnum(str, Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    REQUESTED = "REQUESTED"

    def __str__(self) -> str:
        return str(self.value)
