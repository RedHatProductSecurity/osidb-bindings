from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cvss_version_enum import CvssVersionEnum
from ..models.issuer_enum import IssuerEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="AffectCVSSPostRequest")


@_attrs_define
class AffectCVSSPostRequest(OSIDBModel):
    """AffectCVSS serializer

    Attributes:
        cvss_version (CvssVersionEnum):
        vector (str):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        comment (Union[None, Unset, str]):
        issuer (Union[Unset, IssuerEnum]):  Default: IssuerEnum.RH.
    """

    cvss_version: CvssVersionEnum
    vector: str
    embargoed: bool
    comment: Union[None, Unset, str] = UNSET
    issuer: Union[Unset, IssuerEnum] = IssuerEnum.RH
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cvss_version: str = UNSET
        if not isinstance(self.cvss_version, Unset):
            cvss_version = CvssVersionEnum(self.cvss_version).value

        vector = self.vector

        embargoed = self.embargoed

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        issuer: Union[Unset, str] = UNSET
        if not isinstance(self.issuer, Unset):
            issuer = IssuerEnum(self.issuer).value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(cvss_version, Unset):
            field_dict["cvss_version"] = cvss_version
        if not isinstance(vector, Unset):
            field_dict["vector"] = vector
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(comment, Unset):
            field_dict["comment"] = comment
        if not isinstance(issuer, Unset):
            field_dict["issuer"] = issuer

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        cvss_version: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.cvss_version, Unset):
            cvss_version = (None, str(self.cvss_version.value).encode(), "text/plain")

        vector = (None, str(self.vector).encode(), "text/plain")

        embargoed = (None, str(self.embargoed).encode(), "text/plain")

        comment: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.comment, Unset):
            comment = UNSET
        elif isinstance(self.comment, str):
            comment = (None, str(self.comment).encode(), "text/plain")
        else:
            comment = (None, str(self.comment).encode(), "text/plain")

        issuer: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.issuer, Unset):
            issuer = (None, str(self.issuer.value).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        if not isinstance(cvss_version, Unset):
            field_dict["cvss_version"] = cvss_version
        if not isinstance(vector, Unset):
            field_dict["vector"] = vector
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(comment, Unset):
            field_dict["comment"] = comment
        if not isinstance(issuer, Unset):
            field_dict["issuer"] = issuer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _cvss_version = d.pop("cvss_version", UNSET)
        cvss_version: CvssVersionEnum
        if isinstance(_cvss_version, Unset):
            cvss_version = UNSET
        else:
            cvss_version = CvssVersionEnum(_cvss_version)

        vector = d.pop("vector", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        _issuer = d.pop("issuer", UNSET)
        issuer: Union[Unset, IssuerEnum]
        if isinstance(_issuer, Unset):
            issuer = UNSET
        else:
            issuer = IssuerEnum(_issuer)

        affect_cvss_post_request = cls(
            cvss_version=cvss_version,
            vector=vector,
            embargoed=embargoed,
            comment=comment,
            issuer=issuer,
        )

        affect_cvss_post_request.additional_properties = d
        return affect_cvss_post_request

    @staticmethod
    def get_fields():
        return {
            "cvss_version": CvssVersionEnum,
            "vector": str,
            "embargoed": bool,
            "comment": Union[None, str],
            "issuer": IssuerEnum,
        }

    @classmethod
    def new(cls):
        return cls.from_dict({})

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
