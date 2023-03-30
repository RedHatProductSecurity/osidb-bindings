import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="Erratum")


@attr.s(auto_attribs=True)
class Erratum(OSIDBModel):
    """Erratum serializer"""

    et_id: int
    advisory_name: str
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        et_id = self.et_id
        advisory_name = self.advisory_name
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if et_id is not UNSET:
            field_dict["et_id"] = et_id
        if advisory_name is not UNSET:
            field_dict["advisory_name"] = advisory_name
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if updated_dt is not UNSET:
            field_dict["updated_dt"] = updated_dt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        et_id = d.pop("et_id", UNSET)

        advisory_name = d.pop("advisory_name", UNSET)

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

        erratum = cls(
            et_id=et_id,
            advisory_name=advisory_name,
            created_dt=created_dt,
            updated_dt=updated_dt,
        )

        erratum.additional_properties = d
        return erratum

    @staticmethod
    def get_fields():
        return {
            "et_id": int,
            "advisory_name": str,
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
