import datetime
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.flaw_reference_type import FlawReferenceType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawReferencePost")


@attr.s(auto_attribs=True)
class FlawReferencePost(OSIDBModel):
    """FlawReference serializer"""

    url: str
    uuid: str
    embargoed: bool
    created_dt: datetime.datetime
    description: Union[Unset, str] = UNSET
    type: Union[Unset, FlawReferenceType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        uuid = self.uuid
        embargoed = self.embargoed
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        description = self.description
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):

            type = FlawReferenceType(self.type).value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(url, Unset):
            field_dict["url"] = url
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(description, Unset):
            field_dict["description"] = description
        if not isinstance(type, Unset):
            field_dict["type"] = type

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        url = self.url if self.url is UNSET else (None, str(self.url), "text/plain")
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        embargoed = (
            self.embargoed
            if self.embargoed is UNSET
            else (None, str(self.embargoed), "text/plain")
        )
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        description = (
            self.description
            if self.description is UNSET
            else (None, str(self.description), "text/plain")
        )
        type: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.type, Unset):

            type = FlawReferenceType(self.type).value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        if not isinstance(url, Unset):
            field_dict["url"] = url
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(description, Unset):
            field_dict["description"] = description
        if not isinstance(type, Unset):
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        uuid = d.pop("uuid", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        description = d.pop("description", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FlawReferenceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FlawReferenceType(_type)

        flaw_reference_post = cls(
            url=url,
            uuid=uuid,
            embargoed=embargoed,
            created_dt=created_dt,
            description=description,
            type=type,
        )

        flaw_reference_post.additional_properties = d
        return flaw_reference_post

    @staticmethod
    def get_fields():
        return {
            "url": str,
            "uuid": str,
            "embargoed": bool,
            "created_dt": datetime.datetime,
            "description": str,
            "type": FlawReferenceType,
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
