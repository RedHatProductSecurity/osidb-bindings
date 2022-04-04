from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import UNSET

T = TypeVar("T", bound="TokenRefresh")


@attr.s(auto_attribs=True)
class TokenRefresh:
    """ """

    access: str
    refresh: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access = self.access
        refresh = self.refresh

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if access is not UNSET:
            field_dict["access"] = access
        if refresh is not UNSET:
            field_dict["refresh"] = refresh

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        access = self.access if self.access is UNSET else (None, str(self.access), "text/plain")
        refresh = self.refresh if self.refresh is UNSET else (None, str(self.refresh), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        if access is not UNSET:
            field_dict["access"] = access
        if refresh is not UNSET:
            field_dict["refresh"] = refresh

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access = d.pop("access", UNSET)

        refresh = d.pop("refresh", UNSET)

        token_refresh = cls(
            access=access,
            refresh=refresh,
        )

        token_refresh.additional_properties = d
        return token_refresh

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
