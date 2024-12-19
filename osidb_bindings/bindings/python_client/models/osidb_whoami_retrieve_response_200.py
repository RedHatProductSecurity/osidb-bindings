import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.osidb_whoami_retrieve_response_200_profile import (
        OsidbWhoamiRetrieveResponse200Profile,
    )


T = TypeVar("T", bound="OsidbWhoamiRetrieveResponse200")


@_attrs_define
class OsidbWhoamiRetrieveResponse200(OSIDBModel):
    """
    Attributes:
        dt (Union[Unset, datetime.datetime]):
        email (Union[Unset, str]):
        env (Union[Unset, str]):
        groups (Union[Unset, list[str]]):
        profile (Union[Unset, OsidbWhoamiRetrieveResponse200Profile]):
        revision (Union[Unset, str]):
        username (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    dt: Union[Unset, datetime.datetime] = UNSET
    email: Union[Unset, str] = UNSET
    env: Union[Unset, str] = UNSET
    groups: Union[Unset, list[str]] = UNSET
    profile: Union[Unset, "OsidbWhoamiRetrieveResponse200Profile"] = UNSET
    revision: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        email = self.email

        env = self.env

        groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        revision = self.revision

        username = self.username

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(dt, Unset):
            field_dict["dt"] = dt
        if not isinstance(email, Unset):
            field_dict["email"] = email
        if not isinstance(env, Unset):
            field_dict["env"] = env
        if not isinstance(groups, Unset):
            field_dict["groups"] = groups
        if not isinstance(profile, Unset):
            field_dict["profile"] = profile
        if not isinstance(revision, Unset):
            field_dict["revision"] = revision
        if not isinstance(username, Unset):
            field_dict["username"] = username
        if not isinstance(version, Unset):
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.osidb_whoami_retrieve_response_200_profile import (
            OsidbWhoamiRetrieveResponse200Profile,
        )

        d = src_dict.copy()
        # }
        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        email = d.pop("email", UNSET)

        env = d.pop("env", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))

        # }
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

    @staticmethod
    def get_fields():
        return {
            "dt": datetime.datetime,
            "email": str,
            "env": str,
            "groups": list[str],
            "profile": OsidbWhoamiRetrieveResponse200Profile,
            "revision": str,
            "username": str,
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
