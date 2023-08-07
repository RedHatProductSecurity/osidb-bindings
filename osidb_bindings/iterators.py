"""
osidb-bindings iterators
"""


from typing import Callable


class Paginator:
    """
    Iterable for handling API pagination.

    Receives either starting limit and offset or already existing response from which
    it should continue.

    It keeps calling `.next()` response until pages are exhausted.
    """

    def __init__(
        self,
        session_operation: Callable,
        limit: int = 100,
        offset: int = 0,
        init_response=None,
        **kwargs,
    ):
        self.session_operation = session_operation
        self.__init_limit = limit
        self.__init_offset = offset
        self.__init_response = init_response
        self.current_response = init_response
        self.kwargs = kwargs

    def __iter__(self):
        self.current_response = self.__init_response
        return self

    def __next__(self):
        if self.current_response is None:
            response = self.session_operation(
                limit=self.__init_limit, offset=self.__init_offset, **self.kwargs
            )
            self.current_response = response
            return response
        else:
            response = self.current_response.next()
            if response is not None:
                self.current_response = response
                return response
            else:
                raise StopIteration
