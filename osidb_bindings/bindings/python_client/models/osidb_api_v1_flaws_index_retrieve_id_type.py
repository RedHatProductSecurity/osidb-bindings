from enum import Enum


class OsidbApiV1FlawsIndexRetrieveIdType(str, Enum):
    CVE_ID = "cve_id"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
