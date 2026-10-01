import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.stats_meta_filters import StatsMetaFilters


T = TypeVar("T", bound="StatsMeta")


@_attrs_define
class StatsMeta(OSIDBModel):
    """
    Attributes:
        total_flaws (int):
        sum_group_counts (int):
        group_by (list[str]):
        filters (StatsMetaFilters):
        generated_at (datetime.datetime):
        age_bucket_bounds (Union[Unset, list[int]]):
    """

    total_flaws: int
    sum_group_counts: int
    group_by: list[str]
    filters: "StatsMetaFilters"
    generated_at: datetime.datetime
    age_bucket_bounds: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_flaws = self.total_flaws

        sum_group_counts = self.sum_group_counts

        group_by: list[str] = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = self.group_by

        filters: dict[str, Any] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        generated_at: str = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        age_bucket_bounds: Union[Unset, list[int]] = UNSET
        if not isinstance(self.age_bucket_bounds, Unset):
            age_bucket_bounds = self.age_bucket_bounds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(total_flaws, Unset):
            field_dict["total_flaws"] = total_flaws
        if not isinstance(sum_group_counts, Unset):
            field_dict["sum_group_counts"] = sum_group_counts
        if not isinstance(group_by, Unset):
            field_dict["group_by"] = group_by
        if not isinstance(filters, Unset):
            field_dict["filters"] = filters
        if not isinstance(generated_at, Unset):
            field_dict["generated_at"] = generated_at
        if not isinstance(age_bucket_bounds, Unset):
            field_dict["age_bucket_bounds"] = age_bucket_bounds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.stats_meta_filters import StatsMetaFilters

        d = src_dict.copy()
        total_flaws = d.pop("total_flaws", UNSET)

        sum_group_counts = d.pop("sum_group_counts", UNSET)

        group_by = cast(list[str], d.pop("group_by", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: StatsMetaFilters
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = StatsMetaFilters.from_dict(_filters)

        _generated_at = d.pop("generated_at", UNSET)
        generated_at: datetime.datetime
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        age_bucket_bounds = cast(list[int], d.pop("age_bucket_bounds", UNSET))

        stats_meta = cls(
            total_flaws=total_flaws,
            sum_group_counts=sum_group_counts,
            group_by=group_by,
            filters=filters,
            generated_at=generated_at,
            age_bucket_bounds=age_bucket_bounds,
        )

        stats_meta.additional_properties = d
        return stats_meta

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
