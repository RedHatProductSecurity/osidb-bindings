import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..models.reportable_event_type_enum import ReportableEventTypeEnum
from ..models.responsibility_scope_enum import ResponsibilityScopeEnum
from ..models.srp_report_status_enum import SRPReportStatusEnum
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert
    from ..models.srp_report_milestone import SRPReportMilestone


T = TypeVar("T", bound="RegulatoryReportingApiV1SrpReportsRetrieveResponse200")


@_attrs_define
class RegulatoryReportingApiV1SrpReportsRetrieveResponse200(OSIDBModel):
    """
    Attributes:
        uuid (UUID):
        flaw_id (UUID): The flaw for which this SRP report is being created
        title (str): Title of the SRP report
        responsibility_scope (ResponsibilityScopeEnum):
        reportable_event_type (ReportableEventTypeEnum):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        milestones (list['SRPReportMilestone']):
        alerts (list['Alert']):
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
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    uuid: UUID
    flaw_id: UUID
    title: str
    responsibility_scope: ResponsibilityScopeEnum
    reportable_event_type: ReportableEventTypeEnum
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    milestones: list["SRPReportMilestone"]
    alerts: list["Alert"]
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
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        flaw_id: str = UNSET
        if not isinstance(self.flaw_id, Unset):
            flaw_id = str(self.flaw_id)

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

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        milestones: list[dict[str, Any]] = UNSET
        if not isinstance(self.milestones, Unset):
            milestones = []
            for milestones_item_data in self.milestones:
                milestones_item: dict[str, Any] = UNSET
                if not isinstance(milestones_item_data, Unset):
                    milestones_item = milestones_item_data.to_dict()

                milestones.append(milestones_item)

        alerts: list[dict[str, Any]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                alerts.append(alerts_item)

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

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(flaw_id, Unset):
            field_dict["flaw_id"] = flaw_id
        if not isinstance(title, Unset):
            field_dict["title"] = title
        if not isinstance(responsibility_scope, Unset):
            field_dict["responsibility_scope"] = responsibility_scope
        if not isinstance(reportable_event_type, Unset):
            field_dict["reportable_event_type"] = reportable_event_type
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(milestones, Unset):
            field_dict["milestones"] = milestones
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
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
        from ..models.alert import Alert
        from ..models.srp_report_milestone import SRPReportMilestone

        d = src_dict.copy()
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        _flaw_id = d.pop("flaw_id", UNSET)
        flaw_id: UUID
        if isinstance(_flaw_id, Unset):
            flaw_id = UNSET
        else:
            flaw_id = _flaw_id if isinstance(_flaw_id, UUID) else UUID(_flaw_id)

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

        milestones = []
        _milestones = d.pop("milestones", UNSET)
        for milestones_item_data in _milestones or []:
            _milestones_item = milestones_item_data
            milestones_item: SRPReportMilestone
            if isinstance(_milestones_item, Unset):
                milestones_item = UNSET
            else:
                milestones_item = SRPReportMilestone.from_dict(_milestones_item)

            milestones.append(milestones_item)

        alerts = []
        _alerts = d.pop("alerts", UNSET)
        for alerts_item_data in _alerts or []:
            _alerts_item = alerts_item_data
            alerts_item: Alert
            if isinstance(_alerts_item, Unset):
                alerts_item = UNSET
            else:
                alerts_item = Alert.from_dict(_alerts_item)

            alerts.append(alerts_item)

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

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        regulatory_reporting_api_v1_srp_reports_retrieve_response_200 = cls(
            uuid=uuid,
            flaw_id=flaw_id,
            title=title,
            responsibility_scope=responsibility_scope,
            reportable_event_type=reportable_event_type,
            created_dt=created_dt,
            updated_dt=updated_dt,
            milestones=milestones,
            alerts=alerts,
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
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        regulatory_reporting_api_v1_srp_reports_retrieve_response_200.additional_properties = d
        return regulatory_reporting_api_v1_srp_reports_retrieve_response_200

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
