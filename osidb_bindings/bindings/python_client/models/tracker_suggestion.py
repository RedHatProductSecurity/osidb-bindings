from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.module_component import ModuleComponent
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="TrackerSuggestion")


@attr.s(auto_attribs=True)
class TrackerSuggestion(OSIDBModel):
    """ """

    modules_components: List[ModuleComponent]
    not_applicable: str
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

        not_applicable = self.not_applicable

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

        not_applicable = d.pop("not_applicable", UNSET)

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
            "not_applicable": str,
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
