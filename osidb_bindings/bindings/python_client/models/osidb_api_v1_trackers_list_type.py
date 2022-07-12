from enum import Enum


class OsidbApiV1TrackersListType(str, Enum):
    BUGZILLA = "BUGZILLA"
    JIRA = "JIRA"

    def __str__(self) -> str:
        return str(self.value)
