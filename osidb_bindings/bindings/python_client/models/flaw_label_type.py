from enum import Enum


class FlawLabelType(str, Enum):
    ALIAS = "alias"
    CONTEXT_BASED = "context_based"
    PRODUCT_FAMILY = "product_family"

    def __str__(self) -> str:
        return str(self.value)
