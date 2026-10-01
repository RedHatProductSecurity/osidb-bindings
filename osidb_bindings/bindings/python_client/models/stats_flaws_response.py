from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.stats_flaws_response_groups_item import StatsFlawsResponseGroupsItem
    from ..models.stats_meta import StatsMeta


T = TypeVar("T", bound="StatsFlawsResponse")


@_attrs_define
class StatsFlawsResponse(OSIDBModel):
    """
    Attributes:
        groups (list['StatsFlawsResponseGroupsItem']):
        meta (StatsMeta):
    """

    groups: list["StatsFlawsResponseGroupsItem"]
    meta: "StatsMeta"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups: list[dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item: dict[str, Any] = UNSET
                if not isinstance(groups_item_data, Unset):
                    groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        meta: dict[str, Any] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(groups, Unset):
            field_dict["groups"] = groups
        if not isinstance(meta, Unset):
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.stats_flaws_response_groups_item import (
            StatsFlawsResponseGroupsItem,
        )
        from ..models.stats_meta import StatsMeta

        d = src_dict.copy()
        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            _groups_item = groups_item_data
            groups_item: StatsFlawsResponseGroupsItem
            if isinstance(_groups_item, Unset):
                groups_item = UNSET
            else:
                groups_item = StatsFlawsResponseGroupsItem.from_dict(_groups_item)

            groups.append(groups_item)

        _meta = d.pop("meta", UNSET)
        meta: StatsMeta
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = StatsMeta.from_dict(_meta)

        stats_flaws_response = cls(
            groups=groups,
            meta=meta,
        )

        stats_flaws_response.additional_properties = d
        return stats_flaws_response

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
