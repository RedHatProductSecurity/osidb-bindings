import datetime
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.flaw_reference_type import FlawReferenceType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawReferenceRequest")


@_attrs_define
class FlawReferenceRequest(OSIDBModel):
    """FlawReference serializer

    Attributes:
        flaw (UUID):
        url (str):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        description (Union[Unset, str]):
        type_ (Union[Unset, FlawReferenceType]):
    """

    flaw: UUID
    url: str
    embargoed: bool
    updated_dt: datetime.datetime
    description: Union[Unset, str] = UNSET
    type_: Union[Unset, FlawReferenceType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flaw: str = UNSET
        if not isinstance(self.flaw, Unset):
            flaw = str(self.flaw)

        url = self.url

        embargoed = self.embargoed

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        description = self.description

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = FlawReferenceType(self.type_).value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(url, Unset):
            field_dict["url"] = url
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(description, Unset):
            field_dict["description"] = description
        if not isinstance(type_, Unset):
            field_dict["type"] = type_

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

        url = d.pop("url", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, FlawReferenceType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FlawReferenceType(_type_)

        flaw_reference_request = cls(
            flaw=flaw,
            url=url,
            embargoed=embargoed,
            updated_dt=updated_dt,
            description=description,
            type_=type_,
        )

        flaw_reference_request.additional_properties = d
        return flaw_reference_request

    @staticmethod
    def get_fields():
        return {
            "flaw": UUID,
            "url": str,
            "embargoed": bool,
            "updated_dt": datetime.datetime,
            "description": str,
            "type": FlawReferenceType,
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
