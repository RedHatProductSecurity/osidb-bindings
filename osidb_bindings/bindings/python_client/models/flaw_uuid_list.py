import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawUUIDList")


@attr.s(auto_attribs=True)
class FlawUUIDList(OSIDBModel):
    """ """

    flaw_uuids: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flaw_uuids: List[str] = UNSET
        if not isinstance(self.flaw_uuids, Unset):
            flaw_uuids = self.flaw_uuids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(flaw_uuids, Unset):
            field_dict["flaw_uuids"] = flaw_uuids

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        flaw_uuids: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.flaw_uuids, Unset):
            _temp_flaw_uuids = self.flaw_uuids
            flaw_uuids = (None, json.dumps(_temp_flaw_uuids), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        if not isinstance(flaw_uuids, Unset):
            field_dict["flaw_uuids"] = flaw_uuids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        flaw_uuids = cast(List[str], d.pop("flaw_uuids", UNSET))

        flaw_uuid_list = cls(
            flaw_uuids=flaw_uuids,
        )

        flaw_uuid_list.additional_properties = d
        return flaw_uuid_list

    @staticmethod
    def get_fields():
        return {
            "flaw_uuids": List[str],
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
