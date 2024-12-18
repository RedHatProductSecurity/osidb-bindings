from enum import Enum


class NistCvssValidationEnum(str, Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    REQUESTED = "REQUESTED"

    def __str__(self) -> str:
        return str(self.value)
