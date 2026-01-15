from enum import Enum


class OsidbApiV2FlawsListAffectsTrackerTypeInItem(str, Enum):
    BUGZILLA = "BUGZILLA"
    JIRA = "JIRA"

    def __str__(self) -> str:
        return str(self.value)
