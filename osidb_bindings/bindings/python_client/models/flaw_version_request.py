from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawVersionRequest")


@_attrs_define
class FlawVersionRequest(OSIDBModel):
    """PackageVer serializer used by FlawPackageVersionSerializer.

    Attributes:
        version (str):
    """

    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(version, Unset):
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        flaw_version_request = cls(
            version=version,
        )

        flaw_version_request.additional_properties = d
        return flaw_version_request

    @staticmethod
    def get_fields():
        return {
            "version": str,
        }

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
