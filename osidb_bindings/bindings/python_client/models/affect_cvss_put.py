import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.affect_cvss_put_alerts import AffectCVSSPutAlerts
from ..models.cvss_version_enum import CvssVersionEnum
from ..models.issuer_enum import IssuerEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="AffectCVSSPut")


@attr.s(auto_attribs=True)
class AffectCVSSPut(OSIDBModel):
    """AffectCVSS serializer"""

    cvss_version: CvssVersionEnum
    issuer: IssuerEnum
    score: float
    uuid: str
    vector: str
    embargoed: bool
    alerts: AffectCVSSPutAlerts
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cvss_version: str = UNSET
        if not isinstance(self.cvss_version, Unset):

            cvss_version = CvssVersionEnum(self.cvss_version).value

        issuer: str = UNSET
        if not isinstance(self.issuer, Unset):

            issuer = IssuerEnum(self.issuer).value

        score = self.score
        uuid = self.uuid
        vector = self.vector
        embargoed = self.embargoed
        alerts: Dict[str, Any] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = self.alerts.to_dict()

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(cvss_version, Unset):
            field_dict["cvss_version"] = cvss_version
        if not isinstance(issuer, Unset):
            field_dict["issuer"] = issuer
        if not isinstance(score, Unset):
            field_dict["score"] = score
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(vector, Unset):
            field_dict["vector"] = vector
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(comment, Unset):
            field_dict["comment"] = comment

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        cvss_version: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.cvss_version, Unset):

            cvss_version = CvssVersionEnum(self.cvss_version).value

        issuer: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.issuer, Unset):

            issuer = IssuerEnum(self.issuer).value

        score = (
            self.score if self.score is UNSET else (None, str(self.score), "text/plain")
        )
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        vector = (
            self.vector
            if self.vector is UNSET
            else (None, str(self.vector), "text/plain")
        )
        embargoed = (
            self.embargoed
            if self.embargoed is UNSET
            else (None, str(self.embargoed), "text/plain")
        )
        alerts: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = (None, json.dumps(self.alerts.to_dict()), "application/json")

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        comment = (
            self.comment
            if self.comment is UNSET
            else (None, str(self.comment), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        if not isinstance(cvss_version, Unset):
            field_dict["cvss_version"] = cvss_version
        if not isinstance(issuer, Unset):
            field_dict["issuer"] = issuer
        if not isinstance(score, Unset):
            field_dict["score"] = score
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(vector, Unset):
            field_dict["vector"] = vector
        if not isinstance(embargoed, Unset):
            field_dict["embargoed"] = embargoed
        if not isinstance(alerts, Unset):
            field_dict["alerts"] = alerts
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt
        if not isinstance(comment, Unset):
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _cvss_version = d.pop("cvss_version", UNSET)
        cvss_version: CvssVersionEnum
        if isinstance(_cvss_version, Unset):
            cvss_version = UNSET
        else:
            cvss_version = CvssVersionEnum(_cvss_version)

        _issuer = d.pop("issuer", UNSET)
        issuer: IssuerEnum
        if isinstance(_issuer, Unset):
            issuer = UNSET
        else:
            issuer = IssuerEnum(_issuer)

        score = d.pop("score", UNSET)

        uuid = d.pop("uuid", UNSET)

        vector = d.pop("vector", UNSET)

        embargoed = d.pop("embargoed", UNSET)

        _alerts = d.pop("alerts", UNSET)
        alerts: AffectCVSSPutAlerts
        if isinstance(_alerts, Unset):
            alerts = UNSET
        else:
            alerts = AffectCVSSPutAlerts.from_dict(_alerts)

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

        affect_cvss_put = cls(
            cvss_version=cvss_version,
            issuer=issuer,
            score=score,
            uuid=uuid,
            vector=vector,
            embargoed=embargoed,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            comment=comment,
        )

        affect_cvss_put.additional_properties = d
        return affect_cvss_put

    @staticmethod
    def get_fields():
        return {
            "cvss_version": CvssVersionEnum,
            "issuer": IssuerEnum,
            "score": float,
            "uuid": str,
            "vector": str,
            "embargoed": bool,
            "alerts": AffectCVSSPutAlerts,
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "comment": str,
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
