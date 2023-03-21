from enum import Enum


class Type0D0Enum(str, Enum):
    JIRA = "JIRA"
    BUGZILLA = "BUGZILLA"

    def __str__(self) -> str:
        return str(self.value)
