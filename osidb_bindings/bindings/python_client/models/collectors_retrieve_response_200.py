import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectorsRetrieveResponse200")


@attr.s(auto_attribs=True)
class CollectorsRetrieveResponse200:
    """ """

    dt: Union[Unset, datetime.datetime] = UNSET
    index: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        index: Union[Unset, List[str]] = UNSET
        if not isinstance(self.index, Unset):
            index = self.index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if dt is not UNSET:
            field_dict["dt"] = dt
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        index = cast(List[str], d.pop("index", UNSET))

        collectors_retrieve_response_200 = cls(
            dt=dt,
            index=index,
        )

        collectors_retrieve_response_200.additional_properties = d
        return collectors_retrieve_response_200

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
