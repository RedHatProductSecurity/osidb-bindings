from enum import Enum


class Type96FEnum(str, Enum):
    ALIAS = "alias"
    BU = "bu"
    CONTEXT_BASED = "context_based"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
