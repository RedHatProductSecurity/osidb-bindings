import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.osidb_whoami_retrieve_response_200_profile import OsidbWhoamiRetrieveResponse200Profile
from ..types import UNSET, Unset

T = TypeVar("T", bound="OsidbWhoamiRetrieveResponse200")


@attr.s(auto_attribs=True)
class OsidbWhoamiRetrieveResponse200:
    """ """

    dt: Union[Unset, datetime.datetime] = UNSET
    email: Union[Unset, str] = UNSET
    env: Union[Unset, str] = UNSET
    groups: Union[Unset, List[str]] = UNSET
    profile: Union[Unset, OsidbWhoamiRetrieveResponse200Profile] = UNSET
    revision: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        email = self.email
        env = self.env
        groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        revision = self.revision
        username = self.username
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if dt is not UNSET:
            field_dict["dt"] = dt
        if email is not UNSET:
            field_dict["email"] = email
        if env is not UNSET:
            field_dict["env"] = env
        if groups is not UNSET:
            field_dict["groups"] = groups
        if profile is not UNSET:
            field_dict["profile"] = profile
        if revision is not UNSET:
            field_dict["revision"] = revision
        if username is not UNSET:
            field_dict["username"] = username
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        email = d.pop("email", UNSET)

        env = d.pop("env", UNSET)

        groups = cast(List[str], d.pop("groups", UNSET))

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, OsidbWhoamiRetrieveResponse200Profile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = OsidbWhoamiRetrieveResponse200Profile.from_dict(_profile)

        revision = d.pop("revision", UNSET)

        username = d.pop("username", UNSET)

        version = d.pop("version", UNSET)

        osidb_whoami_retrieve_response_200 = cls(
            dt=dt,
            email=email,
            env=env,
            groups=groups,
            profile=profile,
            revision=revision,
            username=username,
            version=version,
        )

        osidb_whoami_retrieve_response_200.additional_properties = d
        return osidb_whoami_retrieve_response_200

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
