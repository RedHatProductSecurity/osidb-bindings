import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="CollectorsRetrieveResponse200")


@_attrs_define
class CollectorsRetrieveResponse200(OSIDBModel):
    """
    Attributes:
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        index (Union[Unset, list[str]]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    index: Union[Unset, list[str]] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        index: Union[Unset, list[str]] = UNSET
        if not isinstance(self.index, Unset):
            index = self.index

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(dt, Unset):
            field_dict["dt"] = dt
        if not isinstance(env, Unset):
            field_dict["env"] = env
        if not isinstance(index, Unset):
            field_dict["index"] = index
        if not isinstance(revision, Unset):
            field_dict["revision"] = revision
        if not isinstance(version, Unset):
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        # }
        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        index = cast(list[str], d.pop("index", UNSET))

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        collectors_retrieve_response_200 = cls(
            dt=dt,
            env=env,
            index=index,
            revision=revision,
            version=version,
        )

        collectors_retrieve_response_200.additional_properties = d
        return collectors_retrieve_response_200

    @staticmethod
    def get_fields():
        return {
            "dt": datetime.datetime,
            "env": str,
            "index": list[str],
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
