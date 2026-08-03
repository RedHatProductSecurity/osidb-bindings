import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.audit_pgh_context_type_0 import AuditPghContextType0
    from ..models.audit_pgh_data import AuditPghData
    from ..models.audit_pgh_diff import AuditPghDiff


T = TypeVar("T", bound="Audit")


@_attrs_define
class Audit(OSIDBModel):
    """
    Attributes:
        pgh_created_at (datetime.datetime): When the event was created.
        pgh_slug (str): The unique identifier across all event tables.
        pgh_obj_model (str): The object model.
        pgh_label (str): The event label.
        pgh_context (Union['AuditPghContextType0', None]): The context associated with the event.
        pgh_diff (AuditPghDiff): The diff between the previous event of the same label.
        pgh_data (AuditPghData):
        pgh_obj_id (Union[None, Unset, str]): The primary key of the object.
    """

    pgh_created_at: datetime.datetime
    pgh_slug: str
    pgh_obj_model: str
    pgh_label: str
    pgh_context: Union["AuditPghContextType0", None]
    pgh_diff: "AuditPghDiff"
    pgh_data: "AuditPghData"
    pgh_obj_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_pgh_context_type_0 import AuditPghContextType0

        pgh_created_at: str = UNSET
        if not isinstance(self.pgh_created_at, Unset):
            pgh_created_at = self.pgh_created_at.isoformat()

        pgh_slug = self.pgh_slug

        pgh_obj_model = self.pgh_obj_model

        pgh_label = self.pgh_label

        pgh_context: Union[None, dict[str, Any]]
        if isinstance(self.pgh_context, Unset):
            pgh_context = UNSET
        elif isinstance(self.pgh_context, AuditPghContextType0):
            pgh_context = UNSET
            if not isinstance(self.pgh_context, Unset):
                pgh_context = self.pgh_context.to_dict()

        else:
            pgh_context = self.pgh_context

        pgh_diff: dict[str, Any] = UNSET
        if not isinstance(self.pgh_diff, Unset):
            pgh_diff = self.pgh_diff.to_dict()

        pgh_data: dict[str, Any] = UNSET
        if not isinstance(self.pgh_data, Unset):
            pgh_data = self.pgh_data.to_dict()

        pgh_obj_id: Union[None, Unset, str]
        if isinstance(self.pgh_obj_id, Unset):
            pgh_obj_id = UNSET
        else:
            pgh_obj_id = self.pgh_obj_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(pgh_created_at, Unset):
            field_dict["pgh_created_at"] = pgh_created_at
        if not isinstance(pgh_slug, Unset):
            field_dict["pgh_slug"] = pgh_slug
        if not isinstance(pgh_obj_model, Unset):
            field_dict["pgh_obj_model"] = pgh_obj_model
        if not isinstance(pgh_label, Unset):
            field_dict["pgh_label"] = pgh_label
        if not isinstance(pgh_context, Unset):
            field_dict["pgh_context"] = pgh_context
        if not isinstance(pgh_diff, Unset):
            field_dict["pgh_diff"] = pgh_diff
        if not isinstance(pgh_data, Unset):
            field_dict["pgh_data"] = pgh_data
        if not isinstance(pgh_obj_id, Unset):
            field_dict["pgh_obj_id"] = pgh_obj_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.audit_pgh_context_type_0 import AuditPghContextType0
        from ..models.audit_pgh_data import AuditPghData
        from ..models.audit_pgh_diff import AuditPghDiff

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

        def _parse_pgh_context(data: object) -> Union["AuditPghContextType0", None]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _pgh_context_type_0 = data
                pgh_context_type_0: AuditPghContextType0
                if isinstance(_pgh_context_type_0, Unset):
                    pgh_context_type_0 = UNSET
                else:
                    pgh_context_type_0 = AuditPghContextType0.from_dict(
                        _pgh_context_type_0
                    )

                return pgh_context_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AuditPghContextType0", None], data)

        pgh_context = _parse_pgh_context(d.pop("pgh_context", UNSET))

        _pgh_diff = d.pop("pgh_diff", UNSET)
        pgh_diff: AuditPghDiff
        if isinstance(_pgh_diff, Unset):
            pgh_diff = UNSET
        else:
            pgh_diff = AuditPghDiff.from_dict(_pgh_diff)

        _pgh_data = d.pop("pgh_data", UNSET)
        pgh_data: AuditPghData
        if isinstance(_pgh_data, Unset):
            pgh_data = UNSET
        else:
            pgh_data = AuditPghData.from_dict(_pgh_data)

        def _parse_pgh_obj_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pgh_obj_id = _parse_pgh_obj_id(d.pop("pgh_obj_id", UNSET))

        audit = cls(
            pgh_created_at=pgh_created_at,
            pgh_slug=pgh_slug,
            pgh_obj_model=pgh_obj_model,
            pgh_label=pgh_label,
            pgh_context=pgh_context,
            pgh_diff=pgh_diff,
            pgh_data=pgh_data,
            pgh_obj_id=pgh_obj_id,
        )

        audit.additional_properties = d
        return audit

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
