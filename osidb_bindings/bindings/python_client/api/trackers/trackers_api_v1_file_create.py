from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.flaw_uuid_list_request import FlawUUIDListRequest
from ...models.trackers_api_v1_file_create_response_200 import (
    TrackersApiV1FileCreateResponse200,
)
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {
    "exclude_existing_trackers": bool,
}

REQUEST_BODY_TYPE = FlawUUIDListRequest


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawUUIDListRequest,
        FlawUUIDListRequest,
        FlawUUIDListRequest,
    ],
    exclude_existing_trackers: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["exclude_existing_trackers"] = exclude_existing_trackers

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/trackers/api/v1/file",
        "params": params,
    }

    if check_nested_instance(body, FlawUUIDListRequest):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[TrackersApiV1FileCreateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: TrackersApiV1FileCreateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = TrackersApiV1FileCreateResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[TrackersApiV1FileCreateResponse200]:
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
        FlawUUIDListRequest,
        FlawUUIDListRequest,
        FlawUUIDListRequest,
    ],
    exclude_existing_trackers: Union[Unset, bool] = UNSET,
) -> Response[TrackersApiV1FileCreateResponse200]:
    """Given a list of flaws, generates a list of suggested trackers to file.

    Args:
        exclude_existing_trackers (Union[Unset, bool]):
        body (FlawUUIDListRequest):
        body (FlawUUIDListRequest):
        body (FlawUUIDListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrackersApiV1FileCreateResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        body=body,
        exclude_existing_trackers=exclude_existing_trackers,
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
        FlawUUIDListRequest,
        FlawUUIDListRequest,
        FlawUUIDListRequest,
    ],
    exclude_existing_trackers: Union[Unset, bool] = UNSET,
) -> Optional[TrackersApiV1FileCreateResponse200]:
    """Given a list of flaws, generates a list of suggested trackers to file.

    Args:
        exclude_existing_trackers (Union[Unset, bool]):
        body (FlawUUIDListRequest):
        body (FlawUUIDListRequest):
        body (FlawUUIDListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrackersApiV1FileCreateResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        exclude_existing_trackers=exclude_existing_trackers,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        FlawUUIDListRequest,
        FlawUUIDListRequest,
        FlawUUIDListRequest,
    ],
    exclude_existing_trackers: Union[Unset, bool] = UNSET,
) -> Response[TrackersApiV1FileCreateResponse200]:
    """Given a list of flaws, generates a list of suggested trackers to file.

    Args:
        exclude_existing_trackers (Union[Unset, bool]):
        body (FlawUUIDListRequest):
        body (FlawUUIDListRequest):
        body (FlawUUIDListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrackersApiV1FileCreateResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        body=body,
        exclude_existing_trackers=exclude_existing_trackers,
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
        FlawUUIDListRequest,
        FlawUUIDListRequest,
        FlawUUIDListRequest,
    ],
    exclude_existing_trackers: Union[Unset, bool] = UNSET,
) -> Optional[TrackersApiV1FileCreateResponse200]:
    """Given a list of flaws, generates a list of suggested trackers to file.

    Args:
        exclude_existing_trackers (Union[Unset, bool]):
        body (FlawUUIDListRequest):
        body (FlawUUIDListRequest):
        body (FlawUUIDListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrackersApiV1FileCreateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            exclude_existing_trackers=exclude_existing_trackers,
        )
    ).parsed
