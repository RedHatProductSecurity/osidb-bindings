from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    verbose: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osim/api/v1/workflows/{id}".format(
        client.base_url,
        id=id,
    )

    headers: Dict[str, Any] = client.get_headers()

    params: Dict[str, Any] = {
        "verbose": verbose,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    verbose: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        verbose=verbose,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    verbose: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        verbose=verbose,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
