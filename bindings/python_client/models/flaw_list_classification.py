from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.flaw_list_classification_state import FlawListClassificationState
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlawListClassification")


@attr.s(auto_attribs=True)
class FlawListClassification:
    """ """

    workflow: Union[Unset, str] = UNSET
    state: Union[Unset, FlawListClassificationState] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflow = self.workflow
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):

            state = FlawListClassificationState(self.state).value

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
        state: Union[Unset, FlawListClassificationState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = FlawListClassificationState(_state)

        flaw_list_classification = cls(
            workflow=workflow,
            state=state,
        )

        flaw_list_classification.additional_properties = d
        return flaw_list_classification

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
