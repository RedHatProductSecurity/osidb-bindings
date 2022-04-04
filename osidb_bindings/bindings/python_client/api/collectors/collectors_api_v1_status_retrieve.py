from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.collectors_api_v1_status_retrieve_response_200 import CollectorsApiV1StatusRetrieveResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/collectors/api/v1/status".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CollectorsApiV1StatusRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: CollectorsApiV1StatusRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = CollectorsApiV1StatusRetrieveResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CollectorsApiV1StatusRetrieveResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[CollectorsApiV1StatusRetrieveResponse200]:
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
) -> Optional[CollectorsApiV1StatusRetrieveResponse200]:
    """get the overall status of all collectors and the collected data"""

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[CollectorsApiV1StatusRetrieveResponse200]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[CollectorsApiV1StatusRetrieveResponse200]:
    """get the overall status of all collectors and the collected data"""

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
