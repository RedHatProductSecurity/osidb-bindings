from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.affect import Affect
    from ..models.ps_stream_selection import PsStreamSelection


T = TypeVar("T", bound="StreamComponent")


@_attrs_define
class StreamComponent(OSIDBModel):
    """
    Attributes:
        ps_update_stream (str):
        ps_component (str):
        offer (PsStreamSelection):
        selected (bool):
        affect (Affect): Affect serializer
    """

    ps_update_stream: str
    ps_component: str
    offer: "PsStreamSelection"
    selected: bool
    affect: "Affect"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ps_update_stream = self.ps_update_stream

        ps_component = self.ps_component

        offer: dict[str, Any] = UNSET
        if not isinstance(self.offer, Unset):
            offer = self.offer.to_dict()

        selected = self.selected

        affect: dict[str, Any] = UNSET
        if not isinstance(self.affect, Unset):
            affect = self.affect.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream
        if not isinstance(ps_component, Unset):
            field_dict["ps_component"] = ps_component
        if not isinstance(offer, Unset):
            field_dict["offer"] = offer
        if not isinstance(selected, Unset):
            field_dict["selected"] = selected
        if not isinstance(affect, Unset):
            field_dict["affect"] = affect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.affect import Affect
        from ..models.ps_stream_selection import PsStreamSelection

        d = src_dict.copy()
        ps_update_stream = d.pop("ps_update_stream", UNSET)

        ps_component = d.pop("ps_component", UNSET)

        _offer = d.pop("offer", UNSET)
        offer: PsStreamSelection
        if isinstance(_offer, Unset):
            offer = UNSET
        else:
            offer = PsStreamSelection.from_dict(_offer)

        selected = d.pop("selected", UNSET)

        _affect = d.pop("affect", UNSET)
        affect: Affect
        if isinstance(_affect, Unset):
            affect = UNSET
        else:
            affect = Affect.from_dict(_affect)

        stream_component = cls(
            ps_update_stream=ps_update_stream,
            ps_component=ps_component,
            offer=offer,
            selected=selected,
            affect=affect,
        )

        stream_component.additional_properties = d
        return stream_component

    @classmethod
    def get_fields(cls):
        return {f.name: f.type for f in _attrs_fields(cls)}

    @classmethod
    def new(cls):
        return cls.from_dict({})

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
