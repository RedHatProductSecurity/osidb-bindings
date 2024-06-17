import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.alert import Alert
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="Comment")


@attr.s(auto_attribs=True)
class Comment(OSIDBModel):
    """FlawComment serializer for use by FlawSerializer"""

    uuid: str
    text: str
    alerts: List[Alert]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    external_system_id: Union[Unset, str] = UNSET
    order: Union[Unset, None, int] = UNSET
    creator: Union[Unset, str] = UNSET
    is_private: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        text = self.text
        alerts: List[Dict[str, Any]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: Dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                alerts.append(alerts_item)

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        external_system_id = self.external_system_id
        order = self.order
        creator = self.creator
        is_private = self.is_private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(text, Unset):
            field_dict["text"] = text
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(external_system_id, Unset):
            field_dict["external_system_id"] = external_system_id
        if not isinstance(order, Unset):
            field_dict["order"] = order
        if not isinstance(creator, Unset):
            field_dict["creator"] = creator
        if not isinstance(is_private, Unset):
            field_dict["is_private"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        text = d.pop("text", UNSET)

        alerts = []
        _alerts = d.pop("alerts", UNSET)
        if _alerts is UNSET:
            alerts = UNSET
        else:
            for alerts_item_data in _alerts or []:
                _alerts_item = alerts_item_data
                alerts_item: Alert
                if isinstance(_alerts_item, Unset):
                    alerts_item = UNSET
                else:
                    alerts_item = Alert.from_dict(_alerts_item)

                alerts.append(alerts_item)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        external_system_id = d.pop("external_system_id", UNSET)

        order = d.pop("order", UNSET)

        creator = d.pop("creator", UNSET)

        is_private = d.pop("is_private", UNSET)

        comment = cls(
            uuid=uuid,
            text=text,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            external_system_id=external_system_id,
            order=order,
            creator=creator,
            is_private=is_private,
        )

        comment.additional_properties = d
        return comment

    @staticmethod
    def get_fields():
        return {
            "uuid": str,
            "text": str,
            "alerts": List[Alert],
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "external_system_id": str,
            "order": int,
            "creator": str,
            "is_private": bool,
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
