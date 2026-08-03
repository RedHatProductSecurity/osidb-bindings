from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.classification_check import ClassificationCheck
    from ..models.classification_state import ClassificationState


T = TypeVar("T", bound="ClassificationWorkflow")


@_attrs_define
class ClassificationWorkflow(OSIDBModel):
    """Workflow serializer with classification

    Attributes:
        accepts (str):
        name (str):
        description (str):
        priority (int):
        conditions (list['ClassificationCheck']):
        states (list['ClassificationState']):
        classified_state (str):
    """

    accepts: str
    name: str
    description: str
    priority: int
    conditions: list["ClassificationCheck"]
    states: list["ClassificationState"]
    classified_state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepts = self.accepts

        name = self.name

        description = self.description

        priority = self.priority

        conditions: list[dict[str, Any]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item: dict[str, Any] = UNSET
                if not isinstance(conditions_item_data, Unset):
                    conditions_item = conditions_item_data.to_dict()

                conditions.append(conditions_item)

        states: list[dict[str, Any]] = UNSET
        if not isinstance(self.states, Unset):
            states = []
            for states_item_data in self.states:
                states_item: dict[str, Any] = UNSET
                if not isinstance(states_item_data, Unset):
                    states_item = states_item_data.to_dict()

                states.append(states_item)

        classified_state = self.classified_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(accepts, Unset):
            field_dict["accepts"] = accepts
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(description, Unset):
            field_dict["description"] = description
        if not isinstance(priority, Unset):
            field_dict["priority"] = priority
        if not isinstance(conditions, Unset):
            field_dict["conditions"] = conditions
        if not isinstance(states, Unset):
            field_dict["states"] = states
        if not isinstance(classified_state, Unset):
            field_dict["classified_state"] = classified_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.classification_check import ClassificationCheck
        from ..models.classification_state import ClassificationState

        d = src_dict.copy()
        accepts = d.pop("accepts", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        priority = d.pop("priority", UNSET)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            _conditions_item = conditions_item_data
            conditions_item: ClassificationCheck
            if isinstance(_conditions_item, Unset):
                conditions_item = UNSET
            else:
                conditions_item = ClassificationCheck.from_dict(_conditions_item)

            conditions.append(conditions_item)

        states = []
        _states = d.pop("states", UNSET)
        for states_item_data in _states or []:
            _states_item = states_item_data
            states_item: ClassificationState
            if isinstance(_states_item, Unset):
                states_item = UNSET
            else:
                states_item = ClassificationState.from_dict(_states_item)

            states.append(states_item)

        classified_state = d.pop("classified_state", UNSET)

        classification_workflow = cls(
            accepts=accepts,
            name=name,
            description=description,
            priority=priority,
            conditions=conditions,
            states=states,
            classified_state=classified_state,
        )

        classification_workflow.additional_properties = d
        return classification_workflow

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
