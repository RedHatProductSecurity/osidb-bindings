from enum import Enum


class OsidbApiV1FlawsReferencesListType(str, Enum):
    ARTICLE = "ARTICLE"
    EXTERNAL = "EXTERNAL"
    SOURCE = "SOURCE"

    def __str__(self) -> str:
        return str(self.value)
