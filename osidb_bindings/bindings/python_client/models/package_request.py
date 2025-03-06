from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.package_ver_request import PackageVerRequest


T = TypeVar("T", bound="PackageRequest")


@_attrs_define
class PackageRequest(OSIDBModel):
    """package_versions (Package model) serializer for read-only use in FlawSerializer.

    Attributes:
        package (str):
        versions (list['PackageVerRequest']):
    """

    package: str
    versions: list["PackageVerRequest"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package = self.package

        versions: list[dict[str, Any]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item: dict[str, Any] = UNSET
                if not isinstance(versions_item_data, Unset):
                    versions_item = versions_item_data.to_dict()

                versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(package, Unset):
            field_dict["package"] = package
        if not isinstance(versions, Unset):
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.package_ver_request import PackageVerRequest

        d = src_dict.copy()
        package = d.pop("package", UNSET)

        versions = []
        _versions = d.pop("versions", UNSET)
        for versions_item_data in _versions or []:
            _versions_item = versions_item_data
            versions_item: PackageVerRequest
            if isinstance(_versions_item, Unset):
                versions_item = UNSET
            else:
                versions_item = PackageVerRequest.from_dict(_versions_item)

            versions.append(versions_item)

        package_request = cls(
            package=package,
            versions=versions,
        )

        package_request.additional_properties = d
        return package_request

    @staticmethod
    def get_fields():
        return {
            "package": str,
            "versions": list["PackageVerRequest"],
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
