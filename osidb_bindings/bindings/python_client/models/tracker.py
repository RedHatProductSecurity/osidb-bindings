from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr

from ..models.tracker_meta_attr import TrackerMetaAttr
from ..models.tracker_type_enum import TrackerTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Tracker")


@attr.s(auto_attribs=True)
class Tracker:
    """Tracker serializer"""

    uuid: str
    meta_attr: TrackerMetaAttr
    type: Union[None, TrackerTypeEnum]
    external_system_id: Optional[str]
    status: Union[Unset, None, str] = UNSET
    resolution: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        meta_attr: Dict[str, Any] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        type: Union[None, str]
        if self.type is None:
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
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr
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

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: TrackerMetaAttr
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = TrackerMetaAttr.from_dict(_meta_attr)

        def _parse_type(data: object) -> Union[None, TrackerTypeEnum]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _type_type_0 = data
                type_type_0: TrackerTypeEnum
                if isinstance(_type_type_0, Unset):
                    type_type_0 = UNSET
                else:
                    type_type_0 = TrackerTypeEnum(_type_type_0)

                return type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, TrackerTypeEnum], data)

        type = _parse_type(d.pop("type", UNSET))

        external_system_id = d.pop("external_system_id", UNSET)

        status = d.pop("status", UNSET)

        resolution = d.pop("resolution", UNSET)

        tracker = cls(
            uuid=uuid,
            meta_attr=meta_attr,
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
