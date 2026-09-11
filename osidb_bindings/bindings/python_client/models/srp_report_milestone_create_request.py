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
    from ..models.srp_report_milestone_create_request_additional_details import (
        SRPReportMilestoneCreateRequestAdditionalDetails,
    )


T = TypeVar("T", bound="SRPReportMilestoneCreateRequest")


@_attrs_define
class SRPReportMilestoneCreateRequest(OSIDBModel):
    """Serializer for creating SRP Report Milestones.

    Only additional_information_response milestones can be created via the API;
    all other milestone types are auto-created by signals.
    ACLs are inherited from the parent report in the view's perform_create.

        Attributes:
            status (Union[Unset, SRPReportMilestoneStatusEnum]):
            additional_details (Union[Unset, SRPReportMilestoneCreateRequestAdditionalDetails]): Coordinator-provided SRP
                FAQ fields for this milestone stage. OSIM stores and reads these as individual form fields. Values here override
                auto-derived payload fields at submission time.
            request_received_at (Union[None, Unset, datetime.datetime]): When the request was received
            request_source (Union[Unset, str]): Source of the request
            request_text (Union[Unset, str]): Text of the request
            submitted_at (Union[None, Unset, datetime.datetime]): When this milestone was submitted
            owner (Union[Unset, str]): Owner of this milestone
            manual_completion_notes (Union[Unset, str]): Manual completion notes
    """

    status: Union[Unset, SRPReportMilestoneStatusEnum] = UNSET
    additional_details: Union[
        Unset, "SRPReportMilestoneCreateRequestAdditionalDetails"
    ] = UNSET
    request_received_at: Union[None, Unset, datetime.datetime] = UNSET
    request_source: Union[Unset, str] = UNSET
    request_text: Union[Unset, str] = UNSET
    submitted_at: Union[None, Unset, datetime.datetime] = UNSET
    owner: Union[Unset, str] = UNSET
    manual_completion_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = SRPReportMilestoneStatusEnum(self.status).value

        additional_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.additional_details, Unset):
            additional_details = self.additional_details.to_dict()

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

        manual_completion_notes = self.manual_completion_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(additional_details, Unset):
            field_dict["additional_details"] = additional_details
        if not isinstance(request_received_at, Unset):
            field_dict["request_received_at"] = request_received_at
        if not isinstance(request_source, Unset):
            field_dict["request_source"] = request_source
        if not isinstance(request_text, Unset):
            field_dict["request_text"] = request_text
        if not isinstance(submitted_at, Unset):
            field_dict["submitted_at"] = submitted_at
        if not isinstance(owner, Unset):
            field_dict["owner"] = owner
        if not isinstance(manual_completion_notes, Unset):
            field_dict["manual_completion_notes"] = manual_completion_notes

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
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

        request_received_at: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.request_received_at, Unset):
            request_received_at = UNSET
        elif isinstance(self.request_received_at, datetime.datetime):
            request_received_at: bytes = UNSET
            if not isinstance(self.request_received_at, Unset):
                request_received_at = self.request_received_at.isoformat().encode()
        else:
            request_received_at = (
                None,
                str(self.request_received_at).encode(),
                "text/plain",
            )

        request_source = (
            self.request_source
            if isinstance(self.request_source, Unset)
            else (None, str(self.request_source).encode(), "text/plain")
        )

        request_text = (
            self.request_text
            if isinstance(self.request_text, Unset)
            else (None, str(self.request_text).encode(), "text/plain")
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

        manual_completion_notes = (
            self.manual_completion_notes
            if isinstance(self.manual_completion_notes, Unset)
            else (None, str(self.manual_completion_notes).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(additional_details, Unset):
            field_dict["additional_details"] = additional_details
        if not isinstance(request_received_at, Unset):
            field_dict["request_received_at"] = request_received_at
        if not isinstance(request_source, Unset):
            field_dict["request_source"] = request_source
        if not isinstance(request_text, Unset):
            field_dict["request_text"] = request_text
        if not isinstance(submitted_at, Unset):
            field_dict["submitted_at"] = submitted_at
        if not isinstance(owner, Unset):
            field_dict["owner"] = owner
        if not isinstance(manual_completion_notes, Unset):
            field_dict["manual_completion_notes"] = manual_completion_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.srp_report_milestone_create_request_additional_details import (
            SRPReportMilestoneCreateRequestAdditionalDetails,
        )

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, SRPReportMilestoneStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SRPReportMilestoneStatusEnum(_status)

        _additional_details = d.pop("additional_details", UNSET)
        additional_details: Union[
            Unset, SRPReportMilestoneCreateRequestAdditionalDetails
        ]
        if isinstance(_additional_details, Unset):
            additional_details = UNSET
        else:
            additional_details = (
                SRPReportMilestoneCreateRequestAdditionalDetails.from_dict(
                    _additional_details
                )
            )

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

        manual_completion_notes = d.pop("manual_completion_notes", UNSET)

        srp_report_milestone_create_request = cls(
            status=status,
            additional_details=additional_details,
            request_received_at=request_received_at,
            request_source=request_source,
            request_text=request_text,
            submitted_at=submitted_at,
            owner=owner,
            manual_completion_notes=manual_completion_notes,
        )

        srp_report_milestone_create_request.additional_properties = d
        return srp_report_milestone_create_request

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
