from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.flaw import Flaw
from ...models.flawdb_api_v1_flaws_create_format import FlawdbApiV1FlawsCreateFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
    format_: Union[Unset, None, FlawdbApiV1FlawsCreateFormat] = UNSET,
) -> Dict[str, Any]:
    url = "/flawdb/api/v1/flaws"

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):

        json_format_ = FlawdbApiV1FlawsCreateFormat(format_).value if format_ else None

    params: Dict[str, Any] = {
        "format": json_format_,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body: Dict[str, Any] = UNSET
    if not isinstance(json_body, Unset):
        json_body.to_dict()

    multipart_multipart_data: Dict[str, Any] = UNSET
    if not isinstance(multipart_data, Unset):
        multipart_data.to_multipart()

    return {
        "url": url,
        "data": form_data.to_dict(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Flaw]:
    if response.status_code == 201:
        _response_201 = response.json()
        response_201: Flaw
        if isinstance(_response_201, Unset):
            response_201 = UNSET
        else:
            response_201 = Flaw.from_dict(_response_201)

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[Flaw]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
    format_: Union[Unset, None, FlawdbApiV1FlawsCreateFormat] = UNSET,
) -> Response[Flaw]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    )

    response = client.get_session().post(
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
    format_: Union[Unset, None, FlawdbApiV1FlawsCreateFormat] = UNSET,
) -> Optional[Flaw]:
    """ """

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
    format_: Union[Unset, None, FlawdbApiV1FlawsCreateFormat] = UNSET,
) -> Response[Flaw]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
    format_: Union[Unset, None, FlawdbApiV1FlawsCreateFormat] = UNSET,
) -> Optional[Flaw]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
            format_=format_,
        )
    ).parsed
