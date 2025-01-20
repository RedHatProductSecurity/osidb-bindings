from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.auth_token_refresh_create_response_200 import (
    AuthTokenRefreshCreateResponse200,
)
from ...models.token_refresh import TokenRefresh
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = TokenRefresh


def _get_kwargs(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TokenRefresh,
        TokenRefresh,
        TokenRefresh,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/auth/token/refresh",
    }

    if check_nested_instance(body, TokenRefresh):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[AuthTokenRefreshCreateResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: AuthTokenRefreshCreateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = AuthTokenRefreshCreateResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[AuthTokenRefreshCreateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TokenRefresh,
        TokenRefresh,
        TokenRefresh,
    ],
) -> Response[AuthTokenRefreshCreateResponse200]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        body (TokenRefresh):
        body (TokenRefresh):
        body (TokenRefresh):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthTokenRefreshCreateResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        body=body,
    )

    response = requests.post(
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
    body: Union[
        TokenRefresh,
        TokenRefresh,
        TokenRefresh,
    ],
) -> Optional[AuthTokenRefreshCreateResponse200]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        body (TokenRefresh):
        body (TokenRefresh):
        body (TokenRefresh):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthTokenRefreshCreateResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TokenRefresh,
        TokenRefresh,
        TokenRefresh,
    ],
) -> Response[AuthTokenRefreshCreateResponse200]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        body (TokenRefresh):
        body (TokenRefresh):
        body (TokenRefresh):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthTokenRefreshCreateResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        body=body,
    )

    async with client.get_async_session().post(
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
    body: Union[
        TokenRefresh,
        TokenRefresh,
        TokenRefresh,
    ],
) -> Optional[AuthTokenRefreshCreateResponse200]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        body (TokenRefresh):
        body (TokenRefresh):
        body (TokenRefresh):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthTokenRefreshCreateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
