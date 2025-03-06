from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="AuditRequest")


@_attrs_define
class AuditRequest(OSIDBModel):
    """
    Attributes:
        pgh_slug (str): The unique identifier across all event tables.
        pgh_obj_model (str): The object model.
        pgh_label (str): The event label.
        pgh_diff (Any): The diff between the previous event of the same label.
        pgh_obj_id (Union[None, Unset, str]): The primary key of the object.
        pgh_context (Union[Unset, Any]): The context associated with the event.
    """

    pgh_slug: str
    pgh_obj_model: str
    pgh_label: str
    pgh_diff: Any
    pgh_obj_id: Union[None, Unset, str] = UNSET
    pgh_context: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pgh_slug = self.pgh_slug

        pgh_obj_model = self.pgh_obj_model

        pgh_label = self.pgh_label

        pgh_diff = self.pgh_diff

        pgh_obj_id: Union[None, Unset, str]
        if isinstance(self.pgh_obj_id, Unset):
            pgh_obj_id = UNSET
        else:
            pgh_obj_id = self.pgh_obj_id

        pgh_context = self.pgh_context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(pgh_slug, Unset):
            field_dict["pgh_slug"] = pgh_slug
        if not isinstance(pgh_obj_model, Unset):
            field_dict["pgh_obj_model"] = pgh_obj_model
        if not isinstance(pgh_label, Unset):
            field_dict["pgh_label"] = pgh_label
        if not isinstance(pgh_diff, Unset):
            field_dict["pgh_diff"] = pgh_diff
        if not isinstance(pgh_obj_id, Unset):
            field_dict["pgh_obj_id"] = pgh_obj_id
        if not isinstance(pgh_context, Unset):
            field_dict["pgh_context"] = pgh_context

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        pgh_slug = (None, str(self.pgh_slug).encode(), "text/plain")

        pgh_obj_model = (None, str(self.pgh_obj_model).encode(), "text/plain")

        pgh_label = (None, str(self.pgh_label).encode(), "text/plain")

        pgh_diff = (None, str(self.pgh_diff).encode(), "text/plain")

        pgh_obj_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.pgh_obj_id, Unset):
            pgh_obj_id = UNSET
        elif isinstance(self.pgh_obj_id, str):
            pgh_obj_id = (None, str(self.pgh_obj_id).encode(), "text/plain")
        else:
            pgh_obj_id = (None, str(self.pgh_obj_id).encode(), "text/plain")

        pgh_context = (
            self.pgh_context
            if isinstance(self.pgh_context, Unset)
            else (None, str(self.pgh_context).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(pgh_slug, Unset):
            field_dict["pgh_slug"] = pgh_slug
        if not isinstance(pgh_obj_model, Unset):
            field_dict["pgh_obj_model"] = pgh_obj_model
        if not isinstance(pgh_label, Unset):
            field_dict["pgh_label"] = pgh_label
        if not isinstance(pgh_diff, Unset):
            field_dict["pgh_diff"] = pgh_diff
        if not isinstance(pgh_obj_id, Unset):
            field_dict["pgh_obj_id"] = pgh_obj_id
        if not isinstance(pgh_context, Unset):
            field_dict["pgh_context"] = pgh_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        pgh_slug = d.pop("pgh_slug", UNSET)

        pgh_obj_model = d.pop("pgh_obj_model", UNSET)

        pgh_label = d.pop("pgh_label", UNSET)

        pgh_diff = d.pop("pgh_diff", UNSET)

        def _parse_pgh_obj_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pgh_obj_id = _parse_pgh_obj_id(d.pop("pgh_obj_id", UNSET))

        pgh_context = d.pop("pgh_context", UNSET)

        audit_request = cls(
            pgh_slug=pgh_slug,
            pgh_obj_model=pgh_obj_model,
            pgh_label=pgh_label,
            pgh_diff=pgh_diff,
            pgh_obj_id=pgh_obj_id,
            pgh_context=pgh_context,
        )

        audit_request.additional_properties = d
        return audit_request

    @staticmethod
    def get_fields():
        return {
            "pgh_slug": str,
            "pgh_obj_model": str,
            "pgh_label": str,
            "pgh_diff": Any,
            "pgh_obj_id": Union[None, str],
            "pgh_context": Any,
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
