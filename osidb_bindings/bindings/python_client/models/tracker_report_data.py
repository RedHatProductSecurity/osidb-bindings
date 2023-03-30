from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.type_0d0_enum import Type0D0Enum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="TrackerReportData")


@attr.s(auto_attribs=True)
class TrackerReportData(OSIDBModel):
    """ """

    type: Type0D0Enum
    external_system_id: str
    status: str
    resolution: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = Type0D0Enum(self.type).value

        external_system_id = self.external_system_id
        status = self.status
        resolution = self.resolution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if type is not UNSET:
            field_dict["type"] = type
        if external_system_id is not UNSET:
            field_dict["external_system_id"] = external_system_id
        if status is not UNSET:
            field_dict["status"] = status
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Type0D0Enum
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = Type0D0Enum(_type)

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
            "type": Type0D0Enum,
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
