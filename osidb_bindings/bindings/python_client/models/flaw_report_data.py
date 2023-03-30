from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.affect_report_data import AffectReportData
from ..models.blank_enum import BlankEnum
from ..models.resolution_01f_enum import Resolution01FEnum
from ..models.state_enum import StateEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawReportData")


@attr.s(auto_attribs=True)
class FlawReportData(OSIDBModel):
    """ """

    cve_id: Union[Unset, None, str] = UNSET
    state: Union[Unset, StateEnum] = UNSET
    resolution: Union[BlankEnum, Resolution01FEnum, Unset] = UNSET
    affects: Union[Unset, List[AffectReportData]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cve_id = self.cve_id
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):

            state = StateEnum(self.state).value

        resolution: Union[Unset, str]
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        elif isinstance(self.resolution, Resolution01FEnum):
            resolution = UNSET
            if not isinstance(self.resolution, Unset):

                resolution = Resolution01FEnum(self.resolution).value

        else:
            resolution = UNSET
            if not isinstance(self.resolution, Unset):

                resolution = BlankEnum(self.resolution).value

        affects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.affects, Unset):
            affects = []
            for affects_item_data in self.affects:
                affects_item: Dict[str, Any] = UNSET
                if not isinstance(affects_item_data, Unset):
                    affects_item = affects_item_data.to_dict()

                affects.append(affects_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if cve_id is not UNSET:
            field_dict["cve_id"] = cve_id
        if state is not UNSET:
            field_dict["state"] = state
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if affects is not UNSET:
            field_dict["affects"] = affects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cve_id = d.pop("cve_id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, StateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StateEnum(_state)

        def _parse_resolution(
            data: object,
        ) -> Union[BlankEnum, Resolution01FEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _resolution_type_0 = data
                resolution_type_0: Union[Unset, Resolution01FEnum]
                if isinstance(_resolution_type_0, Unset):
                    resolution_type_0 = UNSET
                else:
                    resolution_type_0 = Resolution01FEnum(_resolution_type_0)

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

        affects = []
        _affects = d.pop("affects", UNSET)
        if _affects is UNSET:
            affects = UNSET
        else:
            for affects_item_data in _affects or []:
                _affects_item = affects_item_data
                affects_item: AffectReportData
                if isinstance(_affects_item, Unset):
                    affects_item = UNSET
                else:
                    affects_item = AffectReportData.from_dict(_affects_item)

                affects.append(affects_item)

        flaw_report_data = cls(
            cve_id=cve_id,
            state=state,
            resolution=resolution,
            affects=affects,
        )

        flaw_report_data.additional_properties = d
        return flaw_report_data

    @staticmethod
    def get_fields():
        return {
            "cve_id": str,
            "state": StateEnum,
            "resolution": Union[BlankEnum, Resolution01FEnum],
            "affects": List[AffectReportData],
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
