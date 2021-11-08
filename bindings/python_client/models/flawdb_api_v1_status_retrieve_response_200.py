import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.flawdb_api_v1_status_retrieve_response_200_flawdb_data import (
    FlawdbApiV1StatusRetrieveResponse200FlawdbData,
)
from ..models.flawdb_api_v1_status_retrieve_response_200_flawdb_service import (
    FlawdbApiV1StatusRetrieveResponse200FlawdbService,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlawdbApiV1StatusRetrieveResponse200")


@attr.s(auto_attribs=True)
class FlawdbApiV1StatusRetrieveResponse200:
    """ """

    status: Union[Unset, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    flawdb_service: Union[Unset, FlawdbApiV1StatusRetrieveResponse200FlawdbService] = UNSET
    flawdb_data: Union[Unset, FlawdbApiV1StatusRetrieveResponse200FlawdbData] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        flawdb_service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.flawdb_service, Unset):
            flawdb_service = self.flawdb_service.to_dict()

        flawdb_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.flawdb_data, Unset):
            flawdb_data = self.flawdb_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if dt is not UNSET:
            field_dict["dt"] = dt
        if flawdb_service is not UNSET:
            field_dict["flawdb_service"] = flawdb_service
        if flawdb_data is not UNSET:
            field_dict["flawdb_data"] = flawdb_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        _flawdb_service = d.pop("flawdb_service", UNSET)
        flawdb_service: Union[Unset, FlawdbApiV1StatusRetrieveResponse200FlawdbService]
        if isinstance(_flawdb_service, Unset):
            flawdb_service = UNSET
        else:
            flawdb_service = FlawdbApiV1StatusRetrieveResponse200FlawdbService.from_dict(_flawdb_service)

        _flawdb_data = d.pop("flawdb_data", UNSET)
        flawdb_data: Union[Unset, FlawdbApiV1StatusRetrieveResponse200FlawdbData]
        if isinstance(_flawdb_data, Unset):
            flawdb_data = UNSET
        else:
            flawdb_data = FlawdbApiV1StatusRetrieveResponse200FlawdbData.from_dict(_flawdb_data)

        flawdb_api_v1_status_retrieve_response_200 = cls(
            status=status,
            dt=dt,
            flawdb_service=flawdb_service,
            flawdb_data=flawdb_data,
        )

        flawdb_api_v1_status_retrieve_response_200.additional_properties = d
        return flawdb_api_v1_status_retrieve_response_200

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
