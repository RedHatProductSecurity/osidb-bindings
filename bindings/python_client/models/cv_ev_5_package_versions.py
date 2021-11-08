from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.cv_ev_5_versions import CVEv5Versions

T = TypeVar("T", bound="CVEv5PackageVersions")


@attr.s(auto_attribs=True)
class CVEv5PackageVersions:
    """CVEv5 package versions serializer"""

    package: str
    versions: List[CVEv5Versions]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package = self.package
        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()

            versions.append(versions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package": package,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        package = d.pop("package")

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = CVEv5Versions.from_dict(versions_item_data)

            versions.append(versions_item)

        cv_ev_5_package_versions = cls(
            package=package,
            versions=versions,
        )

        cv_ev_5_package_versions.additional_properties = d
        return cv_ev_5_package_versions

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
