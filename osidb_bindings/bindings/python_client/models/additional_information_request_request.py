import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..models.srp_report_milestone_status_enum import SRPReportMilestoneStatusEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="AdditionalInformationRequestRequest")


@_attrs_define
class AdditionalInformationRequestRequest(OSIDBModel):
    """Serializer for Additional Information Requests nested under a milestone.

    Includes computed fields for deadline tracking, mirroring
    SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
    is_overdue pattern.

        Attributes:
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
    """

    updated_dt: datetime.datetime
    request_received_at: Union[None, Unset, datetime.datetime] = UNSET
    request_source: Union[Unset, str] = UNSET
    request_text: Union[Unset, str] = UNSET
    response_text: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    status: Union[Unset, SRPReportMilestoneStatusEnum] = UNSET
    manual_due_at: Union[None, Unset, datetime.datetime] = UNSET
    manual_completion_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        updated_dt: bytes = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat().encode()

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

        response_text = (
            self.response_text
            if isinstance(self.response_text, Unset)
            else (None, str(self.response_text).encode(), "text/plain")
        )

        owner = (
            self.owner
            if isinstance(self.owner, Unset)
            else (None, str(self.owner).encode(), "text/plain")
        )

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        manual_due_at: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.manual_due_at, Unset):
            manual_due_at = UNSET
        elif isinstance(self.manual_due_at, datetime.datetime):
            manual_due_at: bytes = UNSET
            if not isinstance(self.manual_due_at, Unset):
                manual_due_at = self.manual_due_at.isoformat().encode()
        else:
            manual_due_at = (None, str(self.manual_due_at).encode(), "text/plain")

        manual_completion_notes = (
            self.manual_completion_notes
            if isinstance(self.manual_completion_notes, Unset)
            else (None, str(self.manual_completion_notes).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
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

        additional_information_request_request = cls(
            updated_dt=updated_dt,
            request_received_at=request_received_at,
            request_source=request_source,
            request_text=request_text,
            response_text=response_text,
            owner=owner,
            status=status,
            manual_due_at=manual_due_at,
            manual_completion_notes=manual_completion_notes,
        )

        additional_information_request_request.additional_properties = d
        return additional_information_request_request

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
