import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.flaw_version import FlawVersion
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1FlawsPackageVersionsUpdateResponse200")


@attr.s(auto_attribs=True)
class OsidbApiV1FlawsPackageVersionsUpdateResponse200(OSIDBModel):
    """ """

    package: str
    versions: List[FlawVersion]
    flaw: str
    uuid: str
    embargoed: bool
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
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

        flaw = self.flaw
        uuid = self.uuid
        embargoed = self.embargoed
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(package, Unset):
            field_dict["package"] = package
        if not isinstance(versions, Unset):
            field_dict["versions"] = versions
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(dt, Unset):
            field_dict["dt"] = dt
        if not isinstance(env, Unset):
            field_dict["env"] = env
        if not isinstance(revision, Unset):
            field_dict["revision"] = revision
        if not isinstance(version, Unset):
            field_dict["version"] = version

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

        flaw = d.pop("flaw", UNSET)

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

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_flaws_package_versions_update_response_200 = cls(
            package=package,
            versions=versions,
            flaw=flaw,
            uuid=uuid,
            embargoed=embargoed,
            created_dt=created_dt,
            updated_dt=updated_dt,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_flaws_package_versions_update_response_200.additional_properties = (
            d
        )
        return osidb_api_v1_flaws_package_versions_update_response_200

    @staticmethod
    def get_fields():
        return {
            "package": str,
            "versions": List[FlawVersion],
            "flaw": str,
            "uuid": str,
            "embargoed": bool,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "dt": datetime.datetime,
            "env": str,
            "revision": str,
            "version": str,
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
