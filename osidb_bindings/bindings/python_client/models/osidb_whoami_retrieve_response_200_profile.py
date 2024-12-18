from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbWhoamiRetrieveResponse200Profile")


@_attrs_define
class OsidbWhoamiRetrieveResponse200Profile(OSIDBModel):
    """
    Attributes:
        bz_user_id (Union[Unset, str]):
        jira_user_id (Union[Unset, str]):
    """

    bz_user_id: Union[Unset, str] = UNSET
    jira_user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bz_user_id = self.bz_user_id

        jira_user_id = self.jira_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(bz_user_id, Unset):
            field_dict["bz_user_id"] = bz_user_id
        if not isinstance(jira_user_id, Unset):
            field_dict["jira_user_id"] = jira_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        bz_user_id = d.pop("bz_user_id", UNSET)

        jira_user_id = d.pop("jira_user_id", UNSET)

        osidb_whoami_retrieve_response_200_profile = cls(
            bz_user_id=bz_user_id,
            jira_user_id=jira_user_id,
        )

        osidb_whoami_retrieve_response_200_profile.additional_properties = d
        return osidb_whoami_retrieve_response_200_profile

    @staticmethod
    def get_fields():
        return {
            "bz_user_id": str,
            "jira_user_id": str,
        }

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
