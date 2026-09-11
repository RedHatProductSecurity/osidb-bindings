import datetime
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawUpstreamMappingRequest")


@_attrs_define
class FlawUpstreamMappingRequest(OSIDBModel):
    """TrackingMixin class serializer

    Attributes:
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        upstream_project (UUID):
        notes (Union[Unset, str]):
    """

    updated_dt: datetime.datetime
    upstream_project: UUID
    notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        upstream_project: str = UNSET
        if not isinstance(self.upstream_project, Unset):
            upstream_project = str(self.upstream_project)

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(upstream_project, Unset):
            field_dict["upstream_project"] = upstream_project
        if not isinstance(notes, Unset):
            field_dict["notes"] = notes

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        updated_dt: bytes = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat().encode()

        upstream_project: bytes = UNSET
        if not isinstance(self.upstream_project, Unset):
            upstream_project = str(self.upstream_project)

        notes = (
            self.notes
            if isinstance(self.notes, Unset)
            else (None, str(self.notes).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(upstream_project, Unset):
            field_dict["upstream_project"] = upstream_project
        if not isinstance(notes, Unset):
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        _upstream_project = d.pop("upstream_project", UNSET)
        upstream_project: UUID
        if isinstance(_upstream_project, Unset):
            upstream_project = UNSET
        else:
            upstream_project = (
                _upstream_project
                if isinstance(_upstream_project, UUID)
                else UUID(_upstream_project)
            )

        notes = d.pop("notes", UNSET)

        flaw_upstream_mapping_request = cls(
            updated_dt=updated_dt,
            upstream_project=upstream_project,
            notes=notes,
        )

        flaw_upstream_mapping_request.additional_properties = d
        return flaw_upstream_mapping_request

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
