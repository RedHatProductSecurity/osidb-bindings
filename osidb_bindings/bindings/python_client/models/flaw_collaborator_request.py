from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.state_enum import StateEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawCollaboratorRequest")


@_attrs_define
class FlawCollaboratorRequest(OSIDBModel):
    """FlawCollaborator serializer

    Attributes:
        flaw (UUID):
        label (str):
        state (Union[Unset, StateEnum]):
        contributor (Union[Unset, str]):
        relevant (Union[Unset, bool]):
    """

    flaw: UUID
    label: str
    state: Union[Unset, StateEnum] = UNSET
    contributor: Union[Unset, str] = UNSET
    relevant: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flaw: str = UNSET
        if not isinstance(self.flaw, Unset):
            flaw = str(self.flaw)

        label = self.label

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = StateEnum(self.state).value

        contributor = self.contributor

        relevant = self.relevant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(label, Unset):
            field_dict["label"] = label
        if not isinstance(state, Unset):
            field_dict["state"] = state
        if not isinstance(contributor, Unset):
            field_dict["contributor"] = contributor
        if not isinstance(relevant, Unset):
            field_dict["relevant"] = relevant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _flaw = d.pop("flaw", UNSET)
        flaw: UUID
        if isinstance(_flaw, Unset):
            flaw = UNSET
        else:
            flaw = _flaw if isinstance(_flaw, UUID) else UUID(_flaw)

        label = d.pop("label", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, StateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StateEnum(_state)

        contributor = d.pop("contributor", UNSET)

        relevant = d.pop("relevant", UNSET)

        flaw_collaborator_request = cls(
            flaw=flaw,
            label=label,
            state=state,
            contributor=contributor,
            relevant=relevant,
        )

        flaw_collaborator_request.additional_properties = d
        return flaw_collaborator_request

    @staticmethod
    def get_fields():
        return {
            "flaw": UUID,
            "label": str,
            "state": StateEnum,
            "contributor": str,
            "relevant": bool,
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
