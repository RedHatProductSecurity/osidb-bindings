from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.classification_change_record_reason import (
        ClassificationChangeRecordReason,
    )


T = TypeVar("T", bound="ClassificationChangeRecord")


@_attrs_define
class ClassificationChangeRecord(OSIDBModel):
    """Serializer for a single classification change history record

    Attributes:
        timestamp (str):
        change_type (str):
        workflow (str):
        state (str):
        reason (Union[Unset, ClassificationChangeRecordReason]):
    """

    timestamp: str
    change_type: str
    workflow: str
    state: str
    reason: Union[Unset, "ClassificationChangeRecordReason"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        change_type = self.change_type

        workflow = self.workflow

        state = self.state

        reason: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(timestamp, Unset):
            field_dict["timestamp"] = timestamp
        if not isinstance(change_type, Unset):
            field_dict["change_type"] = change_type
        if not isinstance(workflow, Unset):
            field_dict["workflow"] = workflow
        if not isinstance(state, Unset):
            field_dict["state"] = state
        if not isinstance(reason, Unset):
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.classification_change_record_reason import (
            ClassificationChangeRecordReason,
        )

        d = src_dict.copy()
        timestamp = d.pop("timestamp", UNSET)

        change_type = d.pop("change_type", UNSET)

        workflow = d.pop("workflow", UNSET)

        state = d.pop("state", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, ClassificationChangeRecordReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ClassificationChangeRecordReason.from_dict(_reason)

        classification_change_record = cls(
            timestamp=timestamp,
            change_type=change_type,
            workflow=workflow,
            state=state,
            reason=reason,
        )

        classification_change_record.additional_properties = d
        return classification_change_record

    @classmethod
    def get_fields(cls):
        return {f.name: f.type for f in _attrs_fields(cls)}

    @classmethod
    def new(cls):
        return cls.from_dict({})

    @classmethod
    def from_model(cls: type[T], model: "OSIDBModel") -> T:
        return cls.from_dict(model.to_dict())

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
