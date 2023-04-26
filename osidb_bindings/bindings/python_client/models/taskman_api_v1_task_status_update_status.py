from enum import Enum


class TaskmanApiV1TaskStatusUpdateStatus(str, Enum):
    CLOSED = "Closed"
    IN_PROGRESS = "In Progress"
    NEW = "New"
    REFINEMENT = "Refinement"

    def __str__(self) -> str:
        return str(self.value)
