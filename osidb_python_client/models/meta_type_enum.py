from enum import Enum


class MetaTypeEnum(str, Enum):
    REFERENCE = "REFERENCE"
    ACKNOWLEDGEMENT = "ACKNOWLEDGEMENT"
    EXPLOIT = "EXPLOIT"

    def __str__(self) -> str:
        return str(self.value)
