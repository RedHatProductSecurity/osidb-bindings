"""
osidb-bindings exceptions
"""


class OperationUnsupported(Exception):
    """Session operation is unsupported exception"""


class UndefinedRequestBody(Exception):
    """
    Request body is not defined for the particular
    resource and operation combination exceptiéon
    """
