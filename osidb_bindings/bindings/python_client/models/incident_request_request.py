from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..models.kind_enum import KindEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="IncidentRequestRequest")


@_attrs_define
class IncidentRequestRequest(OSIDBModel):
    """
    Attributes:
        comment (str):
        kind (KindEnum):
    """

    comment: str
    kind: KindEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        kind: str = UNSET
        if not isinstance(self.kind, Unset):
            kind = KindEnum(self.kind).value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(comment, Unset):
            field_dict["comment"] = comment
        if not isinstance(kind, Unset):
            field_dict["kind"] = kind

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        comment = (None, str(self.comment).encode(), "text/plain")

        kind: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.kind, Unset):
            kind = (None, str(self.kind.value).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(comment, Unset):
            field_dict["comment"] = comment
        if not isinstance(kind, Unset):
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        comment = d.pop("comment", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: KindEnum
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = KindEnum(_kind)

        incident_request_request = cls(
            comment=comment,
            kind=kind,
        )

        incident_request_request.additional_properties = d
        return incident_request_request

    @classmethod
    def get_fields(cls):
        return {f.name: f.type for f in _attrs_fields(cls)}

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
