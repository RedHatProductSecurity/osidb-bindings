from enum import Enum


class CvssVersionEnum(str, Enum):
    V2 = "V2"
    V3 = "V3"
    V4 = "V4"

    def __str__(self) -> str:
        return str(self.value)
