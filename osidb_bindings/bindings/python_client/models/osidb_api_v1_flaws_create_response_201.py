import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.impact_enum import ImpactEnum
from ..models.major_incident_state_enum import MajorIncidentStateEnum
from ..models.nist_cvss_validation_enum import NistCvssValidationEnum
from ..models.requires_cve_description_enum import RequiresCveDescriptionEnum
from ..models.source_be_0_enum import SourceBe0Enum
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.affect import Affect
    from ..models.alert import Alert
    from ..models.comment import Comment
    from ..models.flaw_acknowledgment import FlawAcknowledgment
    from ..models.flaw_classification import FlawClassification
    from ..models.flaw_cvss import FlawCVSS
    from ..models.flaw_reference import FlawReference
    from ..models.package import Package


T = TypeVar("T", bound="OsidbApiV1FlawsCreateResponse201")


@_attrs_define
class OsidbApiV1FlawsCreateResponse201(OSIDBModel):
    """
    Attributes:
        uuid (UUID):
        title (str):
        trackers (list[str]):
        comment_zero (str):
        affects (list['Affect']):
        comments (list['Comment']):
        package_versions (list['Package']):
        acknowledgments (list['FlawAcknowledgment']):
        references (list['FlawReference']):
        cvss_scores (list['FlawCVSS']):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        classification (FlawClassification):
        alerts (list['Alert']):
        cve_id (Union[None, Unset, str]):
        impact (Union[BlankEnum, ImpactEnum, Unset]):
        components (Union[Unset, list[str]]):
        cve_description (Union[Unset, str]):
        requires_cve_description (Union[BlankEnum, RequiresCveDescriptionEnum, Unset]):
        statement (Union[Unset, str]):
        cwe_id (Union[Unset, str]):
        unembargo_dt (Union[None, Unset, datetime.datetime]):
        source (Union[BlankEnum, SourceBe0Enum, Unset]):
        reported_dt (Union[None, Unset, datetime.datetime]):
        mitigation (Union[Unset, str]):
        major_incident_state (Union[BlankEnum, MajorIncidentStateEnum, Unset]):
        major_incident_start_dt (Union[None, Unset, datetime.datetime]):
        nist_cvss_validation (Union[BlankEnum, NistCvssValidationEnum, Unset]):
        group_key (Union[Unset, str]):
        owner (Union[Unset, str]):
        task_key (Union[Unset, str]):
        team_id (Union[Unset, str]):
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    uuid: UUID
    title: str
    trackers: list[str]
    comment_zero: str
    affects: list["Affect"]
    comments: list["Comment"]
    package_versions: list["Package"]
    acknowledgments: list["FlawAcknowledgment"]
    references: list["FlawReference"]
    cvss_scores: list["FlawCVSS"]
    embargoed: bool
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    classification: "FlawClassification"
    alerts: list["Alert"]
    cve_id: Union[None, Unset, str] = UNSET
    impact: Union[BlankEnum, ImpactEnum, Unset] = UNSET
    components: Union[Unset, list[str]] = UNSET
    cve_description: Union[Unset, str] = UNSET
    requires_cve_description: Union[BlankEnum, RequiresCveDescriptionEnum, Unset] = (
        UNSET
    )
    statement: Union[Unset, str] = UNSET
    cwe_id: Union[Unset, str] = UNSET
    unembargo_dt: Union[None, Unset, datetime.datetime] = UNSET
    source: Union[BlankEnum, SourceBe0Enum, Unset] = UNSET
    reported_dt: Union[None, Unset, datetime.datetime] = UNSET
    mitigation: Union[Unset, str] = UNSET
    major_incident_state: Union[BlankEnum, MajorIncidentStateEnum, Unset] = UNSET
    major_incident_start_dt: Union[None, Unset, datetime.datetime] = UNSET
    nist_cvss_validation: Union[BlankEnum, NistCvssValidationEnum, Unset] = UNSET
    group_key: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    task_key: Union[Unset, str] = UNSET
    team_id: Union[Unset, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        title = self.title

        trackers: list[str] = UNSET
        if not isinstance(self.trackers, Unset):
            trackers = self.trackers

        comment_zero = self.comment_zero

        affects: list[dict[str, Any]] = UNSET
        if not isinstance(self.affects, Unset):
            affects = []
            for affects_item_data in self.affects:
                affects_item: dict[str, Any] = UNSET
                if not isinstance(affects_item_data, Unset):
                    affects_item = affects_item_data.to_dict()

                affects.append(affects_item)

        comments: list[dict[str, Any]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item: dict[str, Any] = UNSET
                if not isinstance(comments_item_data, Unset):
                    comments_item = comments_item_data.to_dict()

                comments.append(comments_item)

        package_versions: list[dict[str, Any]] = UNSET
        if not isinstance(self.package_versions, Unset):
            package_versions = []
            for package_versions_item_data in self.package_versions:
                package_versions_item: dict[str, Any] = UNSET
                if not isinstance(package_versions_item_data, Unset):
                    package_versions_item = package_versions_item_data.to_dict()

                package_versions.append(package_versions_item)

        acknowledgments: list[dict[str, Any]] = UNSET
        if not isinstance(self.acknowledgments, Unset):
            acknowledgments = []
            for acknowledgments_item_data in self.acknowledgments:
                acknowledgments_item: dict[str, Any] = UNSET
                if not isinstance(acknowledgments_item_data, Unset):
                    acknowledgments_item = acknowledgments_item_data.to_dict()

                acknowledgments.append(acknowledgments_item)

        references: list[dict[str, Any]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item: dict[str, Any] = UNSET
                if not isinstance(references_item_data, Unset):
                    references_item = references_item_data.to_dict()

                references.append(references_item)

        cvss_scores: list[dict[str, Any]] = UNSET
        if not isinstance(self.cvss_scores, Unset):
            cvss_scores = []
            for cvss_scores_item_data in self.cvss_scores:
                cvss_scores_item: dict[str, Any] = UNSET
                if not isinstance(cvss_scores_item_data, Unset):
                    cvss_scores_item = cvss_scores_item_data.to_dict()

                cvss_scores.append(cvss_scores_item)

        embargoed = self.embargoed

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        classification: dict[str, Any] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification.to_dict()

        alerts: list[dict[str, Any]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                alerts.append(alerts_item)

        cve_id: Union[None, Unset, str]
        if isinstance(self.cve_id, Unset):
            cve_id = UNSET
        else:
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

        components: Union[Unset, list[str]] = UNSET
        if not isinstance(self.components, Unset):
            components = self.components

        cve_description = self.cve_description

        requires_cve_description: Union[Unset, str]
        if isinstance(self.requires_cve_description, Unset):
            requires_cve_description = UNSET
        elif isinstance(self.requires_cve_description, RequiresCveDescriptionEnum):
            requires_cve_description = UNSET
            if not isinstance(self.requires_cve_description, Unset):
                requires_cve_description = RequiresCveDescriptionEnum(
                    self.requires_cve_description
                ).value

        else:
            requires_cve_description = UNSET
            if not isinstance(self.requires_cve_description, Unset):
                requires_cve_description = BlankEnum(
                    self.requires_cve_description
                ).value

        statement = self.statement

        cwe_id = self.cwe_id

        unembargo_dt: Union[None, Unset, str]
        if isinstance(self.unembargo_dt, Unset):
            unembargo_dt = UNSET
        elif isinstance(self.unembargo_dt, datetime.datetime):
            unembargo_dt = UNSET
            if not isinstance(self.unembargo_dt, Unset):
                unembargo_dt = self.unembargo_dt.isoformat()

        else:
            unembargo_dt = self.unembargo_dt

        source: Union[Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, SourceBe0Enum):
            source = UNSET
            if not isinstance(self.source, Unset):
                source = SourceBe0Enum(self.source).value

        else:
            source = UNSET
            if not isinstance(self.source, Unset):
                source = BlankEnum(self.source).value

        reported_dt: Union[None, Unset, str]
        if isinstance(self.reported_dt, Unset):
            reported_dt = UNSET
        elif isinstance(self.reported_dt, datetime.datetime):
            reported_dt = UNSET
            if not isinstance(self.reported_dt, Unset):
                reported_dt = self.reported_dt.isoformat()

        else:
            reported_dt = self.reported_dt

        mitigation = self.mitigation

        major_incident_state: Union[Unset, str]
        if isinstance(self.major_incident_state, Unset):
            major_incident_state = UNSET
        elif isinstance(self.major_incident_state, MajorIncidentStateEnum):
            major_incident_state = UNSET
            if not isinstance(self.major_incident_state, Unset):
                major_incident_state = MajorIncidentStateEnum(
                    self.major_incident_state
                ).value

        else:
            major_incident_state = UNSET
            if not isinstance(self.major_incident_state, Unset):
                major_incident_state = BlankEnum(self.major_incident_state).value

        major_incident_start_dt: Union[None, Unset, str]
        if isinstance(self.major_incident_start_dt, Unset):
            major_incident_start_dt = UNSET
        elif isinstance(self.major_incident_start_dt, datetime.datetime):
            major_incident_start_dt = UNSET
            if not isinstance(self.major_incident_start_dt, Unset):
                major_incident_start_dt = self.major_incident_start_dt.isoformat()

        else:
            major_incident_start_dt = self.major_incident_start_dt

        nist_cvss_validation: Union[Unset, str]
        if isinstance(self.nist_cvss_validation, Unset):
            nist_cvss_validation = UNSET
        elif isinstance(self.nist_cvss_validation, NistCvssValidationEnum):
            nist_cvss_validation = UNSET
            if not isinstance(self.nist_cvss_validation, Unset):
                nist_cvss_validation = NistCvssValidationEnum(
                    self.nist_cvss_validation
                ).value

        else:
            nist_cvss_validation = UNSET
            if not isinstance(self.nist_cvss_validation, Unset):
                nist_cvss_validation = BlankEnum(self.nist_cvss_validation).value

        group_key = self.group_key

        owner = self.owner

        task_key = self.task_key

        team_id = self.team_id

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(title, Unset):
            field_dict["title"] = title
        if not isinstance(trackers, Unset):
            field_dict["trackers"] = trackers
        if not isinstance(comment_zero, Unset):
            field_dict["comment_zero"] = comment_zero
        if not isinstance(affects, Unset):
            field_dict["affects"] = affects
        if not isinstance(comments, Unset):
            field_dict["comments"] = comments
        if not isinstance(package_versions, Unset):
            field_dict["package_versions"] = package_versions
        if not isinstance(acknowledgments, Unset):
            field_dict["acknowledgments"] = acknowledgments
        if not isinstance(references, Unset):
            field_dict["references"] = references
        if not isinstance(cvss_scores, Unset):
            field_dict["cvss_scores"] = cvss_scores
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(classification, Unset):
            field_dict["classification"] = classification
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(cve_id, Unset):
            field_dict["cve_id"] = cve_id
        if not isinstance(impact, Unset):
            field_dict["impact"] = impact
        if not isinstance(components, Unset):
            field_dict["components"] = components
        if not isinstance(cve_description, Unset):
            field_dict["cve_description"] = cve_description
        if not isinstance(requires_cve_description, Unset):
            field_dict["requires_cve_description"] = requires_cve_description
        if not isinstance(statement, Unset):
            field_dict["statement"] = statement
        if not isinstance(cwe_id, Unset):
            field_dict["cwe_id"] = cwe_id
        if not isinstance(unembargo_dt, Unset):
            field_dict["unembargo_dt"] = unembargo_dt
        if not isinstance(source, Unset):
            field_dict["source"] = source
        if not isinstance(reported_dt, Unset):
            field_dict["reported_dt"] = reported_dt
        if not isinstance(mitigation, Unset):
            field_dict["mitigation"] = mitigation
        if not isinstance(major_incident_state, Unset):
            field_dict["major_incident_state"] = major_incident_state
        if not isinstance(major_incident_start_dt, Unset):
            field_dict["major_incident_start_dt"] = major_incident_start_dt
        if not isinstance(nist_cvss_validation, Unset):
            field_dict["nist_cvss_validation"] = nist_cvss_validation
        if not isinstance(group_key, Unset):
            field_dict["group_key"] = group_key
        if not isinstance(owner, Unset):
            field_dict["owner"] = owner
        if not isinstance(task_key, Unset):
            field_dict["task_key"] = task_key
        if not isinstance(team_id, Unset):
            field_dict["team_id"] = team_id
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.affect import Affect
        from ..models.alert import Alert
        from ..models.comment import Comment
        from ..models.flaw_acknowledgment import FlawAcknowledgment
        from ..models.flaw_classification import FlawClassification
        from ..models.flaw_cvss import FlawCVSS
        from ..models.flaw_reference import FlawReference
        from ..models.package import Package

        d = src_dict.copy()
        # }
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        title = d.pop("title", UNSET)

        trackers = cast(list[str], d.pop("trackers", UNSET))

        comment_zero = d.pop("comment_zero", UNSET)

        affects = []
        _affects = d.pop("affects", UNSET)
        for affects_item_data in _affects or []:
            # }
            _affects_item = affects_item_data
            affects_item: Affect
            if isinstance(_affects_item, Unset):
                affects_item = UNSET
            else:
                affects_item = Affect.from_dict(_affects_item)

            affects.append(affects_item)

        comments = []
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            # }
            _comments_item = comments_item_data
            comments_item: Comment
            if isinstance(_comments_item, Unset):
                comments_item = UNSET
            else:
                comments_item = Comment.from_dict(_comments_item)

            comments.append(comments_item)

        package_versions = []
        _package_versions = d.pop("package_versions", UNSET)
        for package_versions_item_data in _package_versions or []:
            # }
            _package_versions_item = package_versions_item_data
            package_versions_item: Package
            if isinstance(_package_versions_item, Unset):
                package_versions_item = UNSET
            else:
                package_versions_item = Package.from_dict(_package_versions_item)

            package_versions.append(package_versions_item)

        acknowledgments = []
        _acknowledgments = d.pop("acknowledgments", UNSET)
        for acknowledgments_item_data in _acknowledgments or []:
            # }
            _acknowledgments_item = acknowledgments_item_data
            acknowledgments_item: FlawAcknowledgment
            if isinstance(_acknowledgments_item, Unset):
                acknowledgments_item = UNSET
            else:
                acknowledgments_item = FlawAcknowledgment.from_dict(
                    _acknowledgments_item
                )

            acknowledgments.append(acknowledgments_item)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            # }
            _references_item = references_item_data
            references_item: FlawReference
            if isinstance(_references_item, Unset):
                references_item = UNSET
            else:
                references_item = FlawReference.from_dict(_references_item)

            references.append(references_item)

        cvss_scores = []
        _cvss_scores = d.pop("cvss_scores", UNSET)
        for cvss_scores_item_data in _cvss_scores or []:
            # }
            _cvss_scores_item = cvss_scores_item_data
            cvss_scores_item: FlawCVSS
            if isinstance(_cvss_scores_item, Unset):
                cvss_scores_item = UNSET
            else:
                cvss_scores_item = FlawCVSS.from_dict(_cvss_scores_item)

            cvss_scores.append(cvss_scores_item)

        embargoed = d.pop("embargoed", UNSET)

        # }
        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = isoparse(_created_dt)

        # }
        _updated_dt = d.pop("updated_dt", UNSET)
        updated_dt: datetime.datetime
        if isinstance(_updated_dt, Unset):
            updated_dt = UNSET
        else:
            updated_dt = isoparse(_updated_dt)

        # }
        _classification = d.pop("classification", UNSET)
        classification: FlawClassification
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = FlawClassification.from_dict(_classification)

        alerts = []
        _alerts = d.pop("alerts", UNSET)
        for alerts_item_data in _alerts or []:
            # }
            _alerts_item = alerts_item_data
            alerts_item: Alert
            if isinstance(_alerts_item, Unset):
                alerts_item = UNSET
            else:
                alerts_item = Alert.from_dict(_alerts_item)

            alerts.append(alerts_item)

        def _parse_cve_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cve_id = _parse_cve_id(d.pop("cve_id", UNSET))

        def _parse_impact(data: object) -> Union[BlankEnum, ImpactEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
                _impact_type_0 = data
                impact_type_0: ImpactEnum
                if isinstance(_impact_type_0, Unset):
                    impact_type_0 = UNSET
                else:
                    impact_type_0 = ImpactEnum(_impact_type_0)

                return impact_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            # }
            _impact_type_1 = data
            impact_type_1: BlankEnum
            if isinstance(_impact_type_1, Unset):
                impact_type_1 = UNSET
            else:
                impact_type_1 = BlankEnum(_impact_type_1)

            return impact_type_1

        impact = _parse_impact(d.pop("impact", UNSET))

        components = cast(list[str], d.pop("components", UNSET))

        cve_description = d.pop("cve_description", UNSET)

        def _parse_requires_cve_description(
            data: object,
        ) -> Union[BlankEnum, RequiresCveDescriptionEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
                _requires_cve_description_type_0 = data
                requires_cve_description_type_0: RequiresCveDescriptionEnum
                if isinstance(_requires_cve_description_type_0, Unset):
                    requires_cve_description_type_0 = UNSET
                else:
                    requires_cve_description_type_0 = RequiresCveDescriptionEnum(
                        _requires_cve_description_type_0
                    )

                return requires_cve_description_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            # }
            _requires_cve_description_type_1 = data
            requires_cve_description_type_1: BlankEnum
            if isinstance(_requires_cve_description_type_1, Unset):
                requires_cve_description_type_1 = UNSET
            else:
                requires_cve_description_type_1 = BlankEnum(
                    _requires_cve_description_type_1
                )

            return requires_cve_description_type_1

        requires_cve_description = _parse_requires_cve_description(
            d.pop("requires_cve_description", UNSET)
        )

        statement = d.pop("statement", UNSET)

        cwe_id = d.pop("cwe_id", UNSET)

        def _parse_unembargo_dt(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
                _unembargo_dt_type_0 = data
                unembargo_dt_type_0: datetime.datetime
                if isinstance(_unembargo_dt_type_0, Unset):
                    unembargo_dt_type_0 = UNSET
                else:
                    unembargo_dt_type_0 = isoparse(_unembargo_dt_type_0)

                return unembargo_dt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        unembargo_dt = _parse_unembargo_dt(d.pop("unembargo_dt", UNSET))

        def _parse_source(data: object) -> Union[BlankEnum, SourceBe0Enum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
                _source_type_0 = data
                source_type_0: SourceBe0Enum
                if isinstance(_source_type_0, Unset):
                    source_type_0 = UNSET
                else:
                    source_type_0 = SourceBe0Enum(_source_type_0)

                return source_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            # }
            _source_type_1 = data
            source_type_1: BlankEnum
            if isinstance(_source_type_1, Unset):
                source_type_1 = UNSET
            else:
                source_type_1 = BlankEnum(_source_type_1)

            return source_type_1

        source = _parse_source(d.pop("source", UNSET))

        def _parse_reported_dt(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
                _reported_dt_type_0 = data
                reported_dt_type_0: datetime.datetime
                if isinstance(_reported_dt_type_0, Unset):
                    reported_dt_type_0 = UNSET
                else:
                    reported_dt_type_0 = isoparse(_reported_dt_type_0)

                return reported_dt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        reported_dt = _parse_reported_dt(d.pop("reported_dt", UNSET))

        mitigation = d.pop("mitigation", UNSET)

        def _parse_major_incident_state(
            data: object,
        ) -> Union[BlankEnum, MajorIncidentStateEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
                _major_incident_state_type_0 = data
                major_incident_state_type_0: MajorIncidentStateEnum
                if isinstance(_major_incident_state_type_0, Unset):
                    major_incident_state_type_0 = UNSET
                else:
                    major_incident_state_type_0 = MajorIncidentStateEnum(
                        _major_incident_state_type_0
                    )

                return major_incident_state_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            # }
            _major_incident_state_type_1 = data
            major_incident_state_type_1: BlankEnum
            if isinstance(_major_incident_state_type_1, Unset):
                major_incident_state_type_1 = UNSET
            else:
                major_incident_state_type_1 = BlankEnum(_major_incident_state_type_1)

            return major_incident_state_type_1

        major_incident_state = _parse_major_incident_state(
            d.pop("major_incident_state", UNSET)
        )

        def _parse_major_incident_start_dt(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
                _major_incident_start_dt_type_0 = data
                major_incident_start_dt_type_0: datetime.datetime
                if isinstance(_major_incident_start_dt_type_0, Unset):
                    major_incident_start_dt_type_0 = UNSET
                else:
                    major_incident_start_dt_type_0 = isoparse(
                        _major_incident_start_dt_type_0
                    )

                return major_incident_start_dt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        major_incident_start_dt = _parse_major_incident_start_dt(
            d.pop("major_incident_start_dt", UNSET)
        )

        def _parse_nist_cvss_validation(
            data: object,
        ) -> Union[BlankEnum, NistCvssValidationEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
                _nist_cvss_validation_type_0 = data
                nist_cvss_validation_type_0: NistCvssValidationEnum
                if isinstance(_nist_cvss_validation_type_0, Unset):
                    nist_cvss_validation_type_0 = UNSET
                else:
                    nist_cvss_validation_type_0 = NistCvssValidationEnum(
                        _nist_cvss_validation_type_0
                    )

                return nist_cvss_validation_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            # }
            _nist_cvss_validation_type_1 = data
            nist_cvss_validation_type_1: BlankEnum
            if isinstance(_nist_cvss_validation_type_1, Unset):
                nist_cvss_validation_type_1 = UNSET
            else:
                nist_cvss_validation_type_1 = BlankEnum(_nist_cvss_validation_type_1)

            return nist_cvss_validation_type_1

        nist_cvss_validation = _parse_nist_cvss_validation(
            d.pop("nist_cvss_validation", UNSET)
        )

        group_key = d.pop("group_key", UNSET)

        owner = d.pop("owner", UNSET)

        task_key = d.pop("task_key", UNSET)

        team_id = d.pop("team_id", UNSET)

        # }
        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_flaws_create_response_201 = cls(
            uuid=uuid,
            title=title,
            trackers=trackers,
            comment_zero=comment_zero,
            affects=affects,
            comments=comments,
            package_versions=package_versions,
            acknowledgments=acknowledgments,
            references=references,
            cvss_scores=cvss_scores,
            embargoed=embargoed,
            created_dt=created_dt,
            updated_dt=updated_dt,
            classification=classification,
            alerts=alerts,
            cve_id=cve_id,
            impact=impact,
            components=components,
            cve_description=cve_description,
            requires_cve_description=requires_cve_description,
            statement=statement,
            cwe_id=cwe_id,
            unembargo_dt=unembargo_dt,
            source=source,
            reported_dt=reported_dt,
            mitigation=mitigation,
            major_incident_state=major_incident_state,
            major_incident_start_dt=major_incident_start_dt,
            nist_cvss_validation=nist_cvss_validation,
            group_key=group_key,
            owner=owner,
            task_key=task_key,
            team_id=team_id,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_flaws_create_response_201.additional_properties = d
        return osidb_api_v1_flaws_create_response_201

    @staticmethod
    def get_fields():
        return {
            "uuid": UUID,
            "title": str,
            "trackers": list[str],
            "comment_zero": str,
            "affects": list["Affect"],
            "comments": list["Comment"],
            "package_versions": list["Package"],
            "acknowledgments": list["FlawAcknowledgment"],
            "references": list["FlawReference"],
            "cvss_scores": list["FlawCVSS"],
            "embargoed": bool,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "classification": FlawClassification,
            "alerts": list["Alert"],
            "cve_id": Union[None, str],
            "impact": Union[BlankEnum, ImpactEnum],
            "components": list[str],
            "cve_description": str,
            "requires_cve_description": Union[BlankEnum, RequiresCveDescriptionEnum],
            "statement": str,
            "cwe_id": str,
            "unembargo_dt": Union[None, datetime.datetime],
            "source": Union[BlankEnum, SourceBe0Enum],
            "reported_dt": Union[None, datetime.datetime],
            "mitigation": str,
            "major_incident_state": Union[BlankEnum, MajorIncidentStateEnum],
            "major_incident_start_dt": Union[None, datetime.datetime],
            "nist_cvss_validation": Union[BlankEnum, NistCvssValidationEnum],
            "group_key": str,
            "owner": str,
            "task_key": str,
            "team_id": str,
            "dt": datetime.datetime,
            "env": str,
            "revision": str,
            "version": str,
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
