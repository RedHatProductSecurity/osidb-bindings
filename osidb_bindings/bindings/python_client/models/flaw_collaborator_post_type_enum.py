from enum import Enum


class FlawCollaboratorPostTypeEnum(str, Enum):
    ALIAS = "alias"
    CONTEXT_BASED = "context_based"

    def __str__(self) -> str:
        return str(self.value)
