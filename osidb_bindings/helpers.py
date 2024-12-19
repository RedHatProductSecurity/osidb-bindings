"""
osidb-registry-bindings helpers
"""

import json
from os import getenv
from typing import Any, Union

from .exceptions import OSIDBBindingsException

_MAP = {
    "y": True,
    "yes": True,
    "t": True,
    "true": True,
    "on": True,
    "1": True,
    "n": False,
    "no": False,
    "f": False,
    "false": False,
    "off": False,
    "0": False,
}


def strtobool(value):
    try:
        return _MAP[str(value).lower()]
    except KeyError:
        raise ValueError('"{}" is not a valid bool value'.format(value))


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
