from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.profile import Profile


T = TypeVar("T", bound="User")


@_attrs_define
class User(OSIDBModel):
    """
    Attributes:
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        groups (list[str]):
        profile (Profile):
        email (Union[Unset, str]):
    """

    username: str
    groups: list[str]
    profile: "Profile"
    email: Union[Unset, str] = UNSET
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

        user = cls(
            username=username,
            groups=groups,
            profile=profile,
            email=email,
        )

        user.additional_properties = d
        return user

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
