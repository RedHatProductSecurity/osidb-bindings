import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.not_affected_justification_enum import NotAffectedJustificationEnum
from ..models.special_handling_enum import SpecialHandlingEnum
from ..models.tracker_type import TrackerType
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert
    from ..models.erratum import Erratum


T = TypeVar("T", bound="OsidbApiV1TrackersCreateResponse201")


@_attrs_define
class OsidbApiV1TrackersCreateResponse201(OSIDBModel):
    """
    Attributes:
        errata (list['Erratum']):
        ps_update_stream (str):
        status (str):
        resolution (str):
        not_affected_justification (Union[BlankEnum, NotAffectedJustificationEnum]):
        type_ (TrackerType):
        uuid (UUID):
        special_handling (list[SpecialHandlingEnum]):
        resolved_dt (Union[None, datetime.datetime]):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        alerts (list['Alert']):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        affects (Union[Unset, list[UUID]]):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    errata: list["Erratum"]
    ps_update_stream: str
    status: str
    resolution: str
    not_affected_justification: Union[BlankEnum, NotAffectedJustificationEnum]
    type_: TrackerType
    uuid: UUID
    special_handling: list[SpecialHandlingEnum]
    resolved_dt: Union[None, datetime.datetime]
    embargoed: bool
    alerts: list["Alert"]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    affects: Union[Unset, list[UUID]] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
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

        ps_update_stream = self.ps_update_stream

        status = self.status

        resolution = self.resolution

        not_affected_justification: str
        if isinstance(self.not_affected_justification, NotAffectedJustificationEnum):
            not_affected_justification = UNSET
            if not isinstance(self.not_affected_justification, Unset):
                not_affected_justification = NotAffectedJustificationEnum(
                    self.not_affected_justification
                ).value

        else:
            not_affected_justification = UNSET
            if not isinstance(self.not_affected_justification, Unset):
                not_affected_justification = BlankEnum(
                    self.not_affected_justification
                ).value

        type_: str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = TrackerType(self.type_).value

        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        special_handling: list[str] = UNSET
        if not isinstance(self.special_handling, Unset):
            special_handling = []
            for special_handling_item_data in self.special_handling:
                special_handling_item: str = UNSET
                if not isinstance(special_handling_item_data, Unset):
                    special_handling_item = SpecialHandlingEnum(
                        special_handling_item_data
                    ).value

                special_handling.append(special_handling_item)

        resolved_dt: Union[None, str]
        if isinstance(self.resolved_dt, datetime.datetime):
            resolved_dt = UNSET
            if not isinstance(self.resolved_dt, Unset):
                resolved_dt = self.resolved_dt.isoformat()

        else:
            resolved_dt = self.resolved_dt

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

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(errata, Unset):
            field_dict["errata"] = errata
        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream
        if not isinstance(status, Unset):
            field_dict["status"] = status
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(not_affected_justification, Unset):
            field_dict["not_affected_justification"] = not_affected_justification
        if not isinstance(type_, Unset):
            field_dict["type"] = type_
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(special_handling, Unset):
            field_dict["special_handling"] = special_handling
        if not isinstance(resolved_dt, Unset):
            field_dict["resolved_dt"] = resolved_dt
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alert import Alert
        from ..models.erratum import Erratum

        d = src_dict.copy()
        errata = []
        _errata = d.pop("errata", UNSET)
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

        def _parse_not_affected_justification(
            data: object,
        ) -> Union[BlankEnum, NotAffectedJustificationEnum]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _not_affected_justification_type_0 = data
                not_affected_justification_type_0: NotAffectedJustificationEnum
                if isinstance(_not_affected_justification_type_0, Unset):
                    not_affected_justification_type_0 = UNSET
                else:
                    not_affected_justification_type_0 = NotAffectedJustificationEnum(
                        _not_affected_justification_type_0
                    )

                return not_affected_justification_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _not_affected_justification_type_1 = data
            not_affected_justification_type_1: BlankEnum
            if isinstance(_not_affected_justification_type_1, Unset):
                not_affected_justification_type_1 = UNSET
            else:
                not_affected_justification_type_1 = BlankEnum(
                    _not_affected_justification_type_1
                )

            return not_affected_justification_type_1

        not_affected_justification = _parse_not_affected_justification(
            d.pop("not_affected_justification", UNSET)
        )

        _type_ = d.pop("type", UNSET)
        type_: TrackerType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TrackerType(_type_)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        special_handling = []
        _special_handling = d.pop("special_handling", UNSET)
        for special_handling_item_data in _special_handling or []:
            _special_handling_item = special_handling_item_data
            special_handling_item: SpecialHandlingEnum
            if isinstance(_special_handling_item, Unset):
                special_handling_item = UNSET
            else:
                special_handling_item = SpecialHandlingEnum(_special_handling_item)

            special_handling.append(special_handling_item)

        def _parse_resolved_dt(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _resolved_dt_type_0 = data
                resolved_dt_type_0: datetime.datetime
                if isinstance(_resolved_dt_type_0, Unset):
                    resolved_dt_type_0 = UNSET
                else:
                    resolved_dt_type_0 = isoparse(_resolved_dt_type_0)

                return resolved_dt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        resolved_dt = _parse_resolved_dt(d.pop("resolved_dt", UNSET))

        embargoed = d.pop("embargoed", UNSET)

        alerts = []
        _alerts = d.pop("alerts", UNSET)
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

        affects = []
        _affects = d.pop("affects", UNSET)
        for affects_item_data in _affects or []:
            _affects_item = affects_item_data
            affects_item: UUID
            if isinstance(_affects_item, Unset):
                affects_item = UNSET
            else:
                affects_item = (
                    _affects_item
                    if isinstance(_affects_item, UUID)
                    else UUID(_affects_item)
                )

            affects.append(affects_item)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_trackers_create_response_201 = cls(
            errata=errata,
            ps_update_stream=ps_update_stream,
            status=status,
            resolution=resolution,
            not_affected_justification=not_affected_justification,
            type_=type_,
            uuid=uuid,
            special_handling=special_handling,
            resolved_dt=resolved_dt,
            embargoed=embargoed,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            affects=affects,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_trackers_create_response_201.additional_properties = d
        return osidb_api_v1_trackers_create_response_201

    @staticmethod
    def get_fields():
        return {
            "errata": list["Erratum"],
            "ps_update_stream": str,
            "status": str,
            "resolution": str,
            "not_affected_justification": Union[
                BlankEnum, NotAffectedJustificationEnum
            ],
            "type": TrackerType,
            "uuid": UUID,
            "special_handling": list[SpecialHandlingEnum],
            "resolved_dt": Union[None, datetime.datetime],
            "embargoed": bool,
            "alerts": list["Alert"],
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "affects": list[UUID],
            "dt": datetime.datetime,
            "env": str,
            "revision": str,
            "version": str,
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
