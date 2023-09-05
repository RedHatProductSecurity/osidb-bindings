from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="JiraUser")


@attr.s(auto_attribs=True)
class JiraUser(OSIDBModel):
    """ """

    name: str
    key: str
    email_address: str
    display_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        key = self.key
        email_address = self.email_address
        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(key, Unset):
            field_dict["key"] = key
        if not isinstance(email_address, Unset):
            field_dict["emailAddress"] = email_address
        if not isinstance(display_name, Unset):
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        key = d.pop("key", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        display_name = d.pop("displayName", UNSET)

        jira_user = cls(
            name=name,
            key=key,
            email_address=email_address,
            display_name=display_name,
        )

        jira_user.additional_properties = d
        return jira_user

    @staticmethod
    def get_fields():
        return {
            "name": str,
            "key": str,
            "emailAddress": str,
            "displayName": str,
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
