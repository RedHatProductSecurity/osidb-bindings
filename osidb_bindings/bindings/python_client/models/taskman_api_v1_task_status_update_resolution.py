from enum import Enum


class TaskmanApiV1TaskStatusUpdateResolution(str, Enum):
    CANT_DO = "Can't Do"
    CANNOT_REPRODUCE = "Cannot Reproduce"
    DONE = "Done"
    DONE_ERRATA = "Done-Errata"
    DUPLICATE = "Duplicate"
    MIRRORORPHAN = "MirrorOrphan"
    NOT_A_BUG = "Not a Bug"
    OBSOLETE = "Obsolete"
    TEST_PENDING = "Test Pending"
    WONT_DO = "Won't Do"

    def __str__(self) -> str:
        return str(self.value)
