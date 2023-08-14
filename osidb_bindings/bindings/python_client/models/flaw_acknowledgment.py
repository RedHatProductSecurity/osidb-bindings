import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawAcknowledgment")


@attr.s(auto_attribs=True)
class FlawAcknowledgment(OSIDBModel):
    """FlawAcknowledgment serializer"""

    name: str
    affiliation: str
    from_upstream: bool
    flaw: str
    uuid: str
    embargoed: bool
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        affiliation = self.affiliation
        from_upstream = self.from_upstream
        flaw = self.flaw
        uuid = self.uuid
        embargoed = self.embargoed
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if name is not UNSET:
            field_dict["name"] = name
        if affiliation is not UNSET:
            field_dict["affiliation"] = affiliation
        if from_upstream is not UNSET:
            field_dict["from_upstream"] = from_upstream
        if flaw is not UNSET:
            field_dict["flaw"] = flaw
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if embargoed is not UNSET:
            field_dict["embargoed"] = embargoed
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if updated_dt is not UNSET:
            field_dict["updated_dt"] = updated_dt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        affiliation = d.pop("affiliation", UNSET)

        from_upstream = d.pop("from_upstream", UNSET)

        flaw = d.pop("flaw", UNSET)

        uuid = d.pop("uuid", UNSET)

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

        flaw_acknowledgment = cls(
            name=name,
            affiliation=affiliation,
            from_upstream=from_upstream,
            flaw=flaw,
            uuid=uuid,
            embargoed=embargoed,
            created_dt=created_dt,
            updated_dt=updated_dt,
        )

        flaw_acknowledgment.additional_properties = d
        return flaw_acknowledgment

    @staticmethod
    def get_fields():
        return {
            "name": str,
            "affiliation": str,
            "from_upstream": bool,
            "flaw": str,
            "uuid": str,
            "embargoed": bool,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
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
