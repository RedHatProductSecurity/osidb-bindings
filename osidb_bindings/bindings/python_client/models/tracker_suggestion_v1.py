from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.affect import Affect
    from ..models.module_component import ModuleComponent


T = TypeVar("T", bound="TrackerSuggestionV1")


@_attrs_define
class TrackerSuggestionV1(OSIDBModel):
    """
    Attributes:
        modules_components (list['ModuleComponent']):
        not_applicable (list['Affect']):
    """

    modules_components: list["ModuleComponent"]
    not_applicable: list["Affect"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modules_components: list[dict[str, Any]] = UNSET
        if not isinstance(self.modules_components, Unset):
            modules_components = []
            for modules_components_item_data in self.modules_components:
                modules_components_item: dict[str, Any] = UNSET
                if not isinstance(modules_components_item_data, Unset):
                    modules_components_item = modules_components_item_data.to_dict()

                modules_components.append(modules_components_item)

        not_applicable: list[dict[str, Any]] = UNSET
        if not isinstance(self.not_applicable, Unset):
            not_applicable = []
            for not_applicable_item_data in self.not_applicable:
                not_applicable_item: dict[str, Any] = UNSET
                if not isinstance(not_applicable_item_data, Unset):
                    not_applicable_item = not_applicable_item_data.to_dict()

                not_applicable.append(not_applicable_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(modules_components, Unset):
            field_dict["modules_components"] = modules_components
        if not isinstance(not_applicable, Unset):
            field_dict["not_applicable"] = not_applicable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.affect import Affect
        from ..models.module_component import ModuleComponent

        d = src_dict.copy()
        modules_components = []
        _modules_components = d.pop("modules_components", UNSET)
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
        for not_applicable_item_data in _not_applicable or []:
            _not_applicable_item = not_applicable_item_data
            not_applicable_item: Affect
            if isinstance(_not_applicable_item, Unset):
                not_applicable_item = UNSET
            else:
                not_applicable_item = Affect.from_dict(_not_applicable_item)

            not_applicable.append(not_applicable_item)

        tracker_suggestion_v1 = cls(
            modules_components=modules_components,
            not_applicable=not_applicable,
        )

        tracker_suggestion_v1.additional_properties = d
        return tracker_suggestion_v1

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
