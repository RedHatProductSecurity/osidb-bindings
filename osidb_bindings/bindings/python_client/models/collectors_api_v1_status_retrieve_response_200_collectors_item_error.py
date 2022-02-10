from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CollectorsApiV1StatusRetrieveResponse200CollectorsItemError")


@attr.s(auto_attribs=True)
class CollectorsApiV1StatusRetrieveResponse200CollectorsItemError:
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        collectors_api_v1_status_retrieve_response_200_collectors_item_error = cls()

        collectors_api_v1_status_retrieve_response_200_collectors_item_error.additional_properties = d
        return collectors_api_v1_status_retrieve_response_200_collectors_item_error

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
