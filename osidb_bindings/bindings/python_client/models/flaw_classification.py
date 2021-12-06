from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.flaw_classification_state import FlawClassificationState
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlawClassification")


@attr.s(auto_attribs=True)
class FlawClassification:
    """ """

    workflow: Union[Unset, str] = UNSET
    state: Union[Unset, FlawClassificationState] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflow = self.workflow
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):

            state = FlawClassificationState(self.state).value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        workflow = d.pop("workflow", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, FlawClassificationState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = FlawClassificationState(_state)

        flaw_classification = cls(
            workflow=workflow,
            state=state,
        )

        flaw_classification.additional_properties = d
        return flaw_classification

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
