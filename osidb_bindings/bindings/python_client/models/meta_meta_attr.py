from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..types import OSIDBModel

T = TypeVar("T", bound="MetaMetaAttr")


@attr.s(auto_attribs=True)
class MetaMetaAttr(OSIDBModel):
    """ """

    additional_properties: Dict[str, Optional[str]] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        meta_meta_attr = cls()

        meta_meta_attr.additional_properties = d
        return meta_meta_attr

    @staticmethod
    def get_fields():
        return {}

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Optional[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Optional[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
