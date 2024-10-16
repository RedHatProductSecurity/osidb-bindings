import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="Audit")


@attr.s(auto_attribs=True)
class Audit(OSIDBModel):
    """ """

    pgh_created_at: datetime.datetime
    pgh_slug: str
    pgh_obj_model: str
    pgh_label: str
    pgh_diff: Any
    pgh_data: str
    pgh_obj_id: Union[Unset, None, str] = UNSET
    pgh_context: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pgh_created_at: str = UNSET
        if not isinstance(self.pgh_created_at, Unset):
            pgh_created_at = self.pgh_created_at.isoformat()

        pgh_slug = self.pgh_slug
        pgh_obj_model = self.pgh_obj_model
        pgh_label = self.pgh_label
        pgh_diff = self.pgh_diff

        pgh_data = self.pgh_data
        pgh_obj_id = self.pgh_obj_id
        pgh_context = self.pgh_context

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(pgh_created_at, Unset):
            field_dict["pgh_created_at"] = pgh_created_at
        if not isinstance(pgh_slug, Unset):
            field_dict["pgh_slug"] = pgh_slug
        if not isinstance(pgh_obj_model, Unset):
            field_dict["pgh_obj_model"] = pgh_obj_model
        if not isinstance(pgh_label, Unset):
            field_dict["pgh_label"] = pgh_label
        if not isinstance(pgh_diff, Unset):
            field_dict["pgh_diff"] = pgh_diff
        if not isinstance(pgh_data, Unset):
            field_dict["pgh_data"] = pgh_data
        if not isinstance(pgh_obj_id, Unset):
            field_dict["pgh_obj_id"] = pgh_obj_id
        if not isinstance(pgh_context, Unset):
            field_dict["pgh_context"] = pgh_context

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        pgh_created_at: str = UNSET
        if not isinstance(self.pgh_created_at, Unset):
            pgh_created_at = self.pgh_created_at.isoformat()

        pgh_slug = (
            self.pgh_slug
            if self.pgh_slug is UNSET
            else (None, str(self.pgh_slug), "text/plain")
        )
        pgh_obj_model = (
            self.pgh_obj_model
            if self.pgh_obj_model is UNSET
            else (None, str(self.pgh_obj_model), "text/plain")
        )
        pgh_label = (
            self.pgh_label
            if self.pgh_label is UNSET
            else (None, str(self.pgh_label), "text/plain")
        )
        pgh_diff = self.pgh_diff

        pgh_data = (
            self.pgh_data
            if self.pgh_data is UNSET
            else (None, str(self.pgh_data), "text/plain")
        )
        pgh_obj_id = (
            self.pgh_obj_id
            if self.pgh_obj_id is UNSET
            else (None, str(self.pgh_obj_id), "text/plain")
        )
        pgh_context = self.pgh_context

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        if not isinstance(pgh_created_at, Unset):
            field_dict["pgh_created_at"] = pgh_created_at
        if not isinstance(pgh_slug, Unset):
            field_dict["pgh_slug"] = pgh_slug
        if not isinstance(pgh_obj_model, Unset):
            field_dict["pgh_obj_model"] = pgh_obj_model
        if not isinstance(pgh_label, Unset):
            field_dict["pgh_label"] = pgh_label
        if not isinstance(pgh_diff, Unset):
            field_dict["pgh_diff"] = pgh_diff
        if not isinstance(pgh_data, Unset):
            field_dict["pgh_data"] = pgh_data
        if not isinstance(pgh_obj_id, Unset):
            field_dict["pgh_obj_id"] = pgh_obj_id
        if not isinstance(pgh_context, Unset):
            field_dict["pgh_context"] = pgh_context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _pgh_created_at = d.pop("pgh_created_at", UNSET)
        pgh_created_at: datetime.datetime
        if isinstance(_pgh_created_at, Unset):
            pgh_created_at = UNSET
        else:
            pgh_created_at = isoparse(_pgh_created_at)

        pgh_slug = d.pop("pgh_slug", UNSET)

        pgh_obj_model = d.pop("pgh_obj_model", UNSET)

        pgh_label = d.pop("pgh_label", UNSET)

        pgh_diff = d.pop("pgh_diff", UNSET)

        pgh_data = d.pop("pgh_data", UNSET)

        pgh_obj_id = d.pop("pgh_obj_id", UNSET)

        pgh_context = d.pop("pgh_context", UNSET)

        audit = cls(
            pgh_created_at=pgh_created_at,
            pgh_slug=pgh_slug,
            pgh_obj_model=pgh_obj_model,
            pgh_label=pgh_label,
            pgh_diff=pgh_diff,
            pgh_data=pgh_data,
            pgh_obj_id=pgh_obj_id,
            pgh_context=pgh_context,
        )

        audit.additional_properties = d
        return audit

    @staticmethod
    def get_fields():
        return {
            "pgh_created_at": datetime.datetime,
            "pgh_slug": str,
            "pgh_obj_model": str,
            "pgh_label": str,
            "pgh_diff": Any,
            "pgh_data": str,
            "pgh_obj_id": str,
            "pgh_context": Any,
        }

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
