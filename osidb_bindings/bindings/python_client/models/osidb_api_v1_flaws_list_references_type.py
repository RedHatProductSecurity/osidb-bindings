from enum import Enum


class OsidbApiV1FlawsListReferencesType(str, Enum):
    ARTICLE = "ARTICLE"
    EXTERNAL = "EXTERNAL"
    SOURCE = "SOURCE"
    UPSTREAM = "UPSTREAM"

    def __str__(self) -> str:
        return str(self.value)
