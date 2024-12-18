import datetime
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.alert_type_enum import AlertTypeEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1AlertsRetrieveResponse200")


@_attrs_define
class OsidbApiV1AlertsRetrieveResponse200(OSIDBModel):
    """
    Attributes:
        uuid (UUID):
        name (str):
        description (str):
        parent_uuid (UUID):
        parent_model (str):
        alert_type (Union[Unset, AlertTypeEnum]):
        resolution_steps (Union[Unset, str]):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    uuid: UUID
    name: str
    description: str
    parent_uuid: UUID
    parent_model: str
    alert_type: Union[Unset, AlertTypeEnum] = UNSET
    resolution_steps: Union[Unset, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        description = self.description

        parent_uuid: str = UNSET
        if not isinstance(self.parent_uuid, Unset):
            parent_uuid = str(self.parent_uuid)

        parent_model = self.parent_model

        alert_type: Union[Unset, str] = UNSET
        if not isinstance(self.alert_type, Unset):
            alert_type = AlertTypeEnum(self.alert_type).value

        resolution_steps = self.resolution_steps

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(description, Unset):
            field_dict["description"] = description
        if not isinstance(parent_uuid, Unset):
            field_dict["parent_uuid"] = parent_uuid
        if not isinstance(parent_model, Unset):
            field_dict["parent_model"] = parent_model
        if not isinstance(alert_type, Unset):
            field_dict["alert_type"] = alert_type
        if not isinstance(resolution_steps, Unset):
            field_dict["resolution_steps"] = resolution_steps
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
        # }
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        # }
        _parent_uuid = d.pop("parent_uuid", UNSET)
        parent_uuid: UUID
        if isinstance(_parent_uuid, Unset):
            parent_uuid = UNSET
        else:
            parent_uuid = UUID(_parent_uuid)

        parent_model = d.pop("parent_model", UNSET)

        # }
        _alert_type = d.pop("alert_type", UNSET)
        alert_type: Union[Unset, AlertTypeEnum]
        if isinstance(_alert_type, Unset):
            alert_type = UNSET
        else:
            alert_type = AlertTypeEnum(_alert_type)

        resolution_steps = d.pop("resolution_steps", UNSET)

        # }
        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_alerts_retrieve_response_200 = cls(
            uuid=uuid,
            name=name,
            description=description,
            parent_uuid=parent_uuid,
            parent_model=parent_model,
            alert_type=alert_type,
            resolution_steps=resolution_steps,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_alerts_retrieve_response_200.additional_properties = d
        return osidb_api_v1_alerts_retrieve_response_200

    @staticmethod
    def get_fields():
        return {
            "uuid": UUID,
            "name": str,
            "description": str,
            "parent_uuid": UUID,
            "parent_model": str,
            "alert_type": AlertTypeEnum,
            "resolution_steps": str,
            "dt": datetime.datetime,
            "env": str,
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
