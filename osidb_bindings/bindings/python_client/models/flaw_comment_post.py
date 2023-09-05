import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.flaw_comment_post_meta_attr import FlawCommentPostMetaAttr
from ..models.flaw_comment_type import FlawCommentType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawCommentPost")


@attr.s(auto_attribs=True)
class FlawCommentPost(OSIDBModel):
    """FlawComment serializer for use by flaw_comments endpoint"""

    text: str
    uuid: str
    created_dt: datetime.datetime
    embargoed: bool
    type: Union[Unset, FlawCommentType] = UNSET
    meta_attr: Union[Unset, FlawCommentPostMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        uuid = self.uuid
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        embargoed = self.embargoed
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):

            type = FlawCommentType(self.type).value

        meta_attr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(text, Unset):
            field_dict["text"] = text
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(type, Unset):
            field_dict["type"] = type
        if not isinstance(meta_attr, Unset):
            field_dict["meta_attr"] = meta_attr

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        text = self.text if self.text is UNSET else (None, str(self.text), "text/plain")
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        embargoed = (
            self.embargoed
            if self.embargoed is UNSET
            else (None, str(self.embargoed), "text/plain")
        )
        type: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.type, Unset):

            type = FlawCommentType(self.type).value

        meta_attr: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = (None, json.dumps(self.meta_attr.to_dict()), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        if not isinstance(text, Unset):
            field_dict["text"] = text
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(type, Unset):
            field_dict["type"] = type
        if not isinstance(meta_attr, Unset):
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        uuid = d.pop("uuid", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        embargoed = d.pop("embargoed", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FlawCommentType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FlawCommentType(_type)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, FlawCommentPostMetaAttr]
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = FlawCommentPostMetaAttr.from_dict(_meta_attr)

        flaw_comment_post = cls(
            text=text,
            uuid=uuid,
            created_dt=created_dt,
            embargoed=embargoed,
            type=type,
            meta_attr=meta_attr,
        )

        flaw_comment_post.additional_properties = d
        return flaw_comment_post

    @staticmethod
    def get_fields():
        return {
            "text": str,
            "uuid": str,
            "created_dt": datetime.datetime,
            "embargoed": bool,
            "type": FlawCommentType,
            "meta_attr": FlawCommentPostMetaAttr,
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
