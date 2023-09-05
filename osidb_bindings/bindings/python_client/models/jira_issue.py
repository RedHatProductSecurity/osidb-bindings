from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.jira_issue_fields import JiraIssueFields
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="JiraIssue")


@attr.s(auto_attribs=True)
class JiraIssue(OSIDBModel):
    """ """

    id: int
    key: str
    name: str
    fields: JiraIssueFields
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key = self.key
        name = self.name
        fields: Dict[str, Any] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(id, Unset):
            field_dict["id"] = id
        if not isinstance(key, Unset):
            field_dict["key"] = key
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(fields, Unset):
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: JiraIssueFields
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = JiraIssueFields.from_dict(_fields)

        jira_issue = cls(
            id=id,
            key=key,
            name=name,
            fields=fields,
        )

        jira_issue.additional_properties = d
        return jira_issue

    @staticmethod
    def get_fields():
        return {
            "id": int,
            "key": str,
            "name": str,
            "fields": JiraIssueFields,
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
