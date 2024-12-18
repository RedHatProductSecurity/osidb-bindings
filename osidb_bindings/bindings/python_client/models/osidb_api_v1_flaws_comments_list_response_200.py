import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.flaw_comment import FlawComment
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1FlawsCommentsListResponse200")


@attr.s(auto_attribs=True)
class OsidbApiV1FlawsCommentsListResponse200(OSIDBModel):
    """ """

    count: int
    results: List[FlawComment]
    next_: Union[Unset, None, str] = UNSET
    previous: Union[Unset, None, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        results: List[Dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item: Dict[str, Any] = UNSET
                if not isinstance(results_item_data, Unset):
                    results_item = results_item_data.to_dict()

                results.append(results_item)

        next_ = self.next_
        previous = self.previous
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(count, Unset):
            field_dict["count"] = count
        if not isinstance(results, Unset):
            field_dict["results"] = results
        if not isinstance(next_, Unset):
            field_dict["next"] = next_
        if not isinstance(previous, Unset):
            field_dict["previous"] = previous
        if not isinstance(dt, Unset):
            field_dict["dt"] = dt
        if not isinstance(env, Unset):
            field_dict["env"] = env
        if not isinstance(revision, Unset):
            field_dict["revision"] = revision
        if not isinstance(version, Unset):
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        if _results is UNSET:
            results = UNSET
        else:
            for results_item_data in _results or []:
                _results_item = results_item_data
                results_item: FlawComment
                if isinstance(_results_item, Unset):
                    results_item = UNSET
                else:
                    results_item = FlawComment.from_dict(_results_item)

                results.append(results_item)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_flaws_comments_list_response_200 = cls(
            count=count,
            results=results,
            next_=next_,
            previous=previous,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_flaws_comments_list_response_200.additional_properties = d
        return osidb_api_v1_flaws_comments_list_response_200

    @staticmethod
    def get_fields():
        return {
            "count": int,
            "results": List[FlawComment],
            "next": str,
            "previous": str,
            "dt": datetime.datetime,
            "env": str,
            "revision": str,
            "version": str,
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
