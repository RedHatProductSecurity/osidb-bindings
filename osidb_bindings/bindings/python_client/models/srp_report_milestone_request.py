import datetime
import json
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..models.srp_report_milestone_status_enum import SRPReportMilestoneStatusEnum
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.srp_report_milestone_request_additional_details import (
        SRPReportMilestoneRequestAdditionalDetails,
    )


T = TypeVar("T", bound="SRPReportMilestoneRequest")


@_attrs_define
class SRPReportMilestoneRequest(OSIDBModel):
    """Serializer for SRP Report Milestones.

    Includes computed fields for deadline tracking and status.

        Attributes:
            updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
                detect mit-air collisions.
            status (Union[Unset, SRPReportMilestoneStatusEnum]):
            additional_details (Union[Unset, SRPReportMilestoneRequestAdditionalDetails]): Coordinator-provided SRP FAQ
                fields for this milestone stage. OSIM stores and reads these as individual form fields. Values here override
                auto-derived payload fields at submission time.
            submitted_at (Union[None, Unset, datetime.datetime]): When this milestone was submitted
            owner (Union[Unset, str]): Owner of this milestone
            mitigation_created_at (Union[None, Unset, datetime.datetime]): When the mitigation or patch became available
            mitigation_link (Union[Unset, str]): Link to the mitigation or patch used for reporting
            manual_completion_notes (Union[Unset, str]): Manual completion notes
            due_at (Union[None, Unset, datetime.datetime]):
    """

    updated_dt: datetime.datetime
    status: Union[Unset, SRPReportMilestoneStatusEnum] = UNSET
    additional_details: Union[Unset, "SRPReportMilestoneRequestAdditionalDetails"] = (
        UNSET
    )
    submitted_at: Union[None, Unset, datetime.datetime] = UNSET
    owner: Union[Unset, str] = UNSET
    mitigation_created_at: Union[None, Unset, datetime.datetime] = UNSET
    mitigation_link: Union[Unset, str] = UNSET
    manual_completion_notes: Union[Unset, str] = UNSET
    due_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
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

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        updated_dt: bytes = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat().encode()

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        additional_details: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.additional_details, Unset):
            additional_details = (
                None,
                json.dumps(self.additional_details.to_dict()).encode(),
                "application/json",
            )

        submitted_at: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at: bytes = UNSET
            if not isinstance(self.submitted_at, Unset):
                submitted_at = self.submitted_at.isoformat().encode()
        else:
            submitted_at = (None, str(self.submitted_at).encode(), "text/plain")

        owner = (
            self.owner
            if isinstance(self.owner, Unset)
            else (None, str(self.owner).encode(), "text/plain")
        )

        mitigation_created_at: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.mitigation_created_at, Unset):
            mitigation_created_at = UNSET
        elif isinstance(self.mitigation_created_at, datetime.datetime):
            mitigation_created_at: bytes = UNSET
            if not isinstance(self.mitigation_created_at, Unset):
                mitigation_created_at = self.mitigation_created_at.isoformat().encode()
        else:
            mitigation_created_at = (
                None,
                str(self.mitigation_created_at).encode(),
                "text/plain",
            )

        mitigation_link: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.mitigation_link, Unset):
            mitigation_link = UNSET
        elif isinstance(self.mitigation_link, str):
            mitigation_link = (None, str(self.mitigation_link).encode(), "text/plain")
        else:
            mitigation_link = (None, str(self.mitigation_link).encode(), "text/plain")

        manual_completion_notes = (
            self.manual_completion_notes
            if isinstance(self.manual_completion_notes, Unset)
            else (None, str(self.manual_completion_notes).encode(), "text/plain")
        )

        due_at: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at: bytes = UNSET
            if not isinstance(self.due_at, Unset):
                due_at = self.due_at.isoformat().encode()
        else:
            due_at = (None, str(self.due_at).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.srp_report_milestone_request_additional_details import (
            SRPReportMilestoneRequestAdditionalDetails,
        )

        d = src_dict.copy()
        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SRPReportMilestoneStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SRPReportMilestoneStatusEnum(_status)

        _additional_details = d.pop("additional_details", UNSET)
        additional_details: Union[Unset, SRPReportMilestoneRequestAdditionalDetails]
        if isinstance(_additional_details, Unset):
            additional_details = UNSET
        else:
            additional_details = SRPReportMilestoneRequestAdditionalDetails.from_dict(
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

        srp_report_milestone_request = cls(
            updated_dt=updated_dt,
            status=status,
            additional_details=additional_details,
            submitted_at=submitted_at,
            owner=owner,
            mitigation_created_at=mitigation_created_at,
            mitigation_link=mitigation_link,
            manual_completion_notes=manual_completion_notes,
            due_at=due_at,
        )

        srp_report_milestone_request.additional_properties = d
        return srp_report_milestone_request

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
