from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.regulatory_reporting_api_v1_flaw_upstream_mappings_destroy_response_204 import (
    RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    mapping_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/regulatory-reporting/api/v1/flaw-upstream-mappings/{mapping_uuid}".format(
            mapping_uuid=mapping_uuid,
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204]:
    if response.status_code == 204:
        _response_204 = response.json()
        response_204: RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204
        if isinstance(_response_204, Unset):
            response_204 = UNSET
        else:
            response_204 = RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204.from_dict(
                _response_204
            )

        return response_204


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    mapping_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204]:
    """API endpoint for updating and deleting a single flaw-to-upstream mapping.

    Args:
        mapping_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204]
    """

    kwargs = _get_kwargs(
        mapping_uuid=mapping_uuid,
        client=client,
    )

    response = requests.delete(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(client=client, response=response)


def sync(
    mapping_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204]:
    """API endpoint for updating and deleting a single flaw-to-upstream mapping.

    Args:
        mapping_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204
    """

    return sync_detailed(
        mapping_uuid=mapping_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    mapping_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204]:
    """API endpoint for updating and deleting a single flaw-to-upstream mapping.

    Args:
        mapping_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204]
    """

    kwargs = _get_kwargs(
        mapping_uuid=mapping_uuid,
        client=client,
    )

    async with client.get_async_session().delete(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(client=client, response=resp)


async def asyncio(
    mapping_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204]:
    """API endpoint for updating and deleting a single flaw-to-upstream mapping.

    Args:
        mapping_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegulatoryReportingApiV1FlawUpstreamMappingsDestroyResponse204
    """

    return (
        await asyncio_detailed(
            mapping_uuid=mapping_uuid,
            client=client,
        )
    ).parsed
