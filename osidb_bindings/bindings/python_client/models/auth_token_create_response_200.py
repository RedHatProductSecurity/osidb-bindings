import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="AuthTokenCreateResponse200")


@attr.s(auto_attribs=True)
class AuthTokenCreateResponse200(OSIDBModel):
    """ """

    username: str
    password: str
    access: str
    refresh: str
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        password = self.password
        access = self.access
        refresh = self.refresh
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if isinstance(username, Unset):
            field_dict["username"] = username
        if isinstance(password, Unset):
            field_dict["password"] = password
        if isinstance(access, Unset):
            field_dict["access"] = access
        if isinstance(refresh, Unset):
            field_dict["refresh"] = refresh
        if isinstance(dt, Unset):
            field_dict["dt"] = dt
        if isinstance(env, Unset):
            field_dict["env"] = env
        if isinstance(revision, Unset):
            field_dict["revision"] = revision
        if isinstance(version, Unset):
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        access = d.pop("access", UNSET)

        refresh = d.pop("refresh", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        auth_token_create_response_200 = cls(
            username=username,
            password=password,
            access=access,
            refresh=refresh,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        auth_token_create_response_200.additional_properties = d
        return auth_token_create_response_200

    @staticmethod
    def get_fields():
        return {
            "username": str,
            "password": str,
            "access": str,
            "refresh": str,
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
