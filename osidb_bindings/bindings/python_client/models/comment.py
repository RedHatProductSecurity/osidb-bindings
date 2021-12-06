import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.comment_meta_attr import CommentMetaAttr
from ..models.comment_type_enum import CommentTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Comment")


@attr.s(auto_attribs=True)
class Comment:
    """FlawComment serializer"""

    uuid: str
    created_dt: datetime.datetime
    type: Union[CommentTypeEnum, None, Unset] = UNSET
    external_system_id: Union[Unset, None, str] = UNSET
    order: Union[Unset, None, int] = UNSET
    meta_attr: Union[Unset, None, CommentMetaAttr] = UNSET
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
        elif isinstance(self.type, CommentTypeEnum):
            type = UNSET
            if not isinstance(self.type, Unset):

                type = CommentTypeEnum(self.type).value

        else:
            type = self.type

        external_system_id = self.external_system_id
        order = self.order
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
        if external_system_id is not UNSET:
            field_dict["external_system_id"] = external_system_id
        if order is not UNSET:
            field_dict["order"] = order
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

        def _parse_type(data: object) -> Union[CommentTypeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _type_type_0 = data
                type_type_0: Union[Unset, CommentTypeEnum]
                if isinstance(_type_type_0, Unset):
                    type_type_0 = UNSET
                else:
                    type_type_0 = CommentTypeEnum(_type_type_0)

                return type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[CommentTypeEnum, None, Unset], data)

        type = _parse_type(d.pop("type", UNSET))

        external_system_id = d.pop("external_system_id", UNSET)

        order = d.pop("order", UNSET)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, None, CommentMetaAttr]
        if _meta_attr is None:
            meta_attr = None
        elif isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = CommentMetaAttr.from_dict(_meta_attr)

        comment = cls(
            uuid=uuid,
            created_dt=created_dt,
            type=type,
            external_system_id=external_system_id,
            order=order,
            meta_attr=meta_attr,
        )

        comment.additional_properties = d
        return comment

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
