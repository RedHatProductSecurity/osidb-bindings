from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.regulatory_reporting_api_v1_srp_reports_retrieve_response_200 import (
    RegulatoryReportingApiV1SrpReportsRetrieveResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/srp-reports/{uuid}".format(
            uuid=uuid,
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1SrpReportsRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: RegulatoryReportingApiV1SrpReportsRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = (
                RegulatoryReportingApiV1SrpReportsRetrieveResponse200.from_dict(
                    _response_200
                )
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1SrpReportsRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[RegulatoryReportingApiV1SrpReportsRetrieveResponse200]:
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
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
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
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[RegulatoryReportingApiV1SrpReportsRetrieveResponse200]:
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
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsRetrieveResponse200
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[RegulatoryReportingApiV1SrpReportsRetrieveResponse200]:
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
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
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
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[RegulatoryReportingApiV1SrpReportsRetrieveResponse200]:
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
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsRetrieveResponse200
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
