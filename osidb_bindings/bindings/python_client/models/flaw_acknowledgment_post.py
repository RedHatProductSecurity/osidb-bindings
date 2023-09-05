import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawAcknowledgmentPost")


@attr.s(auto_attribs=True)
class FlawAcknowledgmentPost(OSIDBModel):
    """FlawAcknowledgment serializer"""

    name: str
    affiliation: str
    from_upstream: bool
    uuid: str
    embargoed: bool
    created_dt: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        affiliation = self.affiliation
        from_upstream = self.from_upstream
        uuid = self.uuid
        embargoed = self.embargoed
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(affiliation, Unset):
            field_dict["affiliation"] = affiliation
        if not isinstance(from_upstream, Unset):
            field_dict["from_upstream"] = from_upstream
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if self.name is UNSET else (None, str(self.name), "text/plain")
        affiliation = (
            self.affiliation
            if self.affiliation is UNSET
            else (None, str(self.affiliation), "text/plain")
        )
        from_upstream = (
            self.from_upstream
            if self.from_upstream is UNSET
            else (None, str(self.from_upstream), "text/plain")
        )
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        embargoed = (
            self.embargoed
            if self.embargoed is UNSET
            else (None, str(self.embargoed), "text/plain")
        )
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(affiliation, Unset):
            field_dict["affiliation"] = affiliation
        if not isinstance(from_upstream, Unset):
            field_dict["from_upstream"] = from_upstream
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        affiliation = d.pop("affiliation", UNSET)

        from_upstream = d.pop("from_upstream", UNSET)

        uuid = d.pop("uuid", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        flaw_acknowledgment_post = cls(
            name=name,
            affiliation=affiliation,
            from_upstream=from_upstream,
            uuid=uuid,
            embargoed=embargoed,
            created_dt=created_dt,
        )

        flaw_acknowledgment_post.additional_properties = d
        return flaw_acknowledgment_post

    @staticmethod
    def get_fields():
        return {
            "name": str,
            "affiliation": str,
            "from_upstream": bool,
            "uuid": str,
            "embargoed": bool,
            "created_dt": datetime.datetime,
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
