from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_integrations_partial_update_response_204 import (
    OsidbIntegrationsPartialUpdateResponse204,
)
from ...models.patched_integration_token_patch_request import (
    PatchedIntegrationTokenPatchRequest,
)
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = PatchedIntegrationTokenPatchRequest


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedIntegrationTokenPatchRequest,
        PatchedIntegrationTokenPatchRequest,
        PatchedIntegrationTokenPatchRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/integrations",
    }

    if check_nested_instance(body, PatchedIntegrationTokenPatchRequest):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbIntegrationsPartialUpdateResponse204]:
    if response.status_code == 204:
        _response_204 = response.json()
        response_204: OsidbIntegrationsPartialUpdateResponse204
        if isinstance(_response_204, Unset):
            response_204 = UNSET
        else:
            response_204 = OsidbIntegrationsPartialUpdateResponse204.from_dict(
                _response_204
            )

        return response_204


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbIntegrationsPartialUpdateResponse204]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedIntegrationTokenPatchRequest,
        PatchedIntegrationTokenPatchRequest,
        PatchedIntegrationTokenPatchRequest,
    ],
) -> Response[OsidbIntegrationsPartialUpdateResponse204]:
    """Set third-party integration tokens for the current user.

    Args:
        body (PatchedIntegrationTokenPatchRequest):
        body (PatchedIntegrationTokenPatchRequest):
        body (PatchedIntegrationTokenPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbIntegrationsPartialUpdateResponse204]
    """

    kwargs = _get_kwargs(
        client=client,
        body=body,
    )

    response = requests.patch(
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
    body: Union[
        PatchedIntegrationTokenPatchRequest,
        PatchedIntegrationTokenPatchRequest,
        PatchedIntegrationTokenPatchRequest,
    ],
) -> Optional[OsidbIntegrationsPartialUpdateResponse204]:
    """Set third-party integration tokens for the current user.

    Args:
        body (PatchedIntegrationTokenPatchRequest):
        body (PatchedIntegrationTokenPatchRequest):
        body (PatchedIntegrationTokenPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbIntegrationsPartialUpdateResponse204
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedIntegrationTokenPatchRequest,
        PatchedIntegrationTokenPatchRequest,
        PatchedIntegrationTokenPatchRequest,
    ],
) -> Response[OsidbIntegrationsPartialUpdateResponse204]:
    """Set third-party integration tokens for the current user.

    Args:
        body (PatchedIntegrationTokenPatchRequest):
        body (PatchedIntegrationTokenPatchRequest):
        body (PatchedIntegrationTokenPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbIntegrationsPartialUpdateResponse204]
    """

    kwargs = _get_kwargs(
        client=client,
        body=body,
    )

    async with client.get_async_session().patch(
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
    body: Union[
        PatchedIntegrationTokenPatchRequest,
        PatchedIntegrationTokenPatchRequest,
        PatchedIntegrationTokenPatchRequest,
    ],
) -> Optional[OsidbIntegrationsPartialUpdateResponse204]:
    """Set third-party integration tokens for the current user.

    Args:
        body (PatchedIntegrationTokenPatchRequest):
        body (PatchedIntegrationTokenPatchRequest):
        body (PatchedIntegrationTokenPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbIntegrationsPartialUpdateResponse204
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
