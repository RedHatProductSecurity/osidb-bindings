import datetime
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="UpstreamDataRequest")


@_attrs_define
class UpstreamDataRequest(OSIDBModel):
    """Serializer for OSV/collector upstream metadata attached to a flaw (read-only via API).

    Attributes:
        flaw (UUID):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
    """

    flaw: UUID
    embargoed: bool
    updated_dt: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flaw: str = UNSET
        if not isinstance(self.flaw, Unset):
            flaw = str(self.flaw)

        embargoed = self.embargoed

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _flaw = d.pop("flaw", UNSET)
        flaw: UUID
        if isinstance(_flaw, Unset):
            flaw = UNSET
        else:
            flaw = _flaw if isinstance(_flaw, UUID) else UUID(_flaw)

        embargoed = d.pop("embargoed", UNSET)

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        upstream_data_request = cls(
            flaw=flaw,
            embargoed=embargoed,
            updated_dt=updated_dt,
        )

        upstream_data_request.additional_properties = d
        return upstream_data_request

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
