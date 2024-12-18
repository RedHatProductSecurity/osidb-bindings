import datetime
import json
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.affectedness_enum import AffectednessEnum
from ..models.blank_enum import BlankEnum
from ..models.impact_enum import ImpactEnum
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
        flaw (Union[None, UUID]):
        ps_module (str):
        ps_product (str):
        trackers (list['Tracker']):
        delegated_resolution (str):
        cvss_scores (list['AffectCVSS']):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        alerts (list['Alert']):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        affectedness (Union[AffectednessEnum, BlankEnum, Unset]):
        resolution (Union[BlankEnum, ResolutionEnum, Unset]):
        ps_component (Union[None, Unset, str]):
        impact (Union[BlankEnum, ImpactEnum, Unset]):
        purl (Union[None, Unset, str]):
    """

    uuid: UUID
    flaw: Union[None, UUID]
    ps_module: str
    ps_product: str
    trackers: list["Tracker"]
    delegated_resolution: str
    cvss_scores: list["AffectCVSS"]
    embargoed: bool
    alerts: list["Alert"]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    affectedness: Union[AffectednessEnum, BlankEnum, Unset] = UNSET
    resolution: Union[BlankEnum, ResolutionEnum, Unset] = UNSET
    ps_component: Union[None, Unset, str] = UNSET
    impact: Union[BlankEnum, ImpactEnum, Unset] = UNSET
    purl: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        flaw: Union[None, str]
        if isinstance(self.flaw, UUID):
            flaw = UNSET
            if not isinstance(self.flaw, Unset):
                flaw = str(self.flaw)

        else:
            flaw = self.flaw

        ps_module = self.ps_module

        ps_product = self.ps_product

        trackers: list[dict[str, Any]] = UNSET
        if not isinstance(self.trackers, Unset):
            trackers = []
            for trackers_item_data in self.trackers:
                trackers_item: dict[str, Any] = UNSET
                if not isinstance(trackers_item_data, Unset):
                    trackers_item = trackers_item_data.to_dict()

                trackers.append(trackers_item)

        delegated_resolution = self.delegated_resolution

        cvss_scores: list[dict[str, Any]] = UNSET
        if not isinstance(self.cvss_scores, Unset):
            cvss_scores = []
            for cvss_scores_item_data in self.cvss_scores:
                cvss_scores_item: dict[str, Any] = UNSET
                if not isinstance(cvss_scores_item_data, Unset):
                    cvss_scores_item = cvss_scores_item_data.to_dict()

                cvss_scores.append(cvss_scores_item)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(ps_module, Unset):
            field_dict["ps_module"] = ps_module
        if not isinstance(ps_product, Unset):
            field_dict["ps_product"] = ps_product
        if not isinstance(trackers, Unset):
            field_dict["trackers"] = trackers
        if not isinstance(delegated_resolution, Unset):
            field_dict["delegated_resolution"] = delegated_resolution
        if not isinstance(cvss_scores, Unset):
            field_dict["cvss_scores"] = cvss_scores
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
        if not isinstance(ps_component, Unset):
            field_dict["ps_component"] = ps_component
        if not isinstance(impact, Unset):
            field_dict["impact"] = impact
        if not isinstance(purl, Unset):
            field_dict["purl"] = purl

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        uuid: bytes = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        flaw: tuple[None, bytes, str]

        if isinstance(self.flaw, UUID):
            flaw: bytes = UNSET
            if not isinstance(self.flaw, Unset):
                flaw = str(self.flaw)
        else:
            flaw = (None, str(self.flaw).encode(), "text/plain")

        ps_module = (None, str(self.ps_module).encode(), "text/plain")

        ps_product = (None, str(self.ps_product).encode(), "text/plain")

        trackers: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.trackers, Unset):
            _temp_trackers = []
            for trackers_item_data in self.trackers:
                trackers_item: dict[str, Any] = UNSET
                if not isinstance(trackers_item_data, Unset):
                    trackers_item = trackers_item_data.to_dict()

                _temp_trackers.append(trackers_item)
            trackers = (None, json.dumps(_temp_trackers).encode(), "application/json")

        delegated_resolution = (
            None,
            str(self.delegated_resolution).encode(),
            "text/plain",
        )

        cvss_scores: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.cvss_scores, Unset):
            _temp_cvss_scores = []
            for cvss_scores_item_data in self.cvss_scores:
                cvss_scores_item: dict[str, Any] = UNSET
                if not isinstance(cvss_scores_item_data, Unset):
                    cvss_scores_item = cvss_scores_item_data.to_dict()

                _temp_cvss_scores.append(cvss_scores_item)
            cvss_scores = (
                None,
                json.dumps(_temp_cvss_scores).encode(),
                "application/json",
            )

        embargoed = (None, str(self.embargoed).encode(), "text/plain")

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

        updated_dt: bytes = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat().encode()

        affectedness: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.affectedness, Unset):
            affectedness = UNSET
        elif isinstance(self.affectedness, AffectednessEnum):
            affectedness: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.affectedness, Unset):
                affectedness = (
                    None,
                    str(self.affectedness.value).encode(),
                    "text/plain",
                )
            # CHANGE END (3) #}
        else:
            affectedness: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.affectedness, Unset):
                affectedness = (
                    None,
                    str(self.affectedness.value).encode(),
                    "text/plain",
                )
            # CHANGE END (3) #}

        resolution: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.resolution, Unset):
            resolution = UNSET
        elif isinstance(self.resolution, ResolutionEnum):
            resolution: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.resolution, Unset):
                resolution = (None, str(self.resolution.value).encode(), "text/plain")
            # CHANGE END (3) #}
        else:
            resolution: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.resolution, Unset):
                resolution = (None, str(self.resolution.value).encode(), "text/plain")
            # CHANGE END (3) #}

        ps_component: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.ps_component, Unset):
            ps_component = UNSET
        elif isinstance(self.ps_component, str):
            ps_component = (None, str(self.ps_component).encode(), "text/plain")
        else:
            ps_component = (None, str(self.ps_component).encode(), "text/plain")

        impact: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.impact, Unset):
            impact = UNSET
        elif isinstance(self.impact, ImpactEnum):
            impact: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.impact, Unset):
                impact = (None, str(self.impact.value).encode(), "text/plain")
            # CHANGE END (3) #}
        else:
            impact: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.impact, Unset):
                impact = (None, str(self.impact.value).encode(), "text/plain")
            # CHANGE END (3) #}

        purl: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.purl, Unset):
            purl = UNSET
        elif isinstance(self.purl, str):
            purl = (None, str(self.purl).encode(), "text/plain")
        else:
            purl = (None, str(self.purl).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(ps_module, Unset):
            field_dict["ps_module"] = ps_module
        if not isinstance(ps_product, Unset):
            field_dict["ps_product"] = ps_product
        if not isinstance(trackers, Unset):
            field_dict["trackers"] = trackers
        if not isinstance(delegated_resolution, Unset):
            field_dict["delegated_resolution"] = delegated_resolution
        if not isinstance(cvss_scores, Unset):
            field_dict["cvss_scores"] = cvss_scores
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
        if not isinstance(ps_component, Unset):
            field_dict["ps_component"] = ps_component
        if not isinstance(impact, Unset):
            field_dict["impact"] = impact
        if not isinstance(purl, Unset):
            field_dict["purl"] = purl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.affect_cvss import AffectCVSS
        from ..models.alert import Alert
        from ..models.tracker import Tracker

        d = src_dict.copy()
        # }
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        def _parse_flaw(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
                _flaw_type_0 = data
                flaw_type_0: UUID
                if isinstance(_flaw_type_0, Unset):
                    flaw_type_0 = UNSET
                else:
                    flaw_type_0 = UUID(_flaw_type_0)

                return flaw_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        flaw = _parse_flaw(d.pop("flaw", UNSET))

        ps_module = d.pop("ps_module", UNSET)

        ps_product = d.pop("ps_product", UNSET)

        trackers = []
        _trackers = d.pop("trackers", UNSET)
        for trackers_item_data in _trackers or []:
            # }
            _trackers_item = trackers_item_data
            trackers_item: Tracker
            if isinstance(_trackers_item, Unset):
                trackers_item = UNSET
            else:
                trackers_item = Tracker.from_dict(_trackers_item)

            trackers.append(trackers_item)

        delegated_resolution = d.pop("delegated_resolution", UNSET)

        cvss_scores = []
        _cvss_scores = d.pop("cvss_scores", UNSET)
        for cvss_scores_item_data in _cvss_scores or []:
            # }
            _cvss_scores_item = cvss_scores_item_data
            cvss_scores_item: AffectCVSS
            if isinstance(_cvss_scores_item, Unset):
                cvss_scores_item = UNSET
            else:
                cvss_scores_item = AffectCVSS.from_dict(_cvss_scores_item)

            cvss_scores.append(cvss_scores_item)

        embargoed = d.pop("embargoed", UNSET)

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

        def _parse_affectedness(
            data: object,
        ) -> Union[AffectednessEnum, BlankEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
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
            # }
            _affectedness_type_1 = data
            affectedness_type_1: BlankEnum
            if isinstance(_affectedness_type_1, Unset):
                affectedness_type_1 = UNSET
            else:
                affectedness_type_1 = BlankEnum(_affectedness_type_1)

            return affectedness_type_1

        affectedness = _parse_affectedness(d.pop("affectedness", UNSET))

        def _parse_resolution(data: object) -> Union[BlankEnum, ResolutionEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
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
            # }
            _resolution_type_1 = data
            resolution_type_1: BlankEnum
            if isinstance(_resolution_type_1, Unset):
                resolution_type_1 = UNSET
            else:
                resolution_type_1 = BlankEnum(_resolution_type_1)

            return resolution_type_1

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_ps_component(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ps_component = _parse_ps_component(d.pop("ps_component", UNSET))

        def _parse_impact(data: object) -> Union[BlankEnum, ImpactEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
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
            # }
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

        affect = cls(
            uuid=uuid,
            flaw=flaw,
            ps_module=ps_module,
            ps_product=ps_product,
            trackers=trackers,
            delegated_resolution=delegated_resolution,
            cvss_scores=cvss_scores,
            embargoed=embargoed,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            affectedness=affectedness,
            resolution=resolution,
            ps_component=ps_component,
            impact=impact,
            purl=purl,
        )

        affect.additional_properties = d
        return affect

    @staticmethod
    def get_fields():
        return {
            "uuid": UUID,
            "flaw": Union[None, UUID],
            "ps_module": str,
            "ps_product": str,
            "trackers": list["Tracker"],
            "delegated_resolution": str,
            "cvss_scores": list["AffectCVSS"],
            "embargoed": bool,
            "alerts": list["Alert"],
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "affectedness": Union[AffectednessEnum, BlankEnum],
            "resolution": Union[BlankEnum, ResolutionEnum],
            "ps_component": Union[None, str],
            "impact": Union[BlankEnum, ImpactEnum],
            "purl": Union[None, str],
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
