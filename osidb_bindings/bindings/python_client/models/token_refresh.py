from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="TokenRefresh")


@_attrs_define
class TokenRefresh(OSIDBModel):
    """
    Attributes:
        access (str):
        refresh (str):
    """

    access: str
    refresh: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access = self.access

        refresh = self.refresh

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(access, Unset):
            field_dict["access"] = access
        if not isinstance(refresh, Unset):
            field_dict["refresh"] = refresh

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        access = (None, str(self.access).encode(), "text/plain")

        refresh = (None, str(self.refresh).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(access, Unset):
            field_dict["access"] = access
        if not isinstance(refresh, Unset):
            field_dict["refresh"] = refresh

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        access = d.pop("access", UNSET)

        refresh = d.pop("refresh", UNSET)

        token_refresh = cls(
            access=access,
            refresh=refresh,
        )

        token_refresh.additional_properties = d
        return token_refresh

    @staticmethod
    def get_fields():
        return {
            "access": str,
            "refresh": str,
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
