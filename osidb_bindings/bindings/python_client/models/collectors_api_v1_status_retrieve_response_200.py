import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.collectors_api_v1_status_retrieve_response_200_collectors_item import (
    CollectorsApiV1StatusRetrieveResponse200CollectorsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectorsApiV1StatusRetrieveResponse200")


@attr.s(auto_attribs=True)
class CollectorsApiV1StatusRetrieveResponse200:
    """ """

    collectors: Union[Unset, List[CollectorsApiV1StatusRetrieveResponse200CollectorsItem]] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collectors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.collectors, Unset):
            collectors = []
            for collectors_item_data in self.collectors:
                collectors_item: Dict[str, Any] = UNSET
                if not isinstance(collectors_item_data, Unset):
                    collectors_item = collectors_item_data.to_dict()

                collectors.append(collectors_item)

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if collectors is not UNSET:
            field_dict["collectors"] = collectors
        if dt is not UNSET:
            field_dict["dt"] = dt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        collectors = []
        _collectors = d.pop("collectors", UNSET)
        if _collectors is UNSET:
            collectors = UNSET
        else:
            for collectors_item_data in _collectors or []:
                _collectors_item = collectors_item_data
                collectors_item: CollectorsApiV1StatusRetrieveResponse200CollectorsItem
                if isinstance(_collectors_item, Unset):
                    collectors_item = UNSET
                else:
                    collectors_item = CollectorsApiV1StatusRetrieveResponse200CollectorsItem.from_dict(_collectors_item)

                collectors.append(collectors_item)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        collectors_api_v1_status_retrieve_response_200 = cls(
            collectors=collectors,
            dt=dt,
        )

        collectors_api_v1_status_retrieve_response_200.additional_properties = d
        return collectors_api_v1_status_retrieve_response_200

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
