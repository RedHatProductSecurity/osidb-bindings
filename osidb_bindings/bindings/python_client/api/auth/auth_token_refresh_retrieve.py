from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.auth_token_refresh_retrieve_response_200 import (
    AuthTokenRefreshRetrieveResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    *,
    client: Union[AuthenticatedClient, Client],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/auth/token/refresh",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[AuthTokenRefreshRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: AuthTokenRefreshRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = AuthTokenRefreshRetrieveResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[AuthTokenRefreshRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuthTokenRefreshRetrieveResponse200]:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthTokenRefreshRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = requests.get(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuthTokenRefreshRetrieveResponse200]:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthTokenRefreshRetrieveResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuthTokenRefreshRetrieveResponse200]:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthTokenRefreshRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with client.get_async_session().get(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(client=client, response=resp)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuthTokenRefreshRetrieveResponse200]:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthTokenRefreshRetrieveResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
