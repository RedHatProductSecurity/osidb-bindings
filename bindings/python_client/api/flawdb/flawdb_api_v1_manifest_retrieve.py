from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...models.flawdb_api_v1_manifest_retrieve_format import FlawdbApiV1ManifestRetrieveFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1ManifestRetrieveFormat] = UNSET,
) -> Dict[str, Any]:
    url = "/flawdb/api/v1/manifest"

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params: Dict[str, Any] = {
        "format": json_format_,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
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
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1ManifestRetrieveFormat] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        format_=format_,
    )

    response = client.get_session().get(
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1ManifestRetrieveFormat] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
