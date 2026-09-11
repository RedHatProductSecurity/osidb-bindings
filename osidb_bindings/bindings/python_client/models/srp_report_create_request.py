import json
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..models.reportable_event_type_enum import ReportableEventTypeEnum
from ..models.responsibility_scope_enum import ResponsibilityScopeEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="SRPReportCreateRequest")


@_attrs_define
class SRPReportCreateRequest(OSIDBModel):
    """Serializer for manually creating SRP Reports.

    Status is always EMPTY. ACLs are inherited from the flaw in the
    view's perform_create. evidence is required for manual create.
    srp_reference_id and srp_reference_url are optional. timer_started_at is
    read-only and remains null until the report transitions to IN_PROGRESS.

        Attributes:
            flaw_id (UUID): UUID of the flaw to create an SRP report for
            reportable_event_type (ReportableEventTypeEnum):
            evidence (str):
            title (Union[Unset, str]):
            manufacturer_or_steward_name (Union[Unset, str]): Name of the manufacturer or steward
            responsibility_scope (Union[Unset, ResponsibilityScopeEnum]):
            srp_reference_id (Union[Unset, str]):
            srp_reference_url (Union[Unset, str]):
            member_states_available (Union[Unset, list[str]]): List of EU member state codes where product is available
            designated_csirt_country (Union[Unset, str]): Country code of the designated CSIRT coordinator
            designated_csirt_source (Union[Unset, str]): Source of the designated CSIRT coordinator
            manual_completion_notes (Union[Unset, str]): Manual completion notes
    """

    flaw_id: UUID
    reportable_event_type: ReportableEventTypeEnum
    evidence: str
    title: Union[Unset, str] = UNSET
    manufacturer_or_steward_name: Union[Unset, str] = UNSET
    responsibility_scope: Union[Unset, ResponsibilityScopeEnum] = UNSET
    srp_reference_id: Union[Unset, str] = UNSET
    srp_reference_url: Union[Unset, str] = UNSET
    member_states_available: Union[Unset, list[str]] = UNSET
    designated_csirt_country: Union[Unset, str] = UNSET
    designated_csirt_source: Union[Unset, str] = UNSET
    manual_completion_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flaw_id: str = UNSET
        if not isinstance(self.flaw_id, Unset):
            flaw_id = str(self.flaw_id)

        reportable_event_type: str = UNSET
        if not isinstance(self.reportable_event_type, Unset):
            reportable_event_type = ReportableEventTypeEnum(
                self.reportable_event_type
            ).value

        evidence = self.evidence

        title = self.title

        manufacturer_or_steward_name = self.manufacturer_or_steward_name

        responsibility_scope: Union[Unset, str] = UNSET
        if not isinstance(self.responsibility_scope, Unset):
            responsibility_scope = ResponsibilityScopeEnum(
                self.responsibility_scope
            ).value

        srp_reference_id = self.srp_reference_id

        srp_reference_url = self.srp_reference_url

        member_states_available: Union[Unset, list[str]] = UNSET
        if not isinstance(self.member_states_available, Unset):
            member_states_available = self.member_states_available

        designated_csirt_country = self.designated_csirt_country

        designated_csirt_source = self.designated_csirt_source

        manual_completion_notes = self.manual_completion_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(flaw_id, Unset):
            field_dict["flaw_id"] = flaw_id
        if not isinstance(reportable_event_type, Unset):
            field_dict["reportable_event_type"] = reportable_event_type
        if not isinstance(evidence, Unset):
            field_dict["evidence"] = evidence
        if not isinstance(title, Unset):
            field_dict["title"] = title
        if not isinstance(manufacturer_or_steward_name, Unset):
            field_dict["manufacturer_or_steward_name"] = manufacturer_or_steward_name
        if not isinstance(responsibility_scope, Unset):
            field_dict["responsibility_scope"] = responsibility_scope
        if not isinstance(srp_reference_id, Unset):
            field_dict["srp_reference_id"] = srp_reference_id
        if not isinstance(srp_reference_url, Unset):
            field_dict["srp_reference_url"] = srp_reference_url
        if not isinstance(member_states_available, Unset):
            field_dict["member_states_available"] = member_states_available
        if not isinstance(designated_csirt_country, Unset):
            field_dict["designated_csirt_country"] = designated_csirt_country
        if not isinstance(designated_csirt_source, Unset):
            field_dict["designated_csirt_source"] = designated_csirt_source
        if not isinstance(manual_completion_notes, Unset):
            field_dict["manual_completion_notes"] = manual_completion_notes

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        flaw_id: bytes = UNSET
        if not isinstance(self.flaw_id, Unset):
            flaw_id = str(self.flaw_id)

        reportable_event_type: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.reportable_event_type, Unset):
            reportable_event_type = (
                None,
                str(self.reportable_event_type.value).encode(),
                "text/plain",
            )

        evidence = (None, str(self.evidence).encode(), "text/plain")

        title = (
            self.title
            if isinstance(self.title, Unset)
            else (None, str(self.title).encode(), "text/plain")
        )

        manufacturer_or_steward_name = (
            self.manufacturer_or_steward_name
            if isinstance(self.manufacturer_or_steward_name, Unset)
            else (None, str(self.manufacturer_or_steward_name).encode(), "text/plain")
        )

        responsibility_scope: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.responsibility_scope, Unset):
            responsibility_scope = (
                None,
                str(self.responsibility_scope.value).encode(),
                "text/plain",
            )

        srp_reference_id = (
            self.srp_reference_id
            if isinstance(self.srp_reference_id, Unset)
            else (None, str(self.srp_reference_id).encode(), "text/plain")
        )

        srp_reference_url = (
            self.srp_reference_url
            if isinstance(self.srp_reference_url, Unset)
            else (None, str(self.srp_reference_url).encode(), "text/plain")
        )

        member_states_available: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.member_states_available, Unset):
            _temp_member_states_available = self.member_states_available
            member_states_available = (
                None,
                json.dumps(_temp_member_states_available).encode(),
                "application/json",
            )

        designated_csirt_country = (
            self.designated_csirt_country
            if isinstance(self.designated_csirt_country, Unset)
            else (None, str(self.designated_csirt_country).encode(), "text/plain")
        )

        designated_csirt_source = (
            self.designated_csirt_source
            if isinstance(self.designated_csirt_source, Unset)
            else (None, str(self.designated_csirt_source).encode(), "text/plain")
        )

        manual_completion_notes = (
            self.manual_completion_notes
            if isinstance(self.manual_completion_notes, Unset)
            else (None, str(self.manual_completion_notes).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(flaw_id, Unset):
            field_dict["flaw_id"] = flaw_id
        if not isinstance(reportable_event_type, Unset):
            field_dict["reportable_event_type"] = reportable_event_type
        if not isinstance(evidence, Unset):
            field_dict["evidence"] = evidence
        if not isinstance(title, Unset):
            field_dict["title"] = title
        if not isinstance(manufacturer_or_steward_name, Unset):
            field_dict["manufacturer_or_steward_name"] = manufacturer_or_steward_name
        if not isinstance(responsibility_scope, Unset):
            field_dict["responsibility_scope"] = responsibility_scope
        if not isinstance(srp_reference_id, Unset):
            field_dict["srp_reference_id"] = srp_reference_id
        if not isinstance(srp_reference_url, Unset):
            field_dict["srp_reference_url"] = srp_reference_url
        if not isinstance(member_states_available, Unset):
            field_dict["member_states_available"] = member_states_available
        if not isinstance(designated_csirt_country, Unset):
            field_dict["designated_csirt_country"] = designated_csirt_country
        if not isinstance(designated_csirt_source, Unset):
            field_dict["designated_csirt_source"] = designated_csirt_source
        if not isinstance(manual_completion_notes, Unset):
            field_dict["manual_completion_notes"] = manual_completion_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _flaw_id = d.pop("flaw_id", UNSET)
        flaw_id: UUID
        if isinstance(_flaw_id, Unset):
            flaw_id = UNSET
        else:
            flaw_id = _flaw_id if isinstance(_flaw_id, UUID) else UUID(_flaw_id)

        _reportable_event_type = d.pop("reportable_event_type", UNSET)
        reportable_event_type: ReportableEventTypeEnum
        if isinstance(_reportable_event_type, Unset):
            reportable_event_type = UNSET
        else:
            reportable_event_type = ReportableEventTypeEnum(_reportable_event_type)

        evidence = d.pop("evidence", UNSET)

        title = d.pop("title", UNSET)

        manufacturer_or_steward_name = d.pop("manufacturer_or_steward_name", UNSET)

        _responsibility_scope = d.pop("responsibility_scope", UNSET)
        responsibility_scope: Union[Unset, ResponsibilityScopeEnum]
        if isinstance(_responsibility_scope, Unset):
            responsibility_scope = UNSET
        else:
            responsibility_scope = ResponsibilityScopeEnum(_responsibility_scope)

        srp_reference_id = d.pop("srp_reference_id", UNSET)

        srp_reference_url = d.pop("srp_reference_url", UNSET)

        member_states_available = cast(
            list[str], d.pop("member_states_available", UNSET)
        )

        designated_csirt_country = d.pop("designated_csirt_country", UNSET)

        designated_csirt_source = d.pop("designated_csirt_source", UNSET)

        manual_completion_notes = d.pop("manual_completion_notes", UNSET)

        srp_report_create_request = cls(
            flaw_id=flaw_id,
            reportable_event_type=reportable_event_type,
            evidence=evidence,
            title=title,
            manufacturer_or_steward_name=manufacturer_or_steward_name,
            responsibility_scope=responsibility_scope,
            srp_reference_id=srp_reference_id,
            srp_reference_url=srp_reference_url,
            member_states_available=member_states_available,
            designated_csirt_country=designated_csirt_country,
            designated_csirt_source=designated_csirt_source,
            manual_completion_notes=manual_completion_notes,
        )

        srp_report_create_request.additional_properties = d
        return srp_report_create_request

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
