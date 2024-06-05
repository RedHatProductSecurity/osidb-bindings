import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.alert import Alert
from ..models.flaw_reference_type import FlawReferenceType
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawReferencePost")


@attr.s(auto_attribs=True)
class FlawReferencePost(OSIDBModel):
    """FlawReference serializer"""

    url: str
    uuid: str
    embargoed: bool
    alerts: List[Alert]
    created_dt: datetime.datetime
    description: Union[Unset, str] = UNSET
    type: Union[Unset, FlawReferenceType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        uuid = self.uuid
        embargoed = self.embargoed
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

        description = self.description
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):

            type = FlawReferenceType(self.type).value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(url, Unset):
            field_dict["url"] = url
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(description, Unset):
            field_dict["description"] = description
        if not isinstance(type, Unset):
            field_dict["type"] = type

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        url = self.url if self.url is UNSET else (None, str(self.url), "text/plain")
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        embargoed = (
            self.embargoed
            if self.embargoed is UNSET
            else (None, str(self.embargoed), "text/plain")
        )
        alerts: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.alerts, Unset):
            _temp_alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: Dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                _temp_alerts.append(alerts_item)
            alerts = (None, json.dumps(_temp_alerts), "application/json")

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        description = (
            self.description
            if self.description is UNSET
            else (None, str(self.description), "text/plain")
        )
        type: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.type, Unset):

            type = FlawReferenceType(self.type).value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        if not isinstance(url, Unset):
            field_dict["url"] = url
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(description, Unset):
            field_dict["description"] = description
        if not isinstance(type, Unset):
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        uuid = d.pop("uuid", UNSET)

        embargoed = d.pop("embargoed", UNSET)

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

        description = d.pop("description", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FlawReferenceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FlawReferenceType(_type)

        flaw_reference_post = cls(
            url=url,
            uuid=uuid,
            embargoed=embargoed,
            alerts=alerts,
            created_dt=created_dt,
            description=description,
            type=type,
        )

        flaw_reference_post.additional_properties = d
        return flaw_reference_post

    @staticmethod
    def get_fields():
        return {
            "url": str,
            "uuid": str,
            "embargoed": bool,
            "alerts": List[Alert],
            "created_dt": datetime.datetime,
            "description": str,
            "type": FlawReferenceType,
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
