import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_flaws_references_list_response_200 import (
    OsidbApiV1FlawsReferencesListResponse200,
)
from ...models.osidb_api_v1_flaws_references_list_type import (
    OsidbApiV1FlawsReferencesListType,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "created_dt": datetime.datetime,
    "created_dt__date": datetime.date,
    "created_dt__date__gte": datetime.date,
    "created_dt__date__lte": datetime.date,
    "created_dt__gt": datetime.datetime,
    "created_dt__gte": datetime.datetime,
    "created_dt__lt": datetime.datetime,
    "created_dt__lte": datetime.datetime,
    "description": str,
    "exclude_fields": list[str],
    "include_fields": list[str],
    "limit": int,
    "offset": int,
    "type": OsidbApiV1FlawsReferencesListType,
    "updated_dt": datetime.datetime,
    "updated_dt__date": datetime.date,
    "updated_dt__date__gte": datetime.date,
    "updated_dt__date__lte": datetime.date,
    "updated_dt__gt": datetime.datetime,
    "updated_dt__gte": datetime.datetime,
    "updated_dt__lt": datetime.datetime,
    "updated_dt__lte": datetime.datetime,
    "url": str,
    "uuid": UUID,
}


def _get_kwargs(
    flaw_id: UUID,
    *,
    client: AuthenticatedClient,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    description: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    type_: Union[Unset, OsidbApiV1FlawsReferencesListType] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    json_created_dt: Union[Unset, str] = UNSET
    if not isinstance(created_dt, Unset):
        json_created_dt = created_dt.isoformat()

    params["created_dt"] = json_created_dt

    json_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(created_dt_date, Unset):
        json_created_dt_date = created_dt_date.isoformat()

    params["created_dt__date"] = json_created_dt_date

    json_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(created_dt_date_gte, Unset):
        json_created_dt_date_gte = created_dt_date_gte.isoformat()

    params["created_dt__date__gte"] = json_created_dt_date_gte

    json_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(created_dt_date_lte, Unset):
        json_created_dt_date_lte = created_dt_date_lte.isoformat()

    params["created_dt__date__lte"] = json_created_dt_date_lte

    json_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(created_dt_gt, Unset):
        json_created_dt_gt = created_dt_gt.isoformat()

    params["created_dt__gt"] = json_created_dt_gt

    json_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(created_dt_gte, Unset):
        json_created_dt_gte = created_dt_gte.isoformat()

    params["created_dt__gte"] = json_created_dt_gte

    json_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(created_dt_lt, Unset):
        json_created_dt_lt = created_dt_lt.isoformat()

    params["created_dt__lt"] = json_created_dt_lt

    json_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(created_dt_lte, Unset):
        json_created_dt_lte = created_dt_lte.isoformat()

    params["created_dt__lte"] = json_created_dt_lte

    params["description"] = description

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    json_include_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(include_fields, Unset):
        json_include_fields = include_fields

    params["include_fields"] = json_include_fields

    params["limit"] = limit

    params["offset"] = offset

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = OsidbApiV1FlawsReferencesListType(type_).value

    params["type"] = json_type_

    json_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(updated_dt, Unset):
        json_updated_dt = updated_dt.isoformat()

    params["updated_dt"] = json_updated_dt

    json_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_date, Unset):
        json_updated_dt_date = updated_dt_date.isoformat()

    params["updated_dt__date"] = json_updated_dt_date

    json_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_date_gte, Unset):
        json_updated_dt_date_gte = updated_dt_date_gte.isoformat()

    params["updated_dt__date__gte"] = json_updated_dt_date_gte

    json_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_date_lte, Unset):
        json_updated_dt_date_lte = updated_dt_date_lte.isoformat()

    params["updated_dt__date__lte"] = json_updated_dt_date_lte

    json_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_gt, Unset):
        json_updated_dt_gt = updated_dt_gt.isoformat()

    params["updated_dt__gt"] = json_updated_dt_gt

    json_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_gte, Unset):
        json_updated_dt_gte = updated_dt_gte.isoformat()

    params["updated_dt__gte"] = json_updated_dt_gte

    json_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_lt, Unset):
        json_updated_dt_lt = updated_dt_lt.isoformat()

    params["updated_dt__lt"] = json_updated_dt_lt

    json_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_lte, Unset):
        json_updated_dt_lte = updated_dt_lte.isoformat()

    params["updated_dt__lte"] = json_updated_dt_lte

    params["url"] = url_query

    json_uuid: Union[Unset, str] = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)

    params["uuid"] = json_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/flaws/{flaw_id}/references".format(
            flaw_id=flaw_id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1FlawsReferencesListResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsReferencesListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsReferencesListResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1FlawsReferencesListResponse200]:
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
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    description: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    type_: Union[Unset, OsidbApiV1FlawsReferencesListType] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[OsidbApiV1FlawsReferencesListResponse200]:
    """
    Args:
        flaw_id (UUID):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        type_ (Union[Unset, OsidbApiV1FlawsReferencesListType]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        url_query (Union[Unset, str]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsReferencesListResponse200]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        description=description,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        limit=limit,
        offset=offset,
        type_=type_,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        url_query=url_query,
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
    flaw_id: UUID,
    *,
    client: AuthenticatedClient,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    description: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    type_: Union[Unset, OsidbApiV1FlawsReferencesListType] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[OsidbApiV1FlawsReferencesListResponse200]:
    """
    Args:
        flaw_id (UUID):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        type_ (Union[Unset, OsidbApiV1FlawsReferencesListType]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        url_query (Union[Unset, str]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsReferencesListResponse200
    """

    return sync_detailed(
        flaw_id=flaw_id,
        client=client,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        description=description,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        limit=limit,
        offset=offset,
        type_=type_,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        url_query=url_query,
        uuid=uuid,
    ).parsed


async def asyncio_detailed(
    flaw_id: UUID,
    *,
    client: AuthenticatedClient,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    description: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    type_: Union[Unset, OsidbApiV1FlawsReferencesListType] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[OsidbApiV1FlawsReferencesListResponse200]:
    """
    Args:
        flaw_id (UUID):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        type_ (Union[Unset, OsidbApiV1FlawsReferencesListType]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        url_query (Union[Unset, str]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsReferencesListResponse200]
    """

    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        description=description,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        limit=limit,
        offset=offset,
        type_=type_,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        url_query=url_query,
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
    flaw_id: UUID,
    *,
    client: AuthenticatedClient,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    description: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    type_: Union[Unset, OsidbApiV1FlawsReferencesListType] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[OsidbApiV1FlawsReferencesListResponse200]:
    """
    Args:
        flaw_id (UUID):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        type_ (Union[Unset, OsidbApiV1FlawsReferencesListType]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        url_query (Union[Unset, str]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsReferencesListResponse200
    """

    return (
        await asyncio_detailed(
            flaw_id=flaw_id,
            client=client,
            created_dt=created_dt,
            created_dt_date=created_dt_date,
            created_dt_date_gte=created_dt_date_gte,
            created_dt_date_lte=created_dt_date_lte,
            created_dt_gt=created_dt_gt,
            created_dt_gte=created_dt_gte,
            created_dt_lt=created_dt_lt,
            created_dt_lte=created_dt_lte,
            description=description,
            exclude_fields=exclude_fields,
            include_fields=include_fields,
            limit=limit,
            offset=offset,
            type_=type_,
            updated_dt=updated_dt,
            updated_dt_date=updated_dt_date,
            updated_dt_date_gte=updated_dt_date_gte,
            updated_dt_date_lte=updated_dt_date_lte,
            updated_dt_gt=updated_dt_gt,
            updated_dt_gte=updated_dt_gte,
            updated_dt_lt=updated_dt_lt,
            updated_dt_lte=updated_dt_lte,
            url_query=url_query,
            uuid=uuid,
        )
    ).parsed
