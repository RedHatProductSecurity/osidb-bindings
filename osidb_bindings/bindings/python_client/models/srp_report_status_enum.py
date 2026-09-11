from enum import Enum


class SRPReportStatusEnum(str, Enum):
    EMPTY = "empty"
    IN_PROGRESS = "in_progress"
    SUBMITTED = "submitted"

    def __str__(self) -> str:
        return str(self.value)
