from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.additional_information_request_request import (
    AdditionalInformationRequestRequest,
)
from ...models.regulatory_reporting_api_v1_srp_reports_milestones_additional_information_requests_update_response_200 import (
    RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200,
)
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = AdditionalInformationRequestRequest


def _get_kwargs(
    report_uuid: str,
    milestone_uuid: str,
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AdditionalInformationRequestRequest,
        AdditionalInformationRequestRequest,
        AdditionalInformationRequestRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-information-requests/{uuid}".format(
            report_uuid=report_uuid,
            milestone_uuid=milestone_uuid,
            uuid=uuid,
        ),
    }

    if check_nested_instance(body, AdditionalInformationRequestRequest):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[
    RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200
]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[
    RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    report_uuid: str,
    milestone_uuid: str,
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AdditionalInformationRequestRequest,
        AdditionalInformationRequestRequest,
        AdditionalInformationRequestRequest,
    ],
) -> Response[
    RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200
]:
    """ViewSet for Additional Information Requests (nested under milestones).

    Supports:
    -GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -POST /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -PUT /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}

    Args:
        report_uuid (str):
        milestone_uuid (str):
        uuid (str):
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200]
    """

    kwargs = _get_kwargs(
        report_uuid=report_uuid,
        milestone_uuid=milestone_uuid,
        uuid=uuid,
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
    report_uuid: str,
    milestone_uuid: str,
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AdditionalInformationRequestRequest,
        AdditionalInformationRequestRequest,
        AdditionalInformationRequestRequest,
    ],
) -> Optional[
    RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200
]:
    """ViewSet for Additional Information Requests (nested under milestones).

    Supports:
    -GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -POST /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -PUT /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}

    Args:
        report_uuid (str):
        milestone_uuid (str):
        uuid (str):
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200
    """

    return sync_detailed(
        report_uuid=report_uuid,
        milestone_uuid=milestone_uuid,
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    report_uuid: str,
    milestone_uuid: str,
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AdditionalInformationRequestRequest,
        AdditionalInformationRequestRequest,
        AdditionalInformationRequestRequest,
    ],
) -> Response[
    RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200
]:
    """ViewSet for Additional Information Requests (nested under milestones).

    Supports:
    -GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -POST /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -PUT /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}

    Args:
        report_uuid (str):
        milestone_uuid (str):
        uuid (str):
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200]
    """

    kwargs = _get_kwargs(
        report_uuid=report_uuid,
        milestone_uuid=milestone_uuid,
        uuid=uuid,
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
    report_uuid: str,
    milestone_uuid: str,
    uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AdditionalInformationRequestRequest,
        AdditionalInformationRequestRequest,
        AdditionalInformationRequestRequest,
    ],
) -> Optional[
    RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200
]:
    """ViewSet for Additional Information Requests (nested under milestones).

    Supports:
    -GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -GET /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -POST /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}
    -PUT /regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones/{milestone_uuid}/additional-
    information-requests/{uuid}

    Args:
        report_uuid (str):
        milestone_uuid (str):
        uuid (str):
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.
        body (AdditionalInformationRequestRequest): Serializer for Additional Information Requests
            nested under a milestone.

            Includes computed fields for deadline tracking, mirroring
            SRPReportMilestoneSerializer's due_at/hours_remaining/days_remaining/
            is_overdue pattern.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsMilestonesAdditionalInformationRequestsUpdateResponse200
    """

    return (
        await asyncio_detailed(
            report_uuid=report_uuid,
            milestone_uuid=milestone_uuid,
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
