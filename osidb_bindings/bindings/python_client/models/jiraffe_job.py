import datetime
import json
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.state_enum import StateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="JiraffeJob")


@attr.s(auto_attribs=True)
class JiraffeJob:
    """Serialize JiraffeJob into JSON"""

    uuid: str
    affect_uuids: List[Optional[str]]
    affect_count: str
    state: Union[None, StateEnum, Unset] = UNSET
    comment: Union[Unset, None, str] = UNSET
    created_dt: Union[Unset, None, datetime.datetime] = UNSET
    dry_run: Union[Unset, bool] = UNSET
    update: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        affect_uuids: List[Optional[str]] = UNSET
        if not isinstance(self.affect_uuids, Unset):
            affect_uuids = self.affect_uuids

        affect_count = self.affect_count
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

        dry_run = self.dry_run
        update = self.update

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if affect_uuids is not UNSET:
            field_dict["affect_uuids"] = affect_uuids
        if affect_count is not UNSET:
            field_dict["affect_count"] = affect_count
        if state is not UNSET:
            field_dict["state"] = state
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        affect_uuids: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.affect_uuids, Unset):
            _temp_affect_uuids = self.affect_uuids
            affect_uuids = (None, json.dumps(_temp_affect_uuids), "application/json")

        affect_count = self.affect_count if self.affect_count is UNSET else (None, str(self.affect_count), "text/plain")
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

        dry_run = self.dry_run if self.dry_run is UNSET else (None, str(self.dry_run), "text/plain")
        update = self.update if self.update is UNSET else (None, str(self.update), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if affect_uuids is not UNSET:
            field_dict["affect_uuids"] = affect_uuids
        if affect_count is not UNSET:
            field_dict["affect_count"] = affect_count
        if state is not UNSET:
            field_dict["state"] = state
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        affect_uuids = cast(List[Optional[str]], d.pop("affect_uuids", UNSET))

        affect_count = d.pop("affect_count", UNSET)

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

        dry_run = d.pop("dry_run", UNSET)

        update = d.pop("update", UNSET)

        jiraffe_job = cls(
            uuid=uuid,
            affect_uuids=affect_uuids,
            affect_count=affect_count,
            state=state,
            comment=comment,
            created_dt=created_dt,
            dry_run=dry_run,
            update=update,
        )

        jiraffe_job.additional_properties = d
        return jiraffe_job

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
