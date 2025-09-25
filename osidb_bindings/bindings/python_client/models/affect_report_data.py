from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..models.affectedness_enum import AffectednessEnum
from ..models.blank_enum import BlankEnum
from ..models.resolution_enum import ResolutionEnum
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.tracker_report_data import TrackerReportData


T = TypeVar("T", bound="AffectReportData")


@_attrs_define
class AffectReportData(OSIDBModel):
    """
    Attributes:
        ps_update_stream (str):
        ps_component (str):
        affectedness (Union[AffectednessEnum, BlankEnum, Unset]):
        resolution (Union[BlankEnum, ResolutionEnum, Unset]):
        tracker (Union[Unset, TrackerReportData]):
    """

    ps_update_stream: str
    ps_component: str
    affectedness: Union[AffectednessEnum, BlankEnum, Unset] = UNSET
    resolution: Union[BlankEnum, ResolutionEnum, Unset] = UNSET
    tracker: Union[Unset, "TrackerReportData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ps_update_stream = self.ps_update_stream

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

        tracker: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracker, Unset):
            tracker = self.tracker.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream
        if not isinstance(ps_component, Unset):
            field_dict["ps_component"] = ps_component
        if not isinstance(affectedness, Unset):
            field_dict["affectedness"] = affectedness
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(tracker, Unset):
            field_dict["tracker"] = tracker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracker_report_data import TrackerReportData

        d = src_dict.copy()
        ps_update_stream = d.pop("ps_update_stream", UNSET)

        ps_component = d.pop("ps_component", UNSET)

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

        _tracker = d.pop("tracker", UNSET)
        tracker: Union[Unset, TrackerReportData]
        if isinstance(_tracker, Unset):
            tracker = UNSET
        else:
            tracker = TrackerReportData.from_dict(_tracker)

        affect_report_data = cls(
            ps_update_stream=ps_update_stream,
            ps_component=ps_component,
            affectedness=affectedness,
            resolution=resolution,
            tracker=tracker,
        )

        affect_report_data.additional_properties = d
        return affect_report_data

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
