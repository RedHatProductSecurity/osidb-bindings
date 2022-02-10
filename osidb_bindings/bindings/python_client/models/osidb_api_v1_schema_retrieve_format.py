from enum import Enum


class OsidbApiV1SchemaRetrieveFormat(str, Enum):
    JSON = "json"
    YAML = "yaml"

    def __str__(self) -> str:
        return str(self.value)
