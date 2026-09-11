import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.regulatory_reporting_api_v1_srp_reports_list_response_200 import (
    RegulatoryReportingApiV1SrpReportsListResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "created_dt__gte": datetime.datetime,
    "created_dt__lte": datetime.datetime,
    "flaw_id": UUID,
    "limit": int,
    "offset": int,
    "reportable_event_type": str,
    "responsibility_scope": str,
    "srp_reference_id": str,
    "status": str,
    "timer_started_at__gte": datetime.datetime,
    "timer_started_at__lte": datetime.datetime,
    "title": str,
    "updated_dt__gte": datetime.datetime,
    "updated_dt__lte": datetime.datetime,
    "uuid": UUID,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    reportable_event_type: Union[Unset, str] = UNSET,
    responsibility_scope: Union[Unset, str] = UNSET,
    srp_reference_id: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    timer_started_at_gte: Union[Unset, datetime.datetime] = UNSET,
    timer_started_at_lte: Union[Unset, datetime.datetime] = UNSET,
    title: Union[Unset, str] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    json_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(created_dt_gte, Unset):
        json_created_dt_gte = created_dt_gte.isoformat()

    params["created_dt__gte"] = json_created_dt_gte

    json_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(created_dt_lte, Unset):
        json_created_dt_lte = created_dt_lte.isoformat()

    params["created_dt__lte"] = json_created_dt_lte

    json_flaw_id: Union[Unset, str] = UNSET
    if not isinstance(flaw_id, Unset):
        json_flaw_id = str(flaw_id)

    params["flaw_id"] = json_flaw_id

    params["limit"] = limit

    params["offset"] = offset

    params["reportable_event_type"] = reportable_event_type

    params["responsibility_scope"] = responsibility_scope

    params["srp_reference_id"] = srp_reference_id

    params["status"] = status

    json_timer_started_at_gte: Union[Unset, str] = UNSET
    if not isinstance(timer_started_at_gte, Unset):
        json_timer_started_at_gte = timer_started_at_gte.isoformat()

    params["timer_started_at__gte"] = json_timer_started_at_gte

    json_timer_started_at_lte: Union[Unset, str] = UNSET
    if not isinstance(timer_started_at_lte, Unset):
        json_timer_started_at_lte = timer_started_at_lte.isoformat()

    params["timer_started_at__lte"] = json_timer_started_at_lte

    params["title"] = title

    json_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_gte, Unset):
        json_updated_dt_gte = updated_dt_gte.isoformat()

    params["updated_dt__gte"] = json_updated_dt_gte

    json_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_lte, Unset):
        json_updated_dt_lte = updated_dt_lte.isoformat()

    params["updated_dt__lte"] = json_updated_dt_lte

    json_uuid: Union[Unset, str] = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)

    params["uuid"] = json_uuid

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/srp-reports",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1SrpReportsListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: RegulatoryReportingApiV1SrpReportsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = RegulatoryReportingApiV1SrpReportsListResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1SrpReportsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    reportable_event_type: Union[Unset, str] = UNSET,
    responsibility_scope: Union[Unset, str] = UNSET,
    srp_reference_id: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    timer_started_at_gte: Union[Unset, datetime.datetime] = UNSET,
    timer_started_at_lte: Union[Unset, datetime.datetime] = UNSET,
    title: Union[Unset, str] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[RegulatoryReportingApiV1SrpReportsListResponse200]:
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
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        reportable_event_type (Union[Unset, str]):
        responsibility_scope (Union[Unset, str]):
        srp_reference_id (Union[Unset, str]):
        status (Union[Unset, str]):
        timer_started_at_gte (Union[Unset, datetime.datetime]):
        timer_started_at_lte (Union[Unset, datetime.datetime]):
        title (Union[Unset, str]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        created_dt_gte=created_dt_gte,
        created_dt_lte=created_dt_lte,
        flaw_id=flaw_id,
        limit=limit,
        offset=offset,
        reportable_event_type=reportable_event_type,
        responsibility_scope=responsibility_scope,
        srp_reference_id=srp_reference_id,
        status=status,
        timer_started_at_gte=timer_started_at_gte,
        timer_started_at_lte=timer_started_at_lte,
        title=title,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lte=updated_dt_lte,
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
    *,
    client: AuthenticatedClient,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    reportable_event_type: Union[Unset, str] = UNSET,
    responsibility_scope: Union[Unset, str] = UNSET,
    srp_reference_id: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    timer_started_at_gte: Union[Unset, datetime.datetime] = UNSET,
    timer_started_at_lte: Union[Unset, datetime.datetime] = UNSET,
    title: Union[Unset, str] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[RegulatoryReportingApiV1SrpReportsListResponse200]:
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
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        reportable_event_type (Union[Unset, str]):
        responsibility_scope (Union[Unset, str]):
        srp_reference_id (Union[Unset, str]):
        status (Union[Unset, str]):
        timer_started_at_gte (Union[Unset, datetime.datetime]):
        timer_started_at_lte (Union[Unset, datetime.datetime]):
        title (Union[Unset, str]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsListResponse200
    """

    return sync_detailed(
        client=client,
        created_dt_gte=created_dt_gte,
        created_dt_lte=created_dt_lte,
        flaw_id=flaw_id,
        limit=limit,
        offset=offset,
        reportable_event_type=reportable_event_type,
        responsibility_scope=responsibility_scope,
        srp_reference_id=srp_reference_id,
        status=status,
        timer_started_at_gte=timer_started_at_gte,
        timer_started_at_lte=timer_started_at_lte,
        title=title,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    reportable_event_type: Union[Unset, str] = UNSET,
    responsibility_scope: Union[Unset, str] = UNSET,
    srp_reference_id: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    timer_started_at_gte: Union[Unset, datetime.datetime] = UNSET,
    timer_started_at_lte: Union[Unset, datetime.datetime] = UNSET,
    title: Union[Unset, str] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[RegulatoryReportingApiV1SrpReportsListResponse200]:
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
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        reportable_event_type (Union[Unset, str]):
        responsibility_scope (Union[Unset, str]):
        srp_reference_id (Union[Unset, str]):
        status (Union[Unset, str]):
        timer_started_at_gte (Union[Unset, datetime.datetime]):
        timer_started_at_lte (Union[Unset, datetime.datetime]):
        title (Union[Unset, str]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        created_dt_gte=created_dt_gte,
        created_dt_lte=created_dt_lte,
        flaw_id=flaw_id,
        limit=limit,
        offset=offset,
        reportable_event_type=reportable_event_type,
        responsibility_scope=responsibility_scope,
        srp_reference_id=srp_reference_id,
        status=status,
        timer_started_at_gte=timer_started_at_gte,
        timer_started_at_lte=timer_started_at_lte,
        title=title,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lte=updated_dt_lte,
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
    *,
    client: AuthenticatedClient,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    reportable_event_type: Union[Unset, str] = UNSET,
    responsibility_scope: Union[Unset, str] = UNSET,
    srp_reference_id: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    timer_started_at_gte: Union[Unset, datetime.datetime] = UNSET,
    timer_started_at_lte: Union[Unset, datetime.datetime] = UNSET,
    title: Union[Unset, str] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[RegulatoryReportingApiV1SrpReportsListResponse200]:
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
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        reportable_event_type (Union[Unset, str]):
        responsibility_scope (Union[Unset, str]):
        srp_reference_id (Union[Unset, str]):
        status (Union[Unset, str]):
        timer_started_at_gte (Union[Unset, datetime.datetime]):
        timer_started_at_lte (Union[Unset, datetime.datetime]):
        title (Union[Unset, str]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            created_dt_gte=created_dt_gte,
            created_dt_lte=created_dt_lte,
            flaw_id=flaw_id,
            limit=limit,
            offset=offset,
            reportable_event_type=reportable_event_type,
            responsibility_scope=responsibility_scope,
            srp_reference_id=srp_reference_id,
            status=status,
            timer_started_at_gte=timer_started_at_gte,
            timer_started_at_lte=timer_started_at_lte,
            title=title,
            updated_dt_gte=updated_dt_gte,
            updated_dt_lte=updated_dt_lte,
            uuid=uuid,
        )
    ).parsed
