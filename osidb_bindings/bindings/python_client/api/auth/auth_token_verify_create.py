from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.auth_token_verify_create_response_200 import (
    AuthTokenVerifyCreateResponse200,
)
from ...models.token_verify import TokenVerify
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = TokenVerify


def _get_kwargs(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TokenVerify,
        TokenVerify,
        TokenVerify,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/auth/token/verify",
    }

    if check_nested_instance(body, TokenVerify):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[AuthTokenVerifyCreateResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: AuthTokenVerifyCreateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = AuthTokenVerifyCreateResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[AuthTokenVerifyCreateResponse200]:
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
        TokenVerify,
        TokenVerify,
        TokenVerify,
    ],
) -> Response[AuthTokenVerifyCreateResponse200]:
    """Takes a token and indicates if it is valid.  This view provides no
    information about a token's fitness for a particular use.

    Args:
        body (TokenVerify):
        body (TokenVerify):
        body (TokenVerify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthTokenVerifyCreateResponse200]
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
        TokenVerify,
        TokenVerify,
        TokenVerify,
    ],
) -> Optional[AuthTokenVerifyCreateResponse200]:
    """Takes a token and indicates if it is valid.  This view provides no
    information about a token's fitness for a particular use.

    Args:
        body (TokenVerify):
        body (TokenVerify):
        body (TokenVerify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthTokenVerifyCreateResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TokenVerify,
        TokenVerify,
        TokenVerify,
    ],
) -> Response[AuthTokenVerifyCreateResponse200]:
    """Takes a token and indicates if it is valid.  This view provides no
    information about a token's fitness for a particular use.

    Args:
        body (TokenVerify):
        body (TokenVerify):
        body (TokenVerify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthTokenVerifyCreateResponse200]
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
        TokenVerify,
        TokenVerify,
        TokenVerify,
    ],
) -> Optional[AuthTokenVerifyCreateResponse200]:
    """Takes a token and indicates if it is valid.  This view provides no
    information about a token's fitness for a particular use.

    Args:
        body (TokenVerify):
        body (TokenVerify):
        body (TokenVerify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthTokenVerifyCreateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
