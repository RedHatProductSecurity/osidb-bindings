from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.state_enum import StateEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawCollaborator")


@_attrs_define
class FlawCollaborator(OSIDBModel):
    """FlawCollaborator serializer

    Attributes:
        uuid (UUID):
        label (str):
        type_ (str):
        state (Union[Unset, StateEnum]):
        contributor (Union[Unset, str]):
        relevant (Union[Unset, bool]):
    """

    uuid: UUID
    label: str
    type_: str
    state: Union[Unset, StateEnum] = UNSET
    contributor: Union[Unset, str] = UNSET
    relevant: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        label = self.label

        type_ = self.type_

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = StateEnum(self.state).value

        contributor = self.contributor

        relevant = self.relevant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(label, Unset):
            field_dict["label"] = label
        if not isinstance(type_, Unset):
            field_dict["type"] = type_
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
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        label = d.pop("label", UNSET)

        type_ = d.pop("type", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, StateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StateEnum(_state)

        contributor = d.pop("contributor", UNSET)

        relevant = d.pop("relevant", UNSET)

        flaw_collaborator = cls(
            uuid=uuid,
            label=label,
            type_=type_,
            state=state,
            contributor=contributor,
            relevant=relevant,
        )

        flaw_collaborator.additional_properties = d
        return flaw_collaborator

    @staticmethod
    def get_fields():
        return {
            "uuid": UUID,
            "label": str,
            "type": str,
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
