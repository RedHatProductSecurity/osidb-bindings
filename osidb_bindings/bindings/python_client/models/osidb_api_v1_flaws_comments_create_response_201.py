import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert


T = TypeVar("T", bound="OsidbApiV1FlawsCommentsCreateResponse201")


@_attrs_define
class OsidbApiV1FlawsCommentsCreateResponse201(OSIDBModel):
    """
    Attributes:
        flaw (UUID):
        text (str):
        uuid (UUID):
        external_system_id (str):
        alerts (list['Alert']):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        order (Union[Unset, int]):
        creator (Union[Unset, str]):
        is_private (Union[Unset, bool]):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    flaw: UUID
    text: str
    uuid: UUID
    external_system_id: str
    alerts: list["Alert"]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    embargoed: bool
    order: Union[Unset, int] = UNSET
    creator: Union[Unset, str] = UNSET
    is_private: Union[Unset, bool] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flaw: str = UNSET
        if not isinstance(self.flaw, Unset):
            flaw = str(self.flaw)

        text = self.text

        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        external_system_id = self.external_system_id

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

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alert import Alert

        d = src_dict.copy()
        _flaw = d.pop("flaw", UNSET)
        flaw: UUID
        if isinstance(_flaw, Unset):
            flaw = UNSET
        else:
            flaw = _flaw if isinstance(_flaw, UUID) else UUID(_flaw)

        text = d.pop("text", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        external_system_id = d.pop("external_system_id", UNSET)

        alerts = []
        _alerts = d.pop("alerts", UNSET)
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

        osidb_api_v1_flaws_comments_create_response_201 = cls(
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

        osidb_api_v1_flaws_comments_create_response_201.additional_properties = d
        return osidb_api_v1_flaws_comments_create_response_201

    @staticmethod
    def get_fields():
        return {
            "flaw": UUID,
            "text": str,
            "uuid": UUID,
            "external_system_id": str,
            "alerts": list["Alert"],
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
