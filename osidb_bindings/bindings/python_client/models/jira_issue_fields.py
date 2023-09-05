from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.jira_issue_type import JiraIssueType
from ..models.jira_user import JiraUser
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="JiraIssueFields")


@attr.s(auto_attribs=True)
class JiraIssueFields(OSIDBModel):
    """ """

    issuetype: JiraIssueType
    summary: str
    description: str
    assignee: JiraUser
    reporter: JiraUser
    creator: JiraUser
    customfield_12311140: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuetype: Dict[str, Any] = UNSET
        if not isinstance(self.issuetype, Unset):
            issuetype = self.issuetype.to_dict()

        summary = self.summary
        description = self.description
        assignee: Dict[str, Any] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        reporter: Dict[str, Any] = UNSET
        if not isinstance(self.reporter, Unset):
            reporter = self.reporter.to_dict()

        creator: Dict[str, Any] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        customfield_12311140 = self.customfield_12311140

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(issuetype, Unset):
            field_dict["issuetype"] = issuetype
        if not isinstance(summary, Unset):
            field_dict["summary"] = summary
        if not isinstance(description, Unset):
            field_dict["description"] = description
        if not isinstance(assignee, Unset):
            field_dict["assignee"] = assignee
        if not isinstance(reporter, Unset):
            field_dict["reporter"] = reporter
        if not isinstance(creator, Unset):
            field_dict["creator"] = creator
        if not isinstance(customfield_12311140, Unset):
            field_dict["customfield_12311140"] = customfield_12311140

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _issuetype = d.pop("issuetype", UNSET)
        issuetype: JiraIssueType
        if isinstance(_issuetype, Unset):
            issuetype = UNSET
        else:
            issuetype = JiraIssueType.from_dict(_issuetype)

        summary = d.pop("summary", UNSET)

        description = d.pop("description", UNSET)

        _assignee = d.pop("assignee", UNSET)
        assignee: JiraUser
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = JiraUser.from_dict(_assignee)

        _reporter = d.pop("reporter", UNSET)
        reporter: JiraUser
        if isinstance(_reporter, Unset):
            reporter = UNSET
        else:
            reporter = JiraUser.from_dict(_reporter)

        _creator = d.pop("creator", UNSET)
        creator: JiraUser
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = JiraUser.from_dict(_creator)

        customfield_12311140 = d.pop("customfield_12311140", UNSET)

        jira_issue_fields = cls(
            issuetype=issuetype,
            summary=summary,
            description=description,
            assignee=assignee,
            reporter=reporter,
            creator=creator,
            customfield_12311140=customfield_12311140,
        )

        jira_issue_fields.additional_properties = d
        return jira_issue_fields

    @staticmethod
    def get_fields():
        return {
            "issuetype": JiraIssueType,
            "summary": str,
            "description": str,
            "assignee": JiraUser,
            "reporter": JiraUser,
            "creator": JiraUser,
            "customfield_12311140": str,
        }

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
