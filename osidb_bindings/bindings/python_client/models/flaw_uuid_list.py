import json
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawUUIDList")


@_attrs_define
class FlawUUIDList(OSIDBModel):
    """
    Attributes:
        flaw_uuids (list[UUID]):
    """

    flaw_uuids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flaw_uuids: list[str] = UNSET
        if not isinstance(self.flaw_uuids, Unset):
            flaw_uuids = []
            for flaw_uuids_item_data in self.flaw_uuids:
                flaw_uuids_item: str = UNSET
                if not isinstance(flaw_uuids_item_data, Unset):
                    flaw_uuids_item = str(flaw_uuids_item_data)

                flaw_uuids.append(flaw_uuids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(flaw_uuids, Unset):
            field_dict["flaw_uuids"] = flaw_uuids

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        flaw_uuids: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.flaw_uuids, Unset):
            _temp_flaw_uuids = []
            for flaw_uuids_item_data in self.flaw_uuids:
                flaw_uuids_item: str = UNSET
                if not isinstance(flaw_uuids_item_data, Unset):
                    flaw_uuids_item = str(flaw_uuids_item_data)

                _temp_flaw_uuids.append(flaw_uuids_item)
            flaw_uuids = (
                None,
                json.dumps(_temp_flaw_uuids).encode(),
                "application/json",
            )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(flaw_uuids, Unset):
            field_dict["flaw_uuids"] = flaw_uuids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        flaw_uuids = []
        _flaw_uuids = d.pop("flaw_uuids", UNSET)
        for flaw_uuids_item_data in _flaw_uuids or []:
            # }
            _flaw_uuids_item = flaw_uuids_item_data
            flaw_uuids_item: UUID
            if isinstance(_flaw_uuids_item, Unset):
                flaw_uuids_item = UNSET
            else:
                flaw_uuids_item = UUID(_flaw_uuids_item)

            flaw_uuids.append(flaw_uuids_item)

        flaw_uuid_list = cls(
            flaw_uuids=flaw_uuids,
        )

        flaw_uuid_list.additional_properties = d
        return flaw_uuid_list

    @staticmethod
    def get_fields():
        return {
            "flaw_uuids": list[UUID],
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
