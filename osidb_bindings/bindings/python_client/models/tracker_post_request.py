import datetime
import json
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="TrackerPostRequest")


@_attrs_define
class TrackerPostRequest(OSIDBModel):
    """Tracker serializer

    Attributes:
        ps_update_stream (str):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        affects (Union[Unset, list[UUID]]):
        sync_to_bz (Union[Unset, bool]): Setting sync_to_bz to false disables flaw sync with Bugzilla after this
            operation. Use only as part of bulk actions and trigger a flaw bugzilla sync afterwards. Does nothing if BZ is
            disabled.
    """

    ps_update_stream: str
    embargoed: bool
    updated_dt: datetime.datetime
    affects: Union[Unset, list[UUID]] = UNSET
    sync_to_bz: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ps_update_stream = self.ps_update_stream

        embargoed = self.embargoed

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        affects: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affects, Unset):
            affects = []
            for affects_item_data in self.affects:
                affects_item: str = UNSET
                if not isinstance(affects_item_data, Unset):
                    affects_item = str(affects_item_data)

                affects.append(affects_item)

        sync_to_bz = self.sync_to_bz

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(affects, Unset):
            field_dict["affects"] = affects
        if not isinstance(sync_to_bz, Unset):
            field_dict["sync_to_bz"] = sync_to_bz

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        ps_update_stream = (None, str(self.ps_update_stream).encode(), "text/plain")

        embargoed = (None, str(self.embargoed).encode(), "text/plain")

        updated_dt: bytes = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat().encode()

        affects: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.affects, Unset):
            _temp_affects = []
            for affects_item_data in self.affects:
                affects_item: str = UNSET
                if not isinstance(affects_item_data, Unset):
                    affects_item = str(affects_item_data)

                _temp_affects.append(affects_item)
            affects = (None, json.dumps(_temp_affects).encode(), "application/json")

        sync_to_bz = (
            self.sync_to_bz
            if isinstance(self.sync_to_bz, Unset)
            else (None, str(self.sync_to_bz).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(ps_update_stream, Unset):
            field_dict["ps_update_stream"] = ps_update_stream
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(affects, Unset):
            field_dict["affects"] = affects
        if not isinstance(sync_to_bz, Unset):
            field_dict["sync_to_bz"] = sync_to_bz

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ps_update_stream = d.pop("ps_update_stream", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        affects = []
        _affects = d.pop("affects", UNSET)
        for affects_item_data in _affects or []:
            _affects_item = affects_item_data
            affects_item: UUID
            if isinstance(_affects_item, Unset):
                affects_item = UNSET
            else:
                affects_item = (
                    _affects_item
                    if isinstance(_affects_item, UUID)
                    else UUID(_affects_item)
                )

            affects.append(affects_item)

        sync_to_bz = d.pop("sync_to_bz", UNSET)

        tracker_post_request = cls(
            ps_update_stream=ps_update_stream,
            embargoed=embargoed,
            updated_dt=updated_dt,
            affects=affects,
            sync_to_bz=sync_to_bz,
        )

        tracker_post_request.additional_properties = d
        return tracker_post_request

    @staticmethod
    def get_fields():
        return {
            "ps_update_stream": str,
            "embargoed": bool,
            "updated_dt": datetime.datetime,
            "affects": list[UUID],
            "sync_to_bz": bool,
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
