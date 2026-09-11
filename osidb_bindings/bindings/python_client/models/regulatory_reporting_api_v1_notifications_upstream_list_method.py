from enum import Enum


class RegulatoryReportingApiV1NotificationsUpstreamListMethod(str, Enum):
    EMAIL = "email"
    FORGEJO_ISSUE = "forgejo_issue"
    GITHUB_ISSUE = "github_issue"
    GITLAB_ISSUE = "gitlab_issue"
    OTHER_MANUAL = "other_manual"
    WEBSITE_FORM = "website_form"

    def __str__(self) -> str:
        return str(self.value)
