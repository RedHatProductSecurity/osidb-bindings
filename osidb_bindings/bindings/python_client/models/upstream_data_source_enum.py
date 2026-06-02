from enum import Enum


class UpstreamDataSourceEnum(str, Enum):
    CVEORG = "CVEORG"
    OSV = "OSV"

    def __str__(self) -> str:
        return str(self.value)
