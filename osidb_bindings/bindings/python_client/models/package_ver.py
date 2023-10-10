from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="PackageVer")


@attr.s(auto_attribs=True)
class PackageVer(OSIDBModel):
    """PackageVer model serializer for read-only use in FlawSerializer via
    PackageVerSerializer."""

    version: str
    status: str = "UNAFFECTED"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(version, Unset):
            field_dict["version"] = version
        if not isinstance(status, Unset):
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
