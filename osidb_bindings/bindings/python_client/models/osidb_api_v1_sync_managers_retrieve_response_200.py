import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1SyncManagersRetrieveResponse200")


@_attrs_define
class OsidbApiV1SyncManagersRetrieveResponse200(OSIDBModel):
    """
    Attributes:
        id (int):
        name (str):
        sync_id (str):
        last_scheduled_dt (Union[None, Unset, datetime.datetime]):
        last_started_dt (Union[None, Unset, datetime.datetime]):
        last_finished_dt (Union[None, Unset, datetime.datetime]):
        last_failed_dt (Union[None, Unset, datetime.datetime]):
        last_consecutive_failures (Union[Unset, int]):
        permanently_failed (Union[Unset, bool]):
        last_rescheduled_dt (Union[None, Unset, datetime.datetime]):
        last_consecutive_reschedules (Union[Unset, int]):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    id: int
    name: str
    sync_id: str
    last_scheduled_dt: Union[None, Unset, datetime.datetime] = UNSET
    last_started_dt: Union[None, Unset, datetime.datetime] = UNSET
    last_finished_dt: Union[None, Unset, datetime.datetime] = UNSET
    last_failed_dt: Union[None, Unset, datetime.datetime] = UNSET
    last_consecutive_failures: Union[Unset, int] = UNSET
    permanently_failed: Union[Unset, bool] = UNSET
    last_rescheduled_dt: Union[None, Unset, datetime.datetime] = UNSET
    last_consecutive_reschedules: Union[Unset, int] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sync_id = self.sync_id

        last_scheduled_dt: Union[None, Unset, str]
        if isinstance(self.last_scheduled_dt, Unset):
            last_scheduled_dt = UNSET
        elif isinstance(self.last_scheduled_dt, datetime.datetime):
            last_scheduled_dt = UNSET
            if not isinstance(self.last_scheduled_dt, Unset):
                last_scheduled_dt = self.last_scheduled_dt.isoformat()

        else:
            last_scheduled_dt = self.last_scheduled_dt

        last_started_dt: Union[None, Unset, str]
        if isinstance(self.last_started_dt, Unset):
            last_started_dt = UNSET
        elif isinstance(self.last_started_dt, datetime.datetime):
            last_started_dt = UNSET
            if not isinstance(self.last_started_dt, Unset):
                last_started_dt = self.last_started_dt.isoformat()

        else:
            last_started_dt = self.last_started_dt

        last_finished_dt: Union[None, Unset, str]
        if isinstance(self.last_finished_dt, Unset):
            last_finished_dt = UNSET
        elif isinstance(self.last_finished_dt, datetime.datetime):
            last_finished_dt = UNSET
            if not isinstance(self.last_finished_dt, Unset):
                last_finished_dt = self.last_finished_dt.isoformat()

        else:
            last_finished_dt = self.last_finished_dt

        last_failed_dt: Union[None, Unset, str]
        if isinstance(self.last_failed_dt, Unset):
            last_failed_dt = UNSET
        elif isinstance(self.last_failed_dt, datetime.datetime):
            last_failed_dt = UNSET
            if not isinstance(self.last_failed_dt, Unset):
                last_failed_dt = self.last_failed_dt.isoformat()

        else:
            last_failed_dt = self.last_failed_dt

        last_consecutive_failures = self.last_consecutive_failures

        permanently_failed = self.permanently_failed

        last_rescheduled_dt: Union[None, Unset, str]
        if isinstance(self.last_rescheduled_dt, Unset):
            last_rescheduled_dt = UNSET
        elif isinstance(self.last_rescheduled_dt, datetime.datetime):
            last_rescheduled_dt = UNSET
            if not isinstance(self.last_rescheduled_dt, Unset):
                last_rescheduled_dt = self.last_rescheduled_dt.isoformat()

        else:
            last_rescheduled_dt = self.last_rescheduled_dt

        last_consecutive_reschedules = self.last_consecutive_reschedules

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(id, Unset):
            field_dict["id"] = id
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(sync_id, Unset):
            field_dict["sync_id"] = sync_id
        if not isinstance(last_scheduled_dt, Unset):
            field_dict["last_scheduled_dt"] = last_scheduled_dt
        if not isinstance(last_started_dt, Unset):
            field_dict["last_started_dt"] = last_started_dt
        if not isinstance(last_finished_dt, Unset):
            field_dict["last_finished_dt"] = last_finished_dt
        if not isinstance(last_failed_dt, Unset):
            field_dict["last_failed_dt"] = last_failed_dt
        if not isinstance(last_consecutive_failures, Unset):
            field_dict["last_consecutive_failures"] = last_consecutive_failures
        if not isinstance(permanently_failed, Unset):
            field_dict["permanently_failed"] = permanently_failed
        if not isinstance(last_rescheduled_dt, Unset):
            field_dict["last_rescheduled_dt"] = last_rescheduled_dt
        if not isinstance(last_consecutive_reschedules, Unset):
            field_dict["last_consecutive_reschedules"] = last_consecutive_reschedules
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
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        sync_id = d.pop("sync_id", UNSET)

        def _parse_last_scheduled_dt(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _last_scheduled_dt_type_0 = data
                last_scheduled_dt_type_0: datetime.datetime
                if isinstance(_last_scheduled_dt_type_0, Unset):
                    last_scheduled_dt_type_0 = UNSET
                else:
                    last_scheduled_dt_type_0 = isoparse(_last_scheduled_dt_type_0)

                return last_scheduled_dt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_scheduled_dt = _parse_last_scheduled_dt(d.pop("last_scheduled_dt", UNSET))

        def _parse_last_started_dt(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _last_started_dt_type_0 = data
                last_started_dt_type_0: datetime.datetime
                if isinstance(_last_started_dt_type_0, Unset):
                    last_started_dt_type_0 = UNSET
                else:
                    last_started_dt_type_0 = isoparse(_last_started_dt_type_0)

                return last_started_dt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_started_dt = _parse_last_started_dt(d.pop("last_started_dt", UNSET))

        def _parse_last_finished_dt(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _last_finished_dt_type_0 = data
                last_finished_dt_type_0: datetime.datetime
                if isinstance(_last_finished_dt_type_0, Unset):
                    last_finished_dt_type_0 = UNSET
                else:
                    last_finished_dt_type_0 = isoparse(_last_finished_dt_type_0)

                return last_finished_dt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_finished_dt = _parse_last_finished_dt(d.pop("last_finished_dt", UNSET))

        def _parse_last_failed_dt(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _last_failed_dt_type_0 = data
                last_failed_dt_type_0: datetime.datetime
                if isinstance(_last_failed_dt_type_0, Unset):
                    last_failed_dt_type_0 = UNSET
                else:
                    last_failed_dt_type_0 = isoparse(_last_failed_dt_type_0)

                return last_failed_dt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_failed_dt = _parse_last_failed_dt(d.pop("last_failed_dt", UNSET))

        last_consecutive_failures = d.pop("last_consecutive_failures", UNSET)

        permanently_failed = d.pop("permanently_failed", UNSET)

        def _parse_last_rescheduled_dt(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _last_rescheduled_dt_type_0 = data
                last_rescheduled_dt_type_0: datetime.datetime
                if isinstance(_last_rescheduled_dt_type_0, Unset):
                    last_rescheduled_dt_type_0 = UNSET
                else:
                    last_rescheduled_dt_type_0 = isoparse(_last_rescheduled_dt_type_0)

                return last_rescheduled_dt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_rescheduled_dt = _parse_last_rescheduled_dt(
            d.pop("last_rescheduled_dt", UNSET)
        )

        last_consecutive_reschedules = d.pop("last_consecutive_reschedules", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_sync_managers_retrieve_response_200 = cls(
            id=id,
            name=name,
            sync_id=sync_id,
            last_scheduled_dt=last_scheduled_dt,
            last_started_dt=last_started_dt,
            last_finished_dt=last_finished_dt,
            last_failed_dt=last_failed_dt,
            last_consecutive_failures=last_consecutive_failures,
            permanently_failed=permanently_failed,
            last_rescheduled_dt=last_rescheduled_dt,
            last_consecutive_reschedules=last_consecutive_reschedules,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_sync_managers_retrieve_response_200.additional_properties = d
        return osidb_api_v1_sync_managers_retrieve_response_200

    @classmethod
    def get_fields(cls):
        return {f.name: f.type for f in _attrs_fields(cls)}

    @classmethod
    def new(cls):
        return cls.from_dict({})

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
