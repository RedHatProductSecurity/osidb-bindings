import datetime
import json
from typing import Any, TypeVar, Union, cast

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

T = TypeVar("T", bound="FlawPostRequest")


@_attrs_define
class FlawPostRequest(OSIDBModel):
    """serialize flaw model

    Attributes:
        title (str):
        comment_zero (str):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
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
        team_id (Union[Unset, str]):
    """

    title: str
    comment_zero: str
    embargoed: bool
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
    team_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        comment_zero = self.comment_zero

        embargoed = self.embargoed

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

        team_id = self.team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(title, Unset):
            field_dict["title"] = title
        if not isinstance(comment_zero, Unset):
            field_dict["comment_zero"] = comment_zero
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
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
        if not isinstance(team_id, Unset):
            field_dict["team_id"] = team_id

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        title = (None, str(self.title).encode(), "text/plain")

        comment_zero = (None, str(self.comment_zero).encode(), "text/plain")

        embargoed = (None, str(self.embargoed).encode(), "text/plain")

        cve_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.cve_id, Unset):
            cve_id = UNSET
        elif isinstance(self.cve_id, str):
            cve_id = (None, str(self.cve_id).encode(), "text/plain")
        else:
            cve_id = (None, str(self.cve_id).encode(), "text/plain")

        impact: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.impact, Unset):
            impact = UNSET
        elif isinstance(self.impact, ImpactEnum):
            impact: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.impact, Unset):
                impact = (None, str(self.impact.value).encode(), "text/plain")
        else:
            impact: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.impact, Unset):
                impact = (None, str(self.impact.value).encode(), "text/plain")

        components: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.components, Unset):
            _temp_components = self.components
            components = (
                None,
                json.dumps(_temp_components).encode(),
                "application/json",
            )

        cve_description = (
            self.cve_description
            if isinstance(self.cve_description, Unset)
            else (None, str(self.cve_description).encode(), "text/plain")
        )

        requires_cve_description: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.requires_cve_description, Unset):
            requires_cve_description = UNSET
        elif isinstance(self.requires_cve_description, RequiresCveDescriptionEnum):
            requires_cve_description: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.requires_cve_description, Unset):
                requires_cve_description = (
                    None,
                    str(self.requires_cve_description.value).encode(),
                    "text/plain",
                )
        else:
            requires_cve_description: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.requires_cve_description, Unset):
                requires_cve_description = (
                    None,
                    str(self.requires_cve_description.value).encode(),
                    "text/plain",
                )

        statement = (
            self.statement
            if isinstance(self.statement, Unset)
            else (None, str(self.statement).encode(), "text/plain")
        )

        cwe_id = (
            self.cwe_id
            if isinstance(self.cwe_id, Unset)
            else (None, str(self.cwe_id).encode(), "text/plain")
        )

        unembargo_dt: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.unembargo_dt, Unset):
            unembargo_dt = UNSET
        elif isinstance(self.unembargo_dt, datetime.datetime):
            unembargo_dt: bytes = UNSET
            if not isinstance(self.unembargo_dt, Unset):
                unembargo_dt = self.unembargo_dt.isoformat().encode()
        else:
            unembargo_dt = (None, str(self.unembargo_dt).encode(), "text/plain")

        source: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, SourceBe0Enum):
            source: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.source, Unset):
                source = (None, str(self.source.value).encode(), "text/plain")
        else:
            source: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.source, Unset):
                source = (None, str(self.source.value).encode(), "text/plain")

        reported_dt: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.reported_dt, Unset):
            reported_dt = UNSET
        elif isinstance(self.reported_dt, datetime.datetime):
            reported_dt: bytes = UNSET
            if not isinstance(self.reported_dt, Unset):
                reported_dt = self.reported_dt.isoformat().encode()
        else:
            reported_dt = (None, str(self.reported_dt).encode(), "text/plain")

        mitigation = (
            self.mitigation
            if isinstance(self.mitigation, Unset)
            else (None, str(self.mitigation).encode(), "text/plain")
        )

        major_incident_state: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.major_incident_state, Unset):
            major_incident_state = UNSET
        elif isinstance(self.major_incident_state, MajorIncidentStateEnum):
            major_incident_state: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.major_incident_state, Unset):
                major_incident_state = (
                    None,
                    str(self.major_incident_state.value).encode(),
                    "text/plain",
                )
        else:
            major_incident_state: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.major_incident_state, Unset):
                major_incident_state = (
                    None,
                    str(self.major_incident_state.value).encode(),
                    "text/plain",
                )

        major_incident_start_dt: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.major_incident_start_dt, Unset):
            major_incident_start_dt = UNSET
        elif isinstance(self.major_incident_start_dt, datetime.datetime):
            major_incident_start_dt: bytes = UNSET
            if not isinstance(self.major_incident_start_dt, Unset):
                major_incident_start_dt = (
                    self.major_incident_start_dt.isoformat().encode()
                )
        else:
            major_incident_start_dt = (
                None,
                str(self.major_incident_start_dt).encode(),
                "text/plain",
            )

        nist_cvss_validation: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.nist_cvss_validation, Unset):
            nist_cvss_validation = UNSET
        elif isinstance(self.nist_cvss_validation, NistCvssValidationEnum):
            nist_cvss_validation: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.nist_cvss_validation, Unset):
                nist_cvss_validation = (
                    None,
                    str(self.nist_cvss_validation.value).encode(),
                    "text/plain",
                )
        else:
            nist_cvss_validation: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.nist_cvss_validation, Unset):
                nist_cvss_validation = (
                    None,
                    str(self.nist_cvss_validation.value).encode(),
                    "text/plain",
                )

        group_key = (
            self.group_key
            if isinstance(self.group_key, Unset)
            else (None, str(self.group_key).encode(), "text/plain")
        )

        owner = (
            self.owner
            if isinstance(self.owner, Unset)
            else (None, str(self.owner).encode(), "text/plain")
        )

        team_id = (
            self.team_id
            if isinstance(self.team_id, Unset)
            else (None, str(self.team_id).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(title, Unset):
            field_dict["title"] = title
        if not isinstance(comment_zero, Unset):
            field_dict["comment_zero"] = comment_zero
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
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
        if not isinstance(team_id, Unset):
            field_dict["team_id"] = team_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        comment_zero = d.pop("comment_zero", UNSET)

        embargoed = d.pop("embargoed", UNSET)

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

        team_id = d.pop("team_id", UNSET)

        flaw_post_request = cls(
            title=title,
            comment_zero=comment_zero,
            embargoed=embargoed,
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
            team_id=team_id,
        )

        flaw_post_request.additional_properties = d
        return flaw_post_request

    @staticmethod
    def get_fields():
        return {
            "title": str,
            "comment_zero": str,
            "embargoed": bool,
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
            "team_id": str,
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
