from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.affect import Affect
from ..models.module_component import ModuleComponent
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="TrackerSuggestion")


@attr.s(auto_attribs=True)
class TrackerSuggestion(OSIDBModel):
    """ """

    modules_components: List[ModuleComponent]
    not_applicable: List[Affect]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        modules_components: List[Dict[str, Any]] = UNSET
        if not isinstance(self.modules_components, Unset):
            modules_components = []
            for modules_components_item_data in self.modules_components:
                modules_components_item: Dict[str, Any] = UNSET
                if not isinstance(modules_components_item_data, Unset):
                    modules_components_item = modules_components_item_data.to_dict()

                modules_components.append(modules_components_item)

        not_applicable: List[Dict[str, Any]] = UNSET
        if not isinstance(self.not_applicable, Unset):
            not_applicable = []
            for not_applicable_item_data in self.not_applicable:
                not_applicable_item: Dict[str, Any] = UNSET
                if not isinstance(not_applicable_item_data, Unset):
                    not_applicable_item = not_applicable_item_data.to_dict()

                not_applicable.append(not_applicable_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(modules_components, Unset):
            field_dict["modules_components"] = modules_components
        if not isinstance(not_applicable, Unset):
            field_dict["not_applicable"] = not_applicable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        modules_components = []
        _modules_components = d.pop("modules_components", UNSET)
        if _modules_components is UNSET:
            modules_components = UNSET
        else:
            for modules_components_item_data in _modules_components or []:
                _modules_components_item = modules_components_item_data
                modules_components_item: ModuleComponent
                if isinstance(_modules_components_item, Unset):
                    modules_components_item = UNSET
                else:
                    modules_components_item = ModuleComponent.from_dict(
                        _modules_components_item
                    )

                modules_components.append(modules_components_item)

        not_applicable = []
        _not_applicable = d.pop("not_applicable", UNSET)
        if _not_applicable is UNSET:
            not_applicable = UNSET
        else:
            for not_applicable_item_data in _not_applicable or []:
                _not_applicable_item = not_applicable_item_data
                not_applicable_item: Affect
                if isinstance(_not_applicable_item, Unset):
                    not_applicable_item = UNSET
                else:
                    not_applicable_item = Affect.from_dict(_not_applicable_item)

                not_applicable.append(not_applicable_item)

        tracker_suggestion = cls(
            modules_components=modules_components,
            not_applicable=not_applicable,
        )

        tracker_suggestion.additional_properties = d
        return tracker_suggestion

    @staticmethod
    def get_fields():
        return {
            "modules_components": List[ModuleComponent],
            "not_applicable": List[Affect],
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
