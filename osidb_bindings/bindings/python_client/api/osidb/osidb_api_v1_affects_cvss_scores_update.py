from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.affect_cvss_put import AffectCVSSPut
from ...models.osidb_api_v1_affects_cvss_scores_update_response_200 import (
    OsidbApiV1AffectsCvssScoresUpdateResponse200,
)
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = AffectCVSSPut


def _get_kwargs(
    affect_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectCVSSPut,
        AffectCVSSPut,
        AffectCVSSPut,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/affects/{affect_id}/cvss_scores/{id}".format(
            affect_id=affect_id,
            id=id,
        ),
    }

    if check_nested_instance(body, AffectCVSSPut):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1AffectsCvssScoresUpdateResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1AffectsCvssScoresUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AffectsCvssScoresUpdateResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1AffectsCvssScoresUpdateResponse200]:
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
    body: Union[
        AffectCVSSPut,
        AffectCVSSPut,
        AffectCVSSPut,
    ],
) -> Response[OsidbApiV1AffectsCvssScoresUpdateResponse200]:
    """
    Args:
        affect_id (UUID):
        id (str):
        bugzilla_api_key (str):
        body (AffectCVSSPut): AffectCVSS serializer
        body (AffectCVSSPut): AffectCVSS serializer
        body (AffectCVSSPut): AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AffectsCvssScoresUpdateResponse200]
    """

    kwargs = _get_kwargs(
        affect_id=affect_id,
        id=id,
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
    affect_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectCVSSPut,
        AffectCVSSPut,
        AffectCVSSPut,
    ],
) -> Optional[OsidbApiV1AffectsCvssScoresUpdateResponse200]:
    """
    Args:
        affect_id (UUID):
        id (str):
        bugzilla_api_key (str):
        body (AffectCVSSPut): AffectCVSS serializer
        body (AffectCVSSPut): AffectCVSS serializer
        body (AffectCVSSPut): AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AffectsCvssScoresUpdateResponse200
    """

    return sync_detailed(
        affect_id=affect_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    affect_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectCVSSPut,
        AffectCVSSPut,
        AffectCVSSPut,
    ],
) -> Response[OsidbApiV1AffectsCvssScoresUpdateResponse200]:
    """
    Args:
        affect_id (UUID):
        id (str):
        bugzilla_api_key (str):
        body (AffectCVSSPut): AffectCVSS serializer
        body (AffectCVSSPut): AffectCVSS serializer
        body (AffectCVSSPut): AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AffectsCvssScoresUpdateResponse200]
    """

    kwargs = _get_kwargs(
        affect_id=affect_id,
        id=id,
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
    affect_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectCVSSPut,
        AffectCVSSPut,
        AffectCVSSPut,
    ],
) -> Optional[OsidbApiV1AffectsCvssScoresUpdateResponse200]:
    """
    Args:
        affect_id (UUID):
        id (str):
        bugzilla_api_key (str):
        body (AffectCVSSPut): AffectCVSS serializer
        body (AffectCVSSPut): AffectCVSS serializer
        body (AffectCVSSPut): AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AffectsCvssScoresUpdateResponse200
    """

    return (
        await asyncio_detailed(
            affect_id=affect_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
