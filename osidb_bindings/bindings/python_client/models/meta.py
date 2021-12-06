import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.meta_meta_attr import MetaMetaAttr
from ..models.meta_type_enum import MetaTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Meta")


@attr.s(auto_attribs=True)
class Meta:
    """FlawMeta serializer"""

    uuid: str
    created_dt: datetime.datetime
    type: Union[MetaTypeEnum, None, Unset] = UNSET
    meta_attr: Union[Unset, None, MetaMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        type: Union[None, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        elif self.type is None:
            type = None
        elif isinstance(self.type, MetaTypeEnum):
            type = UNSET
            if not isinstance(self.type, Unset):

                type = MetaTypeEnum(self.type).value

        else:
            type = self.type

        meta_attr: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict() if self.meta_attr else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if type is not UNSET:
            field_dict["type"] = type
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        def _parse_type(data: object) -> Union[MetaTypeEnum, None, Unset]:
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
            return cast(Union[MetaTypeEnum, None, Unset], data)

        type = _parse_type(d.pop("type", UNSET))

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, None, MetaMetaAttr]
        if _meta_attr is None:
            meta_attr = None
        elif isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = MetaMetaAttr.from_dict(_meta_attr)

        meta = cls(
            uuid=uuid,
            created_dt=created_dt,
            type=type,
            meta_attr=meta_attr,
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
