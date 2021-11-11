from enum import Enum


class CommentTypeEnum(str, Enum):
    BUGZILLA = "BUGZILLA"

    def __str__(self) -> str:
        return str(self.value)
