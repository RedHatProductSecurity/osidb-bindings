from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.package_ver import PackageVer
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="Package")


@attr.s(auto_attribs=True)
class Package(OSIDBModel):
    """package_versions (Package model) serializer for read-only use in FlawSerializer."""

    package: str
    versions: List[PackageVer]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package = self.package
        versions: List[Dict[str, Any]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item: Dict[str, Any] = UNSET
                if not isinstance(versions_item_data, Unset):
                    versions_item = versions_item_data.to_dict()

                versions.append(versions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(package, Unset):
            field_dict["package"] = package
        if not isinstance(versions, Unset):
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        package = d.pop("package", UNSET)

        versions = []
        _versions = d.pop("versions", UNSET)
        if _versions is UNSET:
            versions = UNSET
        else:
            for versions_item_data in _versions or []:
                _versions_item = versions_item_data
                versions_item: PackageVer
                if isinstance(_versions_item, Unset):
                    versions_item = UNSET
                else:
                    versions_item = PackageVer.from_dict(_versions_item)

                versions.append(versions_item)

        package = cls(
            package=package,
            versions=versions,
        )

        package.additional_properties = d
        return package

    @staticmethod
    def get_fields():
        return {
            "package": str,
            "versions": List[PackageVer],
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
