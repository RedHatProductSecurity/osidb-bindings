from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_flaws_acknowledgments_destroy_response_200 import (
    OsidbApiV1FlawsAcknowledgmentsDestroyResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    flaw_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/flaws/{flaw_id}/acknowledgments/{id}".format(
            flaw_id=flaw_id,
            id=id,
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsAcknowledgmentsDestroyResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsAcknowledgmentsDestroyResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    flaw_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    """Destroy the instance and proxy the delete to Bugzilla

    Args:
        flaw_id (UUID):
        id (str):
        bugzilla_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        id=id,
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
    flaw_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    """Destroy the instance and proxy the delete to Bugzilla

    Args:
        flaw_id (UUID):
        id (str):
        bugzilla_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsAcknowledgmentsDestroyResponse200
    """

    return sync_detailed(
        flaw_id=flaw_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    flaw_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    """Destroy the instance and proxy the delete to Bugzilla

    Args:
        flaw_id (UUID):
        id (str):
        bugzilla_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        id=id,
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
    flaw_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    """Destroy the instance and proxy the delete to Bugzilla

    Args:
        flaw_id (UUID):
        id (str):
        bugzilla_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsAcknowledgmentsDestroyResponse200
    """

    return (
        await asyncio_detailed(
            flaw_id=flaw_id,
            id=id,
            client=client,
        )
    ).parsed
