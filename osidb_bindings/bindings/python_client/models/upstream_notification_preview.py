from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="UpstreamNotificationPreview")


@_attrs_define
class UpstreamNotificationPreview(OSIDBModel):
    """
    Attributes:
        text_body (str):
        html_body (str):
    """

    text_body: str
    html_body: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_body = self.text_body

        html_body = self.html_body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(text_body, Unset):
            field_dict["text_body"] = text_body
        if not isinstance(html_body, Unset):
            field_dict["html_body"] = html_body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        text_body = d.pop("text_body", UNSET)

        html_body = d.pop("html_body", UNSET)

        upstream_notification_preview = cls(
            text_body=text_body,
            html_body=html_body,
        )

        upstream_notification_preview.additional_properties = d
        return upstream_notification_preview

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
