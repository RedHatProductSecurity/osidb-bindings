"""
osidb-registry-bindings helpers
"""
import json
from distutils.util import strtobool
from os import getenv
from typing import Any, Union

from .exceptions import OSIDBBindingsException


def get_env(
    key: str,
    default: Union[None, str] = None,
    is_bool: bool = False,
    is_int: bool = False,
    is_json: bool = False,
) -> Any:
    """get environment variable"""
    if (is_bool and is_int) or (is_bool and is_json) or (is_int and is_json):
        raise OSIDBBindingsException(
            "Expected environment variable cannot be of multiple types at the same time"
        )

    value = getenv(key, default)
    # consider empty string as empty value
    # as setting the value to non-existing env variable
    # in compose.yml results in an empty string
    if value == "":
        value = default

    if is_bool:
        value = bool(strtobool(value))
    if is_int:
        value = int(value)
    if is_json:
        value = json.loads(value)

    return value
