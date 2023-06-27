from enum import Enum


class TrackerType(str, Enum):
    JIRA = "JIRA"
    BUGZILLA = "BUGZILLA"

    def __str__(self) -> str:
        return str(self.value)
