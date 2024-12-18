import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="Erratum")


@_attrs_define
class Erratum(OSIDBModel):
    """Erratum serializer

    Attributes:
        et_id (int):
        advisory_name (str):
        shipped_dt (Union[None, datetime.datetime]):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime): The updated_dt timestamp attribute is mandatory on update as it is used to
            detect mit-air collisions.
    """

    et_id: int
    advisory_name: str
    shipped_dt: Union[None, datetime.datetime]
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        et_id = self.et_id

        advisory_name = self.advisory_name

        shipped_dt: Union[None, str]
        if isinstance(self.shipped_dt, datetime.datetime):
            shipped_dt = UNSET
            if not isinstance(self.shipped_dt, Unset):
                shipped_dt = self.shipped_dt.isoformat()

        else:
            shipped_dt = self.shipped_dt

        created_dt: str = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        updated_dt: str = UNSET
        if not isinstance(self.updated_dt, Unset):
            updated_dt = self.updated_dt.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(et_id, Unset):
            field_dict["et_id"] = et_id
        if not isinstance(advisory_name, Unset):
            field_dict["advisory_name"] = advisory_name
        if not isinstance(shipped_dt, Unset):
            field_dict["shipped_dt"] = shipped_dt
        if not isinstance(created_dt, Unset):
            field_dict["created_dt"] = created_dt
        if not isinstance(updated_dt, Unset):
            field_dict["updated_dt"] = updated_dt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        et_id = d.pop("et_id", UNSET)

        advisory_name = d.pop("advisory_name", UNSET)

        def _parse_shipped_dt(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                # }
                _shipped_dt_type_0 = data
                shipped_dt_type_0: datetime.datetime
                if isinstance(_shipped_dt_type_0, Unset):
                    shipped_dt_type_0 = UNSET
                else:
                    shipped_dt_type_0 = isoparse(_shipped_dt_type_0)

                return shipped_dt_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        shipped_dt = _parse_shipped_dt(d.pop("shipped_dt", UNSET))

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

        erratum = cls(
            et_id=et_id,
            advisory_name=advisory_name,
            shipped_dt=shipped_dt,
            created_dt=created_dt,
            updated_dt=updated_dt,
        )

        erratum.additional_properties = d
        return erratum

    @staticmethod
    def get_fields():
        return {
            "et_id": int,
            "advisory_name": str,
            "shipped_dt": Union[None, datetime.datetime],
            "created_dt": datetime.datetime,
            "updated_dt": datetime.datetime,
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
