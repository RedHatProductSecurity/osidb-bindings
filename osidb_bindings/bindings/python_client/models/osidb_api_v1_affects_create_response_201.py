import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.affect_cvss import AffectCVSS
from ..models.affectedness_enum import AffectednessEnum
from ..models.alert import Alert
from ..models.blank_enum import BlankEnum
from ..models.impact_enum import ImpactEnum
from ..models.resolution_enum import ResolutionEnum
from ..models.tracker import Tracker
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1AffectsCreateResponse201")


@attr.s(auto_attribs=True)
class OsidbApiV1AffectsCreateResponse201(OSIDBModel):
    """ """

    uuid: str
    ps_module: str
    ps_product: str
    ps_component: str
    trackers: List[Tracker]
    delegated_resolution: str
    cvss_scores: List[AffectCVSS]
    embargoed: bool
    alerts: List[Alert]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    flaw: Optional[str]
    affectedness: Union[AffectednessEnum, BlankEnum, Unset] = UNSET
    resolution: Union[BlankEnum, ResolutionEnum, Unset] = UNSET
    impact: Union[BlankEnum, ImpactEnum, Unset] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        ps_module = self.ps_module
        ps_product = self.ps_product
        ps_component = self.ps_component
        trackers: List[Dict[str, Any]] = UNSET
        if not isinstance(self.trackers, Unset):
            trackers = []
            for trackers_item_data in self.trackers:
                trackers_item: Dict[str, Any] = UNSET
                if not isinstance(trackers_item_data, Unset):
                    trackers_item = trackers_item_data.to_dict()

                trackers.append(trackers_item)

        delegated_resolution = self.delegated_resolution
        cvss_scores: List[Dict[str, Any]] = UNSET
        if not isinstance(self.cvss_scores, Unset):
            cvss_scores = []
            for cvss_scores_item_data in self.cvss_scores:
                cvss_scores_item: Dict[str, Any] = UNSET
                if not isinstance(cvss_scores_item_data, Unset):
                    cvss_scores_item = cvss_scores_item_data.to_dict()

                cvss_scores.append(cvss_scores_item)

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

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        flaw = self.flaw
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

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(ps_module, Unset):
            field_dict["ps_module"] = ps_module
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
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(affectedness, Unset):
            field_dict["affectedness"] = affectedness
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(impact, Unset):
            field_dict["impact"] = impact
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
        uuid = d.pop("uuid", UNSET)

        ps_module = d.pop("ps_module", UNSET)

        ps_product = d.pop("ps_product", UNSET)

        ps_component = d.pop("ps_component", UNSET)

        trackers = []
        _trackers = d.pop("trackers", UNSET)
        if _trackers is UNSET:
            trackers = UNSET
        else:
            for trackers_item_data in _trackers or []:
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
        if _cvss_scores is UNSET:
            cvss_scores = UNSET
        else:
            for cvss_scores_item_data in _cvss_scores or []:
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

        flaw = d.pop("flaw", UNSET)

        def _parse_affectedness(
            data: object,
        ) -> Union[AffectednessEnum, BlankEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _affectedness_type_0 = data
                affectedness_type_0: Union[Unset, AffectednessEnum]
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
            affectedness_type_1: Union[Unset, BlankEnum]
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
                _resolution_type_0 = data
                resolution_type_0: Union[Unset, ResolutionEnum]
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
            resolution_type_1: Union[Unset, BlankEnum]
            if isinstance(_resolution_type_1, Unset):
                resolution_type_1 = UNSET
            else:
                resolution_type_1 = BlankEnum(_resolution_type_1)

            return resolution_type_1

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_impact(data: object) -> Union[BlankEnum, ImpactEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _impact_type_0 = data
                impact_type_0: Union[Unset, ImpactEnum]
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
            impact_type_1: Union[Unset, BlankEnum]
            if isinstance(_impact_type_1, Unset):
                impact_type_1 = UNSET
            else:
                impact_type_1 = BlankEnum(_impact_type_1)

            return impact_type_1

        impact = _parse_impact(d.pop("impact", UNSET))

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_affects_create_response_201 = cls(
            uuid=uuid,
            ps_module=ps_module,
            ps_product=ps_product,
            ps_component=ps_component,
            trackers=trackers,
            delegated_resolution=delegated_resolution,
            cvss_scores=cvss_scores,
            embargoed=embargoed,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            flaw=flaw,
            affectedness=affectedness,
            resolution=resolution,
            impact=impact,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_affects_create_response_201.additional_properties = d
        return osidb_api_v1_affects_create_response_201

    @staticmethod
    def get_fields():
        return {
            "uuid": str,
            "ps_module": str,
            "ps_product": str,
            "ps_component": str,
            "trackers": List[Tracker],
            "delegated_resolution": str,
            "cvss_scores": List[AffectCVSS],
            "embargoed": bool,
            "alerts": List[Alert],
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "flaw": str,
            "affectedness": Union[AffectednessEnum, BlankEnum],
            "resolution": Union[BlankEnum, ResolutionEnum],
            "impact": Union[BlankEnum, ImpactEnum],
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
