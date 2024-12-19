import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cvss_version_enum import CvssVersionEnum
from ..models.issuer_enum import IssuerEnum
from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert


T = TypeVar("T", bound="AffectCVSS")


@_attrs_define
class AffectCVSS(OSIDBModel):
    """AffectCVSS serializer

    Attributes:
        cvss_version (CvssVersionEnum):
        issuer (IssuerEnum):
        score (float):
        uuid (UUID):
        vector (str):
        embargoed (bool): The embargoed boolean attribute is technically read-only as it just indirectly modifies the
            ACLs but is mandatory as it controls the access to the resource.
        alerts (list['Alert']):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
        affect (Union[Unset, UUID]):
        comment (Union[None, Unset, str]):
    """

    cvss_version: CvssVersionEnum
    issuer: IssuerEnum
    score: float
    uuid: UUID
    vector: str
    embargoed: bool
    alerts: list["Alert"]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    affect: Union[Unset, UUID] = UNSET
    comment: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cvss_version: str = UNSET
        if not isinstance(self.cvss_version, Unset):
            cvss_version = CvssVersionEnum(self.cvss_version).value

        issuer: str = UNSET
        if not isinstance(self.issuer, Unset):
            issuer = IssuerEnum(self.issuer).value

        score = self.score

        uuid: str = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        vector = self.vector

        embargoed = self.embargoed

        alerts: list[dict[str, Any]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item: dict[str, Any] = UNSET
                if not isinstance(alerts_item_data, Unset):
                    alerts_item = alerts_item_data.to_dict()

                alerts.append(alerts_item)

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        affect: Union[Unset, str] = UNSET
        if not isinstance(self.affect, Unset):
            affect = str(self.affect)

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}
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
        if not isinstance(affect, Unset):
            field_dict["affect"] = affect
        if not isinstance(comment, Unset):
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alert import Alert

        d = src_dict.copy()
        # }
        _cvss_version = d.pop("cvss_version", UNSET)
        cvss_version: CvssVersionEnum
        if isinstance(_cvss_version, Unset):
            cvss_version = UNSET
        else:
            cvss_version = CvssVersionEnum(_cvss_version)

        # }
        _issuer = d.pop("issuer", UNSET)
        issuer: IssuerEnum
        if isinstance(_issuer, Unset):
            issuer = UNSET
        else:
            issuer = IssuerEnum(_issuer)

        score = d.pop("score", UNSET)

        # }
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        vector = d.pop("vector", UNSET)

        embargoed = d.pop("embargoed", UNSET)

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
        _affect = d.pop("affect", UNSET)
        affect: Union[Unset, UUID]
        if isinstance(_affect, Unset):
            affect = UNSET
        else:
            affect = UUID(_affect)

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        affect_cvss = cls(
            cvss_version=cvss_version,
            issuer=issuer,
            score=score,
            uuid=uuid,
            vector=vector,
            embargoed=embargoed,
            alerts=alerts,
            created_dt=created_dt,
            updated_dt=updated_dt,
            affect=affect,
            comment=comment,
        )

        affect_cvss.additional_properties = d
        return affect_cvss

    @staticmethod
    def get_fields():
        return {
            "cvss_version": CvssVersionEnum,
            "issuer": IssuerEnum,
            "score": float,
            "uuid": UUID,
            "vector": str,
            "embargoed": bool,
            "alerts": list["Alert"],
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
            "affect": UUID,
            "comment": Union[None, str],
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
