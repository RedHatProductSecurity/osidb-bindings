from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.flaw import Flaw
from ...models.flawdb_api_v1_flaws_retrieve_format import FlawdbApiV1FlawsRetrieveFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1FlawsRetrieveFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/flawdb/api/v1/flaws/{id}".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params: Dict[str, Any] = {
        "format": json_format_,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Flaw]:
    if response.status_code == 200:
        response_200 = Flaw.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Flaw]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1FlawsRetrieveFormat] = UNSET,
) -> Response[Flaw]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        format_=format_,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1FlawsRetrieveFormat] = UNSET,
) -> Optional[Flaw]:
    """HTTP GET /flaws/{flaw_id}"""

    return sync_detailed(
        id=id,
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1FlawsRetrieveFormat] = UNSET,
) -> Response[Flaw]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        format_=format_,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1FlawsRetrieveFormat] = UNSET,
) -> Optional[Flaw]:
    """HTTP GET /flaws/{flaw_id}"""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            format_=format_,
        )
    ).parsed
