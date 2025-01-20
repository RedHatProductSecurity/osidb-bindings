"""Contains some shared types for properties"""

from collections.abc import MutableMapping
from http import HTTPStatus
from typing import BinaryIO, Generic, Literal, Optional, TypeVar, get_args, get_origin

from attrs import define

from . import models


class Unset:
    def __bool__(self) -> Literal[False]:
        return False


UNSET: Unset = Unset()

FileJsonType = tuple[Optional[str], BinaryIO, Optional[str]]


@define
class File:
    """Contains information for file uploads"""

    payload: BinaryIO
    file_name: Optional[str] = None
    mime_type: Optional[str] = None

    def to_tuple(self) -> FileJsonType:
        """Return a tuple representation that httpx will accept for multipart/form-data"""
        return self.file_name, self.payload, self.mime_type


T = TypeVar("T")


@define
class Response(Generic[T]):
    """A response from an endpoint"""

    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Optional[T]


class OSIDBModel:
    """Base class for all 'non-primitive' and 'non-enum' models"""

    pass


def check_nested_instance(body, expected_type):
    """Helper function to check nested list instances"""
    if get_origin(expected_type) is list:
        inner_expected_type_name = get_args(expected_type)[0]
        inner_expected_type = getattr(models, inner_expected_type_name)
        return all(check_nested_instance(item, inner_expected_type) for item in body)
    else:
        return isinstance(body, expected_type)


__all__ = [
    "UNSET",
    "File",
    "FileJsonType",
    "OSIDBModel",
    "Response",
    "Unset",
    "check_nested_instance",
]
