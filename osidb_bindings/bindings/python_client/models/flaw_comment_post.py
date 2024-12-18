import datetime
import json
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert


T = TypeVar("T", bound="FlawCommentPost")


@_attrs_define
class FlawCommentPost(OSIDBModel):
    """FlawComment serializer for use by flaw_comments endpoint

    Attributes:
        text (str):
        uuid (UUID):
        alerts (list['Alert']):
        created_dt (datetime.datetime):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        creator (Union[Unset, str]):
        is_private (Union[Unset, bool]):
    """

    text: str
    uuid: UUID
    alerts: list["Alert"]
    created_dt: datetime.datetime
    embargoed: bool
    creator: Union[Unset, str] = UNSET
    is_private: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        alerts: list[dict[str, Any]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                alerts.append(alerts_item)

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        embargoed = self.embargoed

        creator = self.creator

        is_private = self.is_private

        field_dict: dict[str, Any] = {}
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

    def to_multipart(self) -> dict[str, Any]:
        text = (None, str(self.text).encode(), "text/plain")

        uuid: bytes = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        alerts: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.alerts, Unset):
            _temp_alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                _temp_alerts.append(alerts_item)
            alerts = (None, json.dumps(_temp_alerts).encode(), "application/json")

        created_dt: bytes = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat().encode()

        embargoed = (None, str(self.embargoed).encode(), "text/plain")

        creator = (
            self.creator
            if isinstance(self.creator, Unset)
            else (None, str(self.creator).encode(), "text/plain")
        )

        is_private = (
            self.is_private
            if isinstance(self.is_private, Unset)
            else (None, str(self.is_private).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alert import Alert

        d = src_dict.copy()
        text = d.pop("text", UNSET)

        # }
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        alerts = []
        _alerts = d.pop("alerts", UNSET)
        for alerts_item_data in _alerts or []:
            # }
            _alerts_item = alerts_item_data
            alerts_item: Alert
            if isinstance(_alerts_item, Unset):
                alerts_item = UNSET
            else:
                alerts_item = Alert.from_dict(_alerts_item)

            alerts.append(alerts_item)

        # }
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
            "uuid": UUID,
            "alerts": list["Alert"],
            "created_dt": datetime.datetime,
            "embargoed": bool,
            "creator": str,
            "is_private": bool,
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
