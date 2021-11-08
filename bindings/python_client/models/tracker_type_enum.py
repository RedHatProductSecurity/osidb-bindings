from enum import Enum


class TrackerTypeEnum(str, Enum):
    JIRA = "JIRA"
    BUGZILLA = "BUGZILLA"

    def __str__(self) -> str:
        return str(self.value)
