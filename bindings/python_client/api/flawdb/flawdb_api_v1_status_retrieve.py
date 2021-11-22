from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.flawdb_api_v1_status_retrieve_format import FlawdbApiV1StatusRetrieveFormat
from ...models.flawdb_api_v1_status_retrieve_response_200 import FlawdbApiV1StatusRetrieveResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1StatusRetrieveFormat] = UNSET,
) -> Dict[str, Any]:
    url = "/flawdb/api/v1/status"

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):

        json_format_ = FlawdbApiV1StatusRetrieveFormat(format_).value if format_ else None

    params: Dict[str, Any] = {
        "format": json_format_,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[FlawdbApiV1StatusRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: FlawdbApiV1StatusRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = FlawdbApiV1StatusRetrieveResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[FlawdbApiV1StatusRetrieveResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1StatusRetrieveFormat] = UNSET,
) -> Response[FlawdbApiV1StatusRetrieveResponse200]:
    kwargs = _get_kwargs(
        client=client,
        format_=format_,
    )

    response = client.get_session().get(
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1StatusRetrieveFormat] = UNSET,
) -> Optional[FlawdbApiV1StatusRetrieveResponse200]:
    """HTTP get /status"""

    return sync_detailed(
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1StatusRetrieveFormat] = UNSET,
) -> Response[FlawdbApiV1StatusRetrieveResponse200]:
    kwargs = _get_kwargs(
        client=client,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1StatusRetrieveFormat] = UNSET,
) -> Optional[FlawdbApiV1StatusRetrieveResponse200]:
    """HTTP get /status"""

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
        )
    ).parsed
