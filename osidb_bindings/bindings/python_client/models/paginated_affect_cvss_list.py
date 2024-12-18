from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.affect_cvss import AffectCVSS


T = TypeVar("T", bound="PaginatedAffectCVSSList")


@_attrs_define
class PaginatedAffectCVSSList(OSIDBModel):
    """
    Attributes:
        count (int):  Example: 123.
        results (list['AffectCVSS']):
        next_ (Union[None, Unset, str]):  Example: http://api.example.org/accounts/?offset=400&limit=100.
        previous (Union[None, Unset, str]):  Example: http://api.example.org/accounts/?offset=200&limit=100.
    """

    count: int
    results: list["AffectCVSS"]
    next_: Union[None, Unset, str] = UNSET
    previous: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        results: list[dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item: dict[str, Any] = UNSET
                if not isinstance(results_item_data, Unset):
                    results_item = results_item_data.to_dict()

                results.append(results_item)

        next_: Union[None, Unset, str]
        if isinstance(self.next_, Unset):
            next_ = UNSET
        else:
            next_ = self.next_

        previous: Union[None, Unset, str]
        if isinstance(self.previous, Unset):
            previous = UNSET
        else:
            previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(count, Unset):
            field_dict["count"] = count
        if not isinstance(results, Unset):
            field_dict["results"] = results
        if not isinstance(next_, Unset):
            field_dict["next"] = next_
        if not isinstance(previous, Unset):
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.affect_cvss import AffectCVSS

        d = src_dict.copy()
        count = d.pop("count", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            # }
            _results_item = results_item_data
            results_item: AffectCVSS
            if isinstance(_results_item, Unset):
                results_item = UNSET
            else:
                results_item = AffectCVSS.from_dict(_results_item)

            results.append(results_item)

        def _parse_next_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_ = _parse_next_(d.pop("next", UNSET))

        def _parse_previous(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        previous = _parse_previous(d.pop("previous", UNSET))

        paginated_affect_cvss_list = cls(
            count=count,
            results=results,
            next_=next_,
            previous=previous,
        )

        paginated_affect_cvss_list.additional_properties = d
        return paginated_affect_cvss_list

    @staticmethod
    def get_fields():
        return {
            "count": int,
            "results": list["AffectCVSS"],
            "next": Union[None, str],
            "previous": Union[None, str],
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
