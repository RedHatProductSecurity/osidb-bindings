import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.stats_flaws_response_groups_item import StatsFlawsResponseGroupsItem
    from ..models.stats_meta import StatsMeta


T = TypeVar("T", bound="StatsApiV1BetaFlawsRetrieveResponse200")


@_attrs_define
class StatsApiV1BetaFlawsRetrieveResponse200(OSIDBModel):
    """
    Attributes:
        groups (list['StatsFlawsResponseGroupsItem']):
        meta (StatsMeta):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    groups: list["StatsFlawsResponseGroupsItem"]
    meta: "StatsMeta"
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups: list[dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item: dict[str, Any] = UNSET
                if not isinstance(groups_item_data, Unset):
                    groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        meta: dict[str, Any] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(groups, Unset):
            field_dict["groups"] = groups
        if not isinstance(meta, Unset):
            field_dict["meta"] = meta
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
        from ..models.stats_flaws_response_groups_item import (
            StatsFlawsResponseGroupsItem,
        )
        from ..models.stats_meta import StatsMeta

        d = src_dict.copy()
        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            _groups_item = groups_item_data
            groups_item: StatsFlawsResponseGroupsItem
            if isinstance(_groups_item, Unset):
                groups_item = UNSET
            else:
                groups_item = StatsFlawsResponseGroupsItem.from_dict(_groups_item)

            groups.append(groups_item)

        _meta = d.pop("meta", UNSET)
        meta: StatsMeta
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = StatsMeta.from_dict(_meta)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        stats_api_v1_beta_flaws_retrieve_response_200 = cls(
            groups=groups,
            meta=meta,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        stats_api_v1_beta_flaws_retrieve_response_200.additional_properties = d
        return stats_api_v1_beta_flaws_retrieve_response_200

    @classmethod
    def get_fields(cls):
        return {f.name: f.type for f in _attrs_fields(cls)}

    @classmethod
    def new(cls):
        return cls.from_dict({})

    @classmethod
    def from_model(cls: type[T], model: "OSIDBModel") -> T:
        return cls.from_dict(model.to_dict())

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
