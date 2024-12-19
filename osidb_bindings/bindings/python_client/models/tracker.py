import datetime
import json
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tracker_type import TrackerType
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert
    from ..models.erratum import Erratum


T = TypeVar("T", bound="Tracker")


@_attrs_define
class Tracker(OSIDBModel):
    """Tracker serializer

    Attributes:
        errata (list['Erratum']):
        external_system_id (str):
        status (str):
        resolution (str):
        type_ (TrackerType):
        uuid (UUID):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        alerts (list['Alert']):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        affects (Union[Unset, list[UUID]]):
        ps_update_stream (Union[Unset, str]):
        sync_to_bz (Union[Unset, bool]): Setting sync_to_bz to false disables flaw sync with Bugzilla after this
            operation. Use only as part of bulk actions and trigger a flaw bugzilla sync afterwards. Does nothing if BZ is
            disabled.
    """

    errata: list["Erratum"]
    external_system_id: str
    status: str
    resolution: str
    type_: TrackerType
    uuid: UUID
    embargoed: bool
    alerts: list["Alert"]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    affects: Union[Unset, list[UUID]] = UNSET
    ps_update_stream: Union[Unset, str] = UNSET
    sync_to_bz: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errata: list[dict[str, Any]] = UNSET
        if not isinstance(self.errata, Unset):
            errata = []
            for errata_item_data in self.errata:
                errata_item: dict[str, Any] = UNSET
                if not isinstance(errata_item_data, Unset):
                    errata_item = errata_item_data.to_dict()

                errata.append(errata_item)

        external_system_id = self.external_system_id

        status = self.status

        resolution = self.resolution

        type_: str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = TrackerType(self.type_).value

        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        embargoed = self.embargoed

        alerts: list[dict[str, Any]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                alerts.append(alerts_item)

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        affects: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affects, Unset):
            affects = []
            for affects_item_data in self.affects:
                affects_item: str = UNSET
                if not isinstance(affects_item_data, Unset):
                    affects_item = str(affects_item_data)

                affects.append(affects_item)

        ps_update_stream = self.ps_update_stream

        sync_to_bz = self.sync_to_bz

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(errata, Unset):
            field_dict["errata"] = errata
        if not isinstance(external_system_id, Unset):
            field_dict["external_system_id"] = external_system_id
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(type_, Unset):
            field_dict["type"] = type_
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
        if not isinstance(sync_to_bz, Unset):
            field_dict["sync_to_bz"] = sync_to_bz

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        errata: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.errata, Unset):
            _temp_errata = []
            for errata_item_data in self.errata:
                errata_item: dict[str, Any] = UNSET
                if not isinstance(errata_item_data, Unset):
                    errata_item = errata_item_data.to_dict()

                _temp_errata.append(errata_item)
            errata = (None, json.dumps(_temp_errata).encode(), "application/json")

        external_system_id = (None, str(self.external_system_id).encode(), "text/plain")

        status = (None, str(self.status).encode(), "text/plain")

        resolution = (None, str(self.resolution).encode(), "text/plain")

        type_: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = (None, str(self.type_.value).encode(), "text/plain")
        # CHANGE END (3) #}

        uuid: bytes = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        embargoed = (None, str(self.embargoed).encode(), "text/plain")

        alerts: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.alerts, Unset):
            _temp_alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                _temp_alerts.append(alerts_item)
            alerts = (None, json.dumps(_temp_alerts).encode(), "application/json")

        created_dt: bytes = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat().encode()

        updated_dt: bytes = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat().encode()

        affects: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.affects, Unset):
            _temp_affects = []
            for affects_item_data in self.affects:
                affects_item: str = UNSET
                if not isinstance(affects_item_data, Unset):
                    affects_item = str(affects_item_data)

                _temp_affects.append(affects_item)
            affects = (None, json.dumps(_temp_affects).encode(), "application/json")

        ps_update_stream = (
            self.ps_update_stream
            if isinstance(self.ps_update_stream, Unset)
            else (None, str(self.ps_update_stream).encode(), "text/plain")
        )

        sync_to_bz = (
            self.sync_to_bz
            if isinstance(self.sync_to_bz, Unset)
            else (None, str(self.sync_to_bz).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(errata, Unset):
            field_dict["errata"] = errata
        if not isinstance(external_system_id, Unset):
            field_dict["external_system_id"] = external_system_id
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(type_, Unset):
            field_dict["type"] = type_
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
        if not isinstance(sync_to_bz, Unset):
            field_dict["sync_to_bz"] = sync_to_bz

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alert import Alert
        from ..models.erratum import Erratum

        d = src_dict.copy()
        errata = []
        _errata = d.pop("errata", UNSET)
        for errata_item_data in _errata or []:
            # }
            _errata_item = errata_item_data
            errata_item: Erratum
            if isinstance(_errata_item, Unset):
                errata_item = UNSET
            else:
                errata_item = Erratum.from_dict(_errata_item)

            errata.append(errata_item)

        external_system_id = d.pop("external_system_id", UNSET)

        status = d.pop("status", UNSET)

        resolution = d.pop("resolution", UNSET)

        # }
        _type_ = d.pop("type", UNSET)
        type_: TrackerType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TrackerType(_type_)

        # }
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        embargoed = d.pop("embargoed", UNSET)

        alerts = []
        _alerts = d.pop("alerts", UNSET)
        for alerts_item_data in _alerts or []:
            # }
            _alerts_item = alerts_item_data
            alerts_item: Alert
            if isinstance(_alerts_item, Unset):
                alerts_item = UNSET
            else:
                alerts_item = Alert.from_dict(_alerts_item)

            alerts.append(alerts_item)

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

        affects = []
        _affects = d.pop("affects", UNSET)
        for affects_item_data in _affects or []:
            # }
            _affects_item = affects_item_data
            affects_item: UUID
            if isinstance(_affects_item, Unset):
                affects_item = UNSET
            else:
                affects_item = UUID(_affects_item)

            affects.append(affects_item)

        ps_update_stream = d.pop("ps_update_stream", UNSET)

        sync_to_bz = d.pop("sync_to_bz", UNSET)

        tracker = cls(
            errata=errata,
            external_system_id=external_system_id,
            status=status,
            resolution=resolution,
            type_=type_,
            uuid=uuid,
            embargoed=embargoed,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            affects=affects,
            ps_update_stream=ps_update_stream,
            sync_to_bz=sync_to_bz,
        )

        tracker.additional_properties = d
        return tracker

    @staticmethod
    def get_fields():
        return {
            "errata": list["Erratum"],
            "external_system_id": str,
            "status": str,
            "resolution": str,
            "type": TrackerType,
            "uuid": UUID,
            "embargoed": bool,
            "alerts": list["Alert"],
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "affects": list[UUID],
            "ps_update_stream": str,
            "sync_to_bz": bool,
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
