import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.alert import Alert
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1FlawsCommentsRetrieveResponse200")


@attr.s(auto_attribs=True)
class OsidbApiV1FlawsCommentsRetrieveResponse200(OSIDBModel):
    """ """

    flaw: str
    text: str
    uuid: str
    external_system_id: str
    alerts: List[Alert]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    embargoed: bool
    order: Union[Unset, None, int] = UNSET
    creator: Union[Unset, str] = UNSET
    is_private: Union[Unset, bool] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flaw = self.flaw
        text = self.text
        uuid = self.uuid
        external_system_id = self.external_system_id
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

        embargoed = self.embargoed
        order = self.order
        creator = self.creator
        is_private = self.is_private
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(text, Unset):
            field_dict["text"] = text
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(external_system_id, Unset):
            field_dict["external_system_id"] = external_system_id
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(order, Unset):
            field_dict["order"] = order
        if not isinstance(creator, Unset):
            field_dict["creator"] = creator
        if not isinstance(is_private, Unset):
            field_dict["is_private"] = is_private
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        flaw = d.pop("flaw", UNSET)

        text = d.pop("text", UNSET)

        uuid = d.pop("uuid", UNSET)

        external_system_id = d.pop("external_system_id", UNSET)

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

        embargoed = d.pop("embargoed", UNSET)

        order = d.pop("order", UNSET)

        creator = d.pop("creator", UNSET)

        is_private = d.pop("is_private", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_flaws_comments_retrieve_response_200 = cls(
            flaw=flaw,
            text=text,
            uuid=uuid,
            external_system_id=external_system_id,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            embargoed=embargoed,
            order=order,
            creator=creator,
            is_private=is_private,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_flaws_comments_retrieve_response_200.additional_properties = d
        return osidb_api_v1_flaws_comments_retrieve_response_200

    @staticmethod
    def get_fields():
        return {
            "flaw": str,
            "text": str,
            "uuid": str,
            "external_system_id": str,
            "alerts": List[Alert],
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "embargoed": bool,
            "order": int,
            "creator": str,
            "is_private": bool,
            "dt": datetime.datetime,
            "env": str,
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
