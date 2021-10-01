from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.blank_enum import BlankEnum
from ..models.meta_attr import MetaAttr
from ..models.meta_type_enum import MetaTypeEnum
from ..models.null_enum import NullEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Meta")


@attr.s(auto_attribs=True)
class Meta:
    """FlawMeta serializer"""

    uuid: str
    type: Union[BlankEnum, MetaTypeEnum, None, NullEnum, Unset] = UNSET
    attr: Union[Unset, None, MetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        type: Union[None, NoneType, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        elif self.type is None:
            type = None
        elif isinstance(self.type, MetaTypeEnum):
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

        attr: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.attr, Unset):
            attr = self.attr.to_dict() if self.attr else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if attr is not UNSET:
            field_dict["attr"] = attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        def _parse_type(data: object) -> Union[BlankEnum, MetaTypeEnum, None, NullEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _type_type_0 = data
                type_type_0: Union[Unset, MetaTypeEnum]
                if isinstance(_type_type_0, Unset):
                    type_type_0 = UNSET
                else:
                    type_type_0 = MetaTypeEnum(_type_type_0)

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

        _attr = d.pop("attr", UNSET)
        attr: Union[Unset, None, MetaAttr]
        if _attr is None:
            attr = None
        elif isinstance(_attr, Unset):
            attr = UNSET
        else:
            attr = MetaAttr.from_dict(_attr)

        meta = cls(
            uuid=uuid,
            type=type,
            attr=attr,
        )

        meta.additional_properties = d
        return meta

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
