import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_audit_list_response_200 import (
    OsidbApiV1AuditListResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "limit": int,
    "offset": int,
    "pgh_created_at": datetime.datetime,
    "pgh_label": str,
    "pgh_obj_model": str,
    "pgh_slug": str,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pgh_created_at: Union[Unset, datetime.datetime] = UNSET,
    pgh_label: Union[Unset, str] = UNSET,
    pgh_obj_model: Union[Unset, str] = UNSET,
    pgh_slug: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_pgh_created_at: Union[Unset, str] = UNSET
    if not isinstance(pgh_created_at, Unset):
        json_pgh_created_at = pgh_created_at.isoformat()

    params["pgh_created_at"] = json_pgh_created_at

    params["pgh_label"] = pgh_label

    params["pgh_obj_model"] = pgh_obj_model

    params["pgh_slug"] = pgh_slug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/audit",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1AuditListResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1AuditListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AuditListResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1AuditListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pgh_created_at: Union[Unset, datetime.datetime] = UNSET,
    pgh_label: Union[Unset, str] = UNSET,
    pgh_obj_model: Union[Unset, str] = UNSET,
    pgh_slug: Union[Unset, str] = UNSET,
) -> Response[OsidbApiV1AuditListResponse200]:
    """basic view of audit history events

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        pgh_created_at (Union[Unset, datetime.datetime]):
        pgh_label (Union[Unset, str]):
        pgh_obj_model (Union[Unset, str]):
        pgh_slug (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AuditListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        pgh_created_at=pgh_created_at,
        pgh_label=pgh_label,
        pgh_obj_model=pgh_obj_model,
        pgh_slug=pgh_slug,
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
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pgh_created_at: Union[Unset, datetime.datetime] = UNSET,
    pgh_label: Union[Unset, str] = UNSET,
    pgh_obj_model: Union[Unset, str] = UNSET,
    pgh_slug: Union[Unset, str] = UNSET,
) -> Optional[OsidbApiV1AuditListResponse200]:
    """basic view of audit history events

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        pgh_created_at (Union[Unset, datetime.datetime]):
        pgh_label (Union[Unset, str]):
        pgh_obj_model (Union[Unset, str]):
        pgh_slug (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AuditListResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        pgh_created_at=pgh_created_at,
        pgh_label=pgh_label,
        pgh_obj_model=pgh_obj_model,
        pgh_slug=pgh_slug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pgh_created_at: Union[Unset, datetime.datetime] = UNSET,
    pgh_label: Union[Unset, str] = UNSET,
    pgh_obj_model: Union[Unset, str] = UNSET,
    pgh_slug: Union[Unset, str] = UNSET,
) -> Response[OsidbApiV1AuditListResponse200]:
    """basic view of audit history events

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        pgh_created_at (Union[Unset, datetime.datetime]):
        pgh_label (Union[Unset, str]):
        pgh_obj_model (Union[Unset, str]):
        pgh_slug (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AuditListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        pgh_created_at=pgh_created_at,
        pgh_label=pgh_label,
        pgh_obj_model=pgh_obj_model,
        pgh_slug=pgh_slug,
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
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pgh_created_at: Union[Unset, datetime.datetime] = UNSET,
    pgh_label: Union[Unset, str] = UNSET,
    pgh_obj_model: Union[Unset, str] = UNSET,
    pgh_slug: Union[Unset, str] = UNSET,
) -> Optional[OsidbApiV1AuditListResponse200]:
    """basic view of audit history events

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        pgh_created_at (Union[Unset, datetime.datetime]):
        pgh_label (Union[Unset, str]):
        pgh_obj_model (Union[Unset, str]):
        pgh_slug (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AuditListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            pgh_created_at=pgh_created_at,
            pgh_label=pgh_label,
            pgh_obj_model=pgh_obj_model,
            pgh_slug=pgh_slug,
        )
    ).parsed
