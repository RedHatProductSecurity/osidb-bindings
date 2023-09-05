import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.jira_issue import JiraIssue
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="TaskmanApiV1TaskAssigneeRetrieveResponse200")


@attr.s(auto_attribs=True)
class TaskmanApiV1TaskAssigneeRetrieveResponse200(OSIDBModel):
    """ """

    total: int
    issues: List[JiraIssue]
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
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

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(total, Unset):
            field_dict["total"] = total
        if not isinstance(issues, Unset):
            field_dict["issues"] = issues
        if not isinstance(dt, Unset):
            field_dict["dt"] = dt
        if not isinstance(env, Unset):
            field_dict["env"] = env
        if not isinstance(revision, Unset):
            field_dict["revision"] = revision
        if not isinstance(version, Unset):
            field_dict["version"] = version

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

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        taskman_api_v1_task_assignee_retrieve_response_200 = cls(
            total=total,
            issues=issues,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        taskman_api_v1_task_assignee_retrieve_response_200.additional_properties = d
        return taskman_api_v1_task_assignee_retrieve_response_200

    @staticmethod
    def get_fields():
        return {
            "total": int,
            "issues": List[JiraIssue],
            "dt": datetime.datetime,
            "env": str,
            "revision": str,
            "version": str,
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
