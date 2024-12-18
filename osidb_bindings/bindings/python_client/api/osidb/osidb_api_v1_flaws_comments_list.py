from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_flaws_comments_list_response_200 import (
    OsidbApiV1FlawsCommentsListResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "creator": str,
    "exclude_fields": list[str],
    "external_system_id": str,
    "include_fields": list[str],
    "limit": int,
    "offset": int,
    "order": int,
    "uuid": UUID,
}


def _get_kwargs(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    creator: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, int] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["creator"] = creator

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    params["external_system_id"] = external_system_id

    json_include_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(include_fields, Unset):
        json_include_fields = include_fields

    params["include_fields"] = json_include_fields

    params["limit"] = limit

    params["offset"] = offset

    params["order"] = order

    json_uuid: Union[Unset, str] = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)

    params["uuid"] = json_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/flaws/{flaw_id}/comments".format(
            flaw_id=flaw_id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1FlawsCommentsListResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsCommentsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsCommentsListResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1FlawsCommentsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    creator: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, int] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[OsidbApiV1FlawsCommentsListResponse200]:
    """List existing comments for a given flaw. Beware that freshly created comments are not guaranteed to
    keep their original UUIDs, especially if multiple comments are created simultaneously.

    Args:
        flaw_id (str):
        creator (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        external_system_id (Union[Unset, str]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, int]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsCommentsListResponse200]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
        creator=creator,
        exclude_fields=exclude_fields,
        external_system_id=external_system_id,
        include_fields=include_fields,
        limit=limit,
        offset=offset,
        order=order,
        uuid=uuid,
    )

    response = requests.get(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(client=client, response=response)


def sync(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    creator: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, int] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[OsidbApiV1FlawsCommentsListResponse200]:
    """List existing comments for a given flaw. Beware that freshly created comments are not guaranteed to
    keep their original UUIDs, especially if multiple comments are created simultaneously.

    Args:
        flaw_id (str):
        creator (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        external_system_id (Union[Unset, str]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, int]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsCommentsListResponse200
    """

    return sync_detailed(
        flaw_id=flaw_id,
        client=client,
        creator=creator,
        exclude_fields=exclude_fields,
        external_system_id=external_system_id,
        include_fields=include_fields,
        limit=limit,
        offset=offset,
        order=order,
        uuid=uuid,
    ).parsed


async def asyncio_detailed(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    creator: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, int] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[OsidbApiV1FlawsCommentsListResponse200]:
    """List existing comments for a given flaw. Beware that freshly created comments are not guaranteed to
    keep their original UUIDs, especially if multiple comments are created simultaneously.

    Args:
        flaw_id (str):
        creator (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        external_system_id (Union[Unset, str]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, int]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsCommentsListResponse200]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
        creator=creator,
        exclude_fields=exclude_fields,
        external_system_id=external_system_id,
        include_fields=include_fields,
        limit=limit,
        offset=offset,
        order=order,
        uuid=uuid,
    )

    async with client.get_async_session().get(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(client=client, response=resp)


async def asyncio(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    creator: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, int] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[OsidbApiV1FlawsCommentsListResponse200]:
    """List existing comments for a given flaw. Beware that freshly created comments are not guaranteed to
    keep their original UUIDs, especially if multiple comments are created simultaneously.

    Args:
        flaw_id (str):
        creator (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        external_system_id (Union[Unset, str]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, int]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsCommentsListResponse200
    """

    return (
        await asyncio_detailed(
            flaw_id=flaw_id,
            client=client,
            creator=creator,
            exclude_fields=exclude_fields,
            external_system_id=external_system_id,
            include_fields=include_fields,
            limit=limit,
            offset=offset,
            order=order,
            uuid=uuid,
        )
    ).parsed
