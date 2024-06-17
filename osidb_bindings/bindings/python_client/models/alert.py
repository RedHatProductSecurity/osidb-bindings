from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.alert_type_enum import AlertTypeEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="Alert")


@attr.s(auto_attribs=True)
class Alert(OSIDBModel):
    """Alerts indicate some inconsistency in a linked flaw, affect, tracker or other models."""

    uuid: str
    name: str
    description: str
    parent_uuid: str
    parent_model: str
    alert_type: Union[Unset, AlertTypeEnum] = UNSET
    resolution_steps: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        name = self.name
        description = self.description
        parent_uuid = self.parent_uuid
        parent_model = self.parent_model
        alert_type: Union[Unset, str] = UNSET
        if not isinstance(self.alert_type, Unset):

            alert_type = AlertTypeEnum(self.alert_type).value

        resolution_steps = self.resolution_steps

        field_dict: Dict[str, Any] = {}
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        parent_uuid = d.pop("parent_uuid", UNSET)

        parent_model = d.pop("parent_model", UNSET)

        _alert_type = d.pop("alert_type", UNSET)
        alert_type: Union[Unset, AlertTypeEnum]
        if isinstance(_alert_type, Unset):
            alert_type = UNSET
        else:
            alert_type = AlertTypeEnum(_alert_type)

        resolution_steps = d.pop("resolution_steps", UNSET)

        alert = cls(
            uuid=uuid,
            name=name,
            description=description,
            parent_uuid=parent_uuid,
            parent_model=parent_model,
            alert_type=alert_type,
            resolution_steps=resolution_steps,
        )

        alert.additional_properties = d
        return alert

    @staticmethod
    def get_fields():
        return {
            "uuid": str,
            "name": str,
            "description": str,
            "parent_uuid": str,
            "parent_model": str,
            "alert_type": AlertTypeEnum,
            "resolution_steps": str,
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
