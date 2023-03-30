import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.erratum import Erratum
from ..models.tracker_meta_attr import TrackerMetaAttr
from ..models.type_0d0_enum import Type0D0Enum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1TrackersRetrieveResponse200")


@attr.s(auto_attribs=True)
class OsidbApiV1TrackersRetrieveResponse200(OSIDBModel):
    """ """

    uuid: str
    type: Type0D0Enum
    external_system_id: str
    status: str
    errata: List[Erratum]
    meta_attr: TrackerMetaAttr
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    affects: Union[Unset, List[str]] = UNSET
    resolution: Union[Unset, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = Type0D0Enum(self.type).value

        external_system_id = self.external_system_id
        status = self.status
        errata: List[Dict[str, Any]] = UNSET
        if not isinstance(self.errata, Unset):
            errata = []
            for errata_item_data in self.errata:
                errata_item: Dict[str, Any] = UNSET
                if not isinstance(errata_item_data, Unset):
                    errata_item = errata_item_data.to_dict()

                errata.append(errata_item)

        meta_attr: Dict[str, Any] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        affects: Union[Unset, List[str]] = UNSET
        if not isinstance(self.affects, Unset):
            affects = self.affects

        resolution = self.resolution
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if type is not UNSET:
            field_dict["type"] = type
        if external_system_id is not UNSET:
            field_dict["external_system_id"] = external_system_id
        if status is not UNSET:
            field_dict["status"] = status
        if errata is not UNSET:
            field_dict["errata"] = errata
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if updated_dt is not UNSET:
            field_dict["updated_dt"] = updated_dt
        if affects is not UNSET:
            field_dict["affects"] = affects
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if dt is not UNSET:
            field_dict["dt"] = dt
        if env is not UNSET:
            field_dict["env"] = env
        if revision is not UNSET:
            field_dict["revision"] = revision
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        _type = d.pop("type", UNSET)
        type: Type0D0Enum
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = Type0D0Enum(_type)

        external_system_id = d.pop("external_system_id", UNSET)

        status = d.pop("status", UNSET)

        errata = []
        _errata = d.pop("errata", UNSET)
        if _errata is UNSET:
            errata = UNSET
        else:
            for errata_item_data in _errata or []:
                _errata_item = errata_item_data
                errata_item: Erratum
                if isinstance(_errata_item, Unset):
                    errata_item = UNSET
                else:
                    errata_item = Erratum.from_dict(_errata_item)

                errata.append(errata_item)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: TrackerMetaAttr
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = TrackerMetaAttr.from_dict(_meta_attr)

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

        affects = cast(List[str], d.pop("affects", UNSET))

        resolution = d.pop("resolution", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_trackers_retrieve_response_200 = cls(
            uuid=uuid,
            type=type,
            external_system_id=external_system_id,
            status=status,
            errata=errata,
            meta_attr=meta_attr,
            created_dt=created_dt,
            updated_dt=updated_dt,
            affects=affects,
            resolution=resolution,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_trackers_retrieve_response_200.additional_properties = d
        return osidb_api_v1_trackers_retrieve_response_200

    @staticmethod
    def get_fields():
        return {
            "uuid": str,
            "type": Type0D0Enum,
            "external_system_id": str,
            "status": str,
            "errata": List[Erratum],
            "meta_attr": TrackerMetaAttr,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "affects": List[str],
            "resolution": str,
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
