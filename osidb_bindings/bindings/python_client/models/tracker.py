from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.tracker_type_enum import TrackerTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Tracker")


@attr.s(auto_attribs=True)
class Tracker:
    """Tracker serializer"""

    uuid: str
    type: Union[None, TrackerTypeEnum, Unset] = UNSET
    external_system_id: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, str] = UNSET
    resolution: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        type: Union[None, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        elif self.type is None:
            type = None
        elif isinstance(self.type, TrackerTypeEnum):
            type = UNSET
            if not isinstance(self.type, Unset):

                type = TrackerTypeEnum(self.type).value

        else:
            type = self.type

        external_system_id = self.external_system_id
        status = self.status
        resolution = self.resolution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
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
        uuid = d.pop("uuid", UNSET)

        def _parse_type(data: object) -> Union[None, TrackerTypeEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _type_type_0 = data
                type_type_0: Union[Unset, TrackerTypeEnum]
                if isinstance(_type_type_0, Unset):
                    type_type_0 = UNSET
                else:
                    type_type_0 = TrackerTypeEnum(_type_type_0)

                return type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, TrackerTypeEnum, Unset], data)

        type = _parse_type(d.pop("type", UNSET))

        external_system_id = d.pop("external_system_id", UNSET)

        status = d.pop("status", UNSET)

        resolution = d.pop("resolution", UNSET)

        tracker = cls(
            uuid=uuid,
            type=type,
            external_system_id=external_system_id,
            status=status,
            resolution=resolution,
        )

        tracker.additional_properties = d
        return tracker

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
