from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.regulatory_reporting_api_v1_srp_reports_create_response_201 import (
    RegulatoryReportingApiV1SrpReportsCreateResponse201,
)
from ...models.srp_report_create_request import SRPReportCreateRequest
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = SRPReportCreateRequest


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    body: Union[
        SRPReportCreateRequest,
        SRPReportCreateRequest,
        SRPReportCreateRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/srp-reports",
    }

    if check_nested_instance(body, SRPReportCreateRequest):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1SrpReportsCreateResponse201]:
    if response.status_code == 201:
        _response_201 = response.json()
        response_201: RegulatoryReportingApiV1SrpReportsCreateResponse201
        if isinstance(_response_201, Unset):
            response_201 = UNSET
        else:
            response_201 = (
                RegulatoryReportingApiV1SrpReportsCreateResponse201.from_dict(
                    _response_201
                )
            )

        return response_201


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1SrpReportsCreateResponse201]:
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
        SRPReportCreateRequest,
        SRPReportCreateRequest,
        SRPReportCreateRequest,
    ],
) -> Response[RegulatoryReportingApiV1SrpReportsCreateResponse201]:
    """ViewSet for SRP Reports (top-level).

    Supports:
    - GET /regulatory-reporting/api/v1/srp-reports - List all reports with filtering
    - GET /regulatory-reporting/api/v1/srp-reports/{uuid} - Retrieve single report
    - POST /regulatory-reporting/api/v1/srp-reports - Manually create a report
    - PUT /regulatory-reporting/api/v1/srp-reports/{uuid} - Update

    Reports are also auto-created by signals when Critter criteria are met.
    Manual POST creates the report in EMPTY status with milestones.
    DELETE is not allowed. PATCH is globally blacklisted (BLACKLISTED_HTTP_METHODS).

    Args:
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsCreateResponse201]
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
        SRPReportCreateRequest,
        SRPReportCreateRequest,
        SRPReportCreateRequest,
    ],
) -> Optional[RegulatoryReportingApiV1SrpReportsCreateResponse201]:
    """ViewSet for SRP Reports (top-level).

    Supports:
    - GET /regulatory-reporting/api/v1/srp-reports - List all reports with filtering
    - GET /regulatory-reporting/api/v1/srp-reports/{uuid} - Retrieve single report
    - POST /regulatory-reporting/api/v1/srp-reports - Manually create a report
    - PUT /regulatory-reporting/api/v1/srp-reports/{uuid} - Update

    Reports are also auto-created by signals when Critter criteria are met.
    Manual POST creates the report in EMPTY status with milestones.
    DELETE is not allowed. PATCH is globally blacklisted (BLACKLISTED_HTTP_METHODS).

    Args:
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsCreateResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        SRPReportCreateRequest,
        SRPReportCreateRequest,
        SRPReportCreateRequest,
    ],
) -> Response[RegulatoryReportingApiV1SrpReportsCreateResponse201]:
    """ViewSet for SRP Reports (top-level).

    Supports:
    - GET /regulatory-reporting/api/v1/srp-reports - List all reports with filtering
    - GET /regulatory-reporting/api/v1/srp-reports/{uuid} - Retrieve single report
    - POST /regulatory-reporting/api/v1/srp-reports - Manually create a report
    - PUT /regulatory-reporting/api/v1/srp-reports/{uuid} - Update

    Reports are also auto-created by signals when Critter criteria are met.
    Manual POST creates the report in EMPTY status with milestones.
    DELETE is not allowed. PATCH is globally blacklisted (BLACKLISTED_HTTP_METHODS).

    Args:
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsCreateResponse201]
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
        SRPReportCreateRequest,
        SRPReportCreateRequest,
        SRPReportCreateRequest,
    ],
) -> Optional[RegulatoryReportingApiV1SrpReportsCreateResponse201]:
    """ViewSet for SRP Reports (top-level).

    Supports:
    - GET /regulatory-reporting/api/v1/srp-reports - List all reports with filtering
    - GET /regulatory-reporting/api/v1/srp-reports/{uuid} - Retrieve single report
    - POST /regulatory-reporting/api/v1/srp-reports - Manually create a report
    - PUT /regulatory-reporting/api/v1/srp-reports/{uuid} - Update

    Reports are also auto-created by signals when Critter criteria are met.
    Manual POST creates the report in EMPTY status with milestones.
    DELETE is not allowed. PATCH is globally blacklisted (BLACKLISTED_HTTP_METHODS).

    Args:
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.
        body (SRPReportCreateRequest): Serializer for manually creating SRP Reports.

            Status is always EMPTY. ACLs are inherited from the flaw in the
            view's perform_create. evidence is required for manual create.
            srp_reference_id and srp_reference_url are optional. timer_started_at is
            read-only and remains null until the report transitions to IN_PROGRESS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsCreateResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
