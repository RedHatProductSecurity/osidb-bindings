from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.affect_cvss_post import AffectCVSSPost
from ...models.osidb_api_v1_affects_cvss_scores_create_response_201 import (
    OsidbApiV1AffectsCvssScoresCreateResponse201,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = AffectCVSSPost


def _get_kwargs(
    affect_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectCVSSPost,
        AffectCVSSPost,
        AffectCVSSPost,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/affects/{affect_id}/cvss_scores".format(
            affect_id=affect_id,
        ),
    }

    if isinstance(body, AffectCVSSPost):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    if response.status_code == 201:
        # }
        _response_201 = response.json()
        response_201: OsidbApiV1AffectsCvssScoresCreateResponse201
        if isinstance(_response_201, Unset):
            response_201 = UNSET
        else:
            response_201 = OsidbApiV1AffectsCvssScoresCreateResponse201.from_dict(
                _response_201
            )

        return response_201


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    affect_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectCVSSPost,
        AffectCVSSPost,
        AffectCVSSPost,
    ],
) -> Response[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    """
    Args:
        affect_id (UUID):
        bugzilla_api_key (str):
        body (AffectCVSSPost): AffectCVSS serializer
        body (AffectCVSSPost): AffectCVSS serializer
        body (AffectCVSSPost): AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AffectsCvssScoresCreateResponse201]
    """

    kwargs = _get_kwargs(
        affect_id=affect_id,
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
    affect_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectCVSSPost,
        AffectCVSSPost,
        AffectCVSSPost,
    ],
) -> Optional[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    """
    Args:
        affect_id (UUID):
        bugzilla_api_key (str):
        body (AffectCVSSPost): AffectCVSS serializer
        body (AffectCVSSPost): AffectCVSS serializer
        body (AffectCVSSPost): AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AffectsCvssScoresCreateResponse201
    """

    return sync_detailed(
        affect_id=affect_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    affect_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectCVSSPost,
        AffectCVSSPost,
        AffectCVSSPost,
    ],
) -> Response[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    """
    Args:
        affect_id (UUID):
        bugzilla_api_key (str):
        body (AffectCVSSPost): AffectCVSS serializer
        body (AffectCVSSPost): AffectCVSS serializer
        body (AffectCVSSPost): AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AffectsCvssScoresCreateResponse201]
    """

    kwargs = _get_kwargs(
        affect_id=affect_id,
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
    affect_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectCVSSPost,
        AffectCVSSPost,
        AffectCVSSPost,
    ],
) -> Optional[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    """
    Args:
        affect_id (UUID):
        bugzilla_api_key (str):
        body (AffectCVSSPost): AffectCVSS serializer
        body (AffectCVSSPost): AffectCVSS serializer
        body (AffectCVSSPost): AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AffectsCvssScoresCreateResponse201
    """

    return (
        await asyncio_detailed(
            affect_id=affect_id,
            client=client,
            body=body,
        )
    ).parsed
