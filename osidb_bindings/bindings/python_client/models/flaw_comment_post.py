import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.alert import Alert
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawCommentPost")


@attr.s(auto_attribs=True)
class FlawCommentPost(OSIDBModel):
    """FlawComment serializer for use by flaw_comments endpoint"""

    text: str
    uuid: str
    alerts: List[Alert]
    created_dt: datetime.datetime
    embargoed: bool
    creator: Union[Unset, str] = UNSET
    is_private: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        uuid = self.uuid
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

        embargoed = self.embargoed
        creator = self.creator
        is_private = self.is_private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(text, Unset):
            field_dict["text"] = text
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(creator, Unset):
            field_dict["creator"] = creator
        if not isinstance(is_private, Unset):
            field_dict["is_private"] = is_private

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        text = self.text if self.text is UNSET else (None, str(self.text), "text/plain")
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
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

        embargoed = (
            self.embargoed
            if self.embargoed is UNSET
            else (None, str(self.embargoed), "text/plain")
        )
        creator = (
            self.creator
            if self.creator is UNSET
            else (None, str(self.creator), "text/plain")
        )
        is_private = (
            self.is_private
            if self.is_private is UNSET
            else (None, str(self.is_private), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        if not isinstance(text, Unset):
            field_dict["text"] = text
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(creator, Unset):
            field_dict["creator"] = creator
        if not isinstance(is_private, Unset):
            field_dict["is_private"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        uuid = d.pop("uuid", UNSET)

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

        embargoed = d.pop("embargoed", UNSET)

        creator = d.pop("creator", UNSET)

        is_private = d.pop("is_private", UNSET)

        flaw_comment_post = cls(
            text=text,
            uuid=uuid,
            alerts=alerts,
            created_dt=created_dt,
            embargoed=embargoed,
            creator=creator,
            is_private=is_private,
        )

        flaw_comment_post.additional_properties = d
        return flaw_comment_post

    @staticmethod
    def get_fields():
        return {
            "text": str,
            "uuid": str,
            "alerts": List[Alert],
            "created_dt": datetime.datetime,
            "embargoed": bool,
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
