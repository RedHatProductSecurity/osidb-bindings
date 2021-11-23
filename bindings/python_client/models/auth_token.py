from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import UNSET

T = TypeVar("T", bound="AuthToken")


@attr.s(auto_attribs=True)
class AuthToken:
    """ """

    username: str
    password: str
    token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        password = self.password
        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        username = self.username if self.username is UNSET else (None, str(self.username), "text/plain")
        password = self.password if self.password is UNSET else (None, str(self.password), "text/plain")
        token = self.token if self.token is UNSET else (None, str(self.token), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        token = d.pop("token", UNSET)

        auth_token = cls(
            username=username,
            password=password,
            token=token,
        )

        auth_token.additional_properties = d
        return auth_token

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
