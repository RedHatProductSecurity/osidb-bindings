from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import OSIDBModel

T = TypeVar("T", bound="AffectCVSSPutAlerts")


@attr.s(auto_attribs=True)
class AffectCVSSPutAlerts(OSIDBModel):
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        affect_cvss_put_alerts = cls()

        affect_cvss_put_alerts.additional_properties = d
        return affect_cvss_put_alerts

    @staticmethod
    def get_fields():
        return {}

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
