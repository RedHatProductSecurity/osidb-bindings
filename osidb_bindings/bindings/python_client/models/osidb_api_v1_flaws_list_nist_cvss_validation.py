from enum import Enum


class OsidbApiV1FlawsListNistCvssValidation(str, Enum):
    VALUE_0 = ""
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    REQUESTED = "REQUESTED"

    def __str__(self) -> str:
        return str(self.value)
