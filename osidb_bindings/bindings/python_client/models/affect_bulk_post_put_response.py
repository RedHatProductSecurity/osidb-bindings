from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.affect import Affect
    from ..models.affect_bulk_post_put_response_failed_item import (
        AffectBulkPostPutResponseFailedItem,
    )


T = TypeVar("T", bound="AffectBulkPostPutResponse")


@_attrs_define
class AffectBulkPostPutResponse(OSIDBModel):
    """
    Attributes:
        results (list['Affect']):
        failed (Union[Unset, list['AffectBulkPostPutResponseFailedItem']]):
    """

    results: list["Affect"]
    failed: Union[Unset, list["AffectBulkPostPutResponseFailedItem"]] = UNSET
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

        failed: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.failed, Unset):
            failed = []
            for failed_item_data in self.failed:
                failed_item: dict[str, Any] = UNSET
                if not isinstance(failed_item_data, Unset):
                    failed_item = failed_item_data.to_dict()

                failed.append(failed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(results, Unset):
            field_dict["results"] = results
        if not isinstance(failed, Unset):
            field_dict["failed"] = failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.affect import Affect
        from ..models.affect_bulk_post_put_response_failed_item import (
            AffectBulkPostPutResponseFailedItem,
        )

        d = src_dict.copy()
        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            _results_item = results_item_data
            results_item: Affect
            if isinstance(_results_item, Unset):
                results_item = UNSET
            else:
                results_item = Affect.from_dict(_results_item)

            results.append(results_item)

        failed = []
        _failed = d.pop("failed", UNSET)
        for failed_item_data in _failed or []:
            _failed_item = failed_item_data
            failed_item: AffectBulkPostPutResponseFailedItem
            if isinstance(_failed_item, Unset):
                failed_item = UNSET
            else:
                failed_item = AffectBulkPostPutResponseFailedItem.from_dict(
                    _failed_item
                )

            failed.append(failed_item)

        affect_bulk_post_put_response = cls(
            results=results,
            failed=failed,
        )

        affect_bulk_post_put_response.additional_properties = d
        return affect_bulk_post_put_response

    @classmethod
    def get_fields(cls):
        return {f.name: f.type for f in _attrs_fields(cls)}

    @classmethod
    def new(cls):
        return cls.from_dict({})

    @classmethod
    def from_model(cls: type[T], model: "OSIDBModel") -> T:
        return cls.from_dict(model.to_dict())

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
