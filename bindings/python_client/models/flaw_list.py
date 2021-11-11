import datetime
import json
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.affect import Affect
from ..models.blank_enum import BlankEnum
from ..models.comment import Comment
from ..models.flaw_list_meta_attr import FlawListMetaAttr
from ..models.impact_enum import ImpactEnum
from ..models.meta import Meta
from ..models.mitigated_by_enum import MitigatedByEnum
from ..models.source_enum import SourceEnum
from ..models.state_574_enum import State574Enum
from ..models.type_824_enum import Type824Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlawList")


@attr.s(auto_attribs=True)
class FlawList:
    """serialize flaw list model"""

    uuid: str
    updated_dt: datetime.datetime
    type: Type824Enum
    title: str
    trackers: List[str]
    affects: List[Affect]
    meta: List[Meta]
    comments: List[Comment]
    package_versions: List[str]
    cve_id: Optional[str]
    created_dt: Union[Unset, None, datetime.datetime] = UNSET
    state: Union[None, State574Enum, Unset] = UNSET
    resolution: Union[Unset, None, str] = UNSET
    impact: Union[ImpactEnum, None, Unset] = UNSET
    description: Union[Unset, None, str] = UNSET
    summary: Union[Unset, None, str] = UNSET
    statement: Union[Unset, None, str] = UNSET
    cwe_id: Union[Unset, None, str] = UNSET
    embargoed: Union[Unset, None, bool] = UNSET
    unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET
    source: Union[BlankEnum, None, SourceEnum, Unset] = UNSET
    reported_dt: Union[Unset, None, datetime.datetime] = UNSET
    mitigated_by: Union[BlankEnum, MitigatedByEnum, None, Unset] = UNSET
    cvss2: Union[Unset, None, str] = UNSET
    cvss2_score: Union[Unset, None, float] = UNSET
    cvss3: Union[Unset, None, str] = UNSET
    cvss3_score: Union[Unset, None, float] = UNSET
    is_csaw: Union[Unset, None, bool] = UNSET
    meta_attr: Union[Unset, None, FlawListMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        updated_dt = self.updated_dt.isoformat()

        type = self.type.value

        title = self.title
        trackers = self.trackers

        affects = []
        for affects_item_data in self.affects:
            affects_item = affects_item_data.to_dict()

            affects.append(affects_item)

        meta = []
        for meta_item_data in self.meta:
            meta_item = meta_item_data.to_dict()

            meta.append(meta_item)

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()

            comments.append(comments_item)

        package_versions = self.package_versions

        created_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat() if self.created_dt else None

        cve_id = self.cve_id
        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        elif self.state is None:
            state = None
        elif isinstance(self.state, State574Enum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = self.state.value

        else:
            state = self.state

        resolution = self.resolution
        impact: Union[None, Unset, str]
        if isinstance(self.impact, Unset):
            impact = UNSET
        elif self.impact is None:
            impact = None
        elif isinstance(self.impact, ImpactEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):
                impact = self.impact.value

        else:
            impact = self.impact

        description = self.description
        summary = self.summary
        statement = self.statement
        cwe_id = self.cwe_id
        embargoed = self.embargoed
        unembargo_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.unembargo_dt, Unset):
            unembargo_dt = self.unembargo_dt.isoformat() if self.unembargo_dt else None

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        elif self.source is None:
            source = None
        elif isinstance(self.source, SourceEnum):
            source = UNSET
            if not isinstance(self.source, Unset):
                source = self.source.value

        elif isinstance(self.source, BlankEnum):
            source = UNSET
            if not isinstance(self.source, Unset):
                source = self.source.value

        else:
            source = self.source

        reported_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.reported_dt, Unset):
            reported_dt = self.reported_dt.isoformat() if self.reported_dt else None

        mitigated_by: Union[None, Unset, str]
        if isinstance(self.mitigated_by, Unset):
            mitigated_by = UNSET
        elif self.mitigated_by is None:
            mitigated_by = None
        elif isinstance(self.mitigated_by, MitigatedByEnum):
            mitigated_by = UNSET
            if not isinstance(self.mitigated_by, Unset):
                mitigated_by = self.mitigated_by.value

        elif isinstance(self.mitigated_by, BlankEnum):
            mitigated_by = UNSET
            if not isinstance(self.mitigated_by, Unset):
                mitigated_by = self.mitigated_by.value

        else:
            mitigated_by = self.mitigated_by

        cvss2 = self.cvss2
        cvss2_score = self.cvss2_score
        cvss3 = self.cvss3
        cvss3_score = self.cvss3_score
        is_csaw = self.is_csaw
        meta_attr: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict() if self.meta_attr else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "updated_dt": updated_dt,
                "type": type,
                "title": title,
                "trackers": trackers,
                "affects": affects,
                "meta": meta,
                "comments": comments,
                "package_versions": package_versions,
                "cve_id": cve_id,
            }
        )
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if state is not UNSET:
            field_dict["state"] = state
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if impact is not UNSET:
            field_dict["impact"] = impact
        if description is not UNSET:
            field_dict["description"] = description
        if summary is not UNSET:
            field_dict["summary"] = summary
        if statement is not UNSET:
            field_dict["statement"] = statement
        if cwe_id is not UNSET:
            field_dict["cwe_id"] = cwe_id
        if embargoed is not UNSET:
            field_dict["embargoed"] = embargoed
        if unembargo_dt is not UNSET:
            field_dict["unembargo_dt"] = unembargo_dt
        if source is not UNSET:
            field_dict["source"] = source
        if reported_dt is not UNSET:
            field_dict["reported_dt"] = reported_dt
        if mitigated_by is not UNSET:
            field_dict["mitigated_by"] = mitigated_by
        if cvss2 is not UNSET:
            field_dict["cvss2"] = cvss2
        if cvss2_score is not UNSET:
            field_dict["cvss2_score"] = cvss2_score
        if cvss3 is not UNSET:
            field_dict["cvss3"] = cvss3
        if cvss3_score is not UNSET:
            field_dict["cvss3_score"] = cvss3_score
        if is_csaw is not UNSET:
            field_dict["is_csaw"] = is_csaw
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        updated_dt = self.updated_dt.isoformat()

        type = (None, str(self.type.value), "text/plain")

        title = self.title if self.title is UNSET else (None, str(self.title), "text/plain")
        _temp_trackers = self.trackers
        trackers = (None, json.dumps(_temp_trackers), "application/json")

        _temp_affects = []
        for affects_item_data in self.affects:
            affects_item = affects_item_data.to_dict()

            _temp_affects.append(affects_item)
        affects = (None, json.dumps(_temp_affects), "application/json")

        _temp_meta = []
        for meta_item_data in self.meta:
            meta_item = meta_item_data.to_dict()

            _temp_meta.append(meta_item)
        meta = (None, json.dumps(_temp_meta), "application/json")

        _temp_comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()

            _temp_comments.append(comments_item)
        comments = (None, json.dumps(_temp_comments), "application/json")

        _temp_package_versions = self.package_versions
        package_versions = (None, json.dumps(_temp_package_versions), "application/json")

        created_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat() if self.created_dt else None

        cve_id = self.cve_id if self.cve_id is UNSET else (None, str(self.cve_id), "text/plain")
        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        elif self.state is None:
            state = None
        elif isinstance(self.state, State574Enum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = (None, str(self.state.value), "text/plain")

        else:
            state = self.state

        resolution = self.resolution if self.resolution is UNSET else (None, str(self.resolution), "text/plain")
        impact: Union[None, Unset, str]
        if isinstance(self.impact, Unset):
            impact = UNSET
        elif self.impact is None:
            impact = None
        elif isinstance(self.impact, ImpactEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):
                impact = (None, str(self.impact.value), "text/plain")

        else:
            impact = self.impact

        description = self.description if self.description is UNSET else (None, str(self.description), "text/plain")
        summary = self.summary if self.summary is UNSET else (None, str(self.summary), "text/plain")
        statement = self.statement if self.statement is UNSET else (None, str(self.statement), "text/plain")
        cwe_id = self.cwe_id if self.cwe_id is UNSET else (None, str(self.cwe_id), "text/plain")
        embargoed = self.embargoed if self.embargoed is UNSET else (None, str(self.embargoed), "text/plain")
        unembargo_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.unembargo_dt, Unset):
            unembargo_dt = self.unembargo_dt.isoformat() if self.unembargo_dt else None

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        elif self.source is None:
            source = None
        elif isinstance(self.source, SourceEnum):
            source = UNSET
            if not isinstance(self.source, Unset):
                source = (None, str(self.source.value), "text/plain")

        elif isinstance(self.source, BlankEnum):
            source = UNSET
            if not isinstance(self.source, Unset):
                source = (None, str(self.source.value), "text/plain")

        else:
            source = self.source

        reported_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.reported_dt, Unset):
            reported_dt = self.reported_dt.isoformat() if self.reported_dt else None

        mitigated_by: Union[None, Unset, str]
        if isinstance(self.mitigated_by, Unset):
            mitigated_by = UNSET
        elif self.mitigated_by is None:
            mitigated_by = None
        elif isinstance(self.mitigated_by, MitigatedByEnum):
            mitigated_by = UNSET
            if not isinstance(self.mitigated_by, Unset):
                mitigated_by = (None, str(self.mitigated_by.value), "text/plain")

        elif isinstance(self.mitigated_by, BlankEnum):
            mitigated_by = UNSET
            if not isinstance(self.mitigated_by, Unset):
                mitigated_by = (None, str(self.mitigated_by.value), "text/plain")

        else:
            mitigated_by = self.mitigated_by

        cvss2 = self.cvss2 if self.cvss2 is UNSET else (None, str(self.cvss2), "text/plain")
        cvss2_score = self.cvss2_score if self.cvss2_score is UNSET else (None, str(self.cvss2_score), "text/plain")
        cvss3 = self.cvss3 if self.cvss3 is UNSET else (None, str(self.cvss3), "text/plain")
        cvss3_score = self.cvss3_score if self.cvss3_score is UNSET else (None, str(self.cvss3_score), "text/plain")
        is_csaw = self.is_csaw if self.is_csaw is UNSET else (None, str(self.is_csaw), "text/plain")
        meta_attr: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = (None, json.dumps(self.meta_attr.to_dict()), "application/json") if self.meta_attr else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        field_dict.update(
            {
                "uuid": uuid,
                "updated_dt": updated_dt,
                "type": type,
                "title": title,
                "trackers": trackers,
                "affects": affects,
                "meta": meta,
                "comments": comments,
                "package_versions": package_versions,
                "cve_id": cve_id,
            }
        )
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if state is not UNSET:
            field_dict["state"] = state
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if impact is not UNSET:
            field_dict["impact"] = impact
        if description is not UNSET:
            field_dict["description"] = description
        if summary is not UNSET:
            field_dict["summary"] = summary
        if statement is not UNSET:
            field_dict["statement"] = statement
        if cwe_id is not UNSET:
            field_dict["cwe_id"] = cwe_id
        if embargoed is not UNSET:
            field_dict["embargoed"] = embargoed
        if unembargo_dt is not UNSET:
            field_dict["unembargo_dt"] = unembargo_dt
        if source is not UNSET:
            field_dict["source"] = source
        if reported_dt is not UNSET:
            field_dict["reported_dt"] = reported_dt
        if mitigated_by is not UNSET:
            field_dict["mitigated_by"] = mitigated_by
        if cvss2 is not UNSET:
            field_dict["cvss2"] = cvss2
        if cvss2_score is not UNSET:
            field_dict["cvss2_score"] = cvss2_score
        if cvss3 is not UNSET:
            field_dict["cvss3"] = cvss3
        if cvss3_score is not UNSET:
            field_dict["cvss3_score"] = cvss3_score
        if is_csaw is not UNSET:
            field_dict["is_csaw"] = is_csaw
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        updated_dt = isoparse(d.pop("updated_dt"))

        type = Type824Enum(d.pop("type"))

        title = d.pop("title")

        trackers = cast(List[str], d.pop("trackers"))

        affects = []
        _affects = d.pop("affects")
        for affects_item_data in _affects:
            affects_item = Affect.from_dict(affects_item_data)

            affects.append(affects_item)

        meta = []
        _meta = d.pop("meta")
        for meta_item_data in _meta:
            meta_item = Meta.from_dict(meta_item_data)

            meta.append(meta_item)

        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = Comment.from_dict(comments_item_data)

            comments.append(comments_item)

        package_versions = cast(List[str], d.pop("package_versions"))

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: Union[Unset, None, datetime.datetime]
        if _created_dt is None:
            created_dt = None
        elif isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        cve_id = d.pop("cve_id")

        def _parse_state(data: object) -> Union[None, State574Enum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _state_type_0 = data
                state_type_0: Union[Unset, State574Enum]
                if isinstance(_state_type_0, Unset):
                    state_type_0 = UNSET
                else:
                    state_type_0 = State574Enum(_state_type_0)

                return state_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, State574Enum, Unset], data)

        state = _parse_state(d.pop("state", UNSET))

        resolution = d.pop("resolution", UNSET)

        def _parse_impact(data: object) -> Union[ImpactEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _impact_type_0 = data
                impact_type_0: Union[Unset, ImpactEnum]
                if isinstance(_impact_type_0, Unset):
                    impact_type_0 = UNSET
                else:
                    impact_type_0 = ImpactEnum(_impact_type_0)

                return impact_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ImpactEnum, None, Unset], data)

        impact = _parse_impact(d.pop("impact", UNSET))

        description = d.pop("description", UNSET)

        summary = d.pop("summary", UNSET)

        statement = d.pop("statement", UNSET)

        cwe_id = d.pop("cwe_id", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        _unembargo_dt = d.pop("unembargo_dt", UNSET)
        unembargo_dt: Union[Unset, None, datetime.datetime]
        if _unembargo_dt is None:
            unembargo_dt = None
        elif isinstance(_unembargo_dt, Unset):
            unembargo_dt = UNSET
        else:
            unembargo_dt = isoparse(_unembargo_dt)

        def _parse_source(data: object) -> Union[BlankEnum, None, SourceEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _source_type_0 = data
                source_type_0: Union[Unset, SourceEnum]
                if isinstance(_source_type_0, Unset):
                    source_type_0 = UNSET
                else:
                    source_type_0 = SourceEnum(_source_type_0)

                return source_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _source_type_1 = data
                source_type_1: Union[Unset, BlankEnum]
                if isinstance(_source_type_1, Unset):
                    source_type_1 = UNSET
                else:
                    source_type_1 = BlankEnum(_source_type_1)

                return source_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, None, SourceEnum, Unset], data)

        source = _parse_source(d.pop("source", UNSET))

        _reported_dt = d.pop("reported_dt", UNSET)
        reported_dt: Union[Unset, None, datetime.datetime]
        if _reported_dt is None:
            reported_dt = None
        elif isinstance(_reported_dt, Unset):
            reported_dt = UNSET
        else:
            reported_dt = isoparse(_reported_dt)

        def _parse_mitigated_by(data: object) -> Union[BlankEnum, MitigatedByEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _mitigated_by_type_0 = data
                mitigated_by_type_0: Union[Unset, MitigatedByEnum]
                if isinstance(_mitigated_by_type_0, Unset):
                    mitigated_by_type_0 = UNSET
                else:
                    mitigated_by_type_0 = MitigatedByEnum(_mitigated_by_type_0)

                return mitigated_by_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _mitigated_by_type_1 = data
                mitigated_by_type_1: Union[Unset, BlankEnum]
                if isinstance(_mitigated_by_type_1, Unset):
                    mitigated_by_type_1 = UNSET
                else:
                    mitigated_by_type_1 = BlankEnum(_mitigated_by_type_1)

                return mitigated_by_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, MitigatedByEnum, None, Unset], data)

        mitigated_by = _parse_mitigated_by(d.pop("mitigated_by", UNSET))

        cvss2 = d.pop("cvss2", UNSET)

        cvss2_score = d.pop("cvss2_score", UNSET)

        cvss3 = d.pop("cvss3", UNSET)

        cvss3_score = d.pop("cvss3_score", UNSET)

        is_csaw = d.pop("is_csaw", UNSET)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, None, FlawListMetaAttr]
        if _meta_attr is None:
            meta_attr = None
        elif isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = FlawListMetaAttr.from_dict(_meta_attr)

        flaw_list = cls(
            uuid=uuid,
            updated_dt=updated_dt,
            type=type,
            title=title,
            trackers=trackers,
            affects=affects,
            meta=meta,
            comments=comments,
            package_versions=package_versions,
            created_dt=created_dt,
            cve_id=cve_id,
            state=state,
            resolution=resolution,
            impact=impact,
            description=description,
            summary=summary,
            statement=statement,
            cwe_id=cwe_id,
            embargoed=embargoed,
            unembargo_dt=unembargo_dt,
            source=source,
            reported_dt=reported_dt,
            mitigated_by=mitigated_by,
            cvss2=cvss2,
            cvss2_score=cvss2_score,
            cvss3=cvss3,
            cvss3_score=cvss3_score,
            is_csaw=is_csaw,
            meta_attr=meta_attr,
        )

        flaw_list.additional_properties = d
        return flaw_list

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
