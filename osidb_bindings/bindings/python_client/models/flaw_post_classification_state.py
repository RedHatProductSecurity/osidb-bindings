from enum import Enum


class FlawPostClassificationState(str, Enum):
    DRAFT = "DRAFT"
    NEW = "NEW"
    ANALYSIS = "ANALYSIS"
    REVIEW = "REVIEW"
    FIX = "FIX"
    DONE = "DONE"

    def __str__(self) -> str:
        return str(self.value)
