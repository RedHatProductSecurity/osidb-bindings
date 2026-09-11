import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.method_enum import MethodEnum
from ..models.reportability_reason_enum import ReportabilityReasonEnum
from ..models.upstream_notification_status_enum import UpstreamNotificationStatusEnum
from ..models.visibility_enum import VisibilityEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="RegulatoryReportingApiV1NotificationsUpstreamUpdateResponse200")


@_attrs_define
class RegulatoryReportingApiV1NotificationsUpstreamUpdateResponse200(OSIDBModel):
    """
    Attributes:
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        visibility (VisibilityEnum):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        uuid (UUID):
        flaw_uuid (UUID):
        last_error (str):
        upstream_project (Union[None, UUID, Unset]):
        status (Union[Unset, UpstreamNotificationStatusEnum]):
        reportability_reason (Union[BlankEnum, ReportabilityReasonEnum, Unset]):
        method (Union[BlankEnum, MethodEnum, Unset]):
        timer_started_at (Union[None, Unset, datetime.datetime]):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    embargoed: bool
    visibility: VisibilityEnum
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    uuid: UUID
    flaw_uuid: UUID
    last_error: str
    upstream_project: Union[None, UUID, Unset] = UNSET
    status: Union[Unset, UpstreamNotificationStatusEnum] = UNSET
    reportability_reason: Union[BlankEnum, ReportabilityReasonEnum, Unset] = UNSET
    method: Union[BlankEnum, MethodEnum, Unset] = UNSET
    timer_started_at: Union[None, Unset, datetime.datetime] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embargoed = self.embargoed

        visibility: str = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = VisibilityEnum(self.visibility).value

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

        last_error = self.last_error

        upstream_project: Union[None, Unset, str]
        if isinstance(self.upstream_project, Unset):
            upstream_project = UNSET
        elif isinstance(self.upstream_project, UUID):
            upstream_project = UNSET
            if not isinstance(self.upstream_project, Unset):
                upstream_project = str(self.upstream_project)

        else:
            upstream_project = self.upstream_project

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = UpstreamNotificationStatusEnum(self.status).value

        reportability_reason: Union[Unset, str]
        if isinstance(self.reportability_reason, Unset):
            reportability_reason = UNSET
        elif isinstance(self.reportability_reason, ReportabilityReasonEnum):
            reportability_reason = UNSET
            if not isinstance(self.reportability_reason, Unset):
                reportability_reason = ReportabilityReasonEnum(
                    self.reportability_reason
                ).value

        else:
            reportability_reason = UNSET
            if not isinstance(self.reportability_reason, Unset):
                reportability_reason = BlankEnum(self.reportability_reason).value

        method: Union[Unset, str]
        if isinstance(self.method, Unset):
            method = UNSET
        elif isinstance(self.method, MethodEnum):
            method = UNSET
            if not isinstance(self.method, Unset):
                method = MethodEnum(self.method).value

        else:
            method = UNSET
            if not isinstance(self.method, Unset):
                method = BlankEnum(self.method).value

        timer_started_at: Union[None, Unset, str]
        if isinstance(self.timer_started_at, Unset):
            timer_started_at = UNSET
        elif isinstance(self.timer_started_at, datetime.datetime):
            timer_started_at = UNSET
            if not isinstance(self.timer_started_at, Unset):
                timer_started_at = self.timer_started_at.isoformat()

        else:
            timer_started_at = self.timer_started_at

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(visibility, Unset):
            field_dict["visibility"] = visibility
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(flaw_uuid, Unset):
            field_dict["flaw_uuid"] = flaw_uuid
        if not isinstance(last_error, Unset):
            field_dict["last_error"] = last_error
        if not isinstance(upstream_project, Unset):
            field_dict["upstream_project"] = upstream_project
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(reportability_reason, Unset):
            field_dict["reportability_reason"] = reportability_reason
        if not isinstance(method, Unset):
            field_dict["method"] = method
        if not isinstance(timer_started_at, Unset):
            field_dict["timer_started_at"] = timer_started_at
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
        embargoed = d.pop("embargoed", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: VisibilityEnum
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = VisibilityEnum(_visibility)

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

        last_error = d.pop("last_error", UNSET)

        def _parse_upstream_project(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _upstream_project_type_0 = data
                upstream_project_type_0: UUID
                if isinstance(_upstream_project_type_0, Unset):
                    upstream_project_type_0 = UNSET
                else:
                    upstream_project_type_0 = (
                        _upstream_project_type_0
                        if isinstance(_upstream_project_type_0, UUID)
                        else UUID(_upstream_project_type_0)
                    )

                return upstream_project_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        upstream_project = _parse_upstream_project(d.pop("upstream_project", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpstreamNotificationStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpstreamNotificationStatusEnum(_status)

        def _parse_reportability_reason(
            data: object,
        ) -> Union[BlankEnum, ReportabilityReasonEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _reportability_reason_type_0 = data
                reportability_reason_type_0: ReportabilityReasonEnum
                if isinstance(_reportability_reason_type_0, Unset):
                    reportability_reason_type_0 = UNSET
                else:
                    reportability_reason_type_0 = ReportabilityReasonEnum(
                        _reportability_reason_type_0
                    )

                return reportability_reason_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _reportability_reason_type_1 = data
            reportability_reason_type_1: BlankEnum
            if isinstance(_reportability_reason_type_1, Unset):
                reportability_reason_type_1 = UNSET
            else:
                reportability_reason_type_1 = BlankEnum(_reportability_reason_type_1)

            return reportability_reason_type_1

        reportability_reason = _parse_reportability_reason(
            d.pop("reportability_reason", UNSET)
        )

        def _parse_method(data: object) -> Union[BlankEnum, MethodEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _method_type_0 = data
                method_type_0: MethodEnum
                if isinstance(_method_type_0, Unset):
                    method_type_0 = UNSET
                else:
                    method_type_0 = MethodEnum(_method_type_0)

                return method_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _method_type_1 = data
            method_type_1: BlankEnum
            if isinstance(_method_type_1, Unset):
                method_type_1 = UNSET
            else:
                method_type_1 = BlankEnum(_method_type_1)

            return method_type_1

        method = _parse_method(d.pop("method", UNSET))

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

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        regulatory_reporting_api_v1_notifications_upstream_update_response_200 = cls(
            embargoed=embargoed,
            visibility=visibility,
            created_dt=created_dt,
            updated_dt=updated_dt,
            uuid=uuid,
            flaw_uuid=flaw_uuid,
            last_error=last_error,
            upstream_project=upstream_project,
            status=status,
            reportability_reason=reportability_reason,
            method=method,
            timer_started_at=timer_started_at,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        regulatory_reporting_api_v1_notifications_upstream_update_response_200.additional_properties = d
        return regulatory_reporting_api_v1_notifications_upstream_update_response_200

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
