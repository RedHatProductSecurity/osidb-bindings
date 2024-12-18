from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.affect_report_data import AffectReportData


T = TypeVar("T", bound="FlawReportData")


@_attrs_define
class FlawReportData(OSIDBModel):
    """
    Attributes:
        cve_id (Union[None, Unset, str]):
        affects (Union[Unset, list['AffectReportData']]):
    """

    cve_id: Union[None, Unset, str] = UNSET
    affects: Union[Unset, list["AffectReportData"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve_id: Union[None, Unset, str]
        if isinstance(self.cve_id, Unset):
            cve_id = UNSET
        else:
            cve_id = self.cve_id

        affects: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affects, Unset):
            affects = []
            for affects_item_data in self.affects:
                affects_item: dict[str, Any] = UNSET
                if not isinstance(affects_item_data, Unset):
                    affects_item = affects_item_data.to_dict()

                affects.append(affects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(cve_id, Unset):
            field_dict["cve_id"] = cve_id
        if not isinstance(affects, Unset):
            field_dict["affects"] = affects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.affect_report_data import AffectReportData

        d = src_dict.copy()

        def _parse_cve_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cve_id = _parse_cve_id(d.pop("cve_id", UNSET))

        affects = []
        _affects = d.pop("affects", UNSET)
        for affects_item_data in _affects or []:
            # }
            _affects_item = affects_item_data
            affects_item: AffectReportData
            if isinstance(_affects_item, Unset):
                affects_item = UNSET
            else:
                affects_item = AffectReportData.from_dict(_affects_item)

            affects.append(affects_item)

        flaw_report_data = cls(
            cve_id=cve_id,
            affects=affects,
        )

        flaw_report_data.additional_properties = d
        return flaw_report_data

    @staticmethod
    def get_fields():
        return {
            "cve_id": Union[None, str],
            "affects": list["AffectReportData"],
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
