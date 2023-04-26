import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.affect import Affect
from ..models.blank_enum import BlankEnum
from ..models.comment import Comment
from ..models.cv_ev_5_package_versions import CVEv5PackageVersions
from ..models.flaw_classification import FlawClassification
from ..models.flaw_meta_attr import FlawMetaAttr
from ..models.impact_enum import ImpactEnum
from ..models.meta import Meta
from ..models.source_666_enum import Source666Enum
from ..models.type_824_enum import Type824Enum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1FlawsRetrieveResponse200")


@attr.s(auto_attribs=True)
class OsidbApiV1FlawsRetrieveResponse200(OSIDBModel):
    """ """

    uuid: str
    state: str
    resolution: str
    title: str
    trackers: List[str]
    description: str
    affects: List[Affect]
    meta: List[Meta]
    comments: List[Comment]
    meta_attr: FlawMetaAttr
    package_versions: List[CVEv5PackageVersions]
    embargoed: bool
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    classification: FlawClassification
    type: Union[Unset, Type824Enum] = UNSET
    cve_id: Union[Unset, None, str] = UNSET
    impact: Union[BlankEnum, ImpactEnum, Unset] = UNSET
    component: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    statement: Union[Unset, str] = UNSET
    cwe_id: Union[Unset, str] = UNSET
    unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET
    source: Union[BlankEnum, Source666Enum, Unset] = UNSET
    reported_dt: Union[Unset, None, datetime.datetime] = UNSET
    mitigation: Union[Unset, str] = UNSET
    cvss2: Union[Unset, str] = UNSET
    cvss2_score: Union[Unset, None, float] = UNSET
    nvd_cvss2: Union[Unset, str] = UNSET
    cvss3: Union[Unset, str] = UNSET
    cvss3_score: Union[Unset, None, float] = UNSET
    nvd_cvss3: Union[Unset, str] = UNSET
    is_major_incident: Union[Unset, bool] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        state = self.state
        resolution = self.resolution
        title = self.title
        trackers: List[str] = UNSET
        if not isinstance(self.trackers, Unset):
            trackers = self.trackers

        description = self.description
        affects: List[Dict[str, Any]] = UNSET
        if not isinstance(self.affects, Unset):
            affects = []
            for affects_item_data in self.affects:
                affects_item: Dict[str, Any] = UNSET
                if not isinstance(affects_item_data, Unset):
                    affects_item = affects_item_data.to_dict()

                affects.append(affects_item)

        meta: List[Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = []
            for meta_item_data in self.meta:
                meta_item: Dict[str, Any] = UNSET
                if not isinstance(meta_item_data, Unset):
                    meta_item = meta_item_data.to_dict()

                meta.append(meta_item)

        comments: List[Dict[str, Any]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item: Dict[str, Any] = UNSET
                if not isinstance(comments_item_data, Unset):
                    comments_item = comments_item_data.to_dict()

                comments.append(comments_item)

        meta_attr: Dict[str, Any] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        package_versions: List[Dict[str, Any]] = UNSET
        if not isinstance(self.package_versions, Unset):
            package_versions = []
            for package_versions_item_data in self.package_versions:
                package_versions_item: Dict[str, Any] = UNSET
                if not isinstance(package_versions_item_data, Unset):
                    package_versions_item = package_versions_item_data.to_dict()

                package_versions.append(package_versions_item)

        embargoed = self.embargoed
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        classification: Dict[str, Any] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):

            type = Type824Enum(self.type).value

        cve_id = self.cve_id
        impact: Union[Unset, str]
        if isinstance(self.impact, Unset):
            impact = UNSET
        elif isinstance(self.impact, ImpactEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):

                impact = ImpactEnum(self.impact).value

        else:
            impact = UNSET
            if not isinstance(self.impact, Unset):

                impact = BlankEnum(self.impact).value

        component = self.component
        summary = self.summary
        statement = self.statement
        cwe_id = self.cwe_id
        unembargo_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.unembargo_dt, Unset):
            unembargo_dt = self.unembargo_dt.isoformat() if self.unembargo_dt else None

        source: Union[Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, Source666Enum):
            source = UNSET
            if not isinstance(self.source, Unset):

                source = Source666Enum(self.source).value

        else:
            source = UNSET
            if not isinstance(self.source, Unset):

                source = BlankEnum(self.source).value

        reported_dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.reported_dt, Unset):
            reported_dt = self.reported_dt.isoformat() if self.reported_dt else None

        mitigation = self.mitigation
        cvss2 = self.cvss2
        cvss2_score = self.cvss2_score
        nvd_cvss2 = self.nvd_cvss2
        cvss3 = self.cvss3
        cvss3_score = self.cvss3_score
        nvd_cvss3 = self.nvd_cvss3
        is_major_incident = self.is_major_incident
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if state is not UNSET:
            field_dict["state"] = state
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if title is not UNSET:
            field_dict["title"] = title
        if trackers is not UNSET:
            field_dict["trackers"] = trackers
        if description is not UNSET:
            field_dict["description"] = description
        if affects is not UNSET:
            field_dict["affects"] = affects
        if meta is not UNSET:
            field_dict["meta"] = meta
        if comments is not UNSET:
            field_dict["comments"] = comments
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr
        if package_versions is not UNSET:
            field_dict["package_versions"] = package_versions
        if embargoed is not UNSET:
            field_dict["embargoed"] = embargoed
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if updated_dt is not UNSET:
            field_dict["updated_dt"] = updated_dt
        if classification is not UNSET:
            field_dict["classification"] = classification
        if type is not UNSET:
            field_dict["type"] = type
        if cve_id is not UNSET:
            field_dict["cve_id"] = cve_id
        if impact is not UNSET:
            field_dict["impact"] = impact
        if component is not UNSET:
            field_dict["component"] = component
        if summary is not UNSET:
            field_dict["summary"] = summary
        if statement is not UNSET:
            field_dict["statement"] = statement
        if cwe_id is not UNSET:
            field_dict["cwe_id"] = cwe_id
        if unembargo_dt is not UNSET:
            field_dict["unembargo_dt"] = unembargo_dt
        if source is not UNSET:
            field_dict["source"] = source
        if reported_dt is not UNSET:
            field_dict["reported_dt"] = reported_dt
        if mitigation is not UNSET:
            field_dict["mitigation"] = mitigation
        if cvss2 is not UNSET:
            field_dict["cvss2"] = cvss2
        if cvss2_score is not UNSET:
            field_dict["cvss2_score"] = cvss2_score
        if nvd_cvss2 is not UNSET:
            field_dict["nvd_cvss2"] = nvd_cvss2
        if cvss3 is not UNSET:
            field_dict["cvss3"] = cvss3
        if cvss3_score is not UNSET:
            field_dict["cvss3_score"] = cvss3_score
        if nvd_cvss3 is not UNSET:
            field_dict["nvd_cvss3"] = nvd_cvss3
        if is_major_incident is not UNSET:
            field_dict["is_major_incident"] = is_major_incident
        if dt is not UNSET:
            field_dict["dt"] = dt
        if env is not UNSET:
            field_dict["env"] = env
        if revision is not UNSET:
            field_dict["revision"] = revision
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        state = d.pop("state", UNSET)

        resolution = d.pop("resolution", UNSET)

        title = d.pop("title", UNSET)

        trackers = cast(List[str], d.pop("trackers", UNSET))

        description = d.pop("description", UNSET)

        affects = []
        _affects = d.pop("affects", UNSET)
        if _affects is UNSET:
            affects = UNSET
        else:
            for affects_item_data in _affects or []:
                _affects_item = affects_item_data
                affects_item: Affect
                if isinstance(_affects_item, Unset):
                    affects_item = UNSET
                else:
                    affects_item = Affect.from_dict(_affects_item)

                affects.append(affects_item)

        meta = []
        _meta = d.pop("meta", UNSET)
        if _meta is UNSET:
            meta = UNSET
        else:
            for meta_item_data in _meta or []:
                _meta_item = meta_item_data
                meta_item: Meta
                if isinstance(_meta_item, Unset):
                    meta_item = UNSET
                else:
                    meta_item = Meta.from_dict(_meta_item)

                meta.append(meta_item)

        comments = []
        _comments = d.pop("comments", UNSET)
        if _comments is UNSET:
            comments = UNSET
        else:
            for comments_item_data in _comments or []:
                _comments_item = comments_item_data
                comments_item: Comment
                if isinstance(_comments_item, Unset):
                    comments_item = UNSET
                else:
                    comments_item = Comment.from_dict(_comments_item)

                comments.append(comments_item)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: FlawMetaAttr
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = FlawMetaAttr.from_dict(_meta_attr)

        package_versions = []
        _package_versions = d.pop("package_versions", UNSET)
        if _package_versions is UNSET:
            package_versions = UNSET
        else:
            for package_versions_item_data in _package_versions or []:
                _package_versions_item = package_versions_item_data
                package_versions_item: CVEv5PackageVersions
                if isinstance(_package_versions_item, Unset):
                    package_versions_item = UNSET
                else:
                    package_versions_item = CVEv5PackageVersions.from_dict(
                        _package_versions_item
                    )

                package_versions.append(package_versions_item)

        embargoed = d.pop("embargoed", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        _classification = d.pop("classification", UNSET)
        classification: FlawClassification
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = FlawClassification.from_dict(_classification)

        _type = d.pop("type", UNSET)
        type: Union[Unset, Type824Enum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = Type824Enum(_type)

        cve_id = d.pop("cve_id", UNSET)

        def _parse_impact(data: object) -> Union[BlankEnum, ImpactEnum, Unset]:
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
            if not isinstance(data, str):
                raise TypeError()
            _impact_type_1 = data
            impact_type_1: Union[Unset, BlankEnum]
            if isinstance(_impact_type_1, Unset):
                impact_type_1 = UNSET
            else:
                impact_type_1 = BlankEnum(_impact_type_1)

            return impact_type_1

        impact = _parse_impact(d.pop("impact", UNSET))

        component = d.pop("component", UNSET)

        summary = d.pop("summary", UNSET)

        statement = d.pop("statement", UNSET)

        cwe_id = d.pop("cwe_id", UNSET)

        _unembargo_dt = d.pop("unembargo_dt", UNSET)
        unembargo_dt: Union[Unset, None, datetime.datetime]
        if _unembargo_dt is None:
            unembargo_dt = None
        elif isinstance(_unembargo_dt, Unset):
            unembargo_dt = UNSET
        else:
            unembargo_dt = isoparse(_unembargo_dt)

        def _parse_source(data: object) -> Union[BlankEnum, Source666Enum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _source_type_0 = data
                source_type_0: Union[Unset, Source666Enum]
                if isinstance(_source_type_0, Unset):
                    source_type_0 = UNSET
                else:
                    source_type_0 = Source666Enum(_source_type_0)

                return source_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _source_type_1 = data
            source_type_1: Union[Unset, BlankEnum]
            if isinstance(_source_type_1, Unset):
                source_type_1 = UNSET
            else:
                source_type_1 = BlankEnum(_source_type_1)

            return source_type_1

        source = _parse_source(d.pop("source", UNSET))

        _reported_dt = d.pop("reported_dt", UNSET)
        reported_dt: Union[Unset, None, datetime.datetime]
        if _reported_dt is None:
            reported_dt = None
        elif isinstance(_reported_dt, Unset):
            reported_dt = UNSET
        else:
            reported_dt = isoparse(_reported_dt)

        mitigation = d.pop("mitigation", UNSET)

        cvss2 = d.pop("cvss2", UNSET)

        cvss2_score = d.pop("cvss2_score", UNSET)

        nvd_cvss2 = d.pop("nvd_cvss2", UNSET)

        cvss3 = d.pop("cvss3", UNSET)

        cvss3_score = d.pop("cvss3_score", UNSET)

        nvd_cvss3 = d.pop("nvd_cvss3", UNSET)

        is_major_incident = d.pop("is_major_incident", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_flaws_retrieve_response_200 = cls(
            uuid=uuid,
            state=state,
            resolution=resolution,
            title=title,
            trackers=trackers,
            description=description,
            affects=affects,
            meta=meta,
            comments=comments,
            meta_attr=meta_attr,
            package_versions=package_versions,
            embargoed=embargoed,
            created_dt=created_dt,
            updated_dt=updated_dt,
            classification=classification,
            type=type,
            cve_id=cve_id,
            impact=impact,
            component=component,
            summary=summary,
            statement=statement,
            cwe_id=cwe_id,
            unembargo_dt=unembargo_dt,
            source=source,
            reported_dt=reported_dt,
            mitigation=mitigation,
            cvss2=cvss2,
            cvss2_score=cvss2_score,
            nvd_cvss2=nvd_cvss2,
            cvss3=cvss3,
            cvss3_score=cvss3_score,
            nvd_cvss3=nvd_cvss3,
            is_major_incident=is_major_incident,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_flaws_retrieve_response_200.additional_properties = d
        return osidb_api_v1_flaws_retrieve_response_200

    @staticmethod
    def get_fields():
        return {
            "uuid": str,
            "state": str,
            "resolution": str,
            "title": str,
            "trackers": List[str],
            "description": str,
            "affects": List[Affect],
            "meta": List[Meta],
            "comments": List[Comment],
            "meta_attr": FlawMetaAttr,
            "package_versions": List[CVEv5PackageVersions],
            "embargoed": bool,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "classification": FlawClassification,
            "type": Type824Enum,
            "cve_id": str,
            "impact": Union[BlankEnum, ImpactEnum],
            "component": str,
            "summary": str,
            "statement": str,
            "cwe_id": str,
            "unembargo_dt": datetime.datetime,
            "source": Union[BlankEnum, Source666Enum],
            "reported_dt": datetime.datetime,
            "mitigation": str,
            "cvss2": str,
            "cvss2_score": float,
            "nvd_cvss2": str,
            "cvss3": str,
            "cvss3_score": float,
            "nvd_cvss3": str,
            "is_major_incident": bool,
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
