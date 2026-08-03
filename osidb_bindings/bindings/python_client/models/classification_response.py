from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from attrs import fields as _attrs_fields

from ..types import UNSET, OSIDBModel, Unset

if TYPE_CHECKING:
    from ..models.classification_change_record import ClassificationChangeRecord
    from ..models.classification_result import ClassificationResult
    from ..models.classification_workflow import ClassificationWorkflow


T = TypeVar("T", bound="ClassificationResponse")


@_attrs_define
class ClassificationResponse(OSIDBModel):
    """Response serializer for the classification endpoint

    Attributes:
        flaw (UUID):
        classification (ClassificationResult): Serializer for the workflow:state classification result
        workflows (Union[Unset, list['ClassificationWorkflow']]):
        history (Union[Unset, list['ClassificationChangeRecord']]): Classification change history
    """

    flaw: UUID
    classification: "ClassificationResult"
    workflows: Union[Unset, list["ClassificationWorkflow"]] = UNSET
    history: Union[Unset, list["ClassificationChangeRecord"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flaw: str = UNSET
        if not isinstance(self.flaw, Unset):
            flaw = str(self.flaw)

        classification: dict[str, Any] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification.to_dict()

        workflows: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.workflows, Unset):
            workflows = []
            for workflows_item_data in self.workflows:
                workflows_item: dict[str, Any] = UNSET
                if not isinstance(workflows_item_data, Unset):
                    workflows_item = workflows_item_data.to_dict()

                workflows.append(workflows_item)

        history: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item: dict[str, Any] = UNSET
                if not isinstance(history_item_data, Unset):
                    history_item = history_item_data.to_dict()

                history.append(history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(flaw, Unset):
            field_dict["flaw"] = flaw
        if not isinstance(classification, Unset):
            field_dict["classification"] = classification
        if not isinstance(workflows, Unset):
            field_dict["workflows"] = workflows
        if not isinstance(history, Unset):
            field_dict["history"] = history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.classification_change_record import ClassificationChangeRecord
        from ..models.classification_result import ClassificationResult
        from ..models.classification_workflow import ClassificationWorkflow

        d = src_dict.copy()
        _flaw = d.pop("flaw", UNSET)
        flaw: UUID
        if isinstance(_flaw, Unset):
            flaw = UNSET
        else:
            flaw = _flaw if isinstance(_flaw, UUID) else UUID(_flaw)

        _classification = d.pop("classification", UNSET)
        classification: ClassificationResult
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = ClassificationResult.from_dict(_classification)

        workflows = []
        _workflows = d.pop("workflows", UNSET)
        for workflows_item_data in _workflows or []:
            _workflows_item = workflows_item_data
            workflows_item: ClassificationWorkflow
            if isinstance(_workflows_item, Unset):
                workflows_item = UNSET
            else:
                workflows_item = ClassificationWorkflow.from_dict(_workflows_item)

            workflows.append(workflows_item)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            _history_item = history_item_data
            history_item: ClassificationChangeRecord
            if isinstance(_history_item, Unset):
                history_item = UNSET
            else:
                history_item = ClassificationChangeRecord.from_dict(_history_item)

            history.append(history_item)

        classification_response = cls(
            flaw=flaw,
            classification=classification,
            workflows=workflows,
            history=history,
        )

        classification_response.additional_properties = d
        return classification_response

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
