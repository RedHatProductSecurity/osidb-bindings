from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.flaw import Flaw
from ...models.flawdb_api_v1_flaws_retrieve_format import FlawdbApiV1FlawsRetrieveFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    format_: Union[Unset, None, FlawdbApiV1FlawsRetrieveFormat] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "/flawdb/api/v1/flaws/{id}".format(
        id=id,
    )

    json_flaw_meta_type: Union[Unset, None, List[str]] = UNSET
    if not isinstance(flaw_meta_type, Unset):
        if flaw_meta_type is None:
            json_flaw_meta_type = None
        else:
            json_flaw_meta_type = flaw_meta_type

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):

        json_format_ = FlawdbApiV1FlawsRetrieveFormat(format_).value if format_ else None

    json_include_meta_attr: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_meta_attr, Unset):
        if include_meta_attr is None:
            json_include_meta_attr = None
        else:
            json_include_meta_attr = include_meta_attr

    params: Dict[str, Any] = {
        "flaw_meta_type": json_flaw_meta_type,
        "format": json_format_,
        "include_meta_attr": json_include_meta_attr,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Flaw]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: Flaw
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = Flaw.from_dict(_response_200)

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
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    format_: Union[Unset, None, FlawdbApiV1FlawsRetrieveFormat] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
) -> Response[Flaw]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        flaw_meta_type=flaw_meta_type,
        format_=format_,
        include_meta_attr=include_meta_attr,
    )

    response = client.get_session().get(
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    format_: Union[Unset, None, FlawdbApiV1FlawsRetrieveFormat] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
) -> Optional[Flaw]:
    """HTTP GET /flaws/{pk}"""

    return sync_detailed(
        id=id,
        client=client,
        flaw_meta_type=flaw_meta_type,
        format_=format_,
        include_meta_attr=include_meta_attr,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    format_: Union[Unset, None, FlawdbApiV1FlawsRetrieveFormat] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
) -> Response[Flaw]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        flaw_meta_type=flaw_meta_type,
        format_=format_,
        include_meta_attr=include_meta_attr,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    format_: Union[Unset, None, FlawdbApiV1FlawsRetrieveFormat] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
) -> Optional[Flaw]:
    """HTTP GET /flaws/{pk}"""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            flaw_meta_type=flaw_meta_type,
            format_=format_,
            include_meta_attr=include_meta_attr,
        )
    ).parsed
