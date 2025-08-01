from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="IntegrationTokenGet")


@_attrs_define
class IntegrationTokenGet(OSIDBModel):
    """
    Attributes:
        jira (Union[None, str]):
        bugzilla (Union[None, str]):
    """

    jira: Union[None, str]
    bugzilla: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jira: Union[None, str]
        if isinstance(self.jira, Unset):
            jira = UNSET
        jira = self.jira

        bugzilla: Union[None, str]
        if isinstance(self.bugzilla, Unset):
            bugzilla = UNSET
        bugzilla = self.bugzilla

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(jira, Unset):
            field_dict["jira"] = jira
        if not isinstance(bugzilla, Unset):
            field_dict["bugzilla"] = bugzilla

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_jira(data: object) -> Union[None, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, str], data)

        jira = _parse_jira(d.pop("jira", UNSET))

        def _parse_bugzilla(data: object) -> Union[None, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, str], data)

        bugzilla = _parse_bugzilla(d.pop("bugzilla", UNSET))

        integration_token_get = cls(
            jira=jira,
            bugzilla=bugzilla,
        )

        integration_token_get.additional_properties = d
        return integration_token_get

    @classmethod
    def get_fields(cls):
        return {f.name: f.type for f in _attrs_fields(cls)}

    @classmethod
    def new(cls):
        return cls.from_dict({})

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
