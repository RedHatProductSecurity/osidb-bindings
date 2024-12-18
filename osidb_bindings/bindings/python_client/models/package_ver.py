from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="PackageVer")


@_attrs_define
class PackageVer(OSIDBModel):
    """PackageVer model serializer for read-only use in FlawSerializer via
    PackageVerSerializer.

        Attributes:
            version (str):
            status (str):  Default: 'UNAFFECTED'.
    """

    version: str
    status: str = "UNAFFECTED"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(version, Unset):
            field_dict["version"] = version
        if not isinstance(status, Unset):
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        status = d.pop("status", UNSET)

        package_ver = cls(
            version=version,
            status=status,
        )

        package_ver.additional_properties = d
        return package_ver

    @staticmethod
    def get_fields():
        return {
            "version": str,
            "status": str,
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
