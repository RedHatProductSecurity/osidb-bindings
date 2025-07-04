import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.profile import Profile


T = TypeVar("T", bound="OsidbWhoamiRetrieveResponse200")


@_attrs_define
class OsidbWhoamiRetrieveResponse200(OSIDBModel):
    """
    Attributes:
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        groups (list[str]):
        profile (Profile):
        email (Union[Unset, str]):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    username: str
    groups: list[str]
    profile: "Profile"
    email: Union[Unset, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        groups: list[str] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        profile: dict[str, Any] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        email = self.email

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(username, Unset):
            field_dict["username"] = username
        if not isinstance(groups, Unset):
            field_dict["groups"] = groups
        if not isinstance(profile, Unset):
            field_dict["profile"] = profile
        if not isinstance(email, Unset):
            field_dict["email"] = email
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
        from ..models.profile import Profile

        d = src_dict.copy()
        username = d.pop("username", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))

        _profile = d.pop("profile", UNSET)
        profile: Profile
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = Profile.from_dict(_profile)

        email = d.pop("email", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_whoami_retrieve_response_200 = cls(
            username=username,
            groups=groups,
            profile=profile,
            email=email,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_whoami_retrieve_response_200.additional_properties = d
        return osidb_whoami_retrieve_response_200

    @staticmethod
    def get_fields():
        return {
            "username": str,
            "groups": list[str],
            "profile": Profile,
            "email": str,
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
