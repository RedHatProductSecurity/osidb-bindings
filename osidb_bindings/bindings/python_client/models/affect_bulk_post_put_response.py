from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.affect import Affect


T = TypeVar("T", bound="AffectBulkPostPutResponse")


@_attrs_define
class AffectBulkPostPutResponse(OSIDBModel):
    """
    Attributes:
        results (list['Affect']):
    """

    results: list["Affect"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: list[dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item: dict[str, Any] = UNSET
                if not isinstance(results_item_data, Unset):
                    results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(results, Unset):
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.affect import Affect

        d = src_dict.copy()
        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            # }
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
            "results": list["Affect"],
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
