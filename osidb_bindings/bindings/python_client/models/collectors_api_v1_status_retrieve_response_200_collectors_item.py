import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.collectors_api_v1_status_retrieve_response_200_collectors_item_data import (
    CollectorsApiV1StatusRetrieveResponse200CollectorsItemData,
)
from ..models.collectors_api_v1_status_retrieve_response_200_collectors_item_error import (
    CollectorsApiV1StatusRetrieveResponse200CollectorsItemError,
)
from ..models.collectors_api_v1_status_retrieve_response_200_collectors_item_state import (
    CollectorsApiV1StatusRetrieveResponse200CollectorsItemState,
)
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="CollectorsApiV1StatusRetrieveResponse200CollectorsItem")


@attr.s(auto_attribs=True)
class CollectorsApiV1StatusRetrieveResponse200CollectorsItem(OSIDBModel):
    """ """

    data: Union[
        Unset, CollectorsApiV1StatusRetrieveResponse200CollectorsItemData
    ] = UNSET
    depends_on: Union[Unset, List[str]] = UNSET
    error: Union[
        Unset, None, CollectorsApiV1StatusRetrieveResponse200CollectorsItemError
    ] = UNSET
    is_complete: Union[Unset, bool] = UNSET
    is_up2date: Union[Unset, bool] = UNSET
    data_models: Union[Unset, List[str]] = UNSET
    state: Union[
        Unset, CollectorsApiV1StatusRetrieveResponse200CollectorsItemState
    ] = UNSET
    updated_until: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, str] = UNSET
        if not isinstance(self.data, Unset):

            data = CollectorsApiV1StatusRetrieveResponse200CollectorsItemData(
                self.data
            ).value

        depends_on: Union[Unset, List[str]] = UNSET
        if not isinstance(self.depends_on, Unset):
            depends_on = self.depends_on

        error: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict() if self.error else None

        is_complete = self.is_complete
        is_up2date = self.is_up2date
        data_models: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_models, Unset):
            data_models = self.data_models

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):

            state = CollectorsApiV1StatusRetrieveResponse200CollectorsItemState(
                self.state
            ).value

        updated_until: Union[Unset, str] = UNSET
        if not isinstance(self.updated_until, Unset):
            updated_until = self.updated_until.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(data, Unset):
            field_dict["data"] = data
        if not isinstance(depends_on, Unset):
            field_dict["depends_on"] = depends_on
        if not isinstance(error, Unset):
            field_dict["error"] = error
        if not isinstance(is_complete, Unset):
            field_dict["is_complete"] = is_complete
        if not isinstance(is_up2date, Unset):
            field_dict["is_up2date"] = is_up2date
        if not isinstance(data_models, Unset):
            field_dict["data_models"] = data_models
        if not isinstance(state, Unset):
            field_dict["state"] = state
        if not isinstance(updated_until, Unset):
            field_dict["updated_until"] = updated_until

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, CollectorsApiV1StatusRetrieveResponse200CollectorsItemData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CollectorsApiV1StatusRetrieveResponse200CollectorsItemData(_data)

        depends_on = cast(List[str], d.pop("depends_on", UNSET))

        _error = d.pop("error", UNSET)
        error: Union[
            Unset, None, CollectorsApiV1StatusRetrieveResponse200CollectorsItemError
        ]
        if _error is None:
            error = None
        elif isinstance(_error, Unset):
            error = UNSET
        else:
            error = (
                CollectorsApiV1StatusRetrieveResponse200CollectorsItemError.from_dict(
                    _error
                )
            )

        is_complete = d.pop("is_complete", UNSET)

        is_up2date = d.pop("is_up2date", UNSET)

        data_models = cast(List[str], d.pop("data_models", UNSET))

        _state = d.pop("state", UNSET)
        state: Union[Unset, CollectorsApiV1StatusRetrieveResponse200CollectorsItemState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CollectorsApiV1StatusRetrieveResponse200CollectorsItemState(_state)

        _updated_until = d.pop("updated_until", UNSET)
        updated_until: Union[Unset, datetime.datetime]
        if isinstance(_updated_until, Unset):
            updated_until = UNSET
        else:
            updated_until = isoparse(_updated_until)

        collectors_api_v1_status_retrieve_response_200_collectors_item = cls(
            data=data,
            depends_on=depends_on,
            error=error,
            is_complete=is_complete,
            is_up2date=is_up2date,
            data_models=data_models,
            state=state,
            updated_until=updated_until,
        )

        collectors_api_v1_status_retrieve_response_200_collectors_item.additional_properties = (
            d
        )
        return collectors_api_v1_status_retrieve_response_200_collectors_item

    @staticmethod
    def get_fields():
        return {
            "data": CollectorsApiV1StatusRetrieveResponse200CollectorsItemData,
            "depends_on": List[str],
            "error": CollectorsApiV1StatusRetrieveResponse200CollectorsItemError,
            "is_complete": bool,
            "is_up2date": bool,
            "data_models": List[str],
            "state": CollectorsApiV1StatusRetrieveResponse200CollectorsItemState,
            "updated_until": datetime.datetime,
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
