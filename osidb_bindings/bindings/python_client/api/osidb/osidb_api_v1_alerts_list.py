from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_alerts_list_alert_type import OsidbApiV1AlertsListAlertType
from ...models.osidb_api_v1_alerts_list_parent_model import (
    OsidbApiV1AlertsListParentModel,
)
from ...models.osidb_api_v1_alerts_list_response_200 import (
    OsidbApiV1AlertsListResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "alert_type": OsidbApiV1AlertsListAlertType,
    "exclude_fields": list[str],
    "include_fields": list[str],
    "limit": int,
    "name": str,
    "offset": int,
    "parent_model": OsidbApiV1AlertsListParentModel,
    "parent_uuid": UUID,
    "uuid": UUID,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    alert_type: Union[Unset, OsidbApiV1AlertsListAlertType] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    parent_model: Union[Unset, OsidbApiV1AlertsListParentModel] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    json_alert_type: Union[Unset, str] = UNSET
    if not isinstance(alert_type, Unset):
        json_alert_type = OsidbApiV1AlertsListAlertType(alert_type).value

    params["alert_type"] = json_alert_type

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    json_include_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(include_fields, Unset):
        json_include_fields = include_fields

    params["include_fields"] = json_include_fields

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    json_parent_model: Union[Unset, str] = UNSET
    if not isinstance(parent_model, Unset):
        json_parent_model = OsidbApiV1AlertsListParentModel(parent_model).value

    params["parent_model"] = json_parent_model

    json_parent_uuid: Union[Unset, str] = UNSET
    if not isinstance(parent_uuid, Unset):
        json_parent_uuid = str(parent_uuid)

    params["parent_uuid"] = json_parent_uuid

    json_uuid: Union[Unset, str] = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)

    params["uuid"] = json_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/alerts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1AlertsListResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1AlertsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AlertsListResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1AlertsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    alert_type: Union[Unset, OsidbApiV1AlertsListAlertType] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    parent_model: Union[Unset, OsidbApiV1AlertsListParentModel] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[OsidbApiV1AlertsListResponse200]:
    """List existing alerts for all models.

    Args:
        alert_type (Union[Unset, OsidbApiV1AlertsListAlertType]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        offset (Union[Unset, int]):
        parent_model (Union[Unset, OsidbApiV1AlertsListParentModel]):
        parent_uuid (Union[Unset, UUID]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AlertsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        alert_type=alert_type,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        limit=limit,
        name=name,
        offset=offset,
        parent_model=parent_model,
        parent_uuid=parent_uuid,
        uuid=uuid,
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
    alert_type: Union[Unset, OsidbApiV1AlertsListAlertType] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    parent_model: Union[Unset, OsidbApiV1AlertsListParentModel] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[OsidbApiV1AlertsListResponse200]:
    """List existing alerts for all models.

    Args:
        alert_type (Union[Unset, OsidbApiV1AlertsListAlertType]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        offset (Union[Unset, int]):
        parent_model (Union[Unset, OsidbApiV1AlertsListParentModel]):
        parent_uuid (Union[Unset, UUID]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AlertsListResponse200
    """

    return sync_detailed(
        client=client,
        alert_type=alert_type,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        limit=limit,
        name=name,
        offset=offset,
        parent_model=parent_model,
        parent_uuid=parent_uuid,
        uuid=uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    alert_type: Union[Unset, OsidbApiV1AlertsListAlertType] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    parent_model: Union[Unset, OsidbApiV1AlertsListParentModel] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[OsidbApiV1AlertsListResponse200]:
    """List existing alerts for all models.

    Args:
        alert_type (Union[Unset, OsidbApiV1AlertsListAlertType]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        offset (Union[Unset, int]):
        parent_model (Union[Unset, OsidbApiV1AlertsListParentModel]):
        parent_uuid (Union[Unset, UUID]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AlertsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        alert_type=alert_type,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        limit=limit,
        name=name,
        offset=offset,
        parent_model=parent_model,
        parent_uuid=parent_uuid,
        uuid=uuid,
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
    alert_type: Union[Unset, OsidbApiV1AlertsListAlertType] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    parent_model: Union[Unset, OsidbApiV1AlertsListParentModel] = UNSET,
    parent_uuid: Union[Unset, UUID] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[OsidbApiV1AlertsListResponse200]:
    """List existing alerts for all models.

    Args:
        alert_type (Union[Unset, OsidbApiV1AlertsListAlertType]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        offset (Union[Unset, int]):
        parent_model (Union[Unset, OsidbApiV1AlertsListParentModel]):
        parent_uuid (Union[Unset, UUID]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AlertsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            alert_type=alert_type,
            exclude_fields=exclude_fields,
            include_fields=include_fields,
            limit=limit,
            name=name,
            offset=offset,
            parent_model=parent_model,
            parent_uuid=parent_uuid,
            uuid=uuid,
        )
    ).parsed
