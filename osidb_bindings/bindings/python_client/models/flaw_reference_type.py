from enum import Enum


class FlawReferenceType(str, Enum):
    ARTICLE = "ARTICLE"
    EXTERNAL = "EXTERNAL"
    SOURCE = "SOURCE"
    UPSTREAM = "UPSTREAM"

    def __str__(self) -> str:
        return str(self.value)
