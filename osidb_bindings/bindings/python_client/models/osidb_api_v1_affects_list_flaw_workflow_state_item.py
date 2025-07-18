from enum import Enum


class OsidbApiV1AffectsListFlawWorkflowStateItem(str, Enum):
    DONE = "DONE"
    NEW = "NEW"
    PRE_SECONDARY_ASSESSMENT = "PRE_SECONDARY_ASSESSMENT"
    REJECTED = "REJECTED"
    SECONDARY_ASSESSMENT = "SECONDARY_ASSESSMENT"
    TRIAGE = "TRIAGE"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
