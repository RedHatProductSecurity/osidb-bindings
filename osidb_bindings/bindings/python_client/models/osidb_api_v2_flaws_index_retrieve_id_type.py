from enum import Enum


class OsidbApiV2FlawsIndexRetrieveIdType(str, Enum):
    CVE_ID = "cve_id"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
