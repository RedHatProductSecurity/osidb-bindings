from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_integrations_retrieve_response_200 import (
    OsidbIntegrationsRetrieveResponse200,
)
from ...models.osidb_integrations_retrieve_response_503 import (
    OsidbIntegrationsRetrieveResponse503,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/integrations",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[
    Union[OsidbIntegrationsRetrieveResponse200, OsidbIntegrationsRetrieveResponse503]
]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbIntegrationsRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbIntegrationsRetrieveResponse200.from_dict(_response_200)

        return response_200
    if response.status_code == 503:
        _response_503 = response.json()
        response_503: OsidbIntegrationsRetrieveResponse503
        if isinstance(_response_503, Unset):
            response_503 = UNSET
        else:
            response_503 = OsidbIntegrationsRetrieveResponse503.from_dict(_response_503)

        return response_503


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[
    Union[OsidbIntegrationsRetrieveResponse200, OsidbIntegrationsRetrieveResponse503]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[OsidbIntegrationsRetrieveResponse200, OsidbIntegrationsRetrieveResponse503]
]:
    """Set third-party integration tokens for the current user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OsidbIntegrationsRetrieveResponse200, OsidbIntegrationsRetrieveResponse503]]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[OsidbIntegrationsRetrieveResponse200, OsidbIntegrationsRetrieveResponse503]
]:
    """Set third-party integration tokens for the current user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OsidbIntegrationsRetrieveResponse200, OsidbIntegrationsRetrieveResponse503]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[OsidbIntegrationsRetrieveResponse200, OsidbIntegrationsRetrieveResponse503]
]:
    """Set third-party integration tokens for the current user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OsidbIntegrationsRetrieveResponse200, OsidbIntegrationsRetrieveResponse503]]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[OsidbIntegrationsRetrieveResponse200, OsidbIntegrationsRetrieveResponse503]
]:
    """Set third-party integration tokens for the current user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OsidbIntegrationsRetrieveResponse200, OsidbIntegrationsRetrieveResponse503]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
