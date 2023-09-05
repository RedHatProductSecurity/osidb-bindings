import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.erratum import Erratum
from ..models.tracker_meta_attr import TrackerMetaAttr
from ..models.tracker_type import TrackerType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="Tracker")


@attr.s(auto_attribs=True)
class Tracker(OSIDBModel):
    """Tracker serializer"""

    uuid: str
    type: TrackerType
    external_system_id: str
    status: str
    errata: List[Erratum]
    meta_attr: TrackerMetaAttr
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    affects: Union[Unset, List[str]] = UNSET
    resolution: Union[Unset, str] = UNSET
    ps_update_stream: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = TrackerType(self.type).value

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
        ps_update_stream = self.ps_update_stream

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(type, Unset):
            field_dict["type"] = type
        if not isinstance(external_system_id, Unset):
            field_dict["external_system_id"] = external_system_id
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(errata, Unset):
            field_dict["errata"] = errata
        if not isinstance(meta_attr, Unset):
            field_dict["meta_attr"] = meta_attr
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(affects, Unset):
            field_dict["affects"] = affects
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        _type = d.pop("type", UNSET)
        type: TrackerType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TrackerType(_type)

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

        ps_update_stream = d.pop("ps_update_stream", UNSET)

        tracker = cls(
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
            ps_update_stream=ps_update_stream,
        )

        tracker.additional_properties = d
        return tracker

    @staticmethod
    def get_fields():
        return {
            "uuid": str,
            "type": TrackerType,
            "external_system_id": str,
            "status": str,
            "errata": List[Erratum],
            "meta_attr": TrackerMetaAttr,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "affects": List[str],
            "resolution": str,
            "ps_update_stream": str,
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
