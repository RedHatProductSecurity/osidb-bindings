import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="OsidbApiV1AuditUpdateResponse200")


@_attrs_define
class OsidbApiV1AuditUpdateResponse200(OSIDBModel):
    """
    Attributes:
        pgh_created_at (datetime.datetime): When the event was created.
        pgh_slug (str): The unique identifier across all event tables.
        pgh_obj_model (str): The object model.
        pgh_label (str): The event label.
        pgh_diff (Any): The diff between the previous event of the same label.
        pgh_data (str):
        pgh_obj_id (Union[None, Unset, str]): The primary key of the object.
        pgh_context (Union[Unset, Any]): The context associated with the event.
        dt (Union[Unset, datetime.datetime]):
        env (Union[Unset, str]):
        revision (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    pgh_created_at: datetime.datetime
    pgh_slug: str
    pgh_obj_model: str
    pgh_label: str
    pgh_diff: Any
    pgh_data: str
    pgh_obj_id: Union[None, Unset, str] = UNSET
    pgh_context: Union[Unset, Any] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    env: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pgh_created_at: str = UNSET
        if not isinstance(self.pgh_created_at, Unset):
            pgh_created_at = self.pgh_created_at.isoformat()

        pgh_slug = self.pgh_slug

        pgh_obj_model = self.pgh_obj_model

        pgh_label = self.pgh_label

        pgh_diff = self.pgh_diff

        pgh_data = self.pgh_data

        pgh_obj_id: Union[None, Unset, str]
        if isinstance(self.pgh_obj_id, Unset):
            pgh_obj_id = UNSET
        else:
            pgh_obj_id = self.pgh_obj_id

        pgh_context = self.pgh_context

        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        env = self.env

        revision = self.revision

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(pgh_created_at, Unset):
            field_dict["pgh_created_at"] = pgh_created_at
        if not isinstance(pgh_slug, Unset):
            field_dict["pgh_slug"] = pgh_slug
        if not isinstance(pgh_obj_model, Unset):
            field_dict["pgh_obj_model"] = pgh_obj_model
        if not isinstance(pgh_label, Unset):
            field_dict["pgh_label"] = pgh_label
        if not isinstance(pgh_diff, Unset):
            field_dict["pgh_diff"] = pgh_diff
        if not isinstance(pgh_data, Unset):
            field_dict["pgh_data"] = pgh_data
        if not isinstance(pgh_obj_id, Unset):
            field_dict["pgh_obj_id"] = pgh_obj_id
        if not isinstance(pgh_context, Unset):
            field_dict["pgh_context"] = pgh_context
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
        d = src_dict.copy()
        # }
        _pgh_created_at = d.pop("pgh_created_at", UNSET)
        pgh_created_at: datetime.datetime
        if isinstance(_pgh_created_at, Unset):
            pgh_created_at = UNSET
        else:
            pgh_created_at = isoparse(_pgh_created_at)

        pgh_slug = d.pop("pgh_slug", UNSET)

        pgh_obj_model = d.pop("pgh_obj_model", UNSET)

        pgh_label = d.pop("pgh_label", UNSET)

        pgh_diff = d.pop("pgh_diff", UNSET)

        pgh_data = d.pop("pgh_data", UNSET)

        def _parse_pgh_obj_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pgh_obj_id = _parse_pgh_obj_id(d.pop("pgh_obj_id", UNSET))

        pgh_context = d.pop("pgh_context", UNSET)

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

        osidb_api_v1_audit_update_response_200 = cls(
            pgh_created_at=pgh_created_at,
            pgh_slug=pgh_slug,
            pgh_obj_model=pgh_obj_model,
            pgh_label=pgh_label,
            pgh_diff=pgh_diff,
            pgh_data=pgh_data,
            pgh_obj_id=pgh_obj_id,
            pgh_context=pgh_context,
            dt=dt,
            env=env,
            revision=revision,
            version=version,
        )

        osidb_api_v1_audit_update_response_200.additional_properties = d
        return osidb_api_v1_audit_update_response_200

    @staticmethod
    def get_fields():
        return {
            "pgh_created_at": datetime.datetime,
            "pgh_slug": str,
            "pgh_obj_model": str,
            "pgh_label": str,
            "pgh_diff": Any,
            "pgh_data": str,
            "pgh_obj_id": Union[None, str],
            "pgh_context": Any,
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
