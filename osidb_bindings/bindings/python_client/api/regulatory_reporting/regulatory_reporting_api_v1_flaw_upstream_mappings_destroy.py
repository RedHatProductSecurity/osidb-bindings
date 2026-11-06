from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...types import Response

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
) -> Optional[Any]:
    if response.status_code == 204:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[Any]:
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
) -> Response[Any]:
    """API endpoint for updating and deleting a single flaw-to-upstream mapping.

    Args:
        mapping_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    mapping_uuid: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """API endpoint for updating and deleting a single flaw-to-upstream mapping.

    Args:
        mapping_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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
