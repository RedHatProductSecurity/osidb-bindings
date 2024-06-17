from typing import Any, Dict, List, Optional, Union

import requests

from ...client import AuthenticatedClient
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
    "exclude_fields": List[str],
    "include_fields": List[str],
    "limit": int,
    "name": str,
    "offset": int,
    "parent_model": OsidbApiV1AlertsListParentModel,
    "parent_uuid": str,
    "uuid": str,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    alert_type: Union[Unset, None, OsidbApiV1AlertsListAlertType] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    parent_model: Union[Unset, None, OsidbApiV1AlertsListParentModel] = UNSET,
    parent_uuid: Union[Unset, None, str] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/alerts".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_alert_type: Union[Unset, None, str] = UNSET
    if not isinstance(alert_type, Unset):

        json_alert_type = (
            OsidbApiV1AlertsListAlertType(alert_type).value if alert_type else None
        )

    json_exclude_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        if exclude_fields is None:
            json_exclude_fields = None
        else:
            json_exclude_fields = exclude_fields

    json_include_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_fields, Unset):
        if include_fields is None:
            json_include_fields = None
        else:
            json_include_fields = include_fields

    json_parent_model: Union[Unset, None, str] = UNSET
    if not isinstance(parent_model, Unset):

        json_parent_model = (
            OsidbApiV1AlertsListParentModel(parent_model).value
            if parent_model
            else None
        )

    params: Dict[str, Any] = {
        "alert_type": json_alert_type,
        "exclude_fields": json_exclude_fields,
        "include_fields": json_include_fields,
        "limit": limit,
        "name": name,
        "offset": offset,
        "parent_model": json_parent_model,
        "parent_uuid": parent_uuid,
        "uuid": uuid,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1AlertsListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1AlertsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AlertsListResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1AlertsListResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    alert_type: Union[Unset, None, OsidbApiV1AlertsListAlertType] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    parent_model: Union[Unset, None, OsidbApiV1AlertsListParentModel] = UNSET,
    parent_uuid: Union[Unset, None, str] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1AlertsListResponse200]:
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

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    alert_type: Union[Unset, None, OsidbApiV1AlertsListAlertType] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    parent_model: Union[Unset, None, OsidbApiV1AlertsListParentModel] = UNSET,
    parent_uuid: Union[Unset, None, str] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1AlertsListResponse200]:
    """List existing alerts for all models."""

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


async def async_detailed(
    *,
    client: AuthenticatedClient,
    alert_type: Union[Unset, None, OsidbApiV1AlertsListAlertType] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    parent_model: Union[Unset, None, OsidbApiV1AlertsListParentModel] = UNSET,
    parent_uuid: Union[Unset, None, str] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1AlertsListResponse200]:
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

    return _build_response(response=resp)


async def async_(
    *,
    client: AuthenticatedClient,
    alert_type: Union[Unset, None, OsidbApiV1AlertsListAlertType] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    parent_model: Union[Unset, None, OsidbApiV1AlertsListParentModel] = UNSET,
    parent_uuid: Union[Unset, None, str] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1AlertsListResponse200]:
    """List existing alerts for all models."""

    return (
        await async_detailed(
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
