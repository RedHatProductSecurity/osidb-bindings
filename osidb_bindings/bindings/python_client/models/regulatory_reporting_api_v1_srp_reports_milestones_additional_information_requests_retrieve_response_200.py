import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..models.srp_report_milestone_status_enum import SRPReportMilestoneStatusEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar(
    "T",
    bound="RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsRetrieveResponse200",
)


@_attrs_define
class RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsRetrieveResponse200(
    OSIDBModel
):
    """
    Attributes:
        uuid (UUID):
        milestone (UUID): The milestone this additional information request belongs to
        acl_read (list[UUID]):
        acl_write (list[UUID]):
        due_at (Union[None, datetime.datetime]):
        hours_remaining (Union[None, int]):
        days_remaining (Union[None, int]):
        is_overdue (bool):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        request_received_at (Union[None, Unset, datetime.datetime]): When the request was received
        request_source (Union[Unset, str]): Source of the request
        request_text (Union[Unset, str]): Text of the request
        response_text (Union[Unset, str]): Text of the response
        owner (Union[Unset, str]): Owner of this additional information request
        status (Union[Unset, SRPReportMilestoneStatusEnum]):
        manual_due_at (Union[None, Unset, datetime.datetime]): Manual override for the due date
        manual_completion_notes (Union[Unset, str]): Manual completion notes
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    uuid: UUID
    milestone: UUID
    acl_read: list[UUID]
    acl_write: list[UUID]
    due_at: Union[None, datetime.datetime]
    hours_remaining: Union[None, int]
    days_remaining: Union[None, int]
    is_overdue: bool
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    request_received_at: Union[None, Unset, datetime.datetime] = UNSET
    request_source: Union[Unset, str] = UNSET
    request_text: Union[Unset, str] = UNSET
    response_text: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    status: Union[Unset, SRPReportMilestoneStatusEnum] = UNSET
    manual_due_at: Union[None, Unset, datetime.datetime] = UNSET
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

        milestone: str = UNSET
        if not isinstance(self.milestone, Unset):
            milestone = str(self.milestone)

        acl_read: list[str] = UNSET
        if not isinstance(self.acl_read, Unset):
            acl_read = []
            for acl_read_item_data in self.acl_read:
                acl_read_item: str = UNSET
                if not isinstance(acl_read_item_data, Unset):
                    acl_read_item = str(acl_read_item_data)

                acl_read.append(acl_read_item)

        acl_write: list[str] = UNSET
        if not isinstance(self.acl_write, Unset):
            acl_write = []
            for acl_write_item_data in self.acl_write:
                acl_write_item: str = UNSET
                if not isinstance(acl_write_item_data, Unset):
                    acl_write_item = str(acl_write_item_data)

                acl_write.append(acl_write_item)

        due_at: Union[None, str]
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = UNSET
            if not isinstance(self.due_at, Unset):
                due_at = self.due_at.isoformat()

        else:
            due_at = self.due_at

        hours_remaining: Union[None, int]
        if isinstance(self.hours_remaining, Unset):
            hours_remaining = UNSET
        hours_remaining = self.hours_remaining

        days_remaining: Union[None, int]
        if isinstance(self.days_remaining, Unset):
            days_remaining = UNSET
        days_remaining = self.days_remaining

        is_overdue = self.is_overdue

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        request_received_at: Union[None, Unset, str]
        if isinstance(self.request_received_at, Unset):
            request_received_at = UNSET
        elif isinstance(self.request_received_at, datetime.datetime):
            request_received_at = UNSET
            if not isinstance(self.request_received_at, Unset):
                request_received_at = self.request_received_at.isoformat()

        else:
            request_received_at = self.request_received_at

        request_source = self.request_source

        request_text = self.request_text

        response_text = self.response_text

        owner = self.owner

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = SRPReportMilestoneStatusEnum(self.status).value

        manual_due_at: Union[None, Unset, str]
        if isinstance(self.manual_due_at, Unset):
            manual_due_at = UNSET
        elif isinstance(self.manual_due_at, datetime.datetime):
            manual_due_at = UNSET
            if not isinstance(self.manual_due_at, Unset):
                manual_due_at = self.manual_due_at.isoformat()

        else:
            manual_due_at = self.manual_due_at

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
        if not isinstance(milestone, Unset):
            field_dict["milestone"] = milestone
        if not isinstance(acl_read, Unset):
            field_dict["acl_read"] = acl_read
        if not isinstance(acl_write, Unset):
            field_dict["acl_write"] = acl_write
        if not isinstance(due_at, Unset):
            field_dict["due_at"] = due_at
        if not isinstance(hours_remaining, Unset):
            field_dict["hours_remaining"] = hours_remaining
        if not isinstance(days_remaining, Unset):
            field_dict["days_remaining"] = days_remaining
        if not isinstance(is_overdue, Unset):
            field_dict["is_overdue"] = is_overdue
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(request_received_at, Unset):
            field_dict["request_received_at"] = request_received_at
        if not isinstance(request_source, Unset):
            field_dict["request_source"] = request_source
        if not isinstance(request_text, Unset):
            field_dict["request_text"] = request_text
        if not isinstance(response_text, Unset):
            field_dict["response_text"] = response_text
        if not isinstance(owner, Unset):
            field_dict["owner"] = owner
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(manual_due_at, Unset):
            field_dict["manual_due_at"] = manual_due_at
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
        d = src_dict.copy()
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        _milestone = d.pop("milestone", UNSET)
        milestone: UUID
        if isinstance(_milestone, Unset):
            milestone = UNSET
        else:
            milestone = _milestone if isinstance(_milestone, UUID) else UUID(_milestone)

        acl_read = []
        _acl_read = d.pop("acl_read", UNSET)
        for acl_read_item_data in _acl_read or []:
            _acl_read_item = acl_read_item_data
            acl_read_item: UUID
            if isinstance(_acl_read_item, Unset):
                acl_read_item = UNSET
            else:
                acl_read_item = (
                    _acl_read_item
                    if isinstance(_acl_read_item, UUID)
                    else UUID(_acl_read_item)
                )

            acl_read.append(acl_read_item)

        acl_write = []
        _acl_write = d.pop("acl_write", UNSET)
        for acl_write_item_data in _acl_write or []:
            _acl_write_item = acl_write_item_data
            acl_write_item: UUID
            if isinstance(_acl_write_item, Unset):
                acl_write_item = UNSET
            else:
                acl_write_item = (
                    _acl_write_item
                    if isinstance(_acl_write_item, UUID)
                    else UUID(_acl_write_item)
                )

            acl_write.append(acl_write_item)

        def _parse_due_at(data: object) -> Union[None, datetime.datetime]:
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
            return cast(Union[None, datetime.datetime], data)

        due_at = _parse_due_at(d.pop("due_at", UNSET))

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

        def _parse_request_received_at(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _request_received_at_type_0 = data
                request_received_at_type_0: datetime.datetime
                if isinstance(_request_received_at_type_0, Unset):
                    request_received_at_type_0 = UNSET
                else:
                    request_received_at_type_0 = isoparse(_request_received_at_type_0)

                return request_received_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        request_received_at = _parse_request_received_at(
            d.pop("request_received_at", UNSET)
        )

        request_source = d.pop("request_source", UNSET)

        request_text = d.pop("request_text", UNSET)

        response_text = d.pop("response_text", UNSET)

        owner = d.pop("owner", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SRPReportMilestoneStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SRPReportMilestoneStatusEnum(_status)

        def _parse_manual_due_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _manual_due_at_type_0 = data
                manual_due_at_type_0: datetime.datetime
                if isinstance(_manual_due_at_type_0, Unset):
                    manual_due_at_type_0 = UNSET
                else:
                    manual_due_at_type_0 = isoparse(_manual_due_at_type_0)

                return manual_due_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        manual_due_at = _parse_manual_due_at(d.pop("manual_due_at", UNSET))

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

        regulatory_reporting_api_v1_srp_reports_milestones_additional_information_requests_retrieve_response_200 = cls(
            uuid=uuid,
            milestone=milestone,
            acl_read=acl_read,
            acl_write=acl_write,
            due_at=due_at,
            hours_remaining=hours_remaining,
            days_remaining=days_remaining,
            is_overdue=is_overdue,
            created_dt=created_dt,
            updated_dt=updated_dt,
            request_received_at=request_received_at,
            request_source=request_source,
            request_text=request_text,
            response_text=response_text,
            owner=owner,
            status=status,
            manual_due_at=manual_due_at,
            manual_completion_notes=manual_completion_notes,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        regulatory_reporting_api_v1_srp_reports_milestones_additional_information_requests_retrieve_response_200.additional_properties = d
        return regulatory_reporting_api_v1_srp_reports_milestones_additional_information_requests_retrieve_response_200

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
