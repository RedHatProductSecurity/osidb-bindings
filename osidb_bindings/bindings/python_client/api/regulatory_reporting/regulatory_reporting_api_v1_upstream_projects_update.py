from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.regulatory_reporting_api_v1_upstream_projects_update_response_200 import (
    RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200,
)
from ...models.upstream_project_request import UpstreamProjectRequest
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = UpstreamProjectRequest


def _get_kwargs(
    upstream_project_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpstreamProjectRequest,
        UpstreamProjectRequest,
        UpstreamProjectRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/upstream-projects/{upstream_project_uuid}".format(
            upstream_project_uuid=upstream_project_uuid,
        ),
    }

    if check_nested_instance(body, UpstreamProjectRequest):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = (
                RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200.from_dict(
                    _response_200
                )
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    upstream_project_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpstreamProjectRequest,
        UpstreamProjectRequest,
        UpstreamProjectRequest,
    ],
) -> Response[RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        upstream_project_uuid (UUID):
        body (UpstreamProjectRequest): TrackingMixin class serializer
        body (UpstreamProjectRequest): TrackingMixin class serializer
        body (UpstreamProjectRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200]
    """

    kwargs = _get_kwargs(
        upstream_project_uuid=upstream_project_uuid,
        client=client,
        body=body,
    )

    response = requests.put(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(client=client, response=response)


def sync(
    upstream_project_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpstreamProjectRequest,
        UpstreamProjectRequest,
        UpstreamProjectRequest,
    ],
) -> Optional[RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        upstream_project_uuid (UUID):
        body (UpstreamProjectRequest): TrackingMixin class serializer
        body (UpstreamProjectRequest): TrackingMixin class serializer
        body (UpstreamProjectRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200
    """

    return sync_detailed(
        upstream_project_uuid=upstream_project_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    upstream_project_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpstreamProjectRequest,
        UpstreamProjectRequest,
        UpstreamProjectRequest,
    ],
) -> Response[RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        upstream_project_uuid (UUID):
        body (UpstreamProjectRequest): TrackingMixin class serializer
        body (UpstreamProjectRequest): TrackingMixin class serializer
        body (UpstreamProjectRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200]
    """

    kwargs = _get_kwargs(
        upstream_project_uuid=upstream_project_uuid,
        client=client,
        body=body,
    )

    async with client.get_async_session().put(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(client=client, response=resp)


async def asyncio(
    upstream_project_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpstreamProjectRequest,
        UpstreamProjectRequest,
        UpstreamProjectRequest,
    ],
) -> Optional[RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200]:
    """API endpoint for listing, creating, retrieving, and updating upstream project.

    Args:
        upstream_project_uuid (UUID):
        body (UpstreamProjectRequest): TrackingMixin class serializer
        body (UpstreamProjectRequest): TrackingMixin class serializer
        body (UpstreamProjectRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1UpstreamProjectsUpdateResponse200
    """

    return (
        await asyncio_detailed(
            upstream_project_uuid=upstream_project_uuid,
            client=client,
            body=body,
        )
    ).parsed
