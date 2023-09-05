import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.jira_issue_fields import JiraIssueFields
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="TaskmanApiV1GroupCreateResponse200")


@attr.s(auto_attribs=True)
class TaskmanApiV1GroupCreateResponse200(OSIDBModel):
    """ """

    id: int
    key: str
    name: str
    fields: JiraIssueFields
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key = self.key
        name = self.name
        fields: Dict[str, Any] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

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
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: JiraIssueFields
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = JiraIssueFields.from_dict(_fields)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        taskman_api_v1_group_create_response_200 = cls(
            id=id,
            key=key,
            name=name,
            fields=fields,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        taskman_api_v1_group_create_response_200.additional_properties = d
        return taskman_api_v1_group_create_response_200

    @staticmethod
    def get_fields():
        return {
            "id": int,
            "key": str,
            "name": str,
            "fields": JiraIssueFields,
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
