import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.affect import Affect
from ..models.blank_enum import BlankEnum
from ..models.impact_enum import ImpactEnum
from ..models.meta import Meta
from ..models.mitigated_by_enum import MitigatedByEnum
from ..models.null_enum import NullEnum
from ..models.source_enum import SourceEnum
from ..models.state_574_enum import State574Enum
from ..models.type_824_enum import Type824Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Flaw")


@attr.s(auto_attribs=True)
class Flaw:
    """serialize flaw model"""

    uuid: str
    updated_dt: datetime.datetime
    type: Type824Enum
    title: str
    affects: List[Affect]
    meta: List[Meta]
    cve_id: Optional[str]
    created_dt: Union[Unset, None, datetime.datetime] = UNSET
    state: Union[BlankEnum, None, NullEnum, State574Enum, Unset] = UNSET
    resolution: Union[Unset, None, str] = UNSET
    impact: Union[BlankEnum, ImpactEnum, None, NullEnum, Unset] = UNSET
    description: Union[Unset, None, str] = UNSET
    summary: Union[Unset, None, str] = UNSET
    statement: Union[Unset, None, str] = UNSET
    cwe_id: Union[Unset, None, str] = UNSET
    embargoed: Union[Unset, None, bool] = UNSET
    unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET
    source: Union[BlankEnum, None, NullEnum, SourceEnum, Unset] = UNSET
    reported_dt: Union[Unset, None, datetime.datetime] = UNSET
    mitigated_by: Union[BlankEnum, MitigatedByEnum, None, NullEnum, Unset] = UNSET
    cvss2: Union[Unset, None, str] = UNSET
    cvss2_score: Union[Unset, None, float] = UNSET
    cvss3: Union[Unset, None, str] = UNSET
    cvss3_score: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        updated_dt = self.updated_dt.isoformat()

        type = self.type.value

        title = self.title
        affects = []
        for affects_item_data in self.affects:
            affects_item = affects_item_data.to_dict()

            affects.append(affects_item)

        meta = []
        for meta_item_data in self.meta:
            meta_item = meta_item_data.to_dict()

            meta.append(meta_item)

        created_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat() if self.created_dt else None

        cve_id = self.cve_id
        state: Union[None, NoneType, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        elif self.state is None:
            state = None
        elif isinstance(self.state, State574Enum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = self.state.value

        elif isinstance(self.state, BlankEnum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = self.state.value

        else:
            state = UNSET
            if not isinstance(self.state, Unset):
                state = self.state.value

        resolution = self.resolution
        impact: Union[None, NoneType, Unset, str]
        if isinstance(self.impact, Unset):
            impact = UNSET
        elif self.impact is None:
            impact = None
        elif isinstance(self.impact, ImpactEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):
                impact = self.impact.value

        elif isinstance(self.impact, BlankEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):
                impact = self.impact.value

        else:
            impact = UNSET
            if not isinstance(self.impact, Unset):
                impact = self.impact.value

        description = self.description
        summary = self.summary
        statement = self.statement
        cwe_id = self.cwe_id
        embargoed = self.embargoed
        unembargo_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.unembargo_dt, Unset):
            unembargo_dt = self.unembargo_dt.isoformat() if self.unembargo_dt else None

        source: Union[None, NoneType, Unset, str]
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
            source = UNSET
            if not isinstance(self.source, Unset):
                source = self.source.value

        reported_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.reported_dt, Unset):
            reported_dt = self.reported_dt.isoformat() if self.reported_dt else None

        mitigated_by: Union[None, NoneType, Unset, str]
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
            mitigated_by = UNSET
            if not isinstance(self.mitigated_by, Unset):
                mitigated_by = self.mitigated_by.value

        cvss2 = self.cvss2
        cvss2_score = self.cvss2_score
        cvss3 = self.cvss3
        cvss3_score = self.cvss3_score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "updated_dt": updated_dt,
                "type": type,
                "title": title,
                "affects": affects,
                "meta": meta,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        updated_dt = isoparse(d.pop("updated_dt"))

        type = Type824Enum(d.pop("type"))

        title = d.pop("title")

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

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: Union[Unset, None, datetime.datetime]
        if _created_dt is None:
            created_dt = None
        elif isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        cve_id = d.pop("cve_id")

        def _parse_state(data: object) -> Union[BlankEnum, None, NullEnum, State574Enum, Unset]:
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
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _state_type_1 = data
                state_type_1: Union[Unset, BlankEnum]
                if isinstance(_state_type_1, Unset):
                    state_type_1 = UNSET
                else:
                    state_type_1 = BlankEnum(_state_type_1)

                return state_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, NoneType):
                raise TypeError()
            _state_type_2 = data
            state_type_2: Union[Unset, NullEnum]
            if isinstance(_state_type_2, Unset):
                state_type_2 = UNSET
            else:
                state_type_2 = NullEnum(_state_type_2)

            return state_type_2

        state = _parse_state(d.pop("state", UNSET))

        resolution = d.pop("resolution", UNSET)

        def _parse_impact(data: object) -> Union[BlankEnum, ImpactEnum, None, NullEnum, Unset]:
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
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _impact_type_1 = data
                impact_type_1: Union[Unset, BlankEnum]
                if isinstance(_impact_type_1, Unset):
                    impact_type_1 = UNSET
                else:
                    impact_type_1 = BlankEnum(_impact_type_1)

                return impact_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, NoneType):
                raise TypeError()
            _impact_type_2 = data
            impact_type_2: Union[Unset, NullEnum]
            if isinstance(_impact_type_2, Unset):
                impact_type_2 = UNSET
            else:
                impact_type_2 = NullEnum(_impact_type_2)

            return impact_type_2

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

        def _parse_source(data: object) -> Union[BlankEnum, None, NullEnum, SourceEnum, Unset]:
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
            if not isinstance(data, NoneType):
                raise TypeError()
            _source_type_2 = data
            source_type_2: Union[Unset, NullEnum]
            if isinstance(_source_type_2, Unset):
                source_type_2 = UNSET
            else:
                source_type_2 = NullEnum(_source_type_2)

            return source_type_2

        source = _parse_source(d.pop("source", UNSET))

        _reported_dt = d.pop("reported_dt", UNSET)
        reported_dt: Union[Unset, None, datetime.datetime]
        if _reported_dt is None:
            reported_dt = None
        elif isinstance(_reported_dt, Unset):
            reported_dt = UNSET
        else:
            reported_dt = isoparse(_reported_dt)

        def _parse_mitigated_by(data: object) -> Union[BlankEnum, MitigatedByEnum, None, NullEnum, Unset]:
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
            if not isinstance(data, NoneType):
                raise TypeError()
            _mitigated_by_type_2 = data
            mitigated_by_type_2: Union[Unset, NullEnum]
            if isinstance(_mitigated_by_type_2, Unset):
                mitigated_by_type_2 = UNSET
            else:
                mitigated_by_type_2 = NullEnum(_mitigated_by_type_2)

            return mitigated_by_type_2

        mitigated_by = _parse_mitigated_by(d.pop("mitigated_by", UNSET))

        cvss2 = d.pop("cvss2", UNSET)

        cvss2_score = d.pop("cvss2_score", UNSET)

        cvss3 = d.pop("cvss3", UNSET)

        cvss3_score = d.pop("cvss3_score", UNSET)

        flaw = cls(
            uuid=uuid,
            updated_dt=updated_dt,
            type=type,
            title=title,
            affects=affects,
            meta=meta,
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
        )

        flaw.additional_properties = d
        return flaw

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
