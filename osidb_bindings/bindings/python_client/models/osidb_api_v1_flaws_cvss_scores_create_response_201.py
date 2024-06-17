import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.alert import Alert
from ..models.cvss_version_enum import CvssVersionEnum
from ..models.issuer_enum import IssuerEnum
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1FlawsCvssScoresCreateResponse201")


@attr.s(auto_attribs=True)
class OsidbApiV1FlawsCvssScoresCreateResponse201(OSIDBModel):
    """ """

    cvss_version: CvssVersionEnum
    issuer: IssuerEnum
    score: float
    uuid: str
    vector: str
    embargoed: bool
    alerts: List[Alert]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    flaw: Union[Unset, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
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
        alerts: List[Dict[str, Any]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: Dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                alerts.append(alerts_item)

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        flaw = self.flaw
        comment = self.comment
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env
        revision = self.revision
        version = self.version

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
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(comment, Unset):
            field_dict["comment"] = comment
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

        alerts = []
        _alerts = d.pop("alerts", UNSET)
        if _alerts is UNSET:
            alerts = UNSET
        else:
            for alerts_item_data in _alerts or []:
                _alerts_item = alerts_item_data
                alerts_item: Alert
                if isinstance(_alerts_item, Unset):
                    alerts_item = UNSET
                else:
                    alerts_item = Alert.from_dict(_alerts_item)

                alerts.append(alerts_item)

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

        flaw = d.pop("flaw", UNSET)

        comment = d.pop("comment", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        env = d.pop("env", UNSET)

        revision = d.pop("revision", UNSET)

        version = d.pop("version", UNSET)

        osidb_api_v1_flaws_cvss_scores_create_response_201 = cls(
            cvss_version=cvss_version,
            issuer=issuer,
            score=score,
            uuid=uuid,
            vector=vector,
            embargoed=embargoed,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            flaw=flaw,
            comment=comment,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_flaws_cvss_scores_create_response_201.additional_properties = d
        return osidb_api_v1_flaws_cvss_scores_create_response_201

    @staticmethod
    def get_fields():
        return {
            "cvss_version": CvssVersionEnum,
            "issuer": IssuerEnum,
            "score": float,
            "uuid": str,
            "vector": str,
            "embargoed": bool,
            "alerts": List[Alert],
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "flaw": str,
            "comment": str,
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
