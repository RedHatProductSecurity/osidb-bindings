from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="EPSS")


@attr.s(auto_attribs=True)
class EPSS(OSIDBModel):
    """ """

    cve: str
    epss: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cve = self.cve
        epss = self.epss

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(cve, Unset):
            field_dict["cve"] = cve
        if not isinstance(epss, Unset):
            field_dict["epss"] = epss

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cve = d.pop("cve", UNSET)

        epss = d.pop("epss", UNSET)

        epss = cls(
            cve=cve,
            epss=epss,
        )

        epss.additional_properties = d
        return epss

    @staticmethod
    def get_fields():
        return {
            "cve": str,
            "epss": float,
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
