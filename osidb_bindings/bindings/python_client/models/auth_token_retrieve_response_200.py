from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthTokenRetrieveResponse200")


@attr.s(auto_attribs=True)
class AuthTokenRetrieveResponse200:
    """ """

    refresh: Union[Unset, str] = UNSET
    access: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refresh = self.refresh
        access = self.access

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if refresh is not UNSET:
            field_dict["refresh"] = refresh
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        refresh = d.pop("refresh", UNSET)

        access = d.pop("access", UNSET)

        auth_token_retrieve_response_200 = cls(
            refresh=refresh,
            access=access,
        )

        auth_token_retrieve_response_200.additional_properties = d
        return auth_token_retrieve_response_200

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
