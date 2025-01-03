from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import OSIDBModel

T = TypeVar(
    "T", bound="CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0"
)


@_attrs_define
class CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0(OSIDBModel):
    """ """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        collectors_api_v1_status_retrieve_response_200_collectors_item_error_type_0 = (
            cls()
        )

        collectors_api_v1_status_retrieve_response_200_collectors_item_error_type_0.additional_properties = d
        return (
            collectors_api_v1_status_retrieve_response_200_collectors_item_error_type_0
        )

    @staticmethod
    def get_fields():
        return {}

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