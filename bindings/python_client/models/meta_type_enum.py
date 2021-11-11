from enum import Enum


class MetaTypeEnum(str, Enum):
    ERRATA = "ERRATA"
    REFERENCE = "REFERENCE"
    ACKNOWLEDGEMENT = "ACKNOWLEDGEMENT"
    EXPLOIT = "EXPLOIT"
    CSAW = "CSAW"
    CSAW_LITE = "CSAW_LITE"
    REQUIRES_DOC_TEXT = "REQUIRES_DOC_TEXT"
    NIST_CVSS_VALIDATION = "NIST_CVSS_VALIDATION"
    NEED_INFO = "NEED_INFO"
    CHECKLIST = "CHECKLIST"

    def __str__(self) -> str:
        return str(self.value)
