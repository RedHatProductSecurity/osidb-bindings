import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.flaw_version import FlawVersion
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawPackageVersionPut")


@attr.s(auto_attribs=True)
class FlawPackageVersionPut(OSIDBModel):
    """Package model serializer"""

    package: str
    versions: List[FlawVersion]
    uuid: str
    embargoed: bool
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
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

        uuid = self.uuid
        embargoed = self.embargoed
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        field_dict: Dict[str, Any] = {}
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

    def to_multipart(self) -> Dict[str, Any]:
        package = (
            self.package
            if self.package is UNSET
            else (None, str(self.package), "text/plain")
        )
        versions: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.versions, Unset):
            _temp_versions = []
            for versions_item_data in self.versions:
                versions_item: Dict[str, Any] = UNSET
                if not isinstance(versions_item_data, Unset):
                    versions_item = versions_item_data.to_dict()

                _temp_versions.append(versions_item)
            versions = (None, json.dumps(_temp_versions), "application/json")

        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        embargoed = (
            self.embargoed
            if self.embargoed is UNSET
            else (None, str(self.embargoed), "text/plain")
        )
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
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
                versions_item: FlawVersion
                if isinstance(_versions_item, Unset):
                    versions_item = UNSET
                else:
                    versions_item = FlawVersion.from_dict(_versions_item)

                versions.append(versions_item)

        uuid = d.pop("uuid", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

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
            "versions": List[FlawVersion],
            "uuid": str,
            "embargoed": bool,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
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
