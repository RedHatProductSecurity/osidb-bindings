from enum import Enum


class OsidbApiV1AlertsListParentModel(str, Enum):
    AFFECT = "affect"
    AFFECTCVSS = "affectcvss"
    FLAW = "flaw"
    FLAWACKNOWLEDGMENT = "flawacknowledgment"
    FLAWCOMMENT = "flawcomment"
    FLAWCVSS = "flawcvss"
    FLAWREFERENCE = "flawreference"
    PACKAGE = "package"
    SNIPPET = "snippet"
    TRACKER = "tracker"

    def __str__(self) -> str:
        return str(self.value)
