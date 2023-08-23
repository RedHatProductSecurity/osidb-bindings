from typing import Any, Dict, Optional

import requests

from ...client import Client
from ...models.auth_token_refresh_create_response_200 import (
    AuthTokenRefreshCreateResponse200,
)
from ...models.token_refresh import TokenRefresh
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}
REQUEST_BODY_TYPE = TokenRefresh


def _get_kwargs(
    *,
    client: Client,
    form_data: TokenRefresh,
    multipart_data: TokenRefresh,
    json_body: TokenRefresh,
) -> Dict[str, Any]:
    url = "{}/auth/token/refresh".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_json_body: Dict[str, Any] = UNSET
    if not isinstance(json_body, Unset):
        json_body.to_dict()

    multipart_multipart_data: Dict[str, Any] = UNSET
    if not isinstance(multipart_data, Unset):
        multipart_data.to_multipart()

    return {
        "url": url,
        "headers": headers,
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[AuthTokenRefreshCreateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: AuthTokenRefreshCreateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = AuthTokenRefreshCreateResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[AuthTokenRefreshCreateResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    form_data: TokenRefresh,
    multipart_data: TokenRefresh,
    json_body: TokenRefresh,
) -> Response[AuthTokenRefreshCreateResponse200]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = requests.post(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    form_data: TokenRefresh,
    multipart_data: TokenRefresh,
    json_body: TokenRefresh,
) -> Optional[AuthTokenRefreshCreateResponse200]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid."""

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def async_detailed(
    *,
    client: Client,
    form_data: TokenRefresh,
    multipart_data: TokenRefresh,
    json_body: TokenRefresh,
) -> Response[AuthTokenRefreshCreateResponse200]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with client.get_async_session().post(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(response=resp)


async def async_(
    *,
    client: Client,
    form_data: TokenRefresh,
    multipart_data: TokenRefresh,
    json_body: TokenRefresh,
) -> Optional[AuthTokenRefreshCreateResponse200]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid."""

    return (
        await async_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
