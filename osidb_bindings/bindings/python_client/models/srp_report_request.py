import datetime
import json
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..models.reportable_event_type_enum import ReportableEventTypeEnum
from ..models.responsibility_scope_enum import ResponsibilityScopeEnum
from ..models.srp_report_status_enum import SRPReportStatusEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="SRPReportRequest")


@_attrs_define
class SRPReportRequest(OSIDBModel):
    """Serializer for SRP Reports.

    Includes nested milestones. meta_attr is opt-in via include_meta_attr.

        Attributes:
            title (str): Title of the SRP report
            responsibility_scope (ResponsibilityScopeEnum):
            reportable_event_type (ReportableEventTypeEnum):
            updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
                detect mit-air collisions.
            manufacturer_or_steward_name (Union[Unset, str]): Name of the manufacturer or steward
            status (Union[Unset, SRPReportStatusEnum]):
            evidence (Union[Unset, str]): Justification for manually creating this SRP report when automatic criteria were
                not met
            timer_started_at (Union[None, Unset, datetime.datetime]): When the SLA clock started for this report
            srp_reference_id (Union[Unset, str]): Reference ID returned by the SRP after submission
            srp_reference_url (Union[Unset, str]): URL of the SRP reference
            member_states_available (Union[Unset, list[str]]): List of EU member state codes where product is available
            designated_csirt_country (Union[Unset, str]): Country code of the designated CSIRT coordinator
            designated_csirt_source (Union[Unset, str]): Source of the designated CSIRT coordinator
            manual_completion_notes (Union[Unset, str]): Manual completion notes
    """

    title: str
    responsibility_scope: ResponsibilityScopeEnum
    reportable_event_type: ReportableEventTypeEnum
    updated_dt: datetime.datetime
    manufacturer_or_steward_name: Union[Unset, str] = UNSET
    status: Union[Unset, SRPReportStatusEnum] = UNSET
    evidence: Union[Unset, str] = UNSET
    timer_started_at: Union[None, Unset, datetime.datetime] = UNSET
    srp_reference_id: Union[Unset, str] = UNSET
    srp_reference_url: Union[Unset, str] = UNSET
    member_states_available: Union[Unset, list[str]] = UNSET
    designated_csirt_country: Union[Unset, str] = UNSET
    designated_csirt_source: Union[Unset, str] = UNSET
    manual_completion_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        responsibility_scope: str = UNSET
        if not isinstance(self.responsibility_scope, Unset):
            responsibility_scope = ResponsibilityScopeEnum(
                self.responsibility_scope
            ).value

        reportable_event_type: str = UNSET
        if not isinstance(self.reportable_event_type, Unset):
            reportable_event_type = ReportableEventTypeEnum(
                self.reportable_event_type
            ).value

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        manufacturer_or_steward_name = self.manufacturer_or_steward_name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = SRPReportStatusEnum(self.status).value

        evidence = self.evidence

        timer_started_at: Union[None, Unset, str]
        if isinstance(self.timer_started_at, Unset):
            timer_started_at = UNSET
        elif isinstance(self.timer_started_at, datetime.datetime):
            timer_started_at = UNSET
            if not isinstance(self.timer_started_at, Unset):
                timer_started_at = self.timer_started_at.isoformat()

        else:
            timer_started_at = self.timer_started_at

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
        if not isinstance(title, Unset):
            field_dict["title"] = title
        if not isinstance(responsibility_scope, Unset):
            field_dict["responsibility_scope"] = responsibility_scope
        if not isinstance(reportable_event_type, Unset):
            field_dict["reportable_event_type"] = reportable_event_type
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(manufacturer_or_steward_name, Unset):
            field_dict["manufacturer_or_steward_name"] = manufacturer_or_steward_name
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(evidence, Unset):
            field_dict["evidence"] = evidence
        if not isinstance(timer_started_at, Unset):
            field_dict["timer_started_at"] = timer_started_at
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
        title = (None, str(self.title).encode(), "text/plain")

        responsibility_scope: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.responsibility_scope, Unset):
            responsibility_scope = (
                None,
                str(self.responsibility_scope.value).encode(),
                "text/plain",
            )

        reportable_event_type: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.reportable_event_type, Unset):
            reportable_event_type = (
                None,
                str(self.reportable_event_type.value).encode(),
                "text/plain",
            )

        updated_dt: bytes = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat().encode()

        manufacturer_or_steward_name = (
            self.manufacturer_or_steward_name
            if isinstance(self.manufacturer_or_steward_name, Unset)
            else (None, str(self.manufacturer_or_steward_name).encode(), "text/plain")
        )

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        evidence = (
            self.evidence
            if isinstance(self.evidence, Unset)
            else (None, str(self.evidence).encode(), "text/plain")
        )

        timer_started_at: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.timer_started_at, Unset):
            timer_started_at = UNSET
        elif isinstance(self.timer_started_at, datetime.datetime):
            timer_started_at: bytes = UNSET
            if not isinstance(self.timer_started_at, Unset):
                timer_started_at = self.timer_started_at.isoformat().encode()
        else:
            timer_started_at = (None, str(self.timer_started_at).encode(), "text/plain")

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

        if not isinstance(title, Unset):
            field_dict["title"] = title
        if not isinstance(responsibility_scope, Unset):
            field_dict["responsibility_scope"] = responsibility_scope
        if not isinstance(reportable_event_type, Unset):
            field_dict["reportable_event_type"] = reportable_event_type
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(manufacturer_or_steward_name, Unset):
            field_dict["manufacturer_or_steward_name"] = manufacturer_or_steward_name
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(evidence, Unset):
            field_dict["evidence"] = evidence
        if not isinstance(timer_started_at, Unset):
            field_dict["timer_started_at"] = timer_started_at
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
        title = d.pop("title", UNSET)

        _responsibility_scope = d.pop("responsibility_scope", UNSET)
        responsibility_scope: ResponsibilityScopeEnum
        if isinstance(_responsibility_scope, Unset):
            responsibility_scope = UNSET
        else:
            responsibility_scope = ResponsibilityScopeEnum(_responsibility_scope)

        _reportable_event_type = d.pop("reportable_event_type", UNSET)
        reportable_event_type: ReportableEventTypeEnum
        if isinstance(_reportable_event_type, Unset):
            reportable_event_type = UNSET
        else:
            reportable_event_type = ReportableEventTypeEnum(_reportable_event_type)

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        manufacturer_or_steward_name = d.pop("manufacturer_or_steward_name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SRPReportStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SRPReportStatusEnum(_status)

        evidence = d.pop("evidence", UNSET)

        def _parse_timer_started_at(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _timer_started_at_type_0 = data
                timer_started_at_type_0: datetime.datetime
                if isinstance(_timer_started_at_type_0, Unset):
                    timer_started_at_type_0 = UNSET
                else:
                    timer_started_at_type_0 = isoparse(_timer_started_at_type_0)

                return timer_started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        timer_started_at = _parse_timer_started_at(d.pop("timer_started_at", UNSET))

        srp_reference_id = d.pop("srp_reference_id", UNSET)

        srp_reference_url = d.pop("srp_reference_url", UNSET)

        member_states_available = cast(
            list[str], d.pop("member_states_available", UNSET)
        )

        designated_csirt_country = d.pop("designated_csirt_country", UNSET)

        designated_csirt_source = d.pop("designated_csirt_source", UNSET)

        manual_completion_notes = d.pop("manual_completion_notes", UNSET)

        srp_report_request = cls(
            title=title,
            responsibility_scope=responsibility_scope,
            reportable_event_type=reportable_event_type,
            updated_dt=updated_dt,
            manufacturer_or_steward_name=manufacturer_or_steward_name,
            status=status,
            evidence=evidence,
            timer_started_at=timer_started_at,
            srp_reference_id=srp_reference_id,
            srp_reference_url=srp_reference_url,
            member_states_available=member_states_available,
            designated_csirt_country=designated_csirt_country,
            designated_csirt_source=designated_csirt_source,
            manual_completion_notes=manual_completion_notes,
        )

        srp_report_request.additional_properties = d
        return srp_report_request

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
