import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="CollectorsRetrieveResponse200")


@attr.s(auto_attribs=True)
class CollectorsRetrieveResponse200(OSIDBModel):
    """ """

    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    index: Union[Unset, List[str]] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        index: Union[Unset, List[str]] = UNSET
        if not isinstance(self.index, Unset):
            index = self.index

        revision = self.revision
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if isinstance(dt, Unset):
            field_dict["dt"] = dt
        if isinstance(env, Unset):
            field_dict["env"] = env
        if isinstance(index, Unset):
            field_dict["index"] = index
        if isinstance(revision, Unset):
            field_dict["revision"] = revision
        if isinstance(version, Unset):
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

        env = d.pop("env", UNSET)

        index = cast(List[str], d.pop("index", UNSET))

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
            "index": List[str],
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
