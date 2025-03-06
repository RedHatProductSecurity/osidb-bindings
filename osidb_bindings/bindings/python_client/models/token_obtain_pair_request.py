from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="TokenObtainPairRequest")


@_attrs_define
class TokenObtainPairRequest(OSIDBModel):
    """
    Attributes:
        username (str):
        password (str):
    """

    username: str
    password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(username, Unset):
            field_dict["username"] = username
        if not isinstance(password, Unset):
            field_dict["password"] = password

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        username = (None, str(self.username).encode(), "text/plain")

        password = (None, str(self.password).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(username, Unset):
            field_dict["username"] = username
        if not isinstance(password, Unset):
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        token_obtain_pair_request = cls(
            username=username,
            password=password,
        )

        token_obtain_pair_request.additional_properties = d
        return token_obtain_pair_request

    @staticmethod
    def get_fields():
        return {
            "username": str,
            "password": str,
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
