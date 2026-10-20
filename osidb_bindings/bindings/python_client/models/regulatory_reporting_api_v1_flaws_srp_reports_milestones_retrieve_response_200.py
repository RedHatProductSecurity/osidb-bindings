import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..models.milestone_type_enum import MilestoneTypeEnum
from ..models.srp_report_milestone_status_enum import SRPReportMilestoneStatusEnum
from ..models.visibility_enum import VisibilityEnum
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert
    from ..models.srp_report_milestone_additional_details import (
        SRPReportMilestoneAdditionalDetails,
    )
    from ..models.srp_report_milestone_payload_fields_item import (
        SRPReportMilestonePayloadFieldsItem,
    )


T = TypeVar(
    "T", bound="RegulatoryReportingApiV1FlawsSrpReportsMilestonesRetrieveResponse200"
)


@_attrs_define
class RegulatoryReportingApiV1FlawsSrpReportsMilestonesRetrieveResponse200(OSIDBModel):
    """
    Attributes:
        uuid (UUID):
        srp_report (UUID): The SRP report this milestone belongs to
        milestone_type (MilestoneTypeEnum):
        payload_fields (list['SRPReportMilestonePayloadFieldsItem']): Ordered SRP payload form fields with labels,
            values, input type, requiredness, editability, and options for this milestone.
        missing_required_fields (str): Missing required fields
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        hours_remaining (Union[None, int]):
        days_remaining (Union[None, int]):
        is_overdue (bool):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        visibility (VisibilityEnum):
        alerts (list['Alert']):
        status (Union[Unset, SRPReportMilestoneStatusEnum]):
        additional_details (Union[Unset, SRPReportMilestoneAdditionalDetails]): Coordinator-provided SRP FAQ fields for
            this milestone stage. OSIM stores and reads these as individual form fields. Values here override auto-derived
            payload fields at submission time.
        submitted_at (Union[None, Unset, datetime.datetime]): When this milestone was submitted
        owner (Union[Unset, str]): Owner of this milestone
        mitigation_created_at (Union[None, Unset, datetime.datetime]): When the mitigation or patch became available
        mitigation_link (Union[Unset, str]): Link to the mitigation or patch used for reporting
        manual_completion_notes (Union[Unset, str]): Manual completion notes
        due_at (Union[None, Unset, datetime.datetime]):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    uuid: UUID
    srp_report: UUID
    milestone_type: MilestoneTypeEnum
    payload_fields: list["SRPReportMilestonePayloadFieldsItem"]
    missing_required_fields: str
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    hours_remaining: Union[None, int]
    days_remaining: Union[None, int]
    is_overdue: bool
    embargoed: bool
    visibility: VisibilityEnum
    alerts: list["Alert"]
    status: Union[Unset, SRPReportMilestoneStatusEnum] = UNSET
    additional_details: Union[Unset, "SRPReportMilestoneAdditionalDetails"] = UNSET
    submitted_at: Union[None, Unset, datetime.datetime] = UNSET
    owner: Union[Unset, str] = UNSET
    mitigation_created_at: Union[None, Unset, datetime.datetime] = UNSET
    mitigation_link: Union[Unset, str] = UNSET
    manual_completion_notes: Union[Unset, str] = UNSET
    due_at: Union[None, Unset, datetime.datetime] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        srp_report: str = UNSET
        if not isinstance(self.srp_report, Unset):
            srp_report = str(self.srp_report)

        milestone_type: str = UNSET
        if not isinstance(self.milestone_type, Unset):
            milestone_type = MilestoneTypeEnum(self.milestone_type).value

        payload_fields: list[dict[str, Any]] = UNSET
        if not isinstance(self.payload_fields, Unset):
            payload_fields = []
            for payload_fields_item_data in self.payload_fields:
                payload_fields_item: dict[str, Any] = UNSET
                if not isinstance(payload_fields_item_data, Unset):
                    payload_fields_item = payload_fields_item_data.to_dict()

                payload_fields.append(payload_fields_item)

        missing_required_fields = self.missing_required_fields

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        hours_remaining: Union[None, int]
        if isinstance(self.hours_remaining, Unset):
            hours_remaining = UNSET
        hours_remaining = self.hours_remaining

        days_remaining: Union[None, int]
        if isinstance(self.days_remaining, Unset):
            days_remaining = UNSET
        days_remaining = self.days_remaining

        is_overdue = self.is_overdue

        embargoed = self.embargoed

        visibility: str = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = VisibilityEnum(self.visibility).value

        alerts: list[dict[str, Any]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                alerts.append(alerts_item)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = SRPReportMilestoneStatusEnum(self.status).value

        additional_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.additional_details, Unset):
            additional_details = self.additional_details.to_dict()

        submitted_at: Union[None, Unset, str]
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = UNSET
            if not isinstance(self.submitted_at, Unset):
                submitted_at = self.submitted_at.isoformat()

        else:
            submitted_at = self.submitted_at

        owner = self.owner

        mitigation_created_at: Union[None, Unset, str]
        if isinstance(self.mitigation_created_at, Unset):
            mitigation_created_at = UNSET
        elif isinstance(self.mitigation_created_at, datetime.datetime):
            mitigation_created_at = UNSET
            if not isinstance(self.mitigation_created_at, Unset):
                mitigation_created_at = self.mitigation_created_at.isoformat()

        else:
            mitigation_created_at = self.mitigation_created_at

        mitigation_link: Union[Unset, str]
        if isinstance(self.mitigation_link, Unset):
            mitigation_link = UNSET
        else:
            mitigation_link = self.mitigation_link

        manual_completion_notes = self.manual_completion_notes

        due_at: Union[None, Unset, str]
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = UNSET
            if not isinstance(self.due_at, Unset):
                due_at = self.due_at.isoformat()

        else:
            due_at = self.due_at

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
        if not isinstance(srp_report, Unset):
            field_dict["srp_report"] = srp_report
        if not isinstance(milestone_type, Unset):
            field_dict["milestone_type"] = milestone_type
        if not isinstance(payload_fields, Unset):
            field_dict["payload_fields"] = payload_fields
        if not isinstance(missing_required_fields, Unset):
            field_dict["missing_required_fields"] = missing_required_fields
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(hours_remaining, Unset):
            field_dict["hours_remaining"] = hours_remaining
        if not isinstance(days_remaining, Unset):
            field_dict["days_remaining"] = days_remaining
        if not isinstance(is_overdue, Unset):
            field_dict["is_overdue"] = is_overdue
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(visibility, Unset):
            field_dict["visibility"] = visibility
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(additional_details, Unset):
            field_dict["additional_details"] = additional_details
        if not isinstance(submitted_at, Unset):
            field_dict["submitted_at"] = submitted_at
        if not isinstance(owner, Unset):
            field_dict["owner"] = owner
        if not isinstance(mitigation_created_at, Unset):
            field_dict["mitigation_created_at"] = mitigation_created_at
        if not isinstance(mitigation_link, Unset):
            field_dict["mitigation_link"] = mitigation_link
        if not isinstance(manual_completion_notes, Unset):
            field_dict["manual_completion_notes"] = manual_completion_notes
        if not isinstance(due_at, Unset):
            field_dict["due_at"] = due_at
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
        from ..models.srp_report_milestone_additional_details import (
            SRPReportMilestoneAdditionalDetails,
        )
        from ..models.srp_report_milestone_payload_fields_item import (
            SRPReportMilestonePayloadFieldsItem,
        )

        d = src_dict.copy()
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        _srp_report = d.pop("srp_report", UNSET)
        srp_report: UUID
        if isinstance(_srp_report, Unset):
            srp_report = UNSET
        else:
            srp_report = (
                _srp_report if isinstance(_srp_report, UUID) else UUID(_srp_report)
            )

        _milestone_type = d.pop("milestone_type", UNSET)
        milestone_type: MilestoneTypeEnum
        if isinstance(_milestone_type, Unset):
            milestone_type = UNSET
        else:
            milestone_type = MilestoneTypeEnum(_milestone_type)

        payload_fields = []
        _payload_fields = d.pop("payload_fields", UNSET)
        for payload_fields_item_data in _payload_fields or []:
            _payload_fields_item = payload_fields_item_data
            payload_fields_item: SRPReportMilestonePayloadFieldsItem
            if isinstance(_payload_fields_item, Unset):
                payload_fields_item = UNSET
            else:
                payload_fields_item = SRPReportMilestonePayloadFieldsItem.from_dict(
                    _payload_fields_item
                )

            payload_fields.append(payload_fields_item)

        missing_required_fields = d.pop("missing_required_fields", UNSET)

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

        def _parse_hours_remaining(data: object) -> Union[None, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, int], data)

        hours_remaining = _parse_hours_remaining(d.pop("hours_remaining", UNSET))

        def _parse_days_remaining(data: object) -> Union[None, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, int], data)

        days_remaining = _parse_days_remaining(d.pop("days_remaining", UNSET))

        is_overdue = d.pop("is_overdue", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: VisibilityEnum
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = VisibilityEnum(_visibility)

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

        _status = d.pop("status", UNSET)
        status: Union[Unset, SRPReportMilestoneStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SRPReportMilestoneStatusEnum(_status)

        _additional_details = d.pop("additional_details", UNSET)
        additional_details: Union[Unset, SRPReportMilestoneAdditionalDetails]
        if isinstance(_additional_details, Unset):
            additional_details = UNSET
        else:
            additional_details = SRPReportMilestoneAdditionalDetails.from_dict(
                _additional_details
            )

        def _parse_submitted_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _submitted_at_type_0 = data
                submitted_at_type_0: datetime.datetime
                if isinstance(_submitted_at_type_0, Unset):
                    submitted_at_type_0 = UNSET
                else:
                    submitted_at_type_0 = isoparse(_submitted_at_type_0)

                return submitted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at", UNSET))

        owner = d.pop("owner", UNSET)

        def _parse_mitigation_created_at(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _mitigation_created_at_type_0 = data
                mitigation_created_at_type_0: datetime.datetime
                if isinstance(_mitigation_created_at_type_0, Unset):
                    mitigation_created_at_type_0 = UNSET
                else:
                    mitigation_created_at_type_0 = isoparse(
                        _mitigation_created_at_type_0
                    )

                return mitigation_created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        mitigation_created_at = _parse_mitigation_created_at(
            d.pop("mitigation_created_at", UNSET)
        )

        def _parse_mitigation_link(data: object) -> Union[Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, str], data)

        mitigation_link = _parse_mitigation_link(d.pop("mitigation_link", UNSET))

        manual_completion_notes = d.pop("manual_completion_notes", UNSET)

        def _parse_due_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _due_at_type_0 = data
                due_at_type_0: datetime.datetime
                if isinstance(_due_at_type_0, Unset):
                    due_at_type_0 = UNSET
                else:
                    due_at_type_0 = isoparse(_due_at_type_0)

                return due_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        due_at = _parse_due_at(d.pop("due_at", UNSET))

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        regulatory_reporting_api_v1_flaws_srp_reports_milestones_retrieve_response_200 = cls(
            uuid=uuid,
            srp_report=srp_report,
            milestone_type=milestone_type,
            payload_fields=payload_fields,
            missing_required_fields=missing_required_fields,
            created_dt=created_dt,
            updated_dt=updated_dt,
            hours_remaining=hours_remaining,
            days_remaining=days_remaining,
            is_overdue=is_overdue,
            embargoed=embargoed,
            visibility=visibility,
            alerts=alerts,
            status=status,
            additional_details=additional_details,
            submitted_at=submitted_at,
            owner=owner,
            mitigation_created_at=mitigation_created_at,
            mitigation_link=mitigation_link,
            manual_completion_notes=manual_completion_notes,
            due_at=due_at,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        regulatory_reporting_api_v1_flaws_srp_reports_milestones_retrieve_response_200.additional_properties = d
        return regulatory_reporting_api_v1_flaws_srp_reports_milestones_retrieve_response_200

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
