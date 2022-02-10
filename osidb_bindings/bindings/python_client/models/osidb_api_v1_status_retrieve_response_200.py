import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.osidb_api_v1_status_retrieve_response_200_osidb_data import OsidbApiV1StatusRetrieveResponse200OsidbData
from ..models.osidb_api_v1_status_retrieve_response_200_osidb_service import (
    OsidbApiV1StatusRetrieveResponse200OsidbService,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OsidbApiV1StatusRetrieveResponse200")


@attr.s(auto_attribs=True)
class OsidbApiV1StatusRetrieveResponse200:
    """ """

    status: Union[Unset, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    osidb_service: Union[Unset, OsidbApiV1StatusRetrieveResponse200OsidbService] = UNSET
    osidb_data: Union[Unset, OsidbApiV1StatusRetrieveResponse200OsidbData] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        osidb_service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.osidb_service, Unset):
            osidb_service = self.osidb_service.to_dict()

        osidb_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.osidb_data, Unset):
            osidb_data = self.osidb_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if status is not UNSET:
            field_dict["status"] = status
        if dt is not UNSET:
            field_dict["dt"] = dt
        if osidb_service is not UNSET:
            field_dict["osidb_service"] = osidb_service
        if osidb_data is not UNSET:
            field_dict["osidb_data"] = osidb_data

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

        _osidb_service = d.pop("osidb_service", UNSET)
        osidb_service: Union[Unset, OsidbApiV1StatusRetrieveResponse200OsidbService]
        if isinstance(_osidb_service, Unset):
            osidb_service = UNSET
        else:
            osidb_service = OsidbApiV1StatusRetrieveResponse200OsidbService.from_dict(_osidb_service)

        _osidb_data = d.pop("osidb_data", UNSET)
        osidb_data: Union[Unset, OsidbApiV1StatusRetrieveResponse200OsidbData]
        if isinstance(_osidb_data, Unset):
            osidb_data = UNSET
        else:
            osidb_data = OsidbApiV1StatusRetrieveResponse200OsidbData.from_dict(_osidb_data)

        osidb_api_v1_status_retrieve_response_200 = cls(
            status=status,
            dt=dt,
            osidb_service=osidb_service,
            osidb_data=osidb_data,
        )

        osidb_api_v1_status_retrieve_response_200.additional_properties = d
        return osidb_api_v1_status_retrieve_response_200

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
