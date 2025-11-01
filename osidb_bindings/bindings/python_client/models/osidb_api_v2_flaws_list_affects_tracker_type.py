from enum import Enum


class OsidbApiV2FlawsListAffectsTrackerType(str, Enum):
    BUGZILLA = "BUGZILLA"
    JIRA = "JIRA"

    def __str__(self) -> str:
        return str(self.value)
