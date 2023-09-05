from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="AffectMetaAttr")


@attr.s(auto_attribs=True)
class AffectMetaAttr(OSIDBModel):
    """ """

    affectedness: Union[Unset, str] = UNSET
    component: Union[Unset, str] = UNSET
    cvss2: Union[Unset, str] = UNSET
    cvss3: Union[Unset, str] = UNSET
    impact: Union[Unset, str] = UNSET
    module_name: Union[Unset, str] = UNSET
    module_stream: Union[Unset, str] = UNSET
    ps_component: Union[Unset, str] = UNSET
    ps_module: Union[Unset, str] = UNSET
    resolution: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        affectedness = self.affectedness
        component = self.component
        cvss2 = self.cvss2
        cvss3 = self.cvss3
        impact = self.impact
        module_name = self.module_name
        module_stream = self.module_stream
        ps_component = self.ps_component
        ps_module = self.ps_module
        resolution = self.resolution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(affectedness, Unset):
            field_dict["affectedness"] = affectedness
        if not isinstance(component, Unset):
            field_dict["component"] = component
        if not isinstance(cvss2, Unset):
            field_dict["cvss2"] = cvss2
        if not isinstance(cvss3, Unset):
            field_dict["cvss3"] = cvss3
        if not isinstance(impact, Unset):
            field_dict["impact"] = impact
        if not isinstance(module_name, Unset):
            field_dict["module_name"] = module_name
        if not isinstance(module_stream, Unset):
            field_dict["module_stream"] = module_stream
        if not isinstance(ps_component, Unset):
            field_dict["ps_component"] = ps_component
        if not isinstance(ps_module, Unset):
            field_dict["ps_module"] = ps_module
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        affectedness = d.pop("affectedness", UNSET)

        component = d.pop("component", UNSET)

        cvss2 = d.pop("cvss2", UNSET)

        cvss3 = d.pop("cvss3", UNSET)

        impact = d.pop("impact", UNSET)

        module_name = d.pop("module_name", UNSET)

        module_stream = d.pop("module_stream", UNSET)

        ps_component = d.pop("ps_component", UNSET)

        ps_module = d.pop("ps_module", UNSET)

        resolution = d.pop("resolution", UNSET)

        affect_meta_attr = cls(
            affectedness=affectedness,
            component=component,
            cvss2=cvss2,
            cvss3=cvss3,
            impact=impact,
            module_name=module_name,
            module_stream=module_stream,
            ps_component=ps_component,
            ps_module=ps_module,
            resolution=resolution,
        )

        affect_meta_attr.additional_properties = d
        return affect_meta_attr

    @staticmethod
    def get_fields():
        return {
            "affectedness": str,
            "component": str,
            "cvss2": str,
            "cvss3": str,
            "impact": str,
            "module_name": str,
            "module_stream": str,
            "ps_component": str,
            "ps_module": str,
            "resolution": str,
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
