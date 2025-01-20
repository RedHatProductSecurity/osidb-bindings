from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.affect_post import AffectPost
from ...models.osidb_api_v1_affects_bulk_create_response_200 import (
    OsidbApiV1AffectsBulkCreateResponse200,
)
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = list["AffectPost"]


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    body: Union[
        list["AffectPost"],
        list["AffectPost"],
        list["AffectPost"],
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/affects/bulk",
    }

    if check_nested_instance(body, list["AffectPost"]):
        _json_body: list[dict[str, Any]] = UNSET
        if not isinstance(body, Unset):
            _json_body = []
            for body_item_data in body:
                body_item: dict[str, Any] = UNSET
                if not isinstance(body_item_data, Unset):
                    body_item = body_item_data.to_dict()

                _json_body.append(body_item)

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1AffectsBulkCreateResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1AffectsBulkCreateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AffectsBulkCreateResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1AffectsBulkCreateResponse200]:
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
        list["AffectPost"],
        list["AffectPost"],
        list["AffectPost"],
    ],
) -> Response[OsidbApiV1AffectsBulkCreateResponse200]:
    """Bulk create endpoint. Expects a list of dict Affect objects.

    Args:
        bugzilla_api_key (str):
        body (list['AffectPost']):
        body (list['AffectPost']):
        body (list['AffectPost']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AffectsBulkCreateResponse200]
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
        list["AffectPost"],
        list["AffectPost"],
        list["AffectPost"],
    ],
) -> Optional[OsidbApiV1AffectsBulkCreateResponse200]:
    """Bulk create endpoint. Expects a list of dict Affect objects.

    Args:
        bugzilla_api_key (str):
        body (list['AffectPost']):
        body (list['AffectPost']):
        body (list['AffectPost']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AffectsBulkCreateResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        list["AffectPost"],
        list["AffectPost"],
        list["AffectPost"],
    ],
) -> Response[OsidbApiV1AffectsBulkCreateResponse200]:
    """Bulk create endpoint. Expects a list of dict Affect objects.

    Args:
        bugzilla_api_key (str):
        body (list['AffectPost']):
        body (list['AffectPost']):
        body (list['AffectPost']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AffectsBulkCreateResponse200]
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
        list["AffectPost"],
        list["AffectPost"],
        list["AffectPost"],
    ],
) -> Optional[OsidbApiV1AffectsBulkCreateResponse200]:
    """Bulk create endpoint. Expects a list of dict Affect objects.

    Args:
        bugzilla_api_key (str):
        body (list['AffectPost']):
        body (list['AffectPost']):
        body (list['AffectPost']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AffectsBulkCreateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
