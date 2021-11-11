from enum import Enum


class AffectStateEnum(str, Enum):
    NONE = "NONE"
    NEW = "NEW"
    AFFECTED = "AFFECTED"
    NOT_AFFECTED = "NOT_AFFECTED"
    WONT_FIX = "WONT_FIX"
    OOSS = "OOSS"
    DEFERRED = "DEFERRED"

    def __str__(self) -> str:
        return str(self.value)
