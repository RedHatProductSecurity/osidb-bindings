from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tracker_type import TrackerType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="TrackerReportData")


@attr.s(auto_attribs=True)
class TrackerReportData(OSIDBModel):
    """ """

    type: TrackerType
    external_system_id: str
    status: str
    resolution: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = TrackerType(self.type).value

        external_system_id = self.external_system_id
        status = self.status
        resolution = self.resolution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(type, Unset):
            field_dict["type"] = type
        if not isinstance(external_system_id, Unset):
            field_dict["external_system_id"] = external_system_id
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: TrackerType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TrackerType(_type)

        external_system_id = d.pop("external_system_id", UNSET)

        status = d.pop("status", UNSET)

        resolution = d.pop("resolution", UNSET)

        tracker_report_data = cls(
            type=type,
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
