from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.affectedness_enum import AffectednessEnum
from ..models.blank_enum import BlankEnum
from ..models.impact_enum import ImpactEnum
from ..models.not_affected_justification_enum import NotAffectedJustificationEnum
from ..models.resolution_enum import ResolutionEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="AffectPostRequest")


@_attrs_define
class AffectPostRequest(OSIDBModel):
    """Affect serializer

    Attributes:
        flaw (Union[None, UUID]):
        ps_module (str):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        affectedness (Union[AffectednessEnum, BlankEnum, Unset]):
        resolution (Union[BlankEnum, ResolutionEnum, Unset]):
        ps_component (Union[None, Unset, str]):
        impact (Union[BlankEnum, ImpactEnum, Unset]):
        purl (Union[None, Unset, str]):
        not_affected_justification (Union[BlankEnum, NotAffectedJustificationEnum, Unset]):
    """

    flaw: Union[None, UUID]
    ps_module: str
    embargoed: bool
    affectedness: Union[AffectednessEnum, BlankEnum, Unset] = UNSET
    resolution: Union[BlankEnum, ResolutionEnum, Unset] = UNSET
    ps_component: Union[None, Unset, str] = UNSET
    impact: Union[BlankEnum, ImpactEnum, Unset] = UNSET
    purl: Union[None, Unset, str] = UNSET
    not_affected_justification: Union[
        BlankEnum, NotAffectedJustificationEnum, Unset
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flaw: Union[None, str]
        if isinstance(self.flaw, UUID):
            flaw = UNSET
            if not isinstance(self.flaw, Unset):
                flaw = str(self.flaw)

        else:
            flaw = self.flaw

        ps_module = self.ps_module

        embargoed = self.embargoed

        affectedness: Union[Unset, str]
        if isinstance(self.affectedness, Unset):
            affectedness = UNSET
        elif isinstance(self.affectedness, AffectednessEnum):
            affectedness = UNSET
            if not isinstance(self.affectedness, Unset):
                affectedness = AffectednessEnum(self.affectedness).value

        else:
            affectedness = UNSET
            if not isinstance(self.affectedness, Unset):
                affectedness = BlankEnum(self.affectedness).value

        resolution: Union[Unset, str]
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        elif isinstance(self.resolution, ResolutionEnum):
            resolution = UNSET
            if not isinstance(self.resolution, Unset):
                resolution = ResolutionEnum(self.resolution).value

        else:
            resolution = UNSET
            if not isinstance(self.resolution, Unset):
                resolution = BlankEnum(self.resolution).value

        ps_component: Union[None, Unset, str]
        if isinstance(self.ps_component, Unset):
            ps_component = UNSET
        else:
            ps_component = self.ps_component

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

        purl: Union[None, Unset, str]
        if isinstance(self.purl, Unset):
            purl = UNSET
        else:
            purl = self.purl

        not_affected_justification: Union[Unset, str]
        if isinstance(self.not_affected_justification, Unset):
            not_affected_justification = UNSET
        elif isinstance(self.not_affected_justification, NotAffectedJustificationEnum):
            not_affected_justification = UNSET
            if not isinstance(self.not_affected_justification, Unset):
                not_affected_justification = NotAffectedJustificationEnum(
                    self.not_affected_justification
                ).value

        else:
            not_affected_justification = UNSET
            if not isinstance(self.not_affected_justification, Unset):
                not_affected_justification = BlankEnum(
                    self.not_affected_justification
                ).value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(ps_module, Unset):
            field_dict["ps_module"] = ps_module
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(affectedness, Unset):
            field_dict["affectedness"] = affectedness
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(ps_component, Unset):
            field_dict["ps_component"] = ps_component
        if not isinstance(impact, Unset):
            field_dict["impact"] = impact
        if not isinstance(purl, Unset):
            field_dict["purl"] = purl
        if not isinstance(not_affected_justification, Unset):
            field_dict["not_affected_justification"] = not_affected_justification

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        flaw: tuple[None, bytes, str]

        if isinstance(self.flaw, UUID):
            flaw: bytes = UNSET
            if not isinstance(self.flaw, Unset):
                flaw = str(self.flaw)
        else:
            flaw = (None, str(self.flaw).encode(), "text/plain")

        ps_module = (None, str(self.ps_module).encode(), "text/plain")

        embargoed = (None, str(self.embargoed).encode(), "text/plain")

        affectedness: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.affectedness, Unset):
            affectedness = UNSET
        elif isinstance(self.affectedness, AffectednessEnum):
            affectedness: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.affectedness, Unset):
                affectedness = (
                    None,
                    str(self.affectedness.value).encode(),
                    "text/plain",
                )
        else:
            affectedness: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.affectedness, Unset):
                affectedness = (
                    None,
                    str(self.affectedness.value).encode(),
                    "text/plain",
                )

        resolution: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.resolution, Unset):
            resolution = UNSET
        elif isinstance(self.resolution, ResolutionEnum):
            resolution: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.resolution, Unset):
                resolution = (None, str(self.resolution.value).encode(), "text/plain")
        else:
            resolution: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.resolution, Unset):
                resolution = (None, str(self.resolution.value).encode(), "text/plain")

        ps_component: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.ps_component, Unset):
            ps_component = UNSET
        elif isinstance(self.ps_component, str):
            ps_component = (None, str(self.ps_component).encode(), "text/plain")
        else:
            ps_component = (None, str(self.ps_component).encode(), "text/plain")

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

        purl: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.purl, Unset):
            purl = UNSET
        elif isinstance(self.purl, str):
            purl = (None, str(self.purl).encode(), "text/plain")
        else:
            purl = (None, str(self.purl).encode(), "text/plain")

        not_affected_justification: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.not_affected_justification, Unset):
            not_affected_justification = UNSET
        elif isinstance(self.not_affected_justification, NotAffectedJustificationEnum):
            not_affected_justification: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.not_affected_justification, Unset):
                not_affected_justification = (
                    None,
                    str(self.not_affected_justification.value).encode(),
                    "text/plain",
                )
        else:
            not_affected_justification: Union[Unset, tuple[None, bytes, str]] = UNSET
            if not isinstance(self.not_affected_justification, Unset):
                not_affected_justification = (
                    None,
                    str(self.not_affected_justification.value).encode(),
                    "text/plain",
                )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(ps_module, Unset):
            field_dict["ps_module"] = ps_module
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(affectedness, Unset):
            field_dict["affectedness"] = affectedness
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(ps_component, Unset):
            field_dict["ps_component"] = ps_component
        if not isinstance(impact, Unset):
            field_dict["impact"] = impact
        if not isinstance(purl, Unset):
            field_dict["purl"] = purl
        if not isinstance(not_affected_justification, Unset):
            field_dict["not_affected_justification"] = not_affected_justification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_flaw(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _flaw_type_0 = data
                flaw_type_0: UUID
                if isinstance(_flaw_type_0, Unset):
                    flaw_type_0 = UNSET
                else:
                    flaw_type_0 = (
                        _flaw_type_0
                        if isinstance(_flaw_type_0, UUID)
                        else UUID(_flaw_type_0)
                    )

                return flaw_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        flaw = _parse_flaw(d.pop("flaw", UNSET))

        ps_module = d.pop("ps_module", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        def _parse_affectedness(
            data: object,
        ) -> Union[AffectednessEnum, BlankEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _affectedness_type_0 = data
                affectedness_type_0: AffectednessEnum
                if isinstance(_affectedness_type_0, Unset):
                    affectedness_type_0 = UNSET
                else:
                    affectedness_type_0 = AffectednessEnum(_affectedness_type_0)

                return affectedness_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _affectedness_type_1 = data
            affectedness_type_1: BlankEnum
            if isinstance(_affectedness_type_1, Unset):
                affectedness_type_1 = UNSET
            else:
                affectedness_type_1 = BlankEnum(_affectedness_type_1)

            return affectedness_type_1

        affectedness = _parse_affectedness(d.pop("affectedness", UNSET))

        def _parse_resolution(data: object) -> Union[BlankEnum, ResolutionEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _resolution_type_0 = data
                resolution_type_0: ResolutionEnum
                if isinstance(_resolution_type_0, Unset):
                    resolution_type_0 = UNSET
                else:
                    resolution_type_0 = ResolutionEnum(_resolution_type_0)

                return resolution_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _resolution_type_1 = data
            resolution_type_1: BlankEnum
            if isinstance(_resolution_type_1, Unset):
                resolution_type_1 = UNSET
            else:
                resolution_type_1 = BlankEnum(_resolution_type_1)

            return resolution_type_1

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_ps_component(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ps_component = _parse_ps_component(d.pop("ps_component", UNSET))

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

        def _parse_purl(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        purl = _parse_purl(d.pop("purl", UNSET))

        def _parse_not_affected_justification(
            data: object,
        ) -> Union[BlankEnum, NotAffectedJustificationEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _not_affected_justification_type_0 = data
                not_affected_justification_type_0: NotAffectedJustificationEnum
                if isinstance(_not_affected_justification_type_0, Unset):
                    not_affected_justification_type_0 = UNSET
                else:
                    not_affected_justification_type_0 = NotAffectedJustificationEnum(
                        _not_affected_justification_type_0
                    )

                return not_affected_justification_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _not_affected_justification_type_1 = data
            not_affected_justification_type_1: BlankEnum
            if isinstance(_not_affected_justification_type_1, Unset):
                not_affected_justification_type_1 = UNSET
            else:
                not_affected_justification_type_1 = BlankEnum(
                    _not_affected_justification_type_1
                )

            return not_affected_justification_type_1

        not_affected_justification = _parse_not_affected_justification(
            d.pop("not_affected_justification", UNSET)
        )

        affect_post_request = cls(
            flaw=flaw,
            ps_module=ps_module,
            embargoed=embargoed,
            affectedness=affectedness,
            resolution=resolution,
            ps_component=ps_component,
            impact=impact,
            purl=purl,
            not_affected_justification=not_affected_justification,
        )

        affect_post_request.additional_properties = d
        return affect_post_request

    @staticmethod
    def get_fields():
        return {
            "flaw": Union[None, UUID],
            "ps_module": str,
            "embargoed": bool,
            "affectedness": Union[AffectednessEnum, BlankEnum],
            "resolution": Union[BlankEnum, ResolutionEnum],
            "ps_component": Union[None, str],
            "impact": Union[BlankEnum, ImpactEnum],
            "purl": Union[None, str],
            "not_affected_justification": Union[
                BlankEnum, NotAffectedJustificationEnum
            ],
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
