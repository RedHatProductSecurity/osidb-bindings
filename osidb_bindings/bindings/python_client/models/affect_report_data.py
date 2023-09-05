from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.affectedness_enum import AffectednessEnum
from ..models.blank_enum import BlankEnum
from ..models.resolution_enum import ResolutionEnum
from ..models.tracker_report_data import TrackerReportData
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="AffectReportData")


@attr.s(auto_attribs=True)
class AffectReportData(OSIDBModel):
    """ """

    ps_module: str
    ps_component: str
    affectedness: Union[AffectednessEnum, BlankEnum, Unset] = UNSET
    resolution: Union[BlankEnum, ResolutionEnum, Unset] = UNSET
    trackers: Union[Unset, List[TrackerReportData]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ps_module = self.ps_module
        ps_component = self.ps_component
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

        trackers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.trackers, Unset):
            trackers = []
            for trackers_item_data in self.trackers:
                trackers_item: Dict[str, Any] = UNSET
                if not isinstance(trackers_item_data, Unset):
                    trackers_item = trackers_item_data.to_dict()

                trackers.append(trackers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(ps_module, Unset):
            field_dict["ps_module"] = ps_module
        if not isinstance(ps_component, Unset):
            field_dict["ps_component"] = ps_component
        if not isinstance(affectedness, Unset):
            field_dict["affectedness"] = affectedness
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(trackers, Unset):
            field_dict["trackers"] = trackers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ps_module = d.pop("ps_module", UNSET)

        ps_component = d.pop("ps_component", UNSET)

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

        trackers = []
        _trackers = d.pop("trackers", UNSET)
        if _trackers is UNSET:
            trackers = UNSET
        else:
            for trackers_item_data in _trackers or []:
                _trackers_item = trackers_item_data
                trackers_item: TrackerReportData
                if isinstance(_trackers_item, Unset):
                    trackers_item = UNSET
                else:
                    trackers_item = TrackerReportData.from_dict(_trackers_item)

                trackers.append(trackers_item)

        affect_report_data = cls(
            ps_module=ps_module,
            ps_component=ps_component,
            affectedness=affectedness,
            resolution=resolution,
            trackers=trackers,
        )

        affect_report_data.additional_properties = d
        return affect_report_data

    @staticmethod
    def get_fields():
        return {
            "ps_module": str,
            "ps_component": str,
            "affectedness": Union[AffectednessEnum, BlankEnum],
            "resolution": Union[BlankEnum, ResolutionEnum],
            "trackers": List[TrackerReportData],
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
