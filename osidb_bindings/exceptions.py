"""
osidb-bindings exceptions
"""


class OSIDBBindingsException(Exception):
    """Base osidb-bindings exception"""


class MissingEndpointSection(OSIDBBindingsException):
    """Selected API section is missing exception"""


class MissingEndpointMethod(OSIDBBindingsException):
    """Selected API section method is missing exception"""


class MissingEndpointMethodVersion(OSIDBBindingsException):
    """Selected API method version is missing exception"""


class OperationUnsupported(OSIDBBindingsException):
    """Session operation is unsupported exception"""


class UndefinedRequestBody(OSIDBBindingsException):
    """
    Request body is not defined for the particular
    resource and operation combination exception
    """
