from enum import Enum


class NistCvssValidationEnum(str, Enum):
    REQUESTED = "REQUESTED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
