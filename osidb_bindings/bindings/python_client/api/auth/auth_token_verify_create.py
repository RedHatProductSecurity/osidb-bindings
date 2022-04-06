from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.token_verify import TokenVerify
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    form_data: TokenVerify,
    multipart_data: TokenVerify,
    json_body: TokenVerify,
) -> Dict[str, Any]:
    url = "{}/auth/token/verify".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[TokenVerify]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: TokenVerify
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = TokenVerify.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[TokenVerify]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    form_data: TokenVerify,
    multipart_data: TokenVerify,
    json_body: TokenVerify,
) -> Response[TokenVerify]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = httpx.post(
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
    form_data: TokenVerify,
    multipart_data: TokenVerify,
    json_body: TokenVerify,
) -> Optional[TokenVerify]:
    """Takes a token and indicates if it is valid.  This view provides no
    information about a token's fitness for a particular use."""

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    form_data: TokenVerify,
    multipart_data: TokenVerify,
    json_body: TokenVerify,
) -> Response[TokenVerify]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    form_data: TokenVerify,
    multipart_data: TokenVerify,
    json_body: TokenVerify,
) -> Optional[TokenVerify]:
    """Takes a token and indicates if it is valid.  This view provides no
    information about a token's fitness for a particular use."""

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
