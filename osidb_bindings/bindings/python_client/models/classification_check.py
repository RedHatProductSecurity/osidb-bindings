from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="ClassificationCheck")


@_attrs_define
class ClassificationCheck(OSIDBModel):
    """Check serializer with classification

    Attributes:
        accepts (str):
        name (str):
        description (str):
    """

    accepts: str
    name: str
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepts = self.accepts

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(accepts, Unset):
            field_dict["accepts"] = accepts
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(description, Unset):
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        accepts = d.pop("accepts", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        classification_check = cls(
            accepts=accepts,
            name=name,
            description=description,
        )

        classification_check.additional_properties = d
        return classification_check

    @classmethod
    def get_fields(cls):
        return {f.name: f.type for f in _attrs_fields(cls)}

    @classmethod
    def new(cls):
        return cls.from_dict({})

    @classmethod
    def from_model(cls: type[T], model: "OSIDBModel") -> T:
        return cls.from_dict(model.to_dict())

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
