from enum import Enum


class SRPReportMilestoneStatusEnum(str, Enum):
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"
    OBSOLETE = "obsolete"
    REQUIRED = "required"
    SUBMITTED = "submitted"

    def __str__(self) -> str:
        return str(self.value)
