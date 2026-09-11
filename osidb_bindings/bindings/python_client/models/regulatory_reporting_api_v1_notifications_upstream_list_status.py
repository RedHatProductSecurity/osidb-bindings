from enum import Enum


class RegulatoryReportingApiV1NotificationsUpstreamListStatus(str, Enum):
    BLOCKED = "blocked"
    CONTACT_NEEDED = "contact_needed"
    DEFERRED = "deferred"
    FAILED = "failed"
    NOT_APPLICABLE = "not_applicable"
    NOT_REQUIRED = "not_required"
    PREPARED = "prepared"
    QUEUED = "queued"
    REQUIRED = "required"
    REVIEWED = "reviewed"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)
