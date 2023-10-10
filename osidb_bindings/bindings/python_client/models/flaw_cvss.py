import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.issuer_enum import IssuerEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawCVSS")


@attr.s(auto_attribs=True)
class FlawCVSS(OSIDBModel):
    """FlawCVSS serializer"""

    cvss_version: str
    issuer: IssuerEnum
    uuid: str
    vector: str
    embargoed: bool
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    comment: Union[Unset, str] = UNSET
    flaw: Union[Unset, str] = UNSET
    score: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cvss_version = self.cvss_version
        issuer: str = UNSET
        if not isinstance(self.issuer, Unset):

            issuer = IssuerEnum(self.issuer).value

        uuid = self.uuid
        vector = self.vector
        embargoed = self.embargoed
        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        comment = self.comment
        flaw = self.flaw
        score = self.score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(cvss_version, Unset):
            field_dict["cvss_version"] = cvss_version
        if not isinstance(issuer, Unset):
            field_dict["issuer"] = issuer
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(vector, Unset):
            field_dict["vector"] = vector
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(comment, Unset):
            field_dict["comment"] = comment
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(score, Unset):
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cvss_version = d.pop("cvss_version", UNSET)

        _issuer = d.pop("issuer", UNSET)
        issuer: IssuerEnum
        if isinstance(_issuer, Unset):
            issuer = UNSET
        else:
            issuer = IssuerEnum(_issuer)

        uuid = d.pop("uuid", UNSET)

        vector = d.pop("vector", UNSET)

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

        comment = d.pop("comment", UNSET)

        flaw = d.pop("flaw", UNSET)

        score = d.pop("score", UNSET)

        flaw_cvss = cls(
            cvss_version=cvss_version,
            issuer=issuer,
            uuid=uuid,
            vector=vector,
            embargoed=embargoed,
            created_dt=created_dt,
            updated_dt=updated_dt,
            comment=comment,
            flaw=flaw,
            score=score,
        )

        flaw_cvss.additional_properties = d
        return flaw_cvss

    @staticmethod
    def get_fields():
        return {
            "cvss_version": str,
            "issuer": IssuerEnum,
            "uuid": str,
            "vector": str,
            "embargoed": bool,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "comment": str,
            "flaw": str,
            "score": float,
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
