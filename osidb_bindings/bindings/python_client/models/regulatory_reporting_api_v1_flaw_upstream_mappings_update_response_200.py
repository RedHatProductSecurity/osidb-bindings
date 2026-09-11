import datetime
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="RegulatoryReportingApiV1FlawUpstreamMappingsUpdateResponse200")


@_attrs_define
class RegulatoryReportingApiV1FlawUpstreamMappingsUpdateResponse200(OSIDBModel):
    """
    Attributes:
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        uuid (UUID):
        flaw_uuid (UUID):
        upstream_project (UUID):
        notes (Union[Unset, str]):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    uuid: UUID
    flaw_uuid: UUID
    upstream_project: UUID
    notes: Union[Unset, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        flaw_uuid: str = UNSET
        if not isinstance(self.flaw_uuid, Unset):
            flaw_uuid = str(self.flaw_uuid)

        upstream_project: str = UNSET
        if not isinstance(self.upstream_project, Unset):
            upstream_project = str(self.upstream_project)

        notes = self.notes

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(flaw_uuid, Unset):
            field_dict["flaw_uuid"] = flaw_uuid
        if not isinstance(upstream_project, Unset):
            field_dict["upstream_project"] = upstream_project
        if not isinstance(notes, Unset):
            field_dict["notes"] = notes
        if not isinstance(dt, Unset):
            field_dict["dt"] = dt
        if not isinstance(env, Unset):
            field_dict["env"] = env
        if not isinstance(revision, Unset):
            field_dict["revision"] = revision
        if not isinstance(version, Unset):
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        _flaw_uuid = d.pop("flaw_uuid", UNSET)
        flaw_uuid: UUID
        if isinstance(_flaw_uuid, Unset):
            flaw_uuid = UNSET
        else:
            flaw_uuid = _flaw_uuid if isinstance(_flaw_uuid, UUID) else UUID(_flaw_uuid)

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

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        regulatory_reporting_api_v1_flaw_upstream_mappings_update_response_200 = cls(
            created_dt=created_dt,
            updated_dt=updated_dt,
            uuid=uuid,
            flaw_uuid=flaw_uuid,
            upstream_project=upstream_project,
            notes=notes,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        regulatory_reporting_api_v1_flaw_upstream_mappings_update_response_200.additional_properties = d
        return regulatory_reporting_api_v1_flaw_upstream_mappings_update_response_200

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
