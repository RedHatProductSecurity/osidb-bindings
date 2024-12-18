from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flaw_post_classification_state import FlawPostClassificationState
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawPostClassification")


@_attrs_define
class FlawPostClassification(OSIDBModel):
    """
    Attributes:
        workflow (Union[Unset, str]):
        state (Union[Unset, FlawPostClassificationState]):
    """

    workflow: Union[Unset, str] = UNSET
    state: Union[Unset, FlawPostClassificationState] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow = self.workflow

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = FlawPostClassificationState(self.state).value

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

        # }
        _state = d.pop("state", UNSET)
        state: Union[Unset, FlawPostClassificationState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = FlawPostClassificationState(_state)

        flaw_post_classification = cls(
            workflow=workflow,
            state=state,
        )

        flaw_post_classification.additional_properties = d
        return flaw_post_classification

    @staticmethod
    def get_fields():
        return {
            "workflow": str,
            "state": FlawPostClassificationState,
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
