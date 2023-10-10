from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.ps_stream_selection import PsStreamSelection
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="ModuleComponent")


@attr.s(auto_attribs=True)
class ModuleComponent(OSIDBModel):
    """ """

    ps_module: str
    ps_component: str
    streams: List[PsStreamSelection]
    selected: bool
    affect: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ps_module = self.ps_module
        ps_component = self.ps_component
        streams: List[Dict[str, Any]] = UNSET
        if not isinstance(self.streams, Unset):
            streams = []
            for streams_item_data in self.streams:
                streams_item: Dict[str, Any] = UNSET
                if not isinstance(streams_item_data, Unset):
                    streams_item = streams_item_data.to_dict()

                streams.append(streams_item)

        selected = self.selected
        affect = self.affect

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ps_module = d.pop("ps_module", UNSET)

        ps_component = d.pop("ps_component", UNSET)

        streams = []
        _streams = d.pop("streams", UNSET)
        if _streams is UNSET:
            streams = UNSET
        else:
            for streams_item_data in _streams or []:
                _streams_item = streams_item_data
                streams_item: PsStreamSelection
                if isinstance(_streams_item, Unset):
                    streams_item = UNSET
                else:
                    streams_item = PsStreamSelection.from_dict(_streams_item)

                streams.append(streams_item)

        selected = d.pop("selected", UNSET)

        affect = d.pop("affect", UNSET)

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
            "streams": List[PsStreamSelection],
            "selected": bool,
            "affect": str,
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
