from enum import Enum


class FlawClassificationState(str, Enum):
    VALUE_0 = ""
    NEW = "NEW"
    TRIAGE = "TRIAGE"
    PRE_SECONDARY_ASSESSMENT = "PRE_SECONDARY_ASSESSMENT"
    SECONDARY_ASSESSMENT = "SECONDARY_ASSESSMENT"
    DONE = "DONE"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
