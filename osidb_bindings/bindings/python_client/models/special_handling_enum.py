from enum import Enum


class SpecialHandlingEnum(str, Enum):
    COMPLIANCE_PRIORITY = "compliance-priority"
    CONTRACT_PRIORITY = "contract-priority"
    KEV_ACTIVE_EXPLOIT_CASE = "KEV (active exploit case)"
    MAJOR_INCIDENT = "Major Incident"
    MINOR_INCIDENT = "Minor Incident"
    SECURITY_SELECT = "security-select"
    SUPPORT_EXCEPTION = "support-exception"

    def __str__(self) -> str:
        return str(self.value)
