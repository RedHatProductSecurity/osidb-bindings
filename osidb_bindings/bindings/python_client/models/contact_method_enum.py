from enum import Enum


class ContactMethodEnum(str, Enum):
    EMAIL = "email"
    FORGEJO_ISSUE = "forgejo_issue"
    GITHUB_ISSUE = "github_issue"
    GITLAB_ISSUE = "gitlab_issue"
    NONE_FOUND = "none_found"
    OTHER = "other"
    WEBSITE_FORM = "website_form"

    def __str__(self) -> str:
        return str(self.value)
