from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawCommentPostRequest")


@_attrs_define
class FlawCommentPostRequest(OSIDBModel):
    """FlawComment serializer for use by flaw_comments endpoint

    Attributes:
        text (str):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        creator (Union[Unset, str]):
        is_private (Union[Unset, bool]):
    """

    text: str
    embargoed: bool
    creator: Union[Unset, str] = UNSET
    is_private: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        embargoed = self.embargoed

        creator = self.creator

        is_private = self.is_private

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(text, Unset):
            field_dict["text"] = text
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(creator, Unset):
            field_dict["creator"] = creator
        if not isinstance(is_private, Unset):
            field_dict["is_private"] = is_private

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        text = (None, str(self.text).encode(), "text/plain")

        embargoed = (None, str(self.embargoed).encode(), "text/plain")

        creator = (
            self.creator
            if isinstance(self.creator, Unset)
            else (None, str(self.creator).encode(), "text/plain")
        )

        is_private = (
            self.is_private
            if isinstance(self.is_private, Unset)
            else (None, str(self.is_private).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(text, Unset):
            field_dict["text"] = text
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(creator, Unset):
            field_dict["creator"] = creator
        if not isinstance(is_private, Unset):
            field_dict["is_private"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        creator = d.pop("creator", UNSET)

        is_private = d.pop("is_private", UNSET)

        flaw_comment_post_request = cls(
            text=text,
            embargoed=embargoed,
            creator=creator,
            is_private=is_private,
        )

        flaw_comment_post_request.additional_properties = d
        return flaw_comment_post_request

    @staticmethod
    def get_fields():
        return {
            "text": str,
            "embargoed": bool,
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
