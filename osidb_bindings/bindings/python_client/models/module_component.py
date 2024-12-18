from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.affect import Affect
    from ..models.ps_stream_selection import PsStreamSelection


T = TypeVar("T", bound="ModuleComponent")


@_attrs_define
class ModuleComponent(OSIDBModel):
    """
    Attributes:
        ps_module (str):
        ps_component (str):
        streams (list['PsStreamSelection']):
        selected (bool):
        affect (Affect): Affect serializer
    """

    ps_module: str
    ps_component: str
    streams: list["PsStreamSelection"]
    selected: bool
    affect: "Affect"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ps_module = self.ps_module

        ps_component = self.ps_component

        streams: list[dict[str, Any]] = UNSET
        if not isinstance(self.streams, Unset):
            streams = []
            for streams_item_data in self.streams:
                streams_item: dict[str, Any] = UNSET
                if not isinstance(streams_item_data, Unset):
                    streams_item = streams_item_data.to_dict()

                streams.append(streams_item)

        selected = self.selected

        affect: dict[str, Any] = UNSET
        if not isinstance(self.affect, Unset):
            affect = self.affect.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(ps_module, Unset):
            field_dict["ps_module"] = ps_module
        if not isinstance(ps_component, Unset):
            field_dict["ps_component"] = ps_component
        if not isinstance(streams, Unset):
            field_dict["streams"] = streams
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
        ps_module = d.pop("ps_module", UNSET)

        ps_component = d.pop("ps_component", UNSET)

        streams = []
        _streams = d.pop("streams", UNSET)
        for streams_item_data in _streams or []:
            # }
            _streams_item = streams_item_data
            streams_item: PsStreamSelection
            if isinstance(_streams_item, Unset):
                streams_item = UNSET
            else:
                streams_item = PsStreamSelection.from_dict(_streams_item)

            streams.append(streams_item)

        selected = d.pop("selected", UNSET)

        # }
        _affect = d.pop("affect", UNSET)
        affect: Affect
        if isinstance(_affect, Unset):
            affect = UNSET
        else:
            affect = Affect.from_dict(_affect)

        module_component = cls(
            ps_module=ps_module,
            ps_component=ps_component,
            streams=streams,
            selected=selected,
            affect=affect,
        )

        module_component.additional_properties = d
        return module_component

    @staticmethod
    def get_fields():
        return {
            "ps_module": str,
            "ps_component": str,
            "streams": list["PsStreamSelection"],
            "selected": bool,
            "affect": Affect,
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
