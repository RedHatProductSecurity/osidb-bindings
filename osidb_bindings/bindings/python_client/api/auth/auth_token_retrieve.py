from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.auth_token_retrieve_response_200 import AuthTokenRetrieveResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/token".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AuthTokenRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: AuthTokenRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = AuthTokenRetrieveResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AuthTokenRetrieveResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[AuthTokenRetrieveResponse200]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[AuthTokenRetrieveResponse200]:
    """Takes a kerberos ticket and returns an access and refresh JWT pair."""

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[AuthTokenRetrieveResponse200]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[AuthTokenRetrieveResponse200]:
    """Takes a kerberos ticket and returns an access and refresh JWT pair."""

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
