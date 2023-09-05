from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.jira_issue import JiraIssue
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="JiraIssueQueryResult")


@attr.s(auto_attribs=True)
class JiraIssueQueryResult(OSIDBModel):
    """ """

    total: int
    issues: List[JiraIssue]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        issues: List[Dict[str, Any]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item: Dict[str, Any] = UNSET
                if not isinstance(issues_item_data, Unset):
                    issues_item = issues_item_data.to_dict()

                issues.append(issues_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(total, Unset):
            field_dict["total"] = total
        if not isinstance(issues, Unset):
            field_dict["issues"] = issues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total", UNSET)

        issues = []
        _issues = d.pop("issues", UNSET)
        if _issues is UNSET:
            issues = UNSET
        else:
            for issues_item_data in _issues or []:
                _issues_item = issues_item_data
                issues_item: JiraIssue
                if isinstance(_issues_item, Unset):
                    issues_item = UNSET
                else:
                    issues_item = JiraIssue.from_dict(_issues_item)

                issues.append(issues_item)

        jira_issue_query_result = cls(
            total=total,
            issues=issues,
        )

        jira_issue_query_result.additional_properties = d
        return jira_issue_query_result

    @staticmethod
    def get_fields():
        return {
            "total": int,
            "issues": List[JiraIssue],
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
