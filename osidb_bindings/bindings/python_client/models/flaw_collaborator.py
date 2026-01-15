from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..models.flaw_label_type import FlawLabelType
from ..models.state_enum import StateEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawCollaborator")


@_attrs_define
class FlawCollaborator(OSIDBModel):
    """FlawCollaborator serializer

    Attributes:
        uuid (UUID):
        label (str):
        state (Union[Unset, StateEnum]):
        contributor (Union[Unset, str]):
        relevant (Union[Unset, bool]):
        type_ (Union[Unset, FlawLabelType]):  Default: FlawLabelType.CONTEXT_BASED.
    """

    uuid: UUID
    label: str
    state: Union[Unset, StateEnum] = UNSET
    contributor: Union[Unset, str] = UNSET
    relevant: Union[Unset, bool] = UNSET
    type_: Union[Unset, FlawLabelType] = FlawLabelType.CONTEXT_BASED
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        label = self.label

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = StateEnum(self.state).value

        contributor = self.contributor

        relevant = self.relevant

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = FlawLabelType(self.type_).value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(label, Unset):
            field_dict["label"] = label
        if not isinstance(state, Unset):
            field_dict["state"] = state
        if not isinstance(contributor, Unset):
            field_dict["contributor"] = contributor
        if not isinstance(relevant, Unset):
            field_dict["relevant"] = relevant
        if not isinstance(type_, Unset):
            field_dict["type"] = type_

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

        _state = d.pop("state", UNSET)
        state: Union[Unset, StateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StateEnum(_state)

        contributor = d.pop("contributor", UNSET)

        relevant = d.pop("relevant", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, FlawLabelType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FlawLabelType(_type_)

        flaw_collaborator = cls(
            uuid=uuid,
            label=label,
            state=state,
            contributor=contributor,
            relevant=relevant,
            type_=type_,
        )

        flaw_collaborator.additional_properties = d
        return flaw_collaborator

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
