from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.blank_enum import BlankEnum
from ..models.null_enum import NullEnum
from ..models.tracker_type_enum import TrackerTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Tracker")


@attr.s(auto_attribs=True)
class Tracker:
    """Tracker serializer"""

    uuid: str
    type: Union[BlankEnum, None, NullEnum, TrackerTypeEnum, Unset] = UNSET
    key: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        type: Union[None, NoneType, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        elif self.type is None:
            type = None
        elif isinstance(self.type, TrackerTypeEnum):
            type = UNSET
            if not isinstance(self.type, Unset):
                type = self.type.value

        elif isinstance(self.type, BlankEnum):
            type = UNSET
            if not isinstance(self.type, Unset):
                type = self.type.value

        else:
            type = UNSET
            if not isinstance(self.type, Unset):
                type = self.type.value

        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        def _parse_type(data: object) -> Union[BlankEnum, None, NullEnum, TrackerTypeEnum, Unset]:
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
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _type_type_1 = data
                type_type_1: Union[Unset, BlankEnum]
                if isinstance(_type_type_1, Unset):
                    type_type_1 = UNSET
                else:
                    type_type_1 = BlankEnum(_type_type_1)

                return type_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, NoneType):
                raise TypeError()
            _type_type_2 = data
            type_type_2: Union[Unset, NullEnum]
            if isinstance(_type_type_2, Unset):
                type_type_2 = UNSET
            else:
                type_type_2 = NullEnum(_type_type_2)

            return type_type_2

        type = _parse_type(d.pop("type", UNSET))

        key = d.pop("key", UNSET)

        tracker = cls(
            uuid=uuid,
            type=type,
            key=key,
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
