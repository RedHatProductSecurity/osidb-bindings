from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1StatusRetrieveResponse200OsidbData")


@attr.s(auto_attribs=True)
class OsidbApiV1StatusRetrieveResponse200OsidbData(OSIDBModel):
    """ """

    flaw_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flaw_count = self.flaw_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(flaw_count, Unset):
            field_dict["flaw_count"] = flaw_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        flaw_count = d.pop("flaw_count", UNSET)

        osidb_api_v1_status_retrieve_response_200_osidb_data = cls(
            flaw_count=flaw_count,
        )

        osidb_api_v1_status_retrieve_response_200_osidb_data.additional_properties = d
        return osidb_api_v1_status_retrieve_response_200_osidb_data

    @staticmethod
    def get_fields():
        return {
            "flaw_count": int,
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
