from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.regulatory_reporting_api_v1_upstream_projects_create_response_201 import (
    RegulatoryReportingApiV1UpstreamProjectsCreateResponse201,
)
from ...models.upstream_project_post_request import UpstreamProjectPostRequest
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = UpstreamProjectPostRequest


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    body: Union[
        UpstreamProjectPostRequest,
        UpstreamProjectPostRequest,
        UpstreamProjectPostRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/upstream-projects",
    }

    if check_nested_instance(body, UpstreamProjectPostRequest):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1UpstreamProjectsCreateResponse201]:
    if response.status_code == 201:
        _response_201 = response.json()
        response_201: RegulatoryReportingApiV1UpstreamProjectsCreateResponse201
        if isinstance(_response_201, Unset):
            response_201 = UNSET
        else:
            response_201 = (
                RegulatoryReportingApiV1UpstreamProjectsCreateResponse201.from_dict(
                    _response_201
                )
            )

        return response_201


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1UpstreamProjectsCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        UpstreamProjectPostRequest,
        UpstreamProjectPostRequest,
        UpstreamProjectPostRequest,
    ],
) -> Response[RegulatoryReportingApiV1UpstreamProjectsCreateResponse201]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        body (UpstreamProjectPostRequest): TrackingMixin class serializer
        body (UpstreamProjectPostRequest): TrackingMixin class serializer
        body (UpstreamProjectPostRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1UpstreamProjectsCreateResponse201]
    """

    kwargs = _get_kwargs(
        client=client,
        body=body,
    )

    response = requests.post(
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
    body: Union[
        UpstreamProjectPostRequest,
        UpstreamProjectPostRequest,
        UpstreamProjectPostRequest,
    ],
) -> Optional[RegulatoryReportingApiV1UpstreamProjectsCreateResponse201]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        body (UpstreamProjectPostRequest): TrackingMixin class serializer
        body (UpstreamProjectPostRequest): TrackingMixin class serializer
        body (UpstreamProjectPostRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1UpstreamProjectsCreateResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        UpstreamProjectPostRequest,
        UpstreamProjectPostRequest,
        UpstreamProjectPostRequest,
    ],
) -> Response[RegulatoryReportingApiV1UpstreamProjectsCreateResponse201]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        body (UpstreamProjectPostRequest): TrackingMixin class serializer
        body (UpstreamProjectPostRequest): TrackingMixin class serializer
        body (UpstreamProjectPostRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1UpstreamProjectsCreateResponse201]
    """

    kwargs = _get_kwargs(
        client=client,
        body=body,
    )

    async with client.get_async_session().post(
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
    body: Union[
        UpstreamProjectPostRequest,
        UpstreamProjectPostRequest,
        UpstreamProjectPostRequest,
    ],
) -> Optional[RegulatoryReportingApiV1UpstreamProjectsCreateResponse201]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        body (UpstreamProjectPostRequest): TrackingMixin class serializer
        body (UpstreamProjectPostRequest): TrackingMixin class serializer
        body (UpstreamProjectPostRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1UpstreamProjectsCreateResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
