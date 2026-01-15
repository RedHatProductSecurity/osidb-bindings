import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..models.affectedness_enum import AffectednessEnum
from ..models.blank_enum import BlankEnum
from ..models.impact_enum import ImpactEnum
from ..models.resolution_enum import ResolutionEnum
from ..models.visibility_enum import VisibilityEnum
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert
    from ..models.tracker import Tracker


T = TypeVar("T", bound="AffectV1")


@_attrs_define
class AffectV1(OSIDBModel):
    """Read-only serializer for the AffectV1 database view.

    Attributes:
        uuid (UUID):
        affectedness (Union[AffectednessEnum, BlankEnum]):
        resolution (Union[BlankEnum, ResolutionEnum]):
        ps_module (str):
        cve_id (str):
        ps_product (str):
        ps_component (str):
        trackers (list['Tracker']):
        delegated_resolution (str):
        cvss_scores (str):
        purl (str):
        delegated_not_affected_justification (str):
        resolved_dt (Union[None, datetime.datetime]):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        visibility (VisibilityEnum):
        alerts (list['Alert']):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        flaw (Union[None, UUID, Unset]):
        impact (Union[BlankEnum, ImpactEnum, Unset]):
        not_affected_justification (Union[Unset, str]):
    """

    uuid: UUID
    affectedness: Union[AffectednessEnum, BlankEnum]
    resolution: Union[BlankEnum, ResolutionEnum]
    ps_module: str
    cve_id: str
    ps_product: str
    ps_component: str
    trackers: list["Tracker"]
    delegated_resolution: str
    cvss_scores: str
    purl: str
    delegated_not_affected_justification: str
    resolved_dt: Union[None, datetime.datetime]
    embargoed: bool
    visibility: VisibilityEnum
    alerts: list["Alert"]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    flaw: Union[None, UUID, Unset] = UNSET
    impact: Union[BlankEnum, ImpactEnum, Unset] = UNSET
    not_affected_justification: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        affectedness: str
        if isinstance(self.affectedness, Unset):
            affectedness = UNSET
        elif isinstance(self.affectedness, AffectednessEnum):
            affectedness = UNSET
            if not isinstance(self.affectedness, Unset):
                affectedness = AffectednessEnum(self.affectedness).value

        else:
            affectedness = UNSET
            if not isinstance(self.affectedness, Unset):
                affectedness = BlankEnum(self.affectedness).value

        resolution: str
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        elif isinstance(self.resolution, ResolutionEnum):
            resolution = UNSET
            if not isinstance(self.resolution, Unset):
                resolution = ResolutionEnum(self.resolution).value

        else:
            resolution = UNSET
            if not isinstance(self.resolution, Unset):
                resolution = BlankEnum(self.resolution).value

        ps_module = self.ps_module

        cve_id = self.cve_id

        ps_product = self.ps_product

        ps_component = self.ps_component

        trackers: list[dict[str, Any]] = UNSET
        if not isinstance(self.trackers, Unset):
            trackers = []
            for trackers_item_data in self.trackers:
                trackers_item: dict[str, Any] = UNSET
                if not isinstance(trackers_item_data, Unset):
                    trackers_item = trackers_item_data.to_dict()

                trackers.append(trackers_item)

        delegated_resolution = self.delegated_resolution

        cvss_scores = self.cvss_scores

        purl = self.purl

        delegated_not_affected_justification = self.delegated_not_affected_justification

        resolved_dt: Union[None, str]
        if isinstance(self.resolved_dt, Unset):
            resolved_dt = UNSET
        elif isinstance(self.resolved_dt, datetime.datetime):
            resolved_dt = UNSET
            if not isinstance(self.resolved_dt, Unset):
                resolved_dt = self.resolved_dt.isoformat()

        else:
            resolved_dt = self.resolved_dt

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

        flaw: Union[None, Unset, str]
        if isinstance(self.flaw, Unset):
            flaw = UNSET
        elif isinstance(self.flaw, UUID):
            flaw = UNSET
            if not isinstance(self.flaw, Unset):
                flaw = str(self.flaw)

        else:
            flaw = self.flaw

        impact: Union[Unset, str]
        if isinstance(self.impact, Unset):
            impact = UNSET
        elif isinstance(self.impact, ImpactEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):
                impact = ImpactEnum(self.impact).value

        else:
            impact = UNSET
            if not isinstance(self.impact, Unset):
                impact = BlankEnum(self.impact).value

        not_affected_justification = self.not_affected_justification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(affectedness, Unset):
            field_dict["affectedness"] = affectedness
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(ps_module, Unset):
            field_dict["ps_module"] = ps_module
        if not isinstance(cve_id, Unset):
            field_dict["cve_id"] = cve_id
        if not isinstance(ps_product, Unset):
            field_dict["ps_product"] = ps_product
        if not isinstance(ps_component, Unset):
            field_dict["ps_component"] = ps_component
        if not isinstance(trackers, Unset):
            field_dict["trackers"] = trackers
        if not isinstance(delegated_resolution, Unset):
            field_dict["delegated_resolution"] = delegated_resolution
        if not isinstance(cvss_scores, Unset):
            field_dict["cvss_scores"] = cvss_scores
        if not isinstance(purl, Unset):
            field_dict["purl"] = purl
        if not isinstance(delegated_not_affected_justification, Unset):
            field_dict["delegated_not_affected_justification"] = (
                delegated_not_affected_justification
            )
        if not isinstance(resolved_dt, Unset):
            field_dict["resolved_dt"] = resolved_dt
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
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(impact, Unset):
            field_dict["impact"] = impact
        if not isinstance(not_affected_justification, Unset):
            field_dict["not_affected_justification"] = not_affected_justification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alert import Alert
        from ..models.tracker import Tracker

        d = src_dict.copy()
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = _uuid if isinstance(_uuid, UUID) else UUID(_uuid)

        def _parse_affectedness(data: object) -> Union[AffectednessEnum, BlankEnum]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _affectedness_type_0 = data
                affectedness_type_0: AffectednessEnum
                if isinstance(_affectedness_type_0, Unset):
                    affectedness_type_0 = UNSET
                else:
                    affectedness_type_0 = AffectednessEnum(_affectedness_type_0)

                return affectedness_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _affectedness_type_1 = data
            affectedness_type_1: BlankEnum
            if isinstance(_affectedness_type_1, Unset):
                affectedness_type_1 = UNSET
            else:
                affectedness_type_1 = BlankEnum(_affectedness_type_1)

            return affectedness_type_1

        affectedness = _parse_affectedness(d.pop("affectedness", UNSET))

        def _parse_resolution(data: object) -> Union[BlankEnum, ResolutionEnum]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _resolution_type_0 = data
                resolution_type_0: ResolutionEnum
                if isinstance(_resolution_type_0, Unset):
                    resolution_type_0 = UNSET
                else:
                    resolution_type_0 = ResolutionEnum(_resolution_type_0)

                return resolution_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _resolution_type_1 = data
            resolution_type_1: BlankEnum
            if isinstance(_resolution_type_1, Unset):
                resolution_type_1 = UNSET
            else:
                resolution_type_1 = BlankEnum(_resolution_type_1)

            return resolution_type_1

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        ps_module = d.pop("ps_module", UNSET)

        cve_id = d.pop("cve_id", UNSET)

        ps_product = d.pop("ps_product", UNSET)

        ps_component = d.pop("ps_component", UNSET)

        trackers = []
        _trackers = d.pop("trackers", UNSET)
        for trackers_item_data in _trackers or []:
            _trackers_item = trackers_item_data
            trackers_item: Tracker
            if isinstance(_trackers_item, Unset):
                trackers_item = UNSET
            else:
                trackers_item = Tracker.from_dict(_trackers_item)

            trackers.append(trackers_item)

        delegated_resolution = d.pop("delegated_resolution", UNSET)

        cvss_scores = d.pop("cvss_scores", UNSET)

        purl = d.pop("purl", UNSET)

        delegated_not_affected_justification = d.pop(
            "delegated_not_affected_justification", UNSET
        )

        def _parse_resolved_dt(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _resolved_dt_type_0 = data
                resolved_dt_type_0: datetime.datetime
                if isinstance(_resolved_dt_type_0, Unset):
                    resolved_dt_type_0 = UNSET
                else:
                    resolved_dt_type_0 = isoparse(_resolved_dt_type_0)

                return resolved_dt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        resolved_dt = _parse_resolved_dt(d.pop("resolved_dt", UNSET))

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

        def _parse_flaw(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _flaw_type_0 = data
                flaw_type_0: UUID
                if isinstance(_flaw_type_0, Unset):
                    flaw_type_0 = UNSET
                else:
                    flaw_type_0 = (
                        _flaw_type_0
                        if isinstance(_flaw_type_0, UUID)
                        else UUID(_flaw_type_0)
                    )

                return flaw_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        flaw = _parse_flaw(d.pop("flaw", UNSET))

        def _parse_impact(data: object) -> Union[BlankEnum, ImpactEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _impact_type_0 = data
                impact_type_0: ImpactEnum
                if isinstance(_impact_type_0, Unset):
                    impact_type_0 = UNSET
                else:
                    impact_type_0 = ImpactEnum(_impact_type_0)

                return impact_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _impact_type_1 = data
            impact_type_1: BlankEnum
            if isinstance(_impact_type_1, Unset):
                impact_type_1 = UNSET
            else:
                impact_type_1 = BlankEnum(_impact_type_1)

            return impact_type_1

        impact = _parse_impact(d.pop("impact", UNSET))

        not_affected_justification = d.pop("not_affected_justification", UNSET)

        affect_v1 = cls(
            uuid=uuid,
            affectedness=affectedness,
            resolution=resolution,
            ps_module=ps_module,
            cve_id=cve_id,
            ps_product=ps_product,
            ps_component=ps_component,
            trackers=trackers,
            delegated_resolution=delegated_resolution,
            cvss_scores=cvss_scores,
            purl=purl,
            delegated_not_affected_justification=delegated_not_affected_justification,
            resolved_dt=resolved_dt,
            embargoed=embargoed,
            visibility=visibility,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            flaw=flaw,
            impact=impact,
            not_affected_justification=not_affected_justification,
        )

        affect_v1.additional_properties = d
        return affect_v1

    @classmethod
    def get_fields(cls):
        return {f.name: f.type for f in _attrs_fields(cls)}

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
