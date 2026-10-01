from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.stats_api_v1_beta_flaws_retrieve_group_by_item import (
    StatsApiV1BetaFlawsRetrieveGroupByItem,
)
from ...models.stats_api_v1_beta_flaws_retrieve_impact_in_item import (
    StatsApiV1BetaFlawsRetrieveImpactInItem,
)
from ...models.stats_api_v1_beta_flaws_retrieve_impact_not_in_item import (
    StatsApiV1BetaFlawsRetrieveImpactNotInItem,
)
from ...models.stats_api_v1_beta_flaws_retrieve_response_200 import (
    StatsApiV1BetaFlawsRetrieveResponse200,
)
from ...models.stats_api_v1_beta_flaws_retrieve_visibility_in_item import (
    StatsApiV1BetaFlawsRetrieveVisibilityInItem,
)
from ...models.stats_api_v1_beta_flaws_retrieve_visibility_not_in_item import (
    StatsApiV1BetaFlawsRetrieveVisibilityNotInItem,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "age_bucket_bounds": str,
    "group_by": list[StatsApiV1BetaFlawsRetrieveGroupByItem],
    "impact__in": list[StatsApiV1BetaFlawsRetrieveImpactInItem],
    "impact__not_in": list[StatsApiV1BetaFlawsRetrieveImpactNotInItem],
    "ps_product__in": list[str],
    "ps_product__not_in": list[str],
    "visibility__in": list[StatsApiV1BetaFlawsRetrieveVisibilityInItem],
    "visibility__not_in": list[StatsApiV1BetaFlawsRetrieveVisibilityNotInItem],
    "workflow_name__in": list[str],
    "workflow_name__not_in": list[str],
    "workflow_state__in": list[str],
    "workflow_state__not_in": list[str],
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    age_bucket_bounds: Union[Unset, str] = UNSET,
    group_by: list[StatsApiV1BetaFlawsRetrieveGroupByItem],
    impact_in: Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactInItem]] = UNSET,
    impact_not_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveImpactNotInItem]
    ] = UNSET,
    ps_product_in: Union[Unset, list[str]] = UNSET,
    ps_product_not_in: Union[Unset, list[str]] = UNSET,
    visibility_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityInItem]
    ] = UNSET,
    visibility_not_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityNotInItem]
    ] = UNSET,
    workflow_name_in: Union[Unset, list[str]] = UNSET,
    workflow_name_not_in: Union[Unset, list[str]] = UNSET,
    workflow_state_in: Union[Unset, list[str]] = UNSET,
    workflow_state_not_in: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["age_bucket_bounds"] = age_bucket_bounds

    json_group_by: list[str] = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = []
        for group_by_item_data in group_by:
            group_by_item: str = UNSET
            if not isinstance(group_by_item_data, Unset):
                group_by_item = StatsApiV1BetaFlawsRetrieveGroupByItem(
                    group_by_item_data
                ).value

            json_group_by.append(group_by_item)

    params["group_by"] = json_group_by

    json_impact_in: Union[Unset, list[str]] = UNSET
    if not isinstance(impact_in, Unset):
        json_impact_in = []
        for impact_in_item_data in impact_in:
            impact_in_item: str = UNSET
            if not isinstance(impact_in_item_data, Unset):
                impact_in_item = StatsApiV1BetaFlawsRetrieveImpactInItem(
                    impact_in_item_data
                ).value

            json_impact_in.append(impact_in_item)

    params["impact__in"] = json_impact_in

    json_impact_not_in: Union[Unset, list[str]] = UNSET
    if not isinstance(impact_not_in, Unset):
        json_impact_not_in = []
        for impact_not_in_item_data in impact_not_in:
            impact_not_in_item: str = UNSET
            if not isinstance(impact_not_in_item_data, Unset):
                impact_not_in_item = StatsApiV1BetaFlawsRetrieveImpactNotInItem(
                    impact_not_in_item_data
                ).value

            json_impact_not_in.append(impact_not_in_item)

    params["impact__not_in"] = json_impact_not_in

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
                visibility_in_item = StatsApiV1BetaFlawsRetrieveVisibilityInItem(
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
                visibility_not_in_item = StatsApiV1BetaFlawsRetrieveVisibilityNotInItem(
                    visibility_not_in_item_data
                ).value

            json_visibility_not_in.append(visibility_not_in_item)

    params["visibility__not_in"] = json_visibility_not_in

    json_workflow_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(workflow_name_in, Unset):
        json_workflow_name_in = workflow_name_in

    params["workflow_name__in"] = json_workflow_name_in

    json_workflow_name_not_in: Union[Unset, list[str]] = UNSET
    if not isinstance(workflow_name_not_in, Unset):
        json_workflow_name_not_in = workflow_name_not_in

    params["workflow_name__not_in"] = json_workflow_name_not_in

    json_workflow_state_in: Union[Unset, list[str]] = UNSET
    if not isinstance(workflow_state_in, Unset):
        json_workflow_state_in = workflow_state_in

    params["workflow_state__in"] = json_workflow_state_in

    json_workflow_state_not_in: Union[Unset, list[str]] = UNSET
    if not isinstance(workflow_state_not_in, Unset):
        json_workflow_state_not_in = workflow_state_not_in

    params["workflow_state__not_in"] = json_workflow_state_not_in

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/stats/api/v1beta/flaws",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[StatsApiV1BetaFlawsRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: StatsApiV1BetaFlawsRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = StatsApiV1BetaFlawsRetrieveResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[StatsApiV1BetaFlawsRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    age_bucket_bounds: Union[Unset, str] = UNSET,
    group_by: list[StatsApiV1BetaFlawsRetrieveGroupByItem],
    impact_in: Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactInItem]] = UNSET,
    impact_not_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveImpactNotInItem]
    ] = UNSET,
    ps_product_in: Union[Unset, list[str]] = UNSET,
    ps_product_not_in: Union[Unset, list[str]] = UNSET,
    visibility_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityInItem]
    ] = UNSET,
    visibility_not_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityNotInItem]
    ] = UNSET,
    workflow_name_in: Union[Unset, list[str]] = UNSET,
    workflow_name_not_in: Union[Unset, list[str]] = UNSET,
    workflow_state_in: Union[Unset, list[str]] = UNSET,
    workflow_state_not_in: Union[Unset, list[str]] = UNSET,
) -> Response[StatsApiV1BetaFlawsRetrieveResponse200]:
    """[Experimental] Aggregated flaw statistics

     **Experimental.** This endpoint is experimental and may change or be removed without notice. Do not
    build hard dependencies on its shape or behavior.

    Args:
        age_bucket_bounds (Union[Unset, str]):
        group_by (list[StatsApiV1BetaFlawsRetrieveGroupByItem]):
        impact_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactInItem]]):
        impact_not_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactNotInItem]]):
        ps_product_in (Union[Unset, list[str]]):
        ps_product_not_in (Union[Unset, list[str]]):
        visibility_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityInItem]]):
        visibility_not_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityNotInItem]]):
        workflow_name_in (Union[Unset, list[str]]):
        workflow_name_not_in (Union[Unset, list[str]]):
        workflow_state_in (Union[Unset, list[str]]):
        workflow_state_not_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StatsApiV1BetaFlawsRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        age_bucket_bounds=age_bucket_bounds,
        group_by=group_by,
        impact_in=impact_in,
        impact_not_in=impact_not_in,
        ps_product_in=ps_product_in,
        ps_product_not_in=ps_product_not_in,
        visibility_in=visibility_in,
        visibility_not_in=visibility_not_in,
        workflow_name_in=workflow_name_in,
        workflow_name_not_in=workflow_name_not_in,
        workflow_state_in=workflow_state_in,
        workflow_state_not_in=workflow_state_not_in,
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
    age_bucket_bounds: Union[Unset, str] = UNSET,
    group_by: list[StatsApiV1BetaFlawsRetrieveGroupByItem],
    impact_in: Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactInItem]] = UNSET,
    impact_not_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveImpactNotInItem]
    ] = UNSET,
    ps_product_in: Union[Unset, list[str]] = UNSET,
    ps_product_not_in: Union[Unset, list[str]] = UNSET,
    visibility_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityInItem]
    ] = UNSET,
    visibility_not_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityNotInItem]
    ] = UNSET,
    workflow_name_in: Union[Unset, list[str]] = UNSET,
    workflow_name_not_in: Union[Unset, list[str]] = UNSET,
    workflow_state_in: Union[Unset, list[str]] = UNSET,
    workflow_state_not_in: Union[Unset, list[str]] = UNSET,
) -> Optional[StatsApiV1BetaFlawsRetrieveResponse200]:
    """[Experimental] Aggregated flaw statistics

     **Experimental.** This endpoint is experimental and may change or be removed without notice. Do not
    build hard dependencies on its shape or behavior.

    Args:
        age_bucket_bounds (Union[Unset, str]):
        group_by (list[StatsApiV1BetaFlawsRetrieveGroupByItem]):
        impact_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactInItem]]):
        impact_not_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactNotInItem]]):
        ps_product_in (Union[Unset, list[str]]):
        ps_product_not_in (Union[Unset, list[str]]):
        visibility_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityInItem]]):
        visibility_not_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityNotInItem]]):
        workflow_name_in (Union[Unset, list[str]]):
        workflow_name_not_in (Union[Unset, list[str]]):
        workflow_state_in (Union[Unset, list[str]]):
        workflow_state_not_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StatsApiV1BetaFlawsRetrieveResponse200
    """

    return sync_detailed(
        client=client,
        age_bucket_bounds=age_bucket_bounds,
        group_by=group_by,
        impact_in=impact_in,
        impact_not_in=impact_not_in,
        ps_product_in=ps_product_in,
        ps_product_not_in=ps_product_not_in,
        visibility_in=visibility_in,
        visibility_not_in=visibility_not_in,
        workflow_name_in=workflow_name_in,
        workflow_name_not_in=workflow_name_not_in,
        workflow_state_in=workflow_state_in,
        workflow_state_not_in=workflow_state_not_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    age_bucket_bounds: Union[Unset, str] = UNSET,
    group_by: list[StatsApiV1BetaFlawsRetrieveGroupByItem],
    impact_in: Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactInItem]] = UNSET,
    impact_not_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveImpactNotInItem]
    ] = UNSET,
    ps_product_in: Union[Unset, list[str]] = UNSET,
    ps_product_not_in: Union[Unset, list[str]] = UNSET,
    visibility_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityInItem]
    ] = UNSET,
    visibility_not_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityNotInItem]
    ] = UNSET,
    workflow_name_in: Union[Unset, list[str]] = UNSET,
    workflow_name_not_in: Union[Unset, list[str]] = UNSET,
    workflow_state_in: Union[Unset, list[str]] = UNSET,
    workflow_state_not_in: Union[Unset, list[str]] = UNSET,
) -> Response[StatsApiV1BetaFlawsRetrieveResponse200]:
    """[Experimental] Aggregated flaw statistics

     **Experimental.** This endpoint is experimental and may change or be removed without notice. Do not
    build hard dependencies on its shape or behavior.

    Args:
        age_bucket_bounds (Union[Unset, str]):
        group_by (list[StatsApiV1BetaFlawsRetrieveGroupByItem]):
        impact_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactInItem]]):
        impact_not_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactNotInItem]]):
        ps_product_in (Union[Unset, list[str]]):
        ps_product_not_in (Union[Unset, list[str]]):
        visibility_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityInItem]]):
        visibility_not_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityNotInItem]]):
        workflow_name_in (Union[Unset, list[str]]):
        workflow_name_not_in (Union[Unset, list[str]]):
        workflow_state_in (Union[Unset, list[str]]):
        workflow_state_not_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StatsApiV1BetaFlawsRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        age_bucket_bounds=age_bucket_bounds,
        group_by=group_by,
        impact_in=impact_in,
        impact_not_in=impact_not_in,
        ps_product_in=ps_product_in,
        ps_product_not_in=ps_product_not_in,
        visibility_in=visibility_in,
        visibility_not_in=visibility_not_in,
        workflow_name_in=workflow_name_in,
        workflow_name_not_in=workflow_name_not_in,
        workflow_state_in=workflow_state_in,
        workflow_state_not_in=workflow_state_not_in,
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
    age_bucket_bounds: Union[Unset, str] = UNSET,
    group_by: list[StatsApiV1BetaFlawsRetrieveGroupByItem],
    impact_in: Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactInItem]] = UNSET,
    impact_not_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveImpactNotInItem]
    ] = UNSET,
    ps_product_in: Union[Unset, list[str]] = UNSET,
    ps_product_not_in: Union[Unset, list[str]] = UNSET,
    visibility_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityInItem]
    ] = UNSET,
    visibility_not_in: Union[
        Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityNotInItem]
    ] = UNSET,
    workflow_name_in: Union[Unset, list[str]] = UNSET,
    workflow_name_not_in: Union[Unset, list[str]] = UNSET,
    workflow_state_in: Union[Unset, list[str]] = UNSET,
    workflow_state_not_in: Union[Unset, list[str]] = UNSET,
) -> Optional[StatsApiV1BetaFlawsRetrieveResponse200]:
    """[Experimental] Aggregated flaw statistics

     **Experimental.** This endpoint is experimental and may change or be removed without notice. Do not
    build hard dependencies on its shape or behavior.

    Args:
        age_bucket_bounds (Union[Unset, str]):
        group_by (list[StatsApiV1BetaFlawsRetrieveGroupByItem]):
        impact_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactInItem]]):
        impact_not_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveImpactNotInItem]]):
        ps_product_in (Union[Unset, list[str]]):
        ps_product_not_in (Union[Unset, list[str]]):
        visibility_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityInItem]]):
        visibility_not_in (Union[Unset, list[StatsApiV1BetaFlawsRetrieveVisibilityNotInItem]]):
        workflow_name_in (Union[Unset, list[str]]):
        workflow_name_not_in (Union[Unset, list[str]]):
        workflow_state_in (Union[Unset, list[str]]):
        workflow_state_not_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StatsApiV1BetaFlawsRetrieveResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            age_bucket_bounds=age_bucket_bounds,
            group_by=group_by,
            impact_in=impact_in,
            impact_not_in=impact_not_in,
            ps_product_in=ps_product_in,
            ps_product_not_in=ps_product_not_in,
            visibility_in=visibility_in,
            visibility_not_in=visibility_not_in,
            workflow_name_in=workflow_name_in,
            workflow_name_not_in=workflow_name_not_in,
            workflow_state_in=workflow_state_in,
            workflow_state_not_in=workflow_state_not_in,
        )
    ).parsed
