from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="PsStreamSelection")


@_attrs_define
class PsStreamSelection(OSIDBModel):
    """
    Attributes:
        ps_update_stream (str):
        selected (bool):
        acked (bool):
        eus (bool):
        aus (bool):
    """

    ps_update_stream: str
    selected: bool
    acked: bool
    eus: bool
    aus: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ps_update_stream = self.ps_update_stream

        selected = self.selected

        acked = self.acked

        eus = self.eus

        aus = self.aus

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream
        if not isinstance(selected, Unset):
            field_dict["selected"] = selected
        if not isinstance(acked, Unset):
            field_dict["acked"] = acked
        if not isinstance(eus, Unset):
            field_dict["eus"] = eus
        if not isinstance(aus, Unset):
            field_dict["aus"] = aus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ps_update_stream = d.pop("ps_update_stream", UNSET)

        selected = d.pop("selected", UNSET)

        acked = d.pop("acked", UNSET)

        eus = d.pop("eus", UNSET)

        aus = d.pop("aus", UNSET)

        ps_stream_selection = cls(
            ps_update_stream=ps_update_stream,
            selected=selected,
            acked=acked,
            eus=eus,
            aus=aus,
        )

        ps_stream_selection.additional_properties = d
        return ps_stream_selection

    @staticmethod
    def get_fields():
        return {
            "ps_update_stream": str,
            "selected": bool,
            "acked": bool,
            "eus": bool,
            "aus": bool,
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
