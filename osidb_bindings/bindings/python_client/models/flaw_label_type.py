from enum import Enum


class FlawLabelType(str, Enum):
    ALIAS = "alias"
    BU = "bu"
    CONTEXT_BASED = "context_based"
    PRODUCT_FAMILY = "product_family"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
