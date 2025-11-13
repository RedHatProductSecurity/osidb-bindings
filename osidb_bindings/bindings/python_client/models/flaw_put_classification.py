from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..models.flaw_put_classification_state import FlawPutClassificationState
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawPutClassification")


@_attrs_define
class FlawPutClassification(OSIDBModel):
    """
    Attributes:
        workflow (Union[Unset, str]):
        state (Union[Unset, FlawPutClassificationState]):
    """

    workflow: Union[Unset, str] = UNSET
    state: Union[Unset, FlawPutClassificationState] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow = self.workflow

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = FlawPutClassificationState(self.state).value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(workflow, Unset):
            field_dict["workflow"] = workflow
        if not isinstance(state, Unset):
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        workflow = d.pop("workflow", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, FlawPutClassificationState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = FlawPutClassificationState(_state)

        flaw_put_classification = cls(
            workflow=workflow,
            state=state,
        )

        flaw_put_classification.additional_properties = d
        return flaw_put_classification

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
