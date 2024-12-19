from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracker_type import TrackerType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="TrackerReportData")


@_attrs_define
class TrackerReportData(OSIDBModel):
    """
    Attributes:
        type_ (TrackerType):
        external_system_id (str):
        status (Union[Unset, str]):
        resolution (Union[Unset, str]):
    """

    type_: TrackerType
    external_system_id: str
    status: Union[Unset, str] = UNSET
    resolution: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = TrackerType(self.type_).value

        external_system_id = self.external_system_id

        status = self.status

        resolution = self.resolution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(type_, Unset):
            field_dict["type"] = type_
        if not isinstance(external_system_id, Unset):
            field_dict["external_system_id"] = external_system_id
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        # }
        _type_ = d.pop("type", UNSET)
        type_: TrackerType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TrackerType(_type_)

        external_system_id = d.pop("external_system_id", UNSET)

        status = d.pop("status", UNSET)

        resolution = d.pop("resolution", UNSET)

        tracker_report_data = cls(
            type_=type_,
            external_system_id=external_system_id,
            status=status,
            resolution=resolution,
        )

        tracker_report_data.additional_properties = d
        return tracker_report_data

    @staticmethod
    def get_fields():
        return {
            "type": TrackerType,
            "external_system_id": str,
            "status": str,
            "resolution": str,
        }

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
