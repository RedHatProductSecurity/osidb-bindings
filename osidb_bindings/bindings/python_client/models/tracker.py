import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.erratum import Erratum
from ..models.tracker_meta_attr import TrackerMetaAttr
from ..models.tracker_type_enum import TrackerTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Tracker")


@attr.s(auto_attribs=True)
class Tracker:
    """Tracker serializer"""

    uuid: str
    type: TrackerTypeEnum
    external_system_id: str
    status: str
    errata: List[Erratum]
    meta_attr: TrackerMetaAttr
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    affects: Union[Unset, List[str]] = UNSET
    resolution: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = TrackerTypeEnum(self.type).value

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

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        type: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.type, Unset):

            type = TrackerTypeEnum(self.type).value

        external_system_id = (
            self.external_system_id
            if self.external_system_id is UNSET
            else (None, str(self.external_system_id), "text/plain")
        )
        status = self.status if self.status is UNSET else (None, str(self.status), "text/plain")
        errata: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.errata, Unset):
            _temp_errata = []
            for errata_item_data in self.errata:
                errata_item: Dict[str, Any] = UNSET
                if not isinstance(errata_item_data, Unset):
                    errata_item = errata_item_data.to_dict()

                _temp_errata.append(errata_item)
            errata = (None, json.dumps(_temp_errata), "application/json")

        meta_attr: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = (None, json.dumps(self.meta_attr.to_dict()), "application/json")

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        affects: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.affects, Unset):
            _temp_affects = self.affects
            affects = (None, json.dumps(_temp_affects), "application/json")

        resolution = self.resolution if self.resolution is UNSET else (None, str(self.resolution), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        _type = d.pop("type", UNSET)
        type: TrackerTypeEnum
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TrackerTypeEnum(_type)

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
        )

        tracker.additional_properties = d
        return tracker

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
