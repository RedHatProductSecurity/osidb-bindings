from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawLabel")


@_attrs_define
class FlawLabel(OSIDBModel):
    """FlawLabel serializer

    Attributes:
        name (str):
        type_ (str):
    """

    name: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(type_, Unset):
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        flaw_label = cls(
            name=name,
            type_=type_,
        )

        flaw_label.additional_properties = d
        return flaw_label

    @staticmethod
    def get_fields():
        return {
            "name": str,
            "type": str,
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
