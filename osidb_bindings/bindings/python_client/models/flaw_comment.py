import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.flaw_comment_type import FlawCommentType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawComment")


@attr.s(auto_attribs=True)
class FlawComment(OSIDBModel):
    """FlawComment serializer for use by flaw_comments endpoint"""

    flaw: str
    text: str
    uuid: str
    external_system_id: str
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    embargoed: bool
    type: Union[Unset, FlawCommentType] = UNSET
    order: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flaw = self.flaw
        text = self.text
        uuid = self.uuid
        external_system_id = self.external_system_id
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        embargoed = self.embargoed
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):

            type = FlawCommentType(self.type).value

        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if flaw is not UNSET:
            field_dict["flaw"] = flaw
        if text is not UNSET:
            field_dict["text"] = text
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if external_system_id is not UNSET:
            field_dict["external_system_id"] = external_system_id
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if updated_dt is not UNSET:
            field_dict["updated_dt"] = updated_dt
        if embargoed is not UNSET:
            field_dict["embargoed"] = embargoed
        if type is not UNSET:
            field_dict["type"] = type
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        flaw = d.pop("flaw", UNSET)

        text = d.pop("text", UNSET)

        uuid = d.pop("uuid", UNSET)

        external_system_id = d.pop("external_system_id", UNSET)

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

        embargoed = d.pop("embargoed", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FlawCommentType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FlawCommentType(_type)

        order = d.pop("order", UNSET)

        flaw_comment = cls(
            flaw=flaw,
            text=text,
            uuid=uuid,
            external_system_id=external_system_id,
            created_dt=created_dt,
            updated_dt=updated_dt,
            embargoed=embargoed,
            type=type,
            order=order,
        )

        flaw_comment.additional_properties = d
        return flaw_comment

    @staticmethod
    def get_fields():
        return {
            "flaw": str,
            "text": str,
            "uuid": str,
            "external_system_id": str,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "embargoed": bool,
            "type": FlawCommentType,
            "order": int,
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
