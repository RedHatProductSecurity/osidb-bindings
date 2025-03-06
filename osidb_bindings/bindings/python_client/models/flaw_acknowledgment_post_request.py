from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawAcknowledgmentPostRequest")


@_attrs_define
class FlawAcknowledgmentPostRequest(OSIDBModel):
    """FlawAcknowledgment serializer

    Attributes:
        name (str):
        affiliation (str):
        from_upstream (bool):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
    """

    name: str
    affiliation: str
    from_upstream: bool
    embargoed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        affiliation = self.affiliation

        from_upstream = self.from_upstream

        embargoed = self.embargoed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(affiliation, Unset):
            field_dict["affiliation"] = affiliation
        if not isinstance(from_upstream, Unset):
            field_dict["from_upstream"] = from_upstream
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        affiliation = (None, str(self.affiliation).encode(), "text/plain")

        from_upstream = (None, str(self.from_upstream).encode(), "text/plain")

        embargoed = (None, str(self.embargoed).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(affiliation, Unset):
            field_dict["affiliation"] = affiliation
        if not isinstance(from_upstream, Unset):
            field_dict["from_upstream"] = from_upstream
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        affiliation = d.pop("affiliation", UNSET)

        from_upstream = d.pop("from_upstream", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        flaw_acknowledgment_post_request = cls(
            name=name,
            affiliation=affiliation,
            from_upstream=from_upstream,
            embargoed=embargoed,
        )

        flaw_acknowledgment_post_request.additional_properties = d
        return flaw_acknowledgment_post_request

    @staticmethod
    def get_fields():
        return {
            "name": str,
            "affiliation": str,
            "from_upstream": bool,
            "embargoed": bool,
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
