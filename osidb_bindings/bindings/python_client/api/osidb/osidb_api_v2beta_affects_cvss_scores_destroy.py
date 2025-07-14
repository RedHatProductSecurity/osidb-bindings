from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v2_beta_affects_cvss_scores_destroy_response_204 import (
    OsidbApiV2BetaAffectsCvssScoresDestroyResponse204,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    affect_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v2beta/affects/{affect_id}/cvss-scores/{id}".format(
            affect_id=affect_id,
            id=id,
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV2BetaAffectsCvssScoresDestroyResponse204]:
    if response.status_code == 204:
        _response_204 = response.json()
        response_204: OsidbApiV2BetaAffectsCvssScoresDestroyResponse204
        if isinstance(_response_204, Unset):
            response_204 = UNSET
        else:
            response_204 = OsidbApiV2BetaAffectsCvssScoresDestroyResponse204.from_dict(
                _response_204
            )

        return response_204


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV2BetaAffectsCvssScoresDestroyResponse204]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    affect_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV2BetaAffectsCvssScoresDestroyResponse204]:
    """
    Args:
        affect_id (UUID):
        id (str):
        bugzilla_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2BetaAffectsCvssScoresDestroyResponse204]
    """

    kwargs = _get_kwargs(
        affect_id=affect_id,
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
    affect_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV2BetaAffectsCvssScoresDestroyResponse204]:
    """
    Args:
        affect_id (UUID):
        id (str):
        bugzilla_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2BetaAffectsCvssScoresDestroyResponse204
    """

    return sync_detailed(
        affect_id=affect_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    affect_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV2BetaAffectsCvssScoresDestroyResponse204]:
    """
    Args:
        affect_id (UUID):
        id (str):
        bugzilla_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2BetaAffectsCvssScoresDestroyResponse204]
    """

    kwargs = _get_kwargs(
        affect_id=affect_id,
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
    affect_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV2BetaAffectsCvssScoresDestroyResponse204]:
    """
    Args:
        affect_id (UUID):
        id (str):
        bugzilla_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2BetaAffectsCvssScoresDestroyResponse204
    """

    return (
        await asyncio_detailed(
            affect_id=affect_id,
            id=id,
            client=client,
        )
    ).parsed
