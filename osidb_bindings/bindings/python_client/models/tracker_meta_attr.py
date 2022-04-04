from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackerMetaAttr")


@attr.s(auto_attribs=True)
class TrackerMetaAttr:
    """ """

    bz_id: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    qe_owner: Union[Unset, str] = UNSET
    ps_component: Union[Unset, str] = UNSET
    ps_module: Union[Unset, str] = UNSET
    ps_update_stream: Union[Unset, str] = UNSET
    resolution: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bz_id = self.bz_id
        owner = self.owner
        qe_owner = self.qe_owner
        ps_component = self.ps_component
        ps_module = self.ps_module
        ps_update_stream = self.ps_update_stream
        resolution = self.resolution
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if bz_id is not UNSET:
            field_dict["bz_id"] = bz_id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if qe_owner is not UNSET:
            field_dict["qe_owner"] = qe_owner
        if ps_component is not UNSET:
            field_dict["ps_component"] = ps_component
        if ps_module is not UNSET:
            field_dict["ps_module"] = ps_module
        if ps_update_stream is not UNSET:
            field_dict["ps_update_stream"] = ps_update_stream
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bz_id = d.pop("bz_id", UNSET)

        owner = d.pop("owner", UNSET)

        qe_owner = d.pop("qe_owner", UNSET)

        ps_component = d.pop("ps_component", UNSET)

        ps_module = d.pop("ps_module", UNSET)

        ps_update_stream = d.pop("ps_update_stream", UNSET)

        resolution = d.pop("resolution", UNSET)

        status = d.pop("status", UNSET)

        tracker_meta_attr = cls(
            bz_id=bz_id,
            owner=owner,
            qe_owner=qe_owner,
            ps_component=ps_component,
            ps_module=ps_module,
            ps_update_stream=ps_update_stream,
            resolution=resolution,
            status=status,
        )

        tracker_meta_attr.additional_properties = d
        return tracker_meta_attr

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
