"""
osidb-bindings iterators
"""

import re
from functools import partial
from typing import Callable, Optional

from .constants import DEFAULT_LIMIT
from .exceptions import OSIDBBindingsException


class Paginator:
    """
    Iterator for handling API pagination.

    Receives either starting limit and offset together with the retreive list function
    or already existing response from which it should continue.

    It keeps calling `.next()` response until pages are exhausted.
    """

    def __init__(
        self,
        *args,
        retrieve_list_fn: Optional[Callable] = None,
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
        init_response=None,
        **kwargs,
    ):
        if not init_response and not retrieve_list_fn:
            raise OSIDBBindingsException(
                (
                    "Paginator needs either initial response or session"
                    "operation function to obtain the initial response."
                )
            )

        self.retrieve_list_fn = retrieve_list_fn

        # initial starting data
        self.__init_limit = limit
        self.__init_offset = offset
        self.__init_response = init_response

        # current response page
        self.current_response = init_response

        # request arguments
        self.args = args
        self.kwargs = kwargs

    def __iter__(self):
        # restore initial response
        self.current_response = self.__init_response
        return self

    def __next__(self):
        if self.current_response is None:
            # no current response page - obtain the first page
            response = self.retrieve_list_fn(
                *self.args,
                limit=self.__init_limit,
                offset=self.__init_offset,
                **self.kwargs,
            )
            response = self.make_response_iterable(
                response, self.retrieve_list_fn, *self.args, **self.kwargs
            )
            self.current_response = response
            return response
        else:
            # existing current response - call next page
            response = self.current_response.next()
            if response is not None:
                self.current_response = response
                return response
            else:
                raise StopIteration

    @staticmethod
    def make_response_iterable(response, retrieve_list_fn, *args, **kwargs):
        """
        Populate next, prev and iterator helper methods for paginated responses
        """

        response.iterator = Paginator(
            init_response=response,
        )

        for param_name, func_name in (("next_", "next"), ("previous", "prev")):
            kwargs.pop("limit", None)
            kwargs.pop("offset", None)
            param = getattr(response, param_name, None)
            if param is None:
                setattr(response, func_name, lambda: None)
            else:
                limit = re.search(r"limit=(\d+)", param)
                if limit is not None:
                    kwargs["limit"] = limit.group(1)
                offset = re.search(r"offset=(\d+)", param)
                if offset is not None:
                    kwargs["offset"] = offset.group(1)

                setattr(response, func_name, partial(retrieve_list_fn, *args, **kwargs))

        return response
