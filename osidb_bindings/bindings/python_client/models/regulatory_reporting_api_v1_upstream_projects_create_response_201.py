import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.contact_method_enum import ContactMethodEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="RegulatoryReportingApiV1UpstreamProjectsCreateResponse201")


@_attrs_define
class RegulatoryReportingApiV1UpstreamProjectsCreateResponse201(OSIDBModel):
    """
    Attributes:
        created_dt (datetime.datetime):
        uuid (UUID):
        component_name (str):
        repository_url (Union[Unset, str]):
        security_contact (Union[Unset, str]):
        contact_method (Union[BlankEnum, ContactMethodEnum, Unset]):
        contact_url (Union[Unset, str]):
        source (Union[Unset, str]):
        confidence (Union[Unset, str]):
        verified_at (Union[None, Unset, datetime.datetime]):
        verified_by (Union[Unset, str]):
        unsupported (Union[Unset, bool]):
        stewarded_awareness (Union[Unset, bool]):
        stewarded_awareness_reason (Union[Unset, str]):
        stewarded_awareness_marked_by (Union[Unset, str]):
        stewarded_awareness_marked_at (Union[None, Unset, datetime.datetime]):
        notes (Union[Unset, str]):
        purl (Union[Unset, str]):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    created_dt: datetime.datetime
    uuid: UUID
    component_name: str
    repository_url: Union[Unset, str] = UNSET
    security_contact: Union[Unset, str] = UNSET
    contact_method: Union[BlankEnum, ContactMethodEnum, Unset] = UNSET
    contact_url: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    confidence: Union[Unset, str] = UNSET
    verified_at: Union[None, Unset, datetime.datetime] = UNSET
    verified_by: Union[Unset, str] = UNSET
    unsupported: Union[Unset, bool] = UNSET
    stewarded_awareness: Union[Unset, bool] = UNSET
    stewarded_awareness_reason: Union[Unset, str] = UNSET
    stewarded_awareness_marked_by: Union[Unset, str] = UNSET
    stewarded_awareness_marked_at: Union[None, Unset, datetime.datetime] = UNSET
    notes: Union[Unset, str] = UNSET
    purl: Union[Unset, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        component_name = self.component_name

        repository_url = self.repository_url

        security_contact = self.security_contact

        contact_method: Union[Unset, str]
        if isinstance(self.contact_method, Unset):
            contact_method = UNSET
        elif isinstance(self.contact_method, ContactMethodEnum):
            contact_method = UNSET
            if not isinstance(self.contact_method, Unset):
                contact_method = ContactMethodEnum(self.contact_method).value

        else:
            contact_method = UNSET
            if not isinstance(self.contact_method, Unset):
                contact_method = BlankEnum(self.contact_method).value

        contact_url = self.contact_url

        source = self.source

        confidence = self.confidence

        verified_at: Union[None, Unset, str]
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        elif isinstance(self.verified_at, datetime.datetime):
            verified_at = UNSET
            if not isinstance(self.verified_at, Unset):
                verified_at = self.verified_at.isoformat()

        else:
            verified_at = self.verified_at

        verified_by = self.verified_by

        unsupported = self.unsupported

        stewarded_awareness = self.stewarded_awareness

        stewarded_awareness_reason = self.stewarded_awareness_reason

        stewarded_awareness_marked_by = self.stewarded_awareness_marked_by

        stewarded_awareness_marked_at: Union[None, Unset, str]
        if isinstance(self.stewarded_awareness_marked_at, Unset):
            stewarded_awareness_marked_at = UNSET
        elif isinstance(self.stewarded_awareness_marked_at, datetime.datetime):
            stewarded_awareness_marked_at = UNSET
            if not isinstance(self.stewarded_awareness_marked_at, Unset):
                stewarded_awareness_marked_at = (
                    self.stewarded_awareness_marked_at.isoformat()
                )

        else:
            stewarded_awareness_marked_at = self.stewarded_awareness_marked_at

        notes = self.notes

        purl = self.purl

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
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(component_name, Unset):
            field_dict["component_name"] = component_name
        if not isinstance(repository_url, Unset):
            field_dict["repository_url"] = repository_url
        if not isinstance(security_contact, Unset):
            field_dict["security_contact"] = security_contact
        if not isinstance(contact_method, Unset):
            field_dict["contact_method"] = contact_method
        if not isinstance(contact_url, Unset):
            field_dict["contact_url"] = contact_url
        if not isinstance(source, Unset):
            field_dict["source"] = source
        if not isinstance(confidence, Unset):
            field_dict["confidence"] = confidence
        if not isinstance(verified_at, Unset):
            field_dict["verified_at"] = verified_at
        if not isinstance(verified_by, Unset):
            field_dict["verified_by"] = verified_by
        if not isinstance(unsupported, Unset):
            field_dict["unsupported"] = unsupported
        if not isinstance(stewarded_awareness, Unset):
            field_dict["stewarded_awareness"] = stewarded_awareness
        if not isinstance(stewarded_awareness_reason, Unset):
            field_dict["stewarded_awareness_reason"] = stewarded_awareness_reason
        if not isinstance(stewarded_awareness_marked_by, Unset):
            field_dict["stewarded_awareness_marked_by"] = stewarded_awareness_marked_by
        if not isinstance(stewarded_awareness_marked_at, Unset):
            field_dict["stewarded_awareness_marked_at"] = stewarded_awareness_marked_at
        if not isinstance(notes, Unset):
            field_dict["notes"] = notes
        if not isinstance(purl, Unset):
            field_dict["purl"] = purl
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

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        component_name = d.pop("component_name", UNSET)

        repository_url = d.pop("repository_url", UNSET)

        security_contact = d.pop("security_contact", UNSET)

        def _parse_contact_method(
            data: object,
        ) -> Union[BlankEnum, ContactMethodEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _contact_method_type_0 = data
                contact_method_type_0: ContactMethodEnum
                if isinstance(_contact_method_type_0, Unset):
                    contact_method_type_0 = UNSET
                else:
                    contact_method_type_0 = ContactMethodEnum(_contact_method_type_0)

                return contact_method_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _contact_method_type_1 = data
            contact_method_type_1: BlankEnum
            if isinstance(_contact_method_type_1, Unset):
                contact_method_type_1 = UNSET
            else:
                contact_method_type_1 = BlankEnum(_contact_method_type_1)

            return contact_method_type_1

        contact_method = _parse_contact_method(d.pop("contact_method", UNSET))

        contact_url = d.pop("contact_url", UNSET)

        source = d.pop("source", UNSET)

        confidence = d.pop("confidence", UNSET)

        def _parse_verified_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _verified_at_type_0 = data
                verified_at_type_0: datetime.datetime
                if isinstance(_verified_at_type_0, Unset):
                    verified_at_type_0 = UNSET
                else:
                    verified_at_type_0 = isoparse(_verified_at_type_0)

                return verified_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        verified_at = _parse_verified_at(d.pop("verified_at", UNSET))

        verified_by = d.pop("verified_by", UNSET)

        unsupported = d.pop("unsupported", UNSET)

        stewarded_awareness = d.pop("stewarded_awareness", UNSET)

        stewarded_awareness_reason = d.pop("stewarded_awareness_reason", UNSET)

        stewarded_awareness_marked_by = d.pop("stewarded_awareness_marked_by", UNSET)

        def _parse_stewarded_awareness_marked_at(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _stewarded_awareness_marked_at_type_0 = data
                stewarded_awareness_marked_at_type_0: datetime.datetime
                if isinstance(_stewarded_awareness_marked_at_type_0, Unset):
                    stewarded_awareness_marked_at_type_0 = UNSET
                else:
                    stewarded_awareness_marked_at_type_0 = isoparse(
                        _stewarded_awareness_marked_at_type_0
                    )

                return stewarded_awareness_marked_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        stewarded_awareness_marked_at = _parse_stewarded_awareness_marked_at(
            d.pop("stewarded_awareness_marked_at", UNSET)
        )

        notes = d.pop("notes", UNSET)

        purl = d.pop("purl", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        regulatory_reporting_api_v1_upstream_projects_create_response_201 = cls(
            created_dt=created_dt,
            uuid=uuid,
            component_name=component_name,
            repository_url=repository_url,
            security_contact=security_contact,
            contact_method=contact_method,
            contact_url=contact_url,
            source=source,
            confidence=confidence,
            verified_at=verified_at,
            verified_by=verified_by,
            unsupported=unsupported,
            stewarded_awareness=stewarded_awareness,
            stewarded_awareness_reason=stewarded_awareness_reason,
            stewarded_awareness_marked_by=stewarded_awareness_marked_by,
            stewarded_awareness_marked_at=stewarded_awareness_marked_at,
            notes=notes,
            purl=purl,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        regulatory_reporting_api_v1_upstream_projects_create_response_201.additional_properties = d
        return regulatory_reporting_api_v1_upstream_projects_create_response_201

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
