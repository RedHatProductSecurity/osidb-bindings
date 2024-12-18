import datetime
import json
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.flaw_version import FlawVersion


T = TypeVar("T", bound="FlawPackageVersionPut")


@_attrs_define
class FlawPackageVersionPut(OSIDBModel):
    """Package model serializer

    Attributes:
        package (str):
        versions (list['FlawVersion']):
        uuid (UUID):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
    """

    package: str
    versions: list["FlawVersion"]
    uuid: UUID
    embargoed: bool
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
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

        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        embargoed = self.embargoed

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(package, Unset):
            field_dict["package"] = package
        if not isinstance(versions, Unset):
            field_dict["versions"] = versions
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt

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

        uuid: bytes = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        embargoed = (None, str(self.embargoed).encode(), "text/plain")

        created_dt: bytes = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat().encode()

        updated_dt: bytes = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat().encode()

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(package, Unset):
            field_dict["package"] = package
        if not isinstance(versions, Unset):
            field_dict["versions"] = versions
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.flaw_version import FlawVersion

        d = src_dict.copy()
        package = d.pop("package", UNSET)

        versions = []
        _versions = d.pop("versions", UNSET)
        for versions_item_data in _versions or []:
            # }
            _versions_item = versions_item_data
            versions_item: FlawVersion
            if isinstance(_versions_item, Unset):
                versions_item = UNSET
            else:
                versions_item = FlawVersion.from_dict(_versions_item)

            versions.append(versions_item)

        # }
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        embargoed = d.pop("embargoed", UNSET)

        # }
        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        # }
        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        flaw_package_version_put = cls(
            package=package,
            versions=versions,
            uuid=uuid,
            embargoed=embargoed,
            created_dt=created_dt,
            updated_dt=updated_dt,
        )

        flaw_package_version_put.additional_properties = d
        return flaw_package_version_put

    @staticmethod
    def get_fields():
        return {
            "package": str,
            "versions": list["FlawVersion"],
            "uuid": UUID,
            "embargoed": bool,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
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
