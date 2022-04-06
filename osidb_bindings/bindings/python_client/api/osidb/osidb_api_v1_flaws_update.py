from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.flaw import Flaw
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws/{id}".format(
        client.base_url,
        id=id,
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
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
) -> Response[Flaw]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = httpx.put(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
) -> Optional[Flaw]:
    """ """

    return sync_detailed(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
) -> Response[Flaw]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
) -> Optional[Flaw]:
    """ """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
