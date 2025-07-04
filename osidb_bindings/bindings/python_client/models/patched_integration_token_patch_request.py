from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="PatchedIntegrationTokenPatchRequest")


@_attrs_define
class PatchedIntegrationTokenPatchRequest(OSIDBModel):
    """
    Attributes:
        jira (Union[Unset, str]):
        bugzilla (Union[Unset, str]):
    """

    jira: Union[Unset, str] = UNSET
    bugzilla: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jira = self.jira

        bugzilla = self.bugzilla

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(jira, Unset):
            field_dict["jira"] = jira
        if not isinstance(bugzilla, Unset):
            field_dict["bugzilla"] = bugzilla

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        jira = (
            self.jira
            if isinstance(self.jira, Unset)
            else (None, str(self.jira).encode(), "text/plain")
        )

        bugzilla = (
            self.bugzilla
            if isinstance(self.bugzilla, Unset)
            else (None, str(self.bugzilla).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(jira, Unset):
            field_dict["jira"] = jira
        if not isinstance(bugzilla, Unset):
            field_dict["bugzilla"] = bugzilla

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        jira = d.pop("jira", UNSET)

        bugzilla = d.pop("bugzilla", UNSET)

        patched_integration_token_patch_request = cls(
            jira=jira,
            bugzilla=bugzilla,
        )

        patched_integration_token_patch_request.additional_properties = d
        return patched_integration_token_patch_request

    @staticmethod
    def get_fields():
        return {
            "jira": str,
            "bugzilla": str,
        }

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
