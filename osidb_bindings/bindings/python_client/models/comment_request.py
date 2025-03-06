import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="CommentRequest")


@_attrs_define
class CommentRequest(OSIDBModel):
    """FlawComment serializer for use by FlawSerializer

    Attributes:
        text (str):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        external_system_id (Union[Unset, str]):
        order (Union[None, Unset, int]):
        creator (Union[Unset, str]):
        is_private (Union[Unset, bool]):
    """

    text: str
    updated_dt: datetime.datetime
    external_system_id: Union[Unset, str] = UNSET
    order: Union[None, Unset, int] = UNSET
    creator: Union[Unset, str] = UNSET
    is_private: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        external_system_id = self.external_system_id

        order: Union[None, Unset, int]
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        creator = self.creator

        is_private = self.is_private

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(text, Unset):
            field_dict["text"] = text
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(external_system_id, Unset):
            field_dict["external_system_id"] = external_system_id
        if not isinstance(order, Unset):
            field_dict["order"] = order
        if not isinstance(creator, Unset):
            field_dict["creator"] = creator
        if not isinstance(is_private, Unset):
            field_dict["is_private"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        external_system_id = d.pop("external_system_id", UNSET)

        def _parse_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        order = _parse_order(d.pop("order", UNSET))

        creator = d.pop("creator", UNSET)

        is_private = d.pop("is_private", UNSET)

        comment_request = cls(
            text=text,
            updated_dt=updated_dt,
            external_system_id=external_system_id,
            order=order,
            creator=creator,
            is_private=is_private,
        )

        comment_request.additional_properties = d
        return comment_request

    @staticmethod
    def get_fields():
        return {
            "text": str,
            "updated_dt": datetime.datetime,
            "external_system_id": str,
            "order": Union[None, int],
            "creator": str,
            "is_private": bool,
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
