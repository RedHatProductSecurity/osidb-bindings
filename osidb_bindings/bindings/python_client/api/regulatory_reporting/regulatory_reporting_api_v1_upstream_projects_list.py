from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.regulatory_reporting_api_v1_upstream_projects_list_response_200 import (
    RegulatoryReportingApiV1UpstreamProjectsListResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "component": str,
    "exclude_fields": list[str],
    "include_fields": list[str],
    "limit": int,
    "offset": int,
    "purl": str,
    "repository_url": str,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    component: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    purl: Union[Unset, str] = UNSET,
    repository_url: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["component"] = component

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    json_include_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(include_fields, Unset):
        json_include_fields = include_fields

    params["include_fields"] = json_include_fields

    params["limit"] = limit

    params["offset"] = offset

    params["purl"] = purl

    params["repository_url"] = repository_url

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/upstream-projects",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1UpstreamProjectsListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: RegulatoryReportingApiV1UpstreamProjectsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = (
                RegulatoryReportingApiV1UpstreamProjectsListResponse200.from_dict(
                    _response_200
                )
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1UpstreamProjectsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    component: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    purl: Union[Unset, str] = UNSET,
    repository_url: Union[Unset, str] = UNSET,
) -> Response[RegulatoryReportingApiV1UpstreamProjectsListResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        component (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        purl (Union[Unset, str]):
        repository_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1UpstreamProjectsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        component=component,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        limit=limit,
        offset=offset,
        purl=purl,
        repository_url=repository_url,
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
    component: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    purl: Union[Unset, str] = UNSET,
    repository_url: Union[Unset, str] = UNSET,
) -> Optional[RegulatoryReportingApiV1UpstreamProjectsListResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        component (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        purl (Union[Unset, str]):
        repository_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1UpstreamProjectsListResponse200
    """

    return sync_detailed(
        client=client,
        component=component,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        limit=limit,
        offset=offset,
        purl=purl,
        repository_url=repository_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    component: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    purl: Union[Unset, str] = UNSET,
    repository_url: Union[Unset, str] = UNSET,
) -> Response[RegulatoryReportingApiV1UpstreamProjectsListResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        component (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        purl (Union[Unset, str]):
        repository_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1UpstreamProjectsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        component=component,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        limit=limit,
        offset=offset,
        purl=purl,
        repository_url=repository_url,
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
    component: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    purl: Union[Unset, str] = UNSET,
    repository_url: Union[Unset, str] = UNSET,
) -> Optional[RegulatoryReportingApiV1UpstreamProjectsListResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        component (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        purl (Union[Unset, str]):
        repository_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1UpstreamProjectsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            component=component,
            exclude_fields=exclude_fields,
            include_fields=include_fields,
            limit=limit,
            offset=offset,
            purl=purl,
            repository_url=repository_url,
        )
    ).parsed
