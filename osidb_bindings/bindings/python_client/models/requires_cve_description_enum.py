from enum import Enum


class RequiresCveDescriptionEnum(str, Enum):
    REQUESTED = "REQUESTED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
