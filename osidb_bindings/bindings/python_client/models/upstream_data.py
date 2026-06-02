import datetime
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..models.upstream_data_source_enum import UpstreamDataSourceEnum
from ..models.visibility_enum import VisibilityEnum
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert


T = TypeVar("T", bound="UpstreamData")


@_attrs_define
class UpstreamData(OSIDBModel):
    """Serializer for OSV/collector upstream metadata attached to a flaw (read-only via API).

    Attributes:
        uuid (UUID):
        flaw (UUID):
        upstream_purls (Any):
        source (UpstreamDataSourceEnum):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        visibility (VisibilityEnum):
        alerts (list['Alert']):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
    """

    uuid: UUID
    flaw: UUID
    upstream_purls: Any
    source: UpstreamDataSourceEnum
    embargoed: bool
    visibility: VisibilityEnum
    alerts: list["Alert"]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        flaw: str = UNSET
        if not isinstance(self.flaw, Unset):
            flaw = str(self.flaw)

        upstream_purls = self.upstream_purls

        source: str = UNSET
        if not isinstance(self.source, Unset):
            source = UpstreamDataSourceEnum(self.source).value

        embargoed = self.embargoed

        visibility: str = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = VisibilityEnum(self.visibility).value

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(upstream_purls, Unset):
            field_dict["upstream_purls"] = upstream_purls
        if not isinstance(source, Unset):
            field_dict["source"] = source
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(visibility, Unset):
            field_dict["visibility"] = visibility
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alert import Alert

        d = src_dict.copy()
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        _flaw = d.pop("flaw", UNSET)
        flaw: UUID
        if isinstance(_flaw, Unset):
            flaw = UNSET
        else:
            flaw = _flaw if isinstance(_flaw, UUID) else UUID(_flaw)

        upstream_purls = d.pop("upstream_purls", UNSET)

        _source = d.pop("source", UNSET)
        source: UpstreamDataSourceEnum
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = UpstreamDataSourceEnum(_source)

        embargoed = d.pop("embargoed", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: VisibilityEnum
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = VisibilityEnum(_visibility)

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

        upstream_data = cls(
            uuid=uuid,
            flaw=flaw,
            upstream_purls=upstream_purls,
            source=source,
            embargoed=embargoed,
            visibility=visibility,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
        )

        upstream_data.additional_properties = d
        return upstream_data

    @classmethod
    def get_fields(cls):
        return {f.name: f.type for f in _attrs_fields(cls)}

    @classmethod
    def new(cls):
        return cls.from_dict({})

    @classmethod
    def from_model(cls: type[T], model: "OSIDBModel") -> T:
        return cls.from_dict(model.to_dict())

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
