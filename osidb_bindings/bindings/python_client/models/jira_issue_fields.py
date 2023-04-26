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

        customfield_12311140 = self.customfield_12311140

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if issuetype is not UNSET:
            field_dict["issuetype"] = issuetype
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if customfield_12311140 is not UNSET:
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

        customfield_12311140 = d.pop("customfield_12311140", UNSET)

        jira_issue_fields = cls(
            issuetype=issuetype,
            summary=summary,
            description=description,
            assignee=assignee,
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
