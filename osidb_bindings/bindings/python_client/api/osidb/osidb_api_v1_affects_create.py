from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.affect_post_request import AffectPostRequest
from ...models.osidb_api_v1_affects_create_response_201 import (
    OsidbApiV1AffectsCreateResponse201,
)
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = AffectPostRequest


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectPostRequest,
        AffectPostRequest,
        AffectPostRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/affects",
    }

    if check_nested_instance(body, AffectPostRequest):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1AffectsCreateResponse201]:
    if response.status_code == 201:
        _response_201 = response.json()
        response_201: OsidbApiV1AffectsCreateResponse201
        if isinstance(_response_201, Unset):
            response_201 = UNSET
        else:
            response_201 = OsidbApiV1AffectsCreateResponse201.from_dict(_response_201)

        return response_201


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1AffectsCreateResponse201]:
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
        AffectPostRequest,
        AffectPostRequest,
        AffectPostRequest,
    ],
) -> Response[OsidbApiV1AffectsCreateResponse201]:
    """
    Args:
        bugzilla_api_key (Union[Unset, str]):
        jira_api_key (Union[Unset, str]):
        body (AffectPostRequest): Affect serializer
        body (AffectPostRequest): Affect serializer
        body (AffectPostRequest): Affect serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AffectsCreateResponse201]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectPostRequest,
        AffectPostRequest,
        AffectPostRequest,
    ],
) -> Optional[OsidbApiV1AffectsCreateResponse201]:
    """
    Args:
        bugzilla_api_key (Union[Unset, str]):
        jira_api_key (Union[Unset, str]):
        body (AffectPostRequest): Affect serializer
        body (AffectPostRequest): Affect serializer
        body (AffectPostRequest): Affect serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AffectsCreateResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectPostRequest,
        AffectPostRequest,
        AffectPostRequest,
    ],
) -> Response[OsidbApiV1AffectsCreateResponse201]:
    """
    Args:
        bugzilla_api_key (Union[Unset, str]):
        jira_api_key (Union[Unset, str]):
        body (AffectPostRequest): Affect serializer
        body (AffectPostRequest): Affect serializer
        body (AffectPostRequest): Affect serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AffectsCreateResponse201]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    body: Union[
        AffectPostRequest,
        AffectPostRequest,
        AffectPostRequest,
    ],
) -> Optional[OsidbApiV1AffectsCreateResponse201]:
    """
    Args:
        bugzilla_api_key (Union[Unset, str]):
        jira_api_key (Union[Unset, str]):
        body (AffectPostRequest): Affect serializer
        body (AffectPostRequest): Affect serializer
        body (AffectPostRequest): Affect serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AffectsCreateResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
