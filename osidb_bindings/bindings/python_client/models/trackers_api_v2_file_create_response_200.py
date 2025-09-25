import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.affect import Affect
    from ..models.stream_component import StreamComponent


T = TypeVar("T", bound="TrackersApiV2FileCreateResponse200")


@_attrs_define
class TrackersApiV2FileCreateResponse200(OSIDBModel):
    """
    Attributes:
        streams_components (list['StreamComponent']):
        not_applicable (list['Affect']):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    streams_components: list["StreamComponent"]
    not_applicable: list["Affect"]
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        streams_components: list[dict[str, Any]] = UNSET
        if not isinstance(self.streams_components, Unset):
            streams_components = []
            for streams_components_item_data in self.streams_components:
                streams_components_item: dict[str, Any] = UNSET
                if not isinstance(streams_components_item_data, Unset):
                    streams_components_item = streams_components_item_data.to_dict()

                streams_components.append(streams_components_item)

        not_applicable: list[dict[str, Any]] = UNSET
        if not isinstance(self.not_applicable, Unset):
            not_applicable = []
            for not_applicable_item_data in self.not_applicable:
                not_applicable_item: dict[str, Any] = UNSET
                if not isinstance(not_applicable_item_data, Unset):
                    not_applicable_item = not_applicable_item_data.to_dict()

                not_applicable.append(not_applicable_item)

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(streams_components, Unset):
            field_dict["streams_components"] = streams_components
        if not isinstance(not_applicable, Unset):
            field_dict["not_applicable"] = not_applicable
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
        from ..models.affect import Affect
        from ..models.stream_component import StreamComponent

        d = src_dict.copy()
        streams_components = []
        _streams_components = d.pop("streams_components", UNSET)
        for streams_components_item_data in _streams_components or []:
            _streams_components_item = streams_components_item_data
            streams_components_item: StreamComponent
            if isinstance(_streams_components_item, Unset):
                streams_components_item = UNSET
            else:
                streams_components_item = StreamComponent.from_dict(
                    _streams_components_item
                )

            streams_components.append(streams_components_item)

        not_applicable = []
        _not_applicable = d.pop("not_applicable", UNSET)
        for not_applicable_item_data in _not_applicable or []:
            _not_applicable_item = not_applicable_item_data
            not_applicable_item: Affect
            if isinstance(_not_applicable_item, Unset):
                not_applicable_item = UNSET
            else:
                not_applicable_item = Affect.from_dict(_not_applicable_item)

            not_applicable.append(not_applicable_item)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        trackers_api_v2_file_create_response_200 = cls(
            streams_components=streams_components,
            not_applicable=not_applicable,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        trackers_api_v2_file_create_response_200.additional_properties = d
        return trackers_api_v2_file_create_response_200

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
