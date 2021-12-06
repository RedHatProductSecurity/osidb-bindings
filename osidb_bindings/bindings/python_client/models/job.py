import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.state_enum import StateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """serialize job json"""

    uuid: str
    bz_count: str
    cve_count: str
    state: Union[None, StateEnum, Unset] = UNSET
    comment: Union[Unset, None, str] = UNSET
    created_dt: Union[Unset, None, datetime.datetime] = UNSET
    bz_ids: Union[Unset, List[str]] = UNSET
    dry_run: Union[Unset, bool] = UNSET
    update: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        bz_count = self.bz_count
        cve_count = self.cve_count
        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        elif self.state is None:
            state = None
        elif isinstance(self.state, StateEnum):
            state = UNSET
            if not isinstance(self.state, Unset):

                state = StateEnum(self.state).value

        else:
            state = self.state

        comment = self.comment
        created_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat() if self.created_dt else None

        bz_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.bz_ids, Unset):
            bz_ids = self.bz_ids

        dry_run = self.dry_run
        update = self.update

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if bz_count is not UNSET:
            field_dict["bz_count"] = bz_count
        if cve_count is not UNSET:
            field_dict["cve_count"] = cve_count
        if state is not UNSET:
            field_dict["state"] = state
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if bz_ids is not UNSET:
            field_dict["bz_ids"] = bz_ids
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        bz_count = self.bz_count if self.bz_count is UNSET else (None, str(self.bz_count), "text/plain")
        cve_count = self.cve_count if self.cve_count is UNSET else (None, str(self.cve_count), "text/plain")
        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        elif self.state is None:
            state = None
        elif isinstance(self.state, StateEnum):
            state = UNSET
            if not isinstance(self.state, Unset):

                state = StateEnum(self.state).value

        else:
            state = self.state

        comment = self.comment if self.comment is UNSET else (None, str(self.comment), "text/plain")
        created_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat() if self.created_dt else None

        bz_ids: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.bz_ids, Unset):
            _temp_bz_ids = self.bz_ids
            bz_ids = (None, json.dumps(_temp_bz_ids), "application/json")

        dry_run = self.dry_run if self.dry_run is UNSET else (None, str(self.dry_run), "text/plain")
        update = self.update if self.update is UNSET else (None, str(self.update), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if bz_count is not UNSET:
            field_dict["bz_count"] = bz_count
        if cve_count is not UNSET:
            field_dict["cve_count"] = cve_count
        if state is not UNSET:
            field_dict["state"] = state
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if bz_ids is not UNSET:
            field_dict["bz_ids"] = bz_ids
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        bz_count = d.pop("bz_count", UNSET)

        cve_count = d.pop("cve_count", UNSET)

        def _parse_state(data: object) -> Union[None, StateEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _state_type_0 = data
                state_type_0: Union[Unset, StateEnum]
                if isinstance(_state_type_0, Unset):
                    state_type_0 = UNSET
                else:
                    state_type_0 = StateEnum(_state_type_0)

                return state_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, StateEnum, Unset], data)

        state = _parse_state(d.pop("state", UNSET))

        comment = d.pop("comment", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: Union[Unset, None, datetime.datetime]
        if _created_dt is None:
            created_dt = None
        elif isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        bz_ids = cast(List[str], d.pop("bz_ids", UNSET))

        dry_run = d.pop("dry_run", UNSET)

        update = d.pop("update", UNSET)

        job = cls(
            uuid=uuid,
            bz_count=bz_count,
            cve_count=cve_count,
            state=state,
            comment=comment,
            created_dt=created_dt,
            bz_ids=bz_ids,
            dry_run=dry_run,
            update=update,
        )

        job.additional_properties = d
        return job

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
