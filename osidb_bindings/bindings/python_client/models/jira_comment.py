import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.jira_user import JiraUser
from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="JiraComment")


@attr.s(auto_attribs=True)
class JiraComment(OSIDBModel):
    """ """

    id: int
    author: JiraUser
    body: str
    created: datetime.datetime
    updated: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        author: Dict[str, Any] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        body = self.body
        created: str = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(id, Unset):
            field_dict["id"] = id
        if not isinstance(author, Unset):
            field_dict["author"] = author
        if not isinstance(body, Unset):
            field_dict["body"] = body
        if not isinstance(created, Unset):
            field_dict["created"] = created
        if not isinstance(updated, Unset):
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _author = d.pop("author", UNSET)
        author: JiraUser
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = JiraUser.from_dict(_author)

        body = d.pop("body", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        jira_comment = cls(
            id=id,
            author=author,
            body=body,
            created=created,
            updated=updated,
        )

        jira_comment.additional_properties = d
        return jira_comment

    @staticmethod
    def get_fields():
        return {
            "id": int,
            "author": JiraUser,
            "body": str,
            "created": datetime.datetime,
            "updated": datetime.datetime,
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
