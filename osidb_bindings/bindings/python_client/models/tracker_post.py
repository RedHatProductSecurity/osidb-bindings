import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.alert import Alert
from ..models.erratum import Erratum
from ..models.tracker_type import TrackerType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="TrackerPost")


@attr.s(auto_attribs=True)
class TrackerPost(OSIDBModel):
    """Tracker serializer"""

    errata: List[Erratum]
    ps_update_stream: str
    status: str
    resolution: str
    type: TrackerType
    uuid: str
    embargoed: bool
    alerts: List[Alert]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    affects: Union[Unset, List[str]] = UNSET
    sync_to_bz: Union[Unset, bool] = UNSET
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

        ps_update_stream = self.ps_update_stream
        status = self.status
        resolution = self.resolution
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = TrackerType(self.type).value

        uuid = self.uuid
        embargoed = self.embargoed
        alerts: List[Dict[str, Any]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: Dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                alerts.append(alerts_item)

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        affects: Union[Unset, List[str]] = UNSET
        if not isinstance(self.affects, Unset):
            affects = self.affects

        sync_to_bz = self.sync_to_bz

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(errata, Unset):
            field_dict["errata"] = errata
        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
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
        if not isinstance(sync_to_bz, Unset):
            field_dict["sync_to_bz"] = sync_to_bz

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

        ps_update_stream = (
            self.ps_update_stream
            if self.ps_update_stream is UNSET
            else (None, str(self.ps_update_stream), "text/plain")
        )
        status = (
            self.status
            if self.status is UNSET
            else (None, str(self.status), "text/plain")
        )
        resolution = (
            self.resolution
            if self.resolution is UNSET
            else (None, str(self.resolution), "text/plain")
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
            _temp_alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: Dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                _temp_alerts.append(alerts_item)
            alerts = (None, json.dumps(_temp_alerts), "application/json")

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

        sync_to_bz = (
            self.sync_to_bz
            if self.sync_to_bz is UNSET
            else (None, str(self.sync_to_bz), "text/plain")
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
        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
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
        if not isinstance(sync_to_bz, Unset):
            field_dict["sync_to_bz"] = sync_to_bz

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

        ps_update_stream = d.pop("ps_update_stream", UNSET)

        status = d.pop("status", UNSET)

        resolution = d.pop("resolution", UNSET)

        _type = d.pop("type", UNSET)
        type: TrackerType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TrackerType(_type)

        uuid = d.pop("uuid", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        alerts = []
        _alerts = d.pop("alerts", UNSET)
        if _alerts is UNSET:
            alerts = UNSET
        else:
            for alerts_item_data in _alerts or []:
                _alerts_item = alerts_item_data
                alerts_item: Alert
                if isinstance(_alerts_item, Unset):
                    alerts_item = UNSET
                else:
                    alerts_item = Alert.from_dict(_alerts_item)

                alerts.append(alerts_item)

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

        sync_to_bz = d.pop("sync_to_bz", UNSET)

        tracker_post = cls(
            errata=errata,
            ps_update_stream=ps_update_stream,
            status=status,
            resolution=resolution,
            type=type,
            uuid=uuid,
            embargoed=embargoed,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            affects=affects,
            sync_to_bz=sync_to_bz,
        )

        tracker_post.additional_properties = d
        return tracker_post

    @staticmethod
    def get_fields():
        return {
            "errata": List[Erratum],
            "ps_update_stream": str,
            "status": str,
            "resolution": str,
            "type": TrackerType,
            "uuid": str,
            "embargoed": bool,
            "alerts": List[Alert],
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "affects": List[str],
            "sync_to_bz": bool,
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
