import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert


T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment(OSIDBModel):
    """FlawComment serializer for use by FlawSerializer

    Attributes:
        uuid (UUID):
        text (str):
        alerts (list['Alert']):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        external_system_id (Union[Unset, str]):
        order (Union[None, Unset, int]):
        creator (Union[Unset, str]):
        is_private (Union[Unset, bool]):
    """

    uuid: UUID
    text: str
    alerts: list["Alert"]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    external_system_id: Union[Unset, str] = UNSET
    order: Union[None, Unset, int] = UNSET
    creator: Union[Unset, str] = UNSET
    is_private: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        text = self.text

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

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        external_system_id = self.external_system_id

        order: Union[None, Unset, int]
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        creator = self.creator

        is_private = self.is_private

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alert import Alert

        d = src_dict.copy()
        # }
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        text = d.pop("text", UNSET)

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

        # }
        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        external_system_id = d.pop("external_system_id", UNSET)

        def _parse_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        order = _parse_order(d.pop("order", UNSET))

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
            "uuid": UUID,
            "text": str,
            "alerts": list["Alert"],
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "external_system_id": str,
            "order": Union[None, int],
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
