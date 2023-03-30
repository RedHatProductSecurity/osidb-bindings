import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.meta_meta_attr import MetaMetaAttr
from ..models.meta_type_enum import MetaTypeEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="Meta")


@attr.s(auto_attribs=True)
class Meta(OSIDBModel):
    """FlawMeta serializer"""

    uuid: str
    type: MetaTypeEnum
    embargoed: bool
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    meta_attr: Union[Unset, MetaMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = MetaTypeEnum(self.type).value

        embargoed = self.embargoed
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        meta_attr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if type is not UNSET:
            field_dict["type"] = type
        if embargoed is not UNSET:
            field_dict["embargoed"] = embargoed
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if updated_dt is not UNSET:
            field_dict["updated_dt"] = updated_dt
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        _type = d.pop("type", UNSET)
        type: MetaTypeEnum
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = MetaTypeEnum(_type)

        embargoed = d.pop("embargoed", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, MetaMetaAttr]
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = MetaMetaAttr.from_dict(_meta_attr)

        meta = cls(
            uuid=uuid,
            type=type,
            embargoed=embargoed,
            created_dt=created_dt,
            updated_dt=updated_dt,
            meta_attr=meta_attr,
        )

        meta.additional_properties = d
        return meta

    @staticmethod
    def get_fields():
        return {
            "uuid": str,
            "type": MetaTypeEnum,
            "embargoed": bool,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "meta_attr": MetaMetaAttr,
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
