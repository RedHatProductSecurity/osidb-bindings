import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.comment_meta_attr import CommentMetaAttr
from ..models.flaw_comment_type import FlawCommentType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="Comment")


@attr.s(auto_attribs=True)
class Comment(OSIDBModel):
    """FlawComment serializer for use by FlawSerializer"""

    uuid: str
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    type: Union[Unset, FlawCommentType] = UNSET
    external_system_id: Union[Unset, str] = UNSET
    order: Union[Unset, None, int] = UNSET
    meta_attr: Union[Unset, CommentMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):

            type = FlawCommentType(self.type).value

        external_system_id = self.external_system_id
        order = self.order
        meta_attr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(type, Unset):
            field_dict["type"] = type
        if not isinstance(external_system_id, Unset):
            field_dict["external_system_id"] = external_system_id
        if not isinstance(order, Unset):
            field_dict["order"] = order
        if not isinstance(meta_attr, Unset):
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

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FlawCommentType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FlawCommentType(_type)

        external_system_id = d.pop("external_system_id", UNSET)

        order = d.pop("order", UNSET)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, CommentMetaAttr]
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = CommentMetaAttr.from_dict(_meta_attr)

        comment = cls(
            uuid=uuid,
            created_dt=created_dt,
            updated_dt=updated_dt,
            type=type,
            external_system_id=external_system_id,
            order=order,
            meta_attr=meta_attr,
        )

        comment.additional_properties = d
        return comment

    @staticmethod
    def get_fields():
        return {
            "uuid": str,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "type": FlawCommentType,
            "external_system_id": str,
            "order": int,
            "meta_attr": CommentMetaAttr,
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
