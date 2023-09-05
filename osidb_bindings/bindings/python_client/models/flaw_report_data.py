from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.affect_report_data import AffectReportData
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawReportData")


@attr.s(auto_attribs=True)
class FlawReportData(OSIDBModel):
    """ """

    state: str
    resolution: str
    cve_id: Union[Unset, None, str] = UNSET
    affects: Union[Unset, List[AffectReportData]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state
        resolution = self.resolution
        cve_id = self.cve_id
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
        if not isinstance(state, Unset):
            field_dict["state"] = state
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(cve_id, Unset):
            field_dict["cve_id"] = cve_id
        if not isinstance(affects, Unset):
            field_dict["affects"] = affects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = d.pop("state", UNSET)

        resolution = d.pop("resolution", UNSET)

        cve_id = d.pop("cve_id", UNSET)

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
            state=state,
            resolution=resolution,
            cve_id=cve_id,
            affects=affects,
        )

        flaw_report_data.additional_properties = d
        return flaw_report_data

    @staticmethod
    def get_fields():
        return {
            "state": str,
            "resolution": str,
            "cve_id": str,
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
