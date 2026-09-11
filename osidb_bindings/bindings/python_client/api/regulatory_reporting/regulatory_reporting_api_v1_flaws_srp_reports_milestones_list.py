from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.regulatory_reporting_api_v1_flaws_srp_reports_milestones_list_response_200 import (
    RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "limit": int,
    "offset": int,
}


def _get_kwargs(
    flaw_id: str,
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/flaws/{flaw_id}/srp-reports/{report_uuid}/milestones".format(
            flaw_id=flaw_id,
            report_uuid=report_uuid,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    flaw_id: str,
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200]:
    """ViewSet for flaw SRP report milestones (read-only subresource).

    Supports:
    - GET /regulatory-reporting/api/v1/flaws/{flaw_id}/srp-reports/{report_uuid}/milestones - List
    milestones
    - GET /regulatory-reporting/api/v1/flaws/{flaw_id}/srp-reports/{report_uuid}/milestones/{uuid} -
    Retrieve milestone

    Read-only convenience wrapper. Updates must use top-level endpoints.

    Args:
        flaw_id (str):
        report_uuid (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        report_uuid=report_uuid,
        client=client,
        limit=limit,
        offset=offset,
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
    flaw_id: str,
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200]:
    """ViewSet for flaw SRP report milestones (read-only subresource).

    Supports:
    - GET /regulatory-reporting/api/v1/flaws/{flaw_id}/srp-reports/{report_uuid}/milestones - List
    milestones
    - GET /regulatory-reporting/api/v1/flaws/{flaw_id}/srp-reports/{report_uuid}/milestones/{uuid} -
    Retrieve milestone

    Read-only convenience wrapper. Updates must use top-level endpoints.

    Args:
        flaw_id (str):
        report_uuid (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200
    """

    return sync_detailed(
        flaw_id=flaw_id,
        report_uuid=report_uuid,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    flaw_id: str,
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200]:
    """ViewSet for flaw SRP report milestones (read-only subresource).

    Supports:
    - GET /regulatory-reporting/api/v1/flaws/{flaw_id}/srp-reports/{report_uuid}/milestones - List
    milestones
    - GET /regulatory-reporting/api/v1/flaws/{flaw_id}/srp-reports/{report_uuid}/milestones/{uuid} -
    Retrieve milestone

    Read-only convenience wrapper. Updates must use top-level endpoints.

    Args:
        flaw_id (str):
        report_uuid (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        report_uuid=report_uuid,
        client=client,
        limit=limit,
        offset=offset,
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
    flaw_id: str,
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200]:
    """ViewSet for flaw SRP report milestones (read-only subresource).

    Supports:
    - GET /regulatory-reporting/api/v1/flaws/{flaw_id}/srp-reports/{report_uuid}/milestones - List
    milestones
    - GET /regulatory-reporting/api/v1/flaws/{flaw_id}/srp-reports/{report_uuid}/milestones/{uuid} -
    Retrieve milestone

    Read-only convenience wrapper. Updates must use top-level endpoints.

    Args:
        flaw_id (str):
        report_uuid (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1FlawsSrpReportsMilestonesListResponse200
    """

    return (
        await asyncio_detailed(
            flaw_id=flaw_id,
            report_uuid=report_uuid,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
