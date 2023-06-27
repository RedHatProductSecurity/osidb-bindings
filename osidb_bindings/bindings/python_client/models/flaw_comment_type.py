from enum import Enum


class FlawCommentType(str, Enum):
    BUGZILLA = "BUGZILLA"

    def __str__(self) -> str:
        return str(self.value)
