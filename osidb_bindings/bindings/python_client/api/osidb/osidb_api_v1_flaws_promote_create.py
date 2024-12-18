from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_flaws_promote_create_response_200 import (
    OsidbApiV1FlawsPromoteCreateResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/flaws/{flaw_id}/promote".format(
            flaw_id=flaw_id,
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1FlawsPromoteCreateResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsPromoteCreateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsPromoteCreateResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1FlawsPromoteCreateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV1FlawsPromoteCreateResponse200]:
    """workflow promotion API endpoint

    try to adjust workflow classification of flaw to the next state available
    return its workflow:state classification or errors if not possible to promote

    Args:
        flaw_id (str):
        bugzilla_api_key (str):
        jira_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsPromoteCreateResponse200]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
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
    flaw_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1FlawsPromoteCreateResponse200]:
    """workflow promotion API endpoint

    try to adjust workflow classification of flaw to the next state available
    return its workflow:state classification or errors if not possible to promote

    Args:
        flaw_id (str):
        bugzilla_api_key (str):
        jira_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsPromoteCreateResponse200
    """

    return sync_detailed(
        flaw_id=flaw_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV1FlawsPromoteCreateResponse200]:
    """workflow promotion API endpoint

    try to adjust workflow classification of flaw to the next state available
    return its workflow:state classification or errors if not possible to promote

    Args:
        flaw_id (str):
        bugzilla_api_key (str):
        jira_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsPromoteCreateResponse200]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
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
    flaw_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1FlawsPromoteCreateResponse200]:
    """workflow promotion API endpoint

    try to adjust workflow classification of flaw to the next state available
    return its workflow:state classification or errors if not possible to promote

    Args:
        flaw_id (str):
        bugzilla_api_key (str):
        jira_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsPromoteCreateResponse200
    """

    return (
        await asyncio_detailed(
            flaw_id=flaw_id,
            client=client,
        )
    ).parsed
