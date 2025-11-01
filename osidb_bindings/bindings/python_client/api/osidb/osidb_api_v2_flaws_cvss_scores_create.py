from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.flaw_cvssv2_post_request import FlawCVSSV2PostRequest
from ...models.osidb_api_v2_flaws_cvss_scores_create_response_201 import (
    OsidbApiV2FlawsCvssScoresCreateResponse201,
)
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = FlawCVSSV2PostRequest


def _get_kwargs(
    flaw_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawCVSSV2PostRequest,
        FlawCVSSV2PostRequest,
        FlawCVSSV2PostRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v2/flaws/{flaw_id}/cvss-scores".format(
            flaw_id=flaw_id,
        ),
    }

    if check_nested_instance(body, FlawCVSSV2PostRequest):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV2FlawsCvssScoresCreateResponse201]:
    if response.status_code == 201:
        _response_201 = response.json()
        response_201: OsidbApiV2FlawsCvssScoresCreateResponse201
        if isinstance(_response_201, Unset):
            response_201 = UNSET
        else:
            response_201 = OsidbApiV2FlawsCvssScoresCreateResponse201.from_dict(
                _response_201
            )

        return response_201


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV2FlawsCvssScoresCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    flaw_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawCVSSV2PostRequest,
        FlawCVSSV2PostRequest,
        FlawCVSSV2PostRequest,
    ],
) -> Response[OsidbApiV2FlawsCvssScoresCreateResponse201]:
    """
    Args:
        flaw_id (UUID):
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2FlawsCvssScoresCreateResponse201]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
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
    flaw_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawCVSSV2PostRequest,
        FlawCVSSV2PostRequest,
        FlawCVSSV2PostRequest,
    ],
) -> Optional[OsidbApiV2FlawsCvssScoresCreateResponse201]:
    """
    Args:
        flaw_id (UUID):
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2FlawsCvssScoresCreateResponse201
    """

    return sync_detailed(
        flaw_id=flaw_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    flaw_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawCVSSV2PostRequest,
        FlawCVSSV2PostRequest,
        FlawCVSSV2PostRequest,
    ],
) -> Response[OsidbApiV2FlawsCvssScoresCreateResponse201]:
    """
    Args:
        flaw_id (UUID):
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2FlawsCvssScoresCreateResponse201]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
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
    flaw_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawCVSSV2PostRequest,
        FlawCVSSV2PostRequest,
        FlawCVSSV2PostRequest,
    ],
) -> Optional[OsidbApiV2FlawsCvssScoresCreateResponse201]:
    """
    Args:
        flaw_id (UUID):
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer
        body (FlawCVSSV2PostRequest): Abstract serializer for FlawCVSS and AffectCVSS serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2FlawsCvssScoresCreateResponse201
    """

    return (
        await asyncio_detailed(
            flaw_id=flaw_id,
            client=client,
            body=body,
        )
    ).parsed
