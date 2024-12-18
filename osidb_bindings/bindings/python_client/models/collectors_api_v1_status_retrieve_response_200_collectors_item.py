import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.collectors_api_v1_status_retrieve_response_200_collectors_item_data import (
    CollectorsApiV1StatusRetrieveResponse200CollectorsItemData,
)
from ..models.collectors_api_v1_status_retrieve_response_200_collectors_item_state import (
    CollectorsApiV1StatusRetrieveResponse200CollectorsItemState,
)
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.collectors_api_v1_status_retrieve_response_200_collectors_item_error_type_0 import (
        CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0,
    )


T = TypeVar("T", bound="CollectorsApiV1StatusRetrieveResponse200CollectorsItem")


@_attrs_define
class CollectorsApiV1StatusRetrieveResponse200CollectorsItem(OSIDBModel):
    """
    Attributes:
        data (Union[Unset, CollectorsApiV1StatusRetrieveResponse200CollectorsItemData]):
        depends_on (Union[Unset, list[str]]):
        error (Union['CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0', None, Unset]):
        is_complete (Union[Unset, bool]):
        is_up2date (Union[Unset, bool]):
        data_models (Union[Unset, list[str]]):
        state (Union[Unset, CollectorsApiV1StatusRetrieveResponse200CollectorsItemState]):
        updated_until (Union[Unset, datetime.datetime]):
    """

    data: Union[Unset, CollectorsApiV1StatusRetrieveResponse200CollectorsItemData] = (
        UNSET
    )
    depends_on: Union[Unset, list[str]] = UNSET
    error: Union[
        "CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0", None, Unset
    ] = UNSET
    is_complete: Union[Unset, bool] = UNSET
    is_up2date: Union[Unset, bool] = UNSET
    data_models: Union[Unset, list[str]] = UNSET
    state: Union[Unset, CollectorsApiV1StatusRetrieveResponse200CollectorsItemState] = (
        UNSET
    )
    updated_until: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.collectors_api_v1_status_retrieve_response_200_collectors_item_error_type_0 import (
            CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0,
        )

        data: Union[Unset, str] = UNSET
        if not isinstance(self.data, Unset):
            data = CollectorsApiV1StatusRetrieveResponse200CollectorsItemData(
                self.data
            ).value

        depends_on: Union[Unset, list[str]] = UNSET
        if not isinstance(self.depends_on, Unset):
            depends_on = self.depends_on

        error: Union[None, Unset, dict[str, Any]]
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(
            self.error, CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0
        ):
            error = UNSET
            if not isinstance(self.error, Unset):
                error = self.error.to_dict()

        else:
            error = self.error

        is_complete = self.is_complete

        is_up2date = self.is_up2date

        data_models: Union[Unset, list[str]] = UNSET
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

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.collectors_api_v1_status_retrieve_response_200_collectors_item_error_type_0 import (
            CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0,
        )

        d = src_dict.copy()
        # }
        _data = d.pop("data", UNSET)
        data: Union[Unset, CollectorsApiV1StatusRetrieveResponse200CollectorsItemData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CollectorsApiV1StatusRetrieveResponse200CollectorsItemData(_data)

        depends_on = cast(list[str], d.pop("depends_on", UNSET))

        def _parse_error(
            data: object,
        ) -> Union[
            "CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0",
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                # }
                _error_type_0 = data
                error_type_0: (
                    CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0
                )
                if isinstance(_error_type_0, Unset):
                    error_type_0 = UNSET
                else:
                    error_type_0 = CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0.from_dict(
                        _error_type_0
                    )

                return error_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0",
                    None,
                    Unset,
                ],
                data,
            )

        error = _parse_error(d.pop("error", UNSET))

        is_complete = d.pop("is_complete", UNSET)

        is_up2date = d.pop("is_up2date", UNSET)

        data_models = cast(list[str], d.pop("data_models", UNSET))

        # }
        _state = d.pop("state", UNSET)
        state: Union[Unset, CollectorsApiV1StatusRetrieveResponse200CollectorsItemState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CollectorsApiV1StatusRetrieveResponse200CollectorsItemState(_state)

        # }
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

        collectors_api_v1_status_retrieve_response_200_collectors_item.additional_properties = d
        return collectors_api_v1_status_retrieve_response_200_collectors_item

    @staticmethod
    def get_fields():
        return {
            "data": CollectorsApiV1StatusRetrieveResponse200CollectorsItemData,
            "depends_on": list[str],
            "error": Union[
                "CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0", None
            ],
            "is_complete": bool,
            "is_up2date": bool,
            "data_models": list[str],
            "state": CollectorsApiV1StatusRetrieveResponse200CollectorsItemState,
            "updated_until": datetime.datetime,
        }

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
