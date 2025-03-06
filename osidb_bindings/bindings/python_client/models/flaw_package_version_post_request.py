import json
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.flaw_version_request import FlawVersionRequest


T = TypeVar("T", bound="FlawPackageVersionPostRequest")


@_attrs_define
class FlawPackageVersionPostRequest(OSIDBModel):
    """Package model serializer

    Attributes:
        package (str):
        versions (list['FlawVersionRequest']):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
    """

    package: str
    versions: list["FlawVersionRequest"]
    embargoed: bool
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

        embargoed = self.embargoed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(package, Unset):
            field_dict["package"] = package
        if not isinstance(versions, Unset):
            field_dict["versions"] = versions
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        package = (None, str(self.package).encode(), "text/plain")

        versions: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.versions, Unset):
            _temp_versions = []
            for versions_item_data in self.versions:
                versions_item: dict[str, Any] = UNSET
                if not isinstance(versions_item_data, Unset):
                    versions_item = versions_item_data.to_dict()

                _temp_versions.append(versions_item)
            versions = (None, json.dumps(_temp_versions).encode(), "application/json")

        embargoed = (None, str(self.embargoed).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(package, Unset):
            field_dict["package"] = package
        if not isinstance(versions, Unset):
            field_dict["versions"] = versions
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.flaw_version_request import FlawVersionRequest

        d = src_dict.copy()
        package = d.pop("package", UNSET)

        versions = []
        _versions = d.pop("versions", UNSET)
        for versions_item_data in _versions or []:
            _versions_item = versions_item_data
            versions_item: FlawVersionRequest
            if isinstance(_versions_item, Unset):
                versions_item = UNSET
            else:
                versions_item = FlawVersionRequest.from_dict(_versions_item)

            versions.append(versions_item)

        embargoed = d.pop("embargoed", UNSET)

        flaw_package_version_post_request = cls(
            package=package,
            versions=versions,
            embargoed=embargoed,
        )

        flaw_package_version_post_request.additional_properties = d
        return flaw_package_version_post_request

    @staticmethod
    def get_fields():
        return {
            "package": str,
            "versions": list["FlawVersionRequest"],
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
