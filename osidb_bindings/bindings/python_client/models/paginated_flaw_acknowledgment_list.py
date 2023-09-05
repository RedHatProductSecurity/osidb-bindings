from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.flaw_acknowledgment import FlawAcknowledgment
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="PaginatedFlawAcknowledgmentList")


@attr.s(auto_attribs=True)
class PaginatedFlawAcknowledgmentList(OSIDBModel):
    """ """

    count: Union[Unset, int] = UNSET
    next_: Union[Unset, None, str] = UNSET
    previous: Union[Unset, None, str] = UNSET
    results: Union[Unset, List[FlawAcknowledgment]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        next_ = self.next_
        previous = self.previous
        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item: Dict[str, Any] = UNSET
                if not isinstance(results_item_data, Unset):
                    results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(count, Unset):
            field_dict["count"] = count
        if not isinstance(next_, Unset):
            field_dict["next"] = next_
        if not isinstance(previous, Unset):
            field_dict["previous"] = previous
        if not isinstance(results, Unset):
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        if _results is UNSET:
            results = UNSET
        else:
            for results_item_data in _results or []:
                _results_item = results_item_data
                results_item: FlawAcknowledgment
                if isinstance(_results_item, Unset):
                    results_item = UNSET
                else:
                    results_item = FlawAcknowledgment.from_dict(_results_item)

                results.append(results_item)

        paginated_flaw_acknowledgment_list = cls(
            count=count,
            next_=next_,
            previous=previous,
            results=results,
        )

        paginated_flaw_acknowledgment_list.additional_properties = d
        return paginated_flaw_acknowledgment_list

    @staticmethod
    def get_fields():
        return {
            "count": int,
            "next": str,
            "previous": str,
            "results": List[FlawAcknowledgment],
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
