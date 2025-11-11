import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields
from dateutil.parser import isoparse

from ..models.affectedness_enum import AffectednessEnum
from ..models.blank_enum import BlankEnum
from ..models.delegated_not_affected_justification_enum import (
    DelegatedNotAffectedJustificationEnum,
)
from ..models.impact_enum import ImpactEnum
from ..models.not_affected_justification_enum import NotAffectedJustificationEnum
from ..models.resolution_enum import ResolutionEnum
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.affect_cvss import AffectCVSS
    from ..models.alert import Alert
    from ..models.tracker import Tracker


T = TypeVar("T", bound="Affect")


@_attrs_define
class Affect(OSIDBModel):
    """Affect serializer

    Attributes:
        uuid (UUID):
        flaw (UUID):
        ps_update_stream (str):
        cve_id (str):
        ps_product (str):
        tracker (Union['Tracker', None]):
        delegated_resolution (str):
        cvss_scores (list['AffectCVSS']):
        delegated_not_affected_justification (Union[BlankEnum, DelegatedNotAffectedJustificationEnum]):
        resolved_dt (Union[None, datetime.datetime]):
        labels (list[str]):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        alerts (list['Alert']):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        affectedness (Union[AffectednessEnum, BlankEnum, Unset]):
        resolution (Union[BlankEnum, ResolutionEnum, Unset]):
        ps_module (Union[Unset, str]):
        ps_component (Union[None, Unset, str]):
        impact (Union[BlankEnum, ImpactEnum, Unset]):
        purl (Union[None, Unset, str]):
        not_affected_justification (Union[BlankEnum, NotAffectedJustificationEnum, Unset]):
    """

    uuid: UUID
    flaw: UUID
    ps_update_stream: str
    cve_id: str
    ps_product: str
    tracker: Union["Tracker", None]
    delegated_resolution: str
    cvss_scores: list["AffectCVSS"]
    delegated_not_affected_justification: Union[
        BlankEnum, DelegatedNotAffectedJustificationEnum
    ]
    resolved_dt: Union[None, datetime.datetime]
    labels: list[str]
    embargoed: bool
    alerts: list["Alert"]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    affectedness: Union[AffectednessEnum, BlankEnum, Unset] = UNSET
    resolution: Union[BlankEnum, ResolutionEnum, Unset] = UNSET
    ps_module: Union[Unset, str] = UNSET
    ps_component: Union[None, Unset, str] = UNSET
    impact: Union[BlankEnum, ImpactEnum, Unset] = UNSET
    purl: Union[None, Unset, str] = UNSET
    not_affected_justification: Union[
        BlankEnum, NotAffectedJustificationEnum, Unset
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tracker import Tracker

        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        flaw: str = UNSET
        if not isinstance(self.flaw, Unset):
            flaw = str(self.flaw)

        ps_update_stream = self.ps_update_stream

        cve_id = self.cve_id

        ps_product = self.ps_product

        tracker: Union[None, dict[str, Any]]
        if isinstance(self.tracker, Unset):
            tracker = UNSET
        elif isinstance(self.tracker, Tracker):
            tracker = UNSET
            if not isinstance(self.tracker, Unset):
                tracker = self.tracker.to_dict()

        else:
            tracker = self.tracker

        delegated_resolution = self.delegated_resolution

        cvss_scores: list[dict[str, Any]] = UNSET
        if not isinstance(self.cvss_scores, Unset):
            cvss_scores = []
            for cvss_scores_item_data in self.cvss_scores:
                cvss_scores_item: dict[str, Any] = UNSET
                if not isinstance(cvss_scores_item_data, Unset):
                    cvss_scores_item = cvss_scores_item_data.to_dict()

                cvss_scores.append(cvss_scores_item)

        delegated_not_affected_justification: str
        if isinstance(self.delegated_not_affected_justification, Unset):
            delegated_not_affected_justification = UNSET
        elif isinstance(
            self.delegated_not_affected_justification,
            DelegatedNotAffectedJustificationEnum,
        ):
            delegated_not_affected_justification = UNSET
            if not isinstance(self.delegated_not_affected_justification, Unset):
                delegated_not_affected_justification = (
                    DelegatedNotAffectedJustificationEnum(
                        self.delegated_not_affected_justification
                    ).value
                )

        else:
            delegated_not_affected_justification = UNSET
            if not isinstance(self.delegated_not_affected_justification, Unset):
                delegated_not_affected_justification = BlankEnum(
                    self.delegated_not_affected_justification
                ).value

        resolved_dt: Union[None, str]
        if isinstance(self.resolved_dt, Unset):
            resolved_dt = UNSET
        elif isinstance(self.resolved_dt, datetime.datetime):
            resolved_dt = UNSET
            if not isinstance(self.resolved_dt, Unset):
                resolved_dt = self.resolved_dt.isoformat()

        else:
            resolved_dt = self.resolved_dt

        labels: list[str] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        embargoed = self.embargoed

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

        affectedness: Union[Unset, str]
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

        resolution: Union[Unset, str]
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

        ps_component: Union[None, Unset, str]
        if isinstance(self.ps_component, Unset):
            ps_component = UNSET
        else:
            ps_component = self.ps_component

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

        purl: Union[None, Unset, str]
        if isinstance(self.purl, Unset):
            purl = UNSET
        else:
            purl = self.purl

        not_affected_justification: Union[Unset, str]
        if isinstance(self.not_affected_justification, Unset):
            not_affected_justification = UNSET
        elif isinstance(self.not_affected_justification, NotAffectedJustificationEnum):
            not_affected_justification = UNSET
            if not isinstance(self.not_affected_justification, Unset):
                not_affected_justification = NotAffectedJustificationEnum(
                    self.not_affected_justification
                ).value

        else:
            not_affected_justification = UNSET
            if not isinstance(self.not_affected_justification, Unset):
                not_affected_justification = BlankEnum(
                    self.not_affected_justification
                ).value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream
        if not isinstance(cve_id, Unset):
            field_dict["cve_id"] = cve_id
        if not isinstance(ps_product, Unset):
            field_dict["ps_product"] = ps_product
        if not isinstance(tracker, Unset):
            field_dict["tracker"] = tracker
        if not isinstance(delegated_resolution, Unset):
            field_dict["delegated_resolution"] = delegated_resolution
        if not isinstance(cvss_scores, Unset):
            field_dict["cvss_scores"] = cvss_scores
        if not isinstance(delegated_not_affected_justification, Unset):
            field_dict["delegated_not_affected_justification"] = (
                delegated_not_affected_justification
            )
        if not isinstance(resolved_dt, Unset):
            field_dict["resolved_dt"] = resolved_dt
        if not isinstance(labels, Unset):
            field_dict["labels"] = labels
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(affectedness, Unset):
            field_dict["affectedness"] = affectedness
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(ps_module, Unset):
            field_dict["ps_module"] = ps_module
        if not isinstance(ps_component, Unset):
            field_dict["ps_component"] = ps_component
        if not isinstance(impact, Unset):
            field_dict["impact"] = impact
        if not isinstance(purl, Unset):
            field_dict["purl"] = purl
        if not isinstance(not_affected_justification, Unset):
            field_dict["not_affected_justification"] = not_affected_justification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.affect_cvss import AffectCVSS
        from ..models.alert import Alert
        from ..models.tracker import Tracker

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

        ps_update_stream = d.pop("ps_update_stream", UNSET)

        cve_id = d.pop("cve_id", UNSET)

        ps_product = d.pop("ps_product", UNSET)

        def _parse_tracker(data: object) -> Union["Tracker", None]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _tracker_type_1 = data
                tracker_type_1: Tracker
                if isinstance(_tracker_type_1, Unset):
                    tracker_type_1 = UNSET
                else:
                    tracker_type_1 = Tracker.from_dict(_tracker_type_1)

                return tracker_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Tracker", None], data)

        tracker = _parse_tracker(d.pop("tracker", UNSET))

        delegated_resolution = d.pop("delegated_resolution", UNSET)

        cvss_scores = []
        _cvss_scores = d.pop("cvss_scores", UNSET)
        for cvss_scores_item_data in _cvss_scores or []:
            _cvss_scores_item = cvss_scores_item_data
            cvss_scores_item: AffectCVSS
            if isinstance(_cvss_scores_item, Unset):
                cvss_scores_item = UNSET
            else:
                cvss_scores_item = AffectCVSS.from_dict(_cvss_scores_item)

            cvss_scores.append(cvss_scores_item)

        def _parse_delegated_not_affected_justification(
            data: object,
        ) -> Union[BlankEnum, DelegatedNotAffectedJustificationEnum]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _delegated_not_affected_justification_type_0 = data
                delegated_not_affected_justification_type_0: (
                    DelegatedNotAffectedJustificationEnum
                )
                if isinstance(_delegated_not_affected_justification_type_0, Unset):
                    delegated_not_affected_justification_type_0 = UNSET
                else:
                    delegated_not_affected_justification_type_0 = (
                        DelegatedNotAffectedJustificationEnum(
                            _delegated_not_affected_justification_type_0
                        )
                    )

                return delegated_not_affected_justification_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _delegated_not_affected_justification_type_1 = data
            delegated_not_affected_justification_type_1: BlankEnum
            if isinstance(_delegated_not_affected_justification_type_1, Unset):
                delegated_not_affected_justification_type_1 = UNSET
            else:
                delegated_not_affected_justification_type_1 = BlankEnum(
                    _delegated_not_affected_justification_type_1
                )

            return delegated_not_affected_justification_type_1

        delegated_not_affected_justification = (
            _parse_delegated_not_affected_justification(
                d.pop("delegated_not_affected_justification", UNSET)
            )
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

        labels = cast(list[str], d.pop("labels", UNSET))

        embargoed = d.pop("embargoed", UNSET)

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

        def _parse_affectedness(
            data: object,
        ) -> Union[AffectednessEnum, BlankEnum, Unset]:
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

        def _parse_resolution(data: object) -> Union[BlankEnum, ResolutionEnum, Unset]:
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

        def _parse_ps_component(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ps_component = _parse_ps_component(d.pop("ps_component", UNSET))

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

        def _parse_purl(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        purl = _parse_purl(d.pop("purl", UNSET))

        def _parse_not_affected_justification(
            data: object,
        ) -> Union[BlankEnum, NotAffectedJustificationEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _not_affected_justification_type_0 = data
                not_affected_justification_type_0: NotAffectedJustificationEnum
                if isinstance(_not_affected_justification_type_0, Unset):
                    not_affected_justification_type_0 = UNSET
                else:
                    not_affected_justification_type_0 = NotAffectedJustificationEnum(
                        _not_affected_justification_type_0
                    )

                return not_affected_justification_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _not_affected_justification_type_1 = data
            not_affected_justification_type_1: BlankEnum
            if isinstance(_not_affected_justification_type_1, Unset):
                not_affected_justification_type_1 = UNSET
            else:
                not_affected_justification_type_1 = BlankEnum(
                    _not_affected_justification_type_1
                )

            return not_affected_justification_type_1

        not_affected_justification = _parse_not_affected_justification(
            d.pop("not_affected_justification", UNSET)
        )

        affect = cls(
            uuid=uuid,
            flaw=flaw,
            ps_update_stream=ps_update_stream,
            cve_id=cve_id,
            ps_product=ps_product,
            tracker=tracker,
            delegated_resolution=delegated_resolution,
            cvss_scores=cvss_scores,
            delegated_not_affected_justification=delegated_not_affected_justification,
            resolved_dt=resolved_dt,
            labels=labels,
            embargoed=embargoed,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            affectedness=affectedness,
            resolution=resolution,
            ps_module=ps_module,
            ps_component=ps_component,
            impact=impact,
            purl=purl,
            not_affected_justification=not_affected_justification,
        )

        affect.additional_properties = d
        return affect

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
