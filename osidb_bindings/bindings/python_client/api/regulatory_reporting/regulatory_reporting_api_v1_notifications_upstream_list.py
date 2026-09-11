from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.regulatory_reporting_api_v1_notifications_upstream_list_method import (
    RegulatoryReportingApiV1NotificationsUpstreamListMethod,
)
from ...models.regulatory_reporting_api_v1_notifications_upstream_list_response_200 import (
    RegulatoryReportingApiV1NotificationsUpstreamListResponse200,
)
from ...models.regulatory_reporting_api_v1_notifications_upstream_list_status import (
    RegulatoryReportingApiV1NotificationsUpstreamListStatus,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "exclude_fields": list[str],
    "flaw": UUID,
    "include_fields": list[str],
    "limit": int,
    "method": RegulatoryReportingApiV1NotificationsUpstreamListMethod,
    "offset": int,
    "owner": str,
    "status": RegulatoryReportingApiV1NotificationsUpstreamListStatus,
    "upstream_project": UUID,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw: Union[Unset, UUID] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    method: Union[
        Unset, RegulatoryReportingApiV1NotificationsUpstreamListMethod
    ] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner: Union[Unset, str] = UNSET,
    status: Union[
        Unset, RegulatoryReportingApiV1NotificationsUpstreamListStatus
    ] = UNSET,
    upstream_project: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    json_flaw: Union[Unset, str] = UNSET
    if not isinstance(flaw, Unset):
        json_flaw = str(flaw)

    params["flaw"] = json_flaw

    json_include_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(include_fields, Unset):
        json_include_fields = include_fields

    params["include_fields"] = json_include_fields

    params["limit"] = limit

    json_method: Union[Unset, str] = UNSET
    if not isinstance(method, Unset):
        json_method = RegulatoryReportingApiV1NotificationsUpstreamListMethod(
            method
        ).value

    params["method"] = json_method

    params["offset"] = offset

    params["owner"] = owner

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = RegulatoryReportingApiV1NotificationsUpstreamListStatus(
            status
        ).value

    params["status"] = json_status

    json_upstream_project: Union[Unset, str] = UNSET
    if not isinstance(upstream_project, Unset):
        json_upstream_project = str(upstream_project)

    params["upstream_project"] = json_upstream_project

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/notifications/upstream",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1NotificationsUpstreamListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: RegulatoryReportingApiV1NotificationsUpstreamListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = (
                RegulatoryReportingApiV1NotificationsUpstreamListResponse200.from_dict(
                    _response_200
                )
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1NotificationsUpstreamListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw: Union[Unset, UUID] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    method: Union[
        Unset, RegulatoryReportingApiV1NotificationsUpstreamListMethod
    ] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner: Union[Unset, str] = UNSET,
    status: Union[
        Unset, RegulatoryReportingApiV1NotificationsUpstreamListStatus
    ] = UNSET,
    upstream_project: Union[Unset, UUID] = UNSET,
) -> Response[RegulatoryReportingApiV1NotificationsUpstreamListResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream maintainer notifications.

    Args:
        exclude_fields (Union[Unset, list[str]]):
        flaw (Union[Unset, UUID]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        method (Union[Unset, RegulatoryReportingApiV1NotificationsUpstreamListMethod]):
        offset (Union[Unset, int]):
        owner (Union[Unset, str]):
        status (Union[Unset, RegulatoryReportingApiV1NotificationsUpstreamListStatus]):
        upstream_project (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1NotificationsUpstreamListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        exclude_fields=exclude_fields,
        flaw=flaw,
        include_fields=include_fields,
        limit=limit,
        method=method,
        offset=offset,
        owner=owner,
        status=status,
        upstream_project=upstream_project,
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
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw: Union[Unset, UUID] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    method: Union[
        Unset, RegulatoryReportingApiV1NotificationsUpstreamListMethod
    ] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner: Union[Unset, str] = UNSET,
    status: Union[
        Unset, RegulatoryReportingApiV1NotificationsUpstreamListStatus
    ] = UNSET,
    upstream_project: Union[Unset, UUID] = UNSET,
) -> Optional[RegulatoryReportingApiV1NotificationsUpstreamListResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream maintainer notifications.

    Args:
        exclude_fields (Union[Unset, list[str]]):
        flaw (Union[Unset, UUID]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        method (Union[Unset, RegulatoryReportingApiV1NotificationsUpstreamListMethod]):
        offset (Union[Unset, int]):
        owner (Union[Unset, str]):
        status (Union[Unset, RegulatoryReportingApiV1NotificationsUpstreamListStatus]):
        upstream_project (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1NotificationsUpstreamListResponse200
    """

    return sync_detailed(
        client=client,
        exclude_fields=exclude_fields,
        flaw=flaw,
        include_fields=include_fields,
        limit=limit,
        method=method,
        offset=offset,
        owner=owner,
        status=status,
        upstream_project=upstream_project,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw: Union[Unset, UUID] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    method: Union[
        Unset, RegulatoryReportingApiV1NotificationsUpstreamListMethod
    ] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner: Union[Unset, str] = UNSET,
    status: Union[
        Unset, RegulatoryReportingApiV1NotificationsUpstreamListStatus
    ] = UNSET,
    upstream_project: Union[Unset, UUID] = UNSET,
) -> Response[RegulatoryReportingApiV1NotificationsUpstreamListResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream maintainer notifications.

    Args:
        exclude_fields (Union[Unset, list[str]]):
        flaw (Union[Unset, UUID]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        method (Union[Unset, RegulatoryReportingApiV1NotificationsUpstreamListMethod]):
        offset (Union[Unset, int]):
        owner (Union[Unset, str]):
        status (Union[Unset, RegulatoryReportingApiV1NotificationsUpstreamListStatus]):
        upstream_project (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1NotificationsUpstreamListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        exclude_fields=exclude_fields,
        flaw=flaw,
        include_fields=include_fields,
        limit=limit,
        method=method,
        offset=offset,
        owner=owner,
        status=status,
        upstream_project=upstream_project,
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
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw: Union[Unset, UUID] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    method: Union[
        Unset, RegulatoryReportingApiV1NotificationsUpstreamListMethod
    ] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner: Union[Unset, str] = UNSET,
    status: Union[
        Unset, RegulatoryReportingApiV1NotificationsUpstreamListStatus
    ] = UNSET,
    upstream_project: Union[Unset, UUID] = UNSET,
) -> Optional[RegulatoryReportingApiV1NotificationsUpstreamListResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream maintainer notifications.

    Args:
        exclude_fields (Union[Unset, list[str]]):
        flaw (Union[Unset, UUID]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        method (Union[Unset, RegulatoryReportingApiV1NotificationsUpstreamListMethod]):
        offset (Union[Unset, int]):
        owner (Union[Unset, str]):
        status (Union[Unset, RegulatoryReportingApiV1NotificationsUpstreamListStatus]):
        upstream_project (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1NotificationsUpstreamListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            exclude_fields=exclude_fields,
            flaw=flaw,
            include_fields=include_fields,
            limit=limit,
            method=method,
            offset=offset,
            owner=owner,
            status=status,
            upstream_project=upstream_project,
        )
    ).parsed
