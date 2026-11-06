from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.stats_api_v1_beta_trackers_retrieve_group_by_item import (
    StatsApiV1BetaTrackersRetrieveGroupByItem,
)
from ...models.stats_api_v1_beta_trackers_retrieve_response_200 import (
    StatsApiV1BetaTrackersRetrieveResponse200,
)
from ...models.stats_api_v1_beta_trackers_retrieve_visibility_in_item import (
    StatsApiV1BetaTrackersRetrieveVisibilityInItem,
)
from ...models.stats_api_v1_beta_trackers_retrieve_visibility_not_in_item import (
    StatsApiV1BetaTrackersRetrieveVisibilityNotInItem,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "group_by": list[StatsApiV1BetaTrackersRetrieveGroupByItem],
    "ps_product__in": list[str],
    "ps_product__not_in": list[str],
    "visibility__in": list[StatsApiV1BetaTrackersRetrieveVisibilityInItem],
    "visibility__not_in": list[StatsApiV1BetaTrackersRetrieveVisibilityNotInItem],
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    group_by: list[StatsApiV1BetaTrackersRetrieveGroupByItem],
    ps_product_in: Union[Unset, list[str]] = UNSET,
    ps_product_not_in: Union[Unset, list[str]] = UNSET,
    visibility_in: Union[
        Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityInItem]
    ] = UNSET,
    visibility_not_in: Union[
        Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityNotInItem]
    ] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    json_group_by: list[str] = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = []
        for group_by_item_data in group_by:
            group_by_item: str = UNSET
            if not isinstance(group_by_item_data, Unset):
                group_by_item = StatsApiV1BetaTrackersRetrieveGroupByItem(
                    group_by_item_data
                ).value

            json_group_by.append(group_by_item)

    params["group_by"] = json_group_by

    json_ps_product_in: Union[Unset, list[str]] = UNSET
    if not isinstance(ps_product_in, Unset):
        json_ps_product_in = ps_product_in

    params["ps_product__in"] = json_ps_product_in

    json_ps_product_not_in: Union[Unset, list[str]] = UNSET
    if not isinstance(ps_product_not_in, Unset):
        json_ps_product_not_in = ps_product_not_in

    params["ps_product__not_in"] = json_ps_product_not_in

    json_visibility_in: Union[Unset, list[str]] = UNSET
    if not isinstance(visibility_in, Unset):
        json_visibility_in = []
        for visibility_in_item_data in visibility_in:
            visibility_in_item: str = UNSET
            if not isinstance(visibility_in_item_data, Unset):
                visibility_in_item = StatsApiV1BetaTrackersRetrieveVisibilityInItem(
                    visibility_in_item_data
                ).value

            json_visibility_in.append(visibility_in_item)

    params["visibility__in"] = json_visibility_in

    json_visibility_not_in: Union[Unset, list[str]] = UNSET
    if not isinstance(visibility_not_in, Unset):
        json_visibility_not_in = []
        for visibility_not_in_item_data in visibility_not_in:
            visibility_not_in_item: str = UNSET
            if not isinstance(visibility_not_in_item_data, Unset):
                visibility_not_in_item = (
                    StatsApiV1BetaTrackersRetrieveVisibilityNotInItem(
                        visibility_not_in_item_data
                    ).value
                )

            json_visibility_not_in.append(visibility_not_in_item)

    params["visibility__not_in"] = json_visibility_not_in

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/stats/api/v1beta/trackers",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[StatsApiV1BetaTrackersRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: StatsApiV1BetaTrackersRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = StatsApiV1BetaTrackersRetrieveResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[StatsApiV1BetaTrackersRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_by: list[StatsApiV1BetaTrackersRetrieveGroupByItem],
    ps_product_in: Union[Unset, list[str]] = UNSET,
    ps_product_not_in: Union[Unset, list[str]] = UNSET,
    visibility_in: Union[
        Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityInItem]
    ] = UNSET,
    visibility_not_in: Union[
        Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityNotInItem]
    ] = UNSET,
) -> Response[StatsApiV1BetaTrackersRetrieveResponse200]:
    """[Experimental] Aggregated tracker statistics

     **Experimental.** This endpoint is experimental and may change or be removed without notice. Do not
    build hard dependencies on its shape or behavior.

    Args:
        group_by (list[StatsApiV1BetaTrackersRetrieveGroupByItem]):
        ps_product_in (Union[Unset, list[str]]):
        ps_product_not_in (Union[Unset, list[str]]):
        visibility_in (Union[Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityInItem]]):
        visibility_not_in (Union[Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityNotInItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StatsApiV1BetaTrackersRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        group_by=group_by,
        ps_product_in=ps_product_in,
        ps_product_not_in=ps_product_not_in,
        visibility_in=visibility_in,
        visibility_not_in=visibility_not_in,
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
    group_by: list[StatsApiV1BetaTrackersRetrieveGroupByItem],
    ps_product_in: Union[Unset, list[str]] = UNSET,
    ps_product_not_in: Union[Unset, list[str]] = UNSET,
    visibility_in: Union[
        Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityInItem]
    ] = UNSET,
    visibility_not_in: Union[
        Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityNotInItem]
    ] = UNSET,
) -> Optional[StatsApiV1BetaTrackersRetrieveResponse200]:
    """[Experimental] Aggregated tracker statistics

     **Experimental.** This endpoint is experimental and may change or be removed without notice. Do not
    build hard dependencies on its shape or behavior.

    Args:
        group_by (list[StatsApiV1BetaTrackersRetrieveGroupByItem]):
        ps_product_in (Union[Unset, list[str]]):
        ps_product_not_in (Union[Unset, list[str]]):
        visibility_in (Union[Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityInItem]]):
        visibility_not_in (Union[Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityNotInItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StatsApiV1BetaTrackersRetrieveResponse200
    """

    return sync_detailed(
        client=client,
        group_by=group_by,
        ps_product_in=ps_product_in,
        ps_product_not_in=ps_product_not_in,
        visibility_in=visibility_in,
        visibility_not_in=visibility_not_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_by: list[StatsApiV1BetaTrackersRetrieveGroupByItem],
    ps_product_in: Union[Unset, list[str]] = UNSET,
    ps_product_not_in: Union[Unset, list[str]] = UNSET,
    visibility_in: Union[
        Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityInItem]
    ] = UNSET,
    visibility_not_in: Union[
        Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityNotInItem]
    ] = UNSET,
) -> Response[StatsApiV1BetaTrackersRetrieveResponse200]:
    """[Experimental] Aggregated tracker statistics

     **Experimental.** This endpoint is experimental and may change or be removed without notice. Do not
    build hard dependencies on its shape or behavior.

    Args:
        group_by (list[StatsApiV1BetaTrackersRetrieveGroupByItem]):
        ps_product_in (Union[Unset, list[str]]):
        ps_product_not_in (Union[Unset, list[str]]):
        visibility_in (Union[Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityInItem]]):
        visibility_not_in (Union[Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityNotInItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StatsApiV1BetaTrackersRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        group_by=group_by,
        ps_product_in=ps_product_in,
        ps_product_not_in=ps_product_not_in,
        visibility_in=visibility_in,
        visibility_not_in=visibility_not_in,
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
    group_by: list[StatsApiV1BetaTrackersRetrieveGroupByItem],
    ps_product_in: Union[Unset, list[str]] = UNSET,
    ps_product_not_in: Union[Unset, list[str]] = UNSET,
    visibility_in: Union[
        Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityInItem]
    ] = UNSET,
    visibility_not_in: Union[
        Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityNotInItem]
    ] = UNSET,
) -> Optional[StatsApiV1BetaTrackersRetrieveResponse200]:
    """[Experimental] Aggregated tracker statistics

     **Experimental.** This endpoint is experimental and may change or be removed without notice. Do not
    build hard dependencies on its shape or behavior.

    Args:
        group_by (list[StatsApiV1BetaTrackersRetrieveGroupByItem]):
        ps_product_in (Union[Unset, list[str]]):
        ps_product_not_in (Union[Unset, list[str]]):
        visibility_in (Union[Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityInItem]]):
        visibility_not_in (Union[Unset, list[StatsApiV1BetaTrackersRetrieveVisibilityNotInItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StatsApiV1BetaTrackersRetrieveResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            group_by=group_by,
            ps_product_in=ps_product_in,
            ps_product_not_in=ps_product_not_in,
            visibility_in=visibility_in,
            visibility_not_in=visibility_not_in,
        )
    ).parsed
