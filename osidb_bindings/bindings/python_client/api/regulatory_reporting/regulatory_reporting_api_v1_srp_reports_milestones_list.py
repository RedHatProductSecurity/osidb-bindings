import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.regulatory_reporting_api_v1_srp_reports_milestones_list_response_200 import (
    RegulatoryReportingApiV1SrpReportsMilestonesListResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "created_dt__gte": datetime.datetime,
    "created_dt__lte": datetime.datetime,
    "limit": int,
    "milestone_type": str,
    "offset": int,
    "owner": str,
    "request_source": str,
    "request_text": str,
    "srp_report": UUID,
    "status": str,
    "submitted_at__gte": datetime.datetime,
    "submitted_at__lte": datetime.datetime,
    "uuid": UUID,
}


def _get_kwargs(
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    milestone_type: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner: Union[Unset, str] = UNSET,
    request_source: Union[Unset, str] = UNSET,
    request_text: Union[Unset, str] = UNSET,
    srp_report: Union[Unset, UUID] = UNSET,
    status: Union[Unset, str] = UNSET,
    submitted_at_gte: Union[Unset, datetime.datetime] = UNSET,
    submitted_at_lte: Union[Unset, datetime.datetime] = UNSET,
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

    params["limit"] = limit

    params["milestone_type"] = milestone_type

    params["offset"] = offset

    params["owner"] = owner

    params["request_source"] = request_source

    params["request_text"] = request_text

    json_srp_report: Union[Unset, str] = UNSET
    if not isinstance(srp_report, Unset):
        json_srp_report = str(srp_report)

    params["srp_report"] = json_srp_report

    params["status"] = status

    json_submitted_at_gte: Union[Unset, str] = UNSET
    if not isinstance(submitted_at_gte, Unset):
        json_submitted_at_gte = submitted_at_gte.isoformat()

    params["submitted_at__gte"] = json_submitted_at_gte

    json_submitted_at_lte: Union[Unset, str] = UNSET
    if not isinstance(submitted_at_lte, Unset):
        json_submitted_at_lte = submitted_at_lte.isoformat()

    params["submitted_at__lte"] = json_submitted_at_lte

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
        "url": f"{client.base_url}/regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones".format(
            report_uuid=report_uuid,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1SrpReportsMilestonesListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: RegulatoryReportingApiV1SrpReportsMilestonesListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = (
                RegulatoryReportingApiV1SrpReportsMilestonesListResponse200.from_dict(
                    _response_200
                )
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1SrpReportsMilestonesListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    milestone_type: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner: Union[Unset, str] = UNSET,
    request_source: Union[Unset, str] = UNSET,
    request_text: Union[Unset, str] = UNSET,
    srp_report: Union[Unset, UUID] = UNSET,
    status: Union[Unset, str] = UNSET,
    submitted_at_gte: Union[Unset, datetime.datetime] = UNSET,
    submitted_at_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[RegulatoryReportingApiV1SrpReportsMilestonesListResponse200]:
    """ViewSet for SRP Report Milestones (nested under reports).

    Supports:
    - GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones - List milestones for a
    report
    - GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{uuid} - Retrieve single
    milestone
    - POST /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones - Create
    additional_information_response milestone
    - PUT /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{uuid} - Update

    Standard milestones (24h, 72h, final) are auto-created by signals.
    Only additional_information_response milestones can be created via POST.
    PATCH is globally blacklisted (BLACKLISTED_HTTP_METHODS).

    Args:
        report_uuid (str):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):
        milestone_type (Union[Unset, str]):
        offset (Union[Unset, int]):
        owner (Union[Unset, str]):
        request_source (Union[Unset, str]):
        request_text (Union[Unset, str]):
        srp_report (Union[Unset, UUID]):
        status (Union[Unset, str]):
        submitted_at_gte (Union[Unset, datetime.datetime]):
        submitted_at_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsMilestonesListResponse200]
    """

    kwargs = _get_kwargs(
        report_uuid=report_uuid,
        client=client,
        created_dt_gte=created_dt_gte,
        created_dt_lte=created_dt_lte,
        limit=limit,
        milestone_type=milestone_type,
        offset=offset,
        owner=owner,
        request_source=request_source,
        request_text=request_text,
        srp_report=srp_report,
        status=status,
        submitted_at_gte=submitted_at_gte,
        submitted_at_lte=submitted_at_lte,
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
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    milestone_type: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner: Union[Unset, str] = UNSET,
    request_source: Union[Unset, str] = UNSET,
    request_text: Union[Unset, str] = UNSET,
    srp_report: Union[Unset, UUID] = UNSET,
    status: Union[Unset, str] = UNSET,
    submitted_at_gte: Union[Unset, datetime.datetime] = UNSET,
    submitted_at_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[RegulatoryReportingApiV1SrpReportsMilestonesListResponse200]:
    """ViewSet for SRP Report Milestones (nested under reports).

    Supports:
    - GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones - List milestones for a
    report
    - GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{uuid} - Retrieve single
    milestone
    - POST /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones - Create
    additional_information_response milestone
    - PUT /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{uuid} - Update

    Standard milestones (24h, 72h, final) are auto-created by signals.
    Only additional_information_response milestones can be created via POST.
    PATCH is globally blacklisted (BLACKLISTED_HTTP_METHODS).

    Args:
        report_uuid (str):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):
        milestone_type (Union[Unset, str]):
        offset (Union[Unset, int]):
        owner (Union[Unset, str]):
        request_source (Union[Unset, str]):
        request_text (Union[Unset, str]):
        srp_report (Union[Unset, UUID]):
        status (Union[Unset, str]):
        submitted_at_gte (Union[Unset, datetime.datetime]):
        submitted_at_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsMilestonesListResponse200
    """

    return sync_detailed(
        report_uuid=report_uuid,
        client=client,
        created_dt_gte=created_dt_gte,
        created_dt_lte=created_dt_lte,
        limit=limit,
        milestone_type=milestone_type,
        offset=offset,
        owner=owner,
        request_source=request_source,
        request_text=request_text,
        srp_report=srp_report,
        status=status,
        submitted_at_gte=submitted_at_gte,
        submitted_at_lte=submitted_at_lte,
        uuid=uuid,
    ).parsed


async def asyncio_detailed(
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    milestone_type: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner: Union[Unset, str] = UNSET,
    request_source: Union[Unset, str] = UNSET,
    request_text: Union[Unset, str] = UNSET,
    srp_report: Union[Unset, UUID] = UNSET,
    status: Union[Unset, str] = UNSET,
    submitted_at_gte: Union[Unset, datetime.datetime] = UNSET,
    submitted_at_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[RegulatoryReportingApiV1SrpReportsMilestonesListResponse200]:
    """ViewSet for SRP Report Milestones (nested under reports).

    Supports:
    - GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones - List milestones for a
    report
    - GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{uuid} - Retrieve single
    milestone
    - POST /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones - Create
    additional_information_response milestone
    - PUT /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{uuid} - Update

    Standard milestones (24h, 72h, final) are auto-created by signals.
    Only additional_information_response milestones can be created via POST.
    PATCH is globally blacklisted (BLACKLISTED_HTTP_METHODS).

    Args:
        report_uuid (str):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):
        milestone_type (Union[Unset, str]):
        offset (Union[Unset, int]):
        owner (Union[Unset, str]):
        request_source (Union[Unset, str]):
        request_text (Union[Unset, str]):
        srp_report (Union[Unset, UUID]):
        status (Union[Unset, str]):
        submitted_at_gte (Union[Unset, datetime.datetime]):
        submitted_at_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsMilestonesListResponse200]
    """

    kwargs = _get_kwargs(
        report_uuid=report_uuid,
        client=client,
        created_dt_gte=created_dt_gte,
        created_dt_lte=created_dt_lte,
        limit=limit,
        milestone_type=milestone_type,
        offset=offset,
        owner=owner,
        request_source=request_source,
        request_text=request_text,
        srp_report=srp_report,
        status=status,
        submitted_at_gte=submitted_at_gte,
        submitted_at_lte=submitted_at_lte,
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
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    milestone_type: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    owner: Union[Unset, str] = UNSET,
    request_source: Union[Unset, str] = UNSET,
    request_text: Union[Unset, str] = UNSET,
    srp_report: Union[Unset, UUID] = UNSET,
    status: Union[Unset, str] = UNSET,
    submitted_at_gte: Union[Unset, datetime.datetime] = UNSET,
    submitted_at_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[RegulatoryReportingApiV1SrpReportsMilestonesListResponse200]:
    """ViewSet for SRP Report Milestones (nested under reports).

    Supports:
    - GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones - List milestones for a
    report
    - GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{uuid} - Retrieve single
    milestone
    - POST /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones - Create
    additional_information_response milestone
    - PUT /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{uuid} - Update

    Standard milestones (24h, 72h, final) are auto-created by signals.
    Only additional_information_response milestones can be created via POST.
    PATCH is globally blacklisted (BLACKLISTED_HTTP_METHODS).

    Args:
        report_uuid (str):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):
        milestone_type (Union[Unset, str]):
        offset (Union[Unset, int]):
        owner (Union[Unset, str]):
        request_source (Union[Unset, str]):
        request_text (Union[Unset, str]):
        srp_report (Union[Unset, UUID]):
        status (Union[Unset, str]):
        submitted_at_gte (Union[Unset, datetime.datetime]):
        submitted_at_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsMilestonesListResponse200
    """

    return (
        await asyncio_detailed(
            report_uuid=report_uuid,
            client=client,
            created_dt_gte=created_dt_gte,
            created_dt_lte=created_dt_lte,
            limit=limit,
            milestone_type=milestone_type,
            offset=offset,
            owner=owner,
            request_source=request_source,
            request_text=request_text,
            srp_report=srp_report,
            status=status,
            submitted_at_gte=submitted_at_gte,
            submitted_at_lte=submitted_at_lte,
            uuid=uuid,
        )
    ).parsed
