from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_affects_retrieve_response_200 import (
    OsidbApiV1AffectsRetrieveResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "exclude_fields": list[str],
    "include_fields": list[str],
    "include_history": bool,
    "include_meta_attr": list[str],
}


def _get_kwargs(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    json_include_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(include_fields, Unset):
        json_include_fields = include_fields

    params["include_fields"] = json_include_fields

    params["include_history"] = include_history

    json_include_meta_attr: Union[Unset, list[str]] = UNSET
    if not isinstance(include_meta_attr, Unset):
        json_include_meta_attr = include_meta_attr

    params["include_meta_attr"] = json_include_meta_attr

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/affects/{uuid}".format(
            uuid=uuid,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1AffectsRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1AffectsRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AffectsRetrieveResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1AffectsRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
) -> Response[OsidbApiV1AffectsRetrieveResponse200]:
    """
    Args:
        uuid (UUID):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
        include_meta_attr (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AffectsRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        include_history=include_history,
        include_meta_attr=include_meta_attr,
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
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
) -> Optional[OsidbApiV1AffectsRetrieveResponse200]:
    """
    Args:
        uuid (UUID):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
        include_meta_attr (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AffectsRetrieveResponse200
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        include_history=include_history,
        include_meta_attr=include_meta_attr,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
) -> Response[OsidbApiV1AffectsRetrieveResponse200]:
    """
    Args:
        uuid (UUID):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
        include_meta_attr (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AffectsRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        include_history=include_history,
        include_meta_attr=include_meta_attr,
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
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
) -> Optional[OsidbApiV1AffectsRetrieveResponse200]:
    """
    Args:
        uuid (UUID):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
        include_meta_attr (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AffectsRetrieveResponse200
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            exclude_fields=exclude_fields,
            include_fields=include_fields,
            include_history=include_history,
            include_meta_attr=include_meta_attr,
        )
    ).parsed
