from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.affect import Affect
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="AffectBulkPostPutResponse")


@attr.s(auto_attribs=True)
class AffectBulkPostPutResponse(OSIDBModel):
    """ """

    results: List[Affect]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results: List[Dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item: Dict[str, Any] = UNSET
                if not isinstance(results_item_data, Unset):
                    results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(results, Unset):
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        results = []
        _results = d.pop("results", UNSET)
        if _results is UNSET:
            results = UNSET
        else:
            for results_item_data in _results or []:
                _results_item = results_item_data
                results_item: Affect
                if isinstance(_results_item, Unset):
                    results_item = UNSET
                else:
                    results_item = Affect.from_dict(_results_item)

                results.append(results_item)

        affect_bulk_post_put_response = cls(
            results=results,
        )

        affect_bulk_post_put_response.additional_properties = d
        return affect_bulk_post_put_response

    @staticmethod
    def get_fields():
        return {
            "results": List[Affect],
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
