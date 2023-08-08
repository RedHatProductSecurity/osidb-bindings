"""
osidb-bindings exceptions
"""


class OSIDBBindingsException(Exception):
    """Base osidb-bindings exception"""


class OperationUnsupported(OSIDBBindingsException):
    """Session operation is unsupported exception"""


class UndefinedRequestBody(OSIDBBindingsException):
    """
    Request body is not defined for the particular
    resource and operation combination exceptiéon
    """
