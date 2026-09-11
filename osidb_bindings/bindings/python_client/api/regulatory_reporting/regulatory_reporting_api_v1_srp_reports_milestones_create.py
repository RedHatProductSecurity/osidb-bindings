from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.regulatory_reporting_api_v1_srp_reports_milestones_create_response_201 import (
    RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201,
)
from ...models.srp_report_milestone_create_request import (
    SRPReportMilestoneCreateRequest,
)
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = SRPReportMilestoneCreateRequest


def _get_kwargs(
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        SRPReportMilestoneCreateRequest,
        SRPReportMilestoneCreateRequest,
        SRPReportMilestoneCreateRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/srp-reports/{report_uuid}/milestones".format(
            report_uuid=report_uuid,
        ),
    }

    if check_nested_instance(body, SRPReportMilestoneCreateRequest):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201]:
    if response.status_code == 201:
        _response_201 = response.json()
        response_201: RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201
        if isinstance(_response_201, Unset):
            response_201 = UNSET
        else:
            response_201 = (
                RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201.from_dict(
                    _response_201
                )
            )

        return response_201


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201]:
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
    body: Union[
        SRPReportMilestoneCreateRequest,
        SRPReportMilestoneCreateRequest,
        SRPReportMilestoneCreateRequest,
    ],
) -> Response[RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201]:
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
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201]
    """

    kwargs = _get_kwargs(
        report_uuid=report_uuid,
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
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        SRPReportMilestoneCreateRequest,
        SRPReportMilestoneCreateRequest,
        SRPReportMilestoneCreateRequest,
    ],
) -> Optional[RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201]:
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
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201
    """

    return sync_detailed(
        report_uuid=report_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        SRPReportMilestoneCreateRequest,
        SRPReportMilestoneCreateRequest,
        SRPReportMilestoneCreateRequest,
    ],
) -> Response[RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201]:
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
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201]
    """

    kwargs = _get_kwargs(
        report_uuid=report_uuid,
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
    report_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        SRPReportMilestoneCreateRequest,
        SRPReportMilestoneCreateRequest,
        SRPReportMilestoneCreateRequest,
    ],
) -> Optional[RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201]:
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
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.
        body (SRPReportMilestoneCreateRequest): Serializer for creating SRP Report Milestones.

            Only additional_information_response milestones can be created via the API;
            all other milestone types are auto-created by signals.
            ACLs are inherited from the parent report in the view's perform_create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1SrpReportsMilestonesCreateResponse201
    """

    return (
        await asyncio_detailed(
            report_uuid=report_uuid,
            client=client,
            body=body,
        )
    ).parsed
