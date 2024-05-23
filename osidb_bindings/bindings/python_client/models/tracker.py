import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.erratum import Erratum
from ..models.tracker_alerts import TrackerAlerts
from ..models.tracker_meta_attr import TrackerMetaAttr
from ..models.tracker_type import TrackerType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="Tracker")


@attr.s(auto_attribs=True)
class Tracker(OSIDBModel):
    """Tracker serializer"""

    errata: List[Erratum]
    external_system_id: str
    meta_attr: TrackerMetaAttr
    status: str
    type: TrackerType
    uuid: str
    embargoed: bool
    alerts: TrackerAlerts
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    affects: Union[Unset, List[str]] = UNSET
    ps_update_stream: Union[Unset, str] = UNSET
    resolution: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errata: List[Dict[str, Any]] = UNSET
        if not isinstance(self.errata, Unset):
            errata = []
            for errata_item_data in self.errata:
                errata_item: Dict[str, Any] = UNSET
                if not isinstance(errata_item_data, Unset):
                    errata_item = errata_item_data.to_dict()

                errata.append(errata_item)

        external_system_id = self.external_system_id
        meta_attr: Dict[str, Any] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        status = self.status
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = TrackerType(self.type).value

        uuid = self.uuid
        embargoed = self.embargoed
        alerts: Dict[str, Any] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = self.alerts.to_dict()

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        affects: Union[Unset, List[str]] = UNSET
        if not isinstance(self.affects, Unset):
            affects = self.affects

        ps_update_stream = self.ps_update_stream
        resolution = self.resolution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(errata, Unset):
            field_dict["errata"] = errata
        if not isinstance(external_system_id, Unset):
            field_dict["external_system_id"] = external_system_id
        if not isinstance(meta_attr, Unset):
            field_dict["meta_attr"] = meta_attr
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(type, Unset):
            field_dict["type"] = type
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(affects, Unset):
            field_dict["affects"] = affects
        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        errata: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.errata, Unset):
            _temp_errata = []
            for errata_item_data in self.errata:
                errata_item: Dict[str, Any] = UNSET
                if not isinstance(errata_item_data, Unset):
                    errata_item = errata_item_data.to_dict()

                _temp_errata.append(errata_item)
            errata = (None, json.dumps(_temp_errata), "application/json")

        external_system_id = (
            self.external_system_id
            if self.external_system_id is UNSET
            else (None, str(self.external_system_id), "text/plain")
        )
        meta_attr: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = (None, json.dumps(self.meta_attr.to_dict()), "application/json")

        status = (
            self.status
            if self.status is UNSET
            else (None, str(self.status), "text/plain")
        )
        type: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.type, Unset):

            type = TrackerType(self.type).value

        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        embargoed = (
            self.embargoed
            if self.embargoed is UNSET
            else (None, str(self.embargoed), "text/plain")
        )
        alerts: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = (None, json.dumps(self.alerts.to_dict()), "application/json")

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

        ps_update_stream = (
            self.ps_update_stream
            if self.ps_update_stream is UNSET
            else (None, str(self.ps_update_stream), "text/plain")
        )
        resolution = (
            self.resolution
            if self.resolution is UNSET
            else (None, str(self.resolution), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        if not isinstance(errata, Unset):
            field_dict["errata"] = errata
        if not isinstance(external_system_id, Unset):
            field_dict["external_system_id"] = external_system_id
        if not isinstance(meta_attr, Unset):
            field_dict["meta_attr"] = meta_attr
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(type, Unset):
            field_dict["type"] = type
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(affects, Unset):
            field_dict["affects"] = affects
        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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

        external_system_id = d.pop("external_system_id", UNSET)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: TrackerMetaAttr
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = TrackerMetaAttr.from_dict(_meta_attr)

        status = d.pop("status", UNSET)

        _type = d.pop("type", UNSET)
        type: TrackerType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TrackerType(_type)

        uuid = d.pop("uuid", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        _alerts = d.pop("alerts", UNSET)
        alerts: TrackerAlerts
        if isinstance(_alerts, Unset):
            alerts = UNSET
        else:
            alerts = TrackerAlerts.from_dict(_alerts)

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

        ps_update_stream = d.pop("ps_update_stream", UNSET)

        resolution = d.pop("resolution", UNSET)

        tracker = cls(
            errata=errata,
            external_system_id=external_system_id,
            meta_attr=meta_attr,
            status=status,
            type=type,
            uuid=uuid,
            embargoed=embargoed,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            affects=affects,
            ps_update_stream=ps_update_stream,
            resolution=resolution,
        )

        tracker.additional_properties = d
        return tracker

    @staticmethod
    def get_fields():
        return {
            "errata": List[Erratum],
            "external_system_id": str,
            "meta_attr": TrackerMetaAttr,
            "status": str,
            "type": TrackerType,
            "uuid": str,
            "embargoed": bool,
            "alerts": TrackerAlerts,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "affects": List[str],
            "ps_update_stream": str,
            "resolution": str,
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
