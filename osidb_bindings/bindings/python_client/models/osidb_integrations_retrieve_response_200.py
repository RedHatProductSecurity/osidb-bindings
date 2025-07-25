import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbIntegrationsRetrieveResponse200")


@_attrs_define
class OsidbIntegrationsRetrieveResponse200(OSIDBModel):
    """
    Attributes:
        jira (Union[None, str]):
        bugzilla (Union[None, str]):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    jira: Union[None, str]
    bugzilla: Union[None, str]
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jira: Union[None, str]
        if isinstance(self.jira, Unset):
            jira = UNSET
        jira = self.jira

        bugzilla: Union[None, str]
        if isinstance(self.bugzilla, Unset):
            bugzilla = UNSET
        bugzilla = self.bugzilla

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(jira, Unset):
            field_dict["jira"] = jira
        if not isinstance(bugzilla, Unset):
            field_dict["bugzilla"] = bugzilla
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

        def _parse_jira(data: object) -> Union[None, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, str], data)

        jira = _parse_jira(d.pop("jira", UNSET))

        def _parse_bugzilla(data: object) -> Union[None, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, str], data)

        bugzilla = _parse_bugzilla(d.pop("bugzilla", UNSET))

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_integrations_retrieve_response_200 = cls(
            jira=jira,
            bugzilla=bugzilla,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_integrations_retrieve_response_200.additional_properties = d
        return osidb_integrations_retrieve_response_200

    @staticmethod
    def get_fields():
        return {
            "jira": Union[None, str],
            "bugzilla": Union[None, str],
            "dt": datetime.datetime,
            "env": str,
            "revision": str,
            "version": str,
        }

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
