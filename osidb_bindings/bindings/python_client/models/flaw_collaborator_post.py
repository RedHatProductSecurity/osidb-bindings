from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.state_enum import StateEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawCollaboratorPost")


@_attrs_define
class FlawCollaboratorPost(OSIDBModel):
    """FlawCollaborator serializer

    Attributes:
        uuid (UUID):
        label (str):
        state (Union[Unset, StateEnum]):
        contributor (Union[Unset, str]):
    """

    uuid: UUID
    label: str
    state: Union[Unset, StateEnum] = UNSET
    contributor: Union[Unset, str] = UNSET
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

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        uuid: bytes = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        label = (None, str(self.label).encode(), "text/plain")

        state: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.state, Unset):
            state = (None, str(self.state.value).encode(), "text/plain")
        # CHANGE END (3) #}

        contributor = (
            self.contributor
            if isinstance(self.contributor, Unset)
            else (None, str(self.contributor).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(label, Unset):
            field_dict["label"] = label
        if not isinstance(state, Unset):
            field_dict["state"] = state
        if not isinstance(contributor, Unset):
            field_dict["contributor"] = contributor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        # }
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        label = d.pop("label", UNSET)

        # }
        _state = d.pop("state", UNSET)
        state: Union[Unset, StateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StateEnum(_state)

        contributor = d.pop("contributor", UNSET)

        flaw_collaborator_post = cls(
            uuid=uuid,
            label=label,
            state=state,
            contributor=contributor,
        )

        flaw_collaborator_post.additional_properties = d
        return flaw_collaborator_post

    @staticmethod
    def get_fields():
        return {
            "uuid": UUID,
            "label": str,
            "state": StateEnum,
            "contributor": str,
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
