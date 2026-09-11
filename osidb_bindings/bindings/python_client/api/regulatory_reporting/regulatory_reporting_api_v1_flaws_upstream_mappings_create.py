from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.flaw_upstream_mapping_request import FlawUpstreamMappingRequest
from ...models.regulatory_reporting_api_v1_flaws_upstream_mappings_create_response_201 import (
    RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201,
)
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = FlawUpstreamMappingRequest


def _get_kwargs(
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawUpstreamMappingRequest,
        FlawUpstreamMappingRequest,
        FlawUpstreamMappingRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/flaws/{flaw_uuid}/upstream-mappings".format(
            flaw_uuid=flaw_uuid,
        ),
    }

    if check_nested_instance(body, FlawUpstreamMappingRequest):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201]:
    if response.status_code == 201:
        _response_201 = response.json()
        response_201: RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201
        if isinstance(_response_201, Unset):
            response_201 = UNSET
        else:
            response_201 = RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201.from_dict(
                _response_201
            )

        return response_201


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawUpstreamMappingRequest,
        FlawUpstreamMappingRequest,
        FlawUpstreamMappingRequest,
    ],
) -> Response[RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201]:
    """API endpoint for listing and creating flaw-to-upstream mappings

    Args:
        flaw_uuid (str):
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201]
    """

    kwargs = _get_kwargs(
        flaw_uuid=flaw_uuid,
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
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawUpstreamMappingRequest,
        FlawUpstreamMappingRequest,
        FlawUpstreamMappingRequest,
    ],
) -> Optional[RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201]:
    """API endpoint for listing and creating flaw-to-upstream mappings

    Args:
        flaw_uuid (str):
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201
    """

    return sync_detailed(
        flaw_uuid=flaw_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawUpstreamMappingRequest,
        FlawUpstreamMappingRequest,
        FlawUpstreamMappingRequest,
    ],
) -> Response[RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201]:
    """API endpoint for listing and creating flaw-to-upstream mappings

    Args:
        flaw_uuid (str):
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201]
    """

    kwargs = _get_kwargs(
        flaw_uuid=flaw_uuid,
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
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawUpstreamMappingRequest,
        FlawUpstreamMappingRequest,
        FlawUpstreamMappingRequest,
    ],
) -> Optional[RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201]:
    """API endpoint for listing and creating flaw-to-upstream mappings

    Args:
        flaw_uuid (str):
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer
        body (FlawUpstreamMappingRequest): TrackingMixin class serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1FlawsUpstreamMappingsCreateResponse201
    """

    return (
        await asyncio_detailed(
            flaw_uuid=flaw_uuid,
            client=client,
            body=body,
        )
    ).parsed
