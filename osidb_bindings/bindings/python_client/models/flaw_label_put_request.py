from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..models.state_enum import StateEnum
from ..models.type_96f_enum import Type96FEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawLabelPutRequest")


@_attrs_define
class FlawLabelPutRequest(OSIDBModel):
    """Flaw label serializer with type-specific fields

    Attributes:
        name (str):
        type_ (Union[Unset, Type96FEnum]):
        state (Union[Unset, StateEnum]):
        contributor (Union[Unset, str]):
        relevant (Union[Unset, bool]):
    """

    name: str
    type_: Union[Unset, Type96FEnum] = UNSET
    state: Union[Unset, StateEnum] = UNSET
    contributor: Union[Unset, str] = UNSET
    relevant: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = Type96FEnum(self.type_).value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = StateEnum(self.state).value

        contributor = self.contributor

        relevant = self.relevant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(type_, Unset):
            field_dict["type"] = type_
        if not isinstance(state, Unset):
            field_dict["state"] = state
        if not isinstance(contributor, Unset):
            field_dict["contributor"] = contributor
        if not isinstance(relevant, Unset):
            field_dict["relevant"] = relevant

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        type_: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = (None, str(self.type_.value).encode(), "text/plain")

        state: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.state, Unset):
            state = (None, str(self.state.value).encode(), "text/plain")

        contributor = (
            self.contributor
            if isinstance(self.contributor, Unset)
            else (None, str(self.contributor).encode(), "text/plain")
        )

        relevant = (
            self.relevant
            if isinstance(self.relevant, Unset)
            else (None, str(self.relevant).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(name, Unset):
            field_dict["name"] = name
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
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, Type96FEnum]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Type96FEnum(_type_)

        _state = d.pop("state", UNSET)
        state: Union[Unset, StateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StateEnum(_state)

        contributor = d.pop("contributor", UNSET)

        relevant = d.pop("relevant", UNSET)

        flaw_label_put_request = cls(
            name=name,
            type_=type_,
            state=state,
            contributor=contributor,
            relevant=relevant,
        )

        flaw_label_put_request.additional_properties = d
        return flaw_label_put_request

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
