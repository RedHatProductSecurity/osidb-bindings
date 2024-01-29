from enum import Enum


class FlawReferenceType(str, Enum):
    ARTICLE = "ARTICLE"
    EXTERNAL = "EXTERNAL"
    SOURCE = "SOURCE"

    def __str__(self) -> str:
        return str(self.value)
