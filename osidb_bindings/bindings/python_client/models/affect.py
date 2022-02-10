from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.affect_meta_attr import AffectMetaAttr
from ..models.affect_type_enum import AffectTypeEnum
from ..models.affectedness_enum import AffectednessEnum
from ..models.blank_enum import BlankEnum
from ..models.impact_enum import ImpactEnum
from ..models.resolution_enum import ResolutionEnum
from ..models.tracker import Tracker
from ..types import UNSET, Unset

T = TypeVar("T", bound="Affect")


@attr.s(auto_attribs=True)
class Affect:
    """Affect serializer"""

    uuid: str
    trackers: List[Tracker]
    meta_attr: AffectMetaAttr
    delegated_resolution: str
    type: Union[AffectTypeEnum, None, Unset] = UNSET
    affectedness: Union[AffectednessEnum, None, Unset] = UNSET
    resolution: Union[None, ResolutionEnum, Unset] = UNSET
    ps_module: Union[Unset, None, str] = UNSET
    ps_component: Union[Unset, None, str] = UNSET
    statement: Union[Unset, None, str] = UNSET
    impact: Union[BlankEnum, ImpactEnum, None, Unset] = UNSET
    cvss2: Union[Unset, None, str] = UNSET
    cvss2_score: Union[Unset, None, float] = UNSET
    cvss3: Union[Unset, None, str] = UNSET
    cvss3_score: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        trackers: List[Dict[str, Any]] = UNSET
        if not isinstance(self.trackers, Unset):
            trackers = []
            for trackers_item_data in self.trackers:
                trackers_item: Dict[str, Any] = UNSET
                if not isinstance(trackers_item_data, Unset):
                    trackers_item = trackers_item_data.to_dict()

                trackers.append(trackers_item)

        meta_attr: Dict[str, Any] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        delegated_resolution = self.delegated_resolution
        type: Union[None, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        elif self.type is None:
            type = None
        elif isinstance(self.type, AffectTypeEnum):
            type = UNSET
            if not isinstance(self.type, Unset):

                type = AffectTypeEnum(self.type).value

        else:
            type = self.type

        affectedness: Union[None, Unset, str]
        if isinstance(self.affectedness, Unset):
            affectedness = UNSET
        elif self.affectedness is None:
            affectedness = None
        elif isinstance(self.affectedness, AffectednessEnum):
            affectedness = UNSET
            if not isinstance(self.affectedness, Unset):

                affectedness = AffectednessEnum(self.affectedness).value

        else:
            affectedness = self.affectedness

        resolution: Union[None, Unset, str]
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        elif self.resolution is None:
            resolution = None
        elif isinstance(self.resolution, ResolutionEnum):
            resolution = UNSET
            if not isinstance(self.resolution, Unset):

                resolution = ResolutionEnum(self.resolution).value

        else:
            resolution = self.resolution

        ps_module = self.ps_module
        ps_component = self.ps_component
        statement = self.statement
        impact: Union[None, Unset, str]
        if isinstance(self.impact, Unset):
            impact = UNSET
        elif self.impact is None:
            impact = None
        elif isinstance(self.impact, ImpactEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):

                impact = ImpactEnum(self.impact).value

        elif isinstance(self.impact, BlankEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):

                impact = BlankEnum(self.impact).value

        else:
            impact = self.impact

        cvss2 = self.cvss2
        cvss2_score = self.cvss2_score
        cvss3 = self.cvss3
        cvss3_score = self.cvss3_score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if trackers is not UNSET:
            field_dict["trackers"] = trackers
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr
        if delegated_resolution is not UNSET:
            field_dict["delegated_resolution"] = delegated_resolution
        if type is not UNSET:
            field_dict["type"] = type
        if affectedness is not UNSET:
            field_dict["affectedness"] = affectedness
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if ps_module is not UNSET:
            field_dict["ps_module"] = ps_module
        if ps_component is not UNSET:
            field_dict["ps_component"] = ps_component
        if statement is not UNSET:
            field_dict["statement"] = statement
        if impact is not UNSET:
            field_dict["impact"] = impact
        if cvss2 is not UNSET:
            field_dict["cvss2"] = cvss2
        if cvss2_score is not UNSET:
            field_dict["cvss2_score"] = cvss2_score
        if cvss3 is not UNSET:
            field_dict["cvss3"] = cvss3
        if cvss3_score is not UNSET:
            field_dict["cvss3_score"] = cvss3_score

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

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

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: AffectMetaAttr
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = AffectMetaAttr.from_dict(_meta_attr)

        delegated_resolution = d.pop("delegated_resolution", UNSET)

        def _parse_type(data: object) -> Union[AffectTypeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _type_type_0 = data
                type_type_0: Union[Unset, AffectTypeEnum]
                if isinstance(_type_type_0, Unset):
                    type_type_0 = UNSET
                else:
                    type_type_0 = AffectTypeEnum(_type_type_0)

                return type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[AffectTypeEnum, None, Unset], data)

        type = _parse_type(d.pop("type", UNSET))

        def _parse_affectedness(data: object) -> Union[AffectednessEnum, None, Unset]:
            if data is None:
                return data
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
            return cast(Union[AffectednessEnum, None, Unset], data)

        affectedness = _parse_affectedness(d.pop("affectedness", UNSET))

        def _parse_resolution(data: object) -> Union[None, ResolutionEnum, Unset]:
            if data is None:
                return data
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
            return cast(Union[None, ResolutionEnum, Unset], data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        ps_module = d.pop("ps_module", UNSET)

        ps_component = d.pop("ps_component", UNSET)

        statement = d.pop("statement", UNSET)

        def _parse_impact(data: object) -> Union[BlankEnum, ImpactEnum, None, Unset]:
            if data is None:
                return data
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
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _impact_type_1 = data
                impact_type_1: Union[Unset, BlankEnum]
                if isinstance(_impact_type_1, Unset):
                    impact_type_1 = UNSET
                else:
                    impact_type_1 = BlankEnum(_impact_type_1)

                return impact_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, ImpactEnum, None, Unset], data)

        impact = _parse_impact(d.pop("impact", UNSET))

        cvss2 = d.pop("cvss2", UNSET)

        cvss2_score = d.pop("cvss2_score", UNSET)

        cvss3 = d.pop("cvss3", UNSET)

        cvss3_score = d.pop("cvss3_score", UNSET)

        affect = cls(
            uuid=uuid,
            trackers=trackers,
            meta_attr=meta_attr,
            delegated_resolution=delegated_resolution,
            type=type,
            affectedness=affectedness,
            resolution=resolution,
            ps_module=ps_module,
            ps_component=ps_component,
            statement=statement,
            impact=impact,
            cvss2=cvss2,
            cvss2_score=cvss2_score,
            cvss3=cvss3,
            cvss3_score=cvss3_score,
        )

        affect.additional_properties = d
        return affect

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
