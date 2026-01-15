import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v2_affects_cvss_scores_list_issuer import (
    OsidbApiV2AffectsCvssScoresListIssuer,
)
from ...models.osidb_api_v2_affects_cvss_scores_list_issuer_in_item import (
    OsidbApiV2AffectsCvssScoresListIssuerInItem,
)
from ...models.osidb_api_v2_affects_cvss_scores_list_response_200 import (
    OsidbApiV2AffectsCvssScoresListResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "comment": str,
    "comment__in": list[str],
    "created_dt": datetime.datetime,
    "created_dt__date": datetime.date,
    "created_dt__date__gte": datetime.date,
    "created_dt__date__lte": datetime.date,
    "created_dt__gt": datetime.datetime,
    "created_dt__gte": datetime.datetime,
    "created_dt__lt": datetime.datetime,
    "created_dt__lte": datetime.datetime,
    "cvss_version": str,
    "exclude_fields": list[str],
    "include_fields": list[str],
    "issuer": OsidbApiV2AffectsCvssScoresListIssuer,
    "issuer__in": list[OsidbApiV2AffectsCvssScoresListIssuerInItem],
    "limit": int,
    "offset": int,
    "score": float,
    "updated_dt": datetime.datetime,
    "updated_dt__date": datetime.date,
    "updated_dt__date__gte": datetime.date,
    "updated_dt__date__lte": datetime.date,
    "updated_dt__gt": datetime.datetime,
    "updated_dt__gte": datetime.datetime,
    "updated_dt__lt": datetime.datetime,
    "updated_dt__lte": datetime.datetime,
    "uuid": UUID,
    "uuid__in": list[UUID],
    "vector": str,
    "vector__in": list[str],
}


def _get_kwargs(
    affect_id: UUID,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, str] = UNSET,
    comment_in: Union[Unset, list[str]] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_version: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    issuer: Union[Unset, OsidbApiV2AffectsCvssScoresListIssuer] = UNSET,
    issuer_in: Union[Unset, list[OsidbApiV2AffectsCvssScoresListIssuerInItem]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    score: Union[Unset, float] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    vector: Union[Unset, str] = UNSET,
    vector_in: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["comment"] = comment

    json_comment_in: Union[Unset, list[str]] = UNSET
    if not isinstance(comment_in, Unset):
        json_comment_in = comment_in

    params["comment__in"] = json_comment_in

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

    params["cvss_version"] = cvss_version

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    json_include_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(include_fields, Unset):
        json_include_fields = include_fields

    params["include_fields"] = json_include_fields

    json_issuer: Union[Unset, str] = UNSET
    if not isinstance(issuer, Unset):
        json_issuer = OsidbApiV2AffectsCvssScoresListIssuer(issuer).value

    params["issuer"] = json_issuer

    json_issuer_in: Union[Unset, list[str]] = UNSET
    if not isinstance(issuer_in, Unset):
        json_issuer_in = []
        for issuer_in_item_data in issuer_in:
            issuer_in_item: str = UNSET
            if not isinstance(issuer_in_item_data, Unset):
                issuer_in_item = OsidbApiV2AffectsCvssScoresListIssuerInItem(
                    issuer_in_item_data
                ).value

            json_issuer_in.append(issuer_in_item)

    params["issuer__in"] = json_issuer_in

    params["limit"] = limit

    params["offset"] = offset

    params["score"] = score

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

    json_uuid: Union[Unset, str] = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)

    params["uuid"] = json_uuid

    json_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(uuid_in, Unset):
        json_uuid_in = []
        for uuid_in_item_data in uuid_in:
            uuid_in_item: str = UNSET
            if not isinstance(uuid_in_item_data, Unset):
                uuid_in_item = str(uuid_in_item_data)

            json_uuid_in.append(uuid_in_item)

    params["uuid__in"] = json_uuid_in

    params["vector"] = vector

    json_vector_in: Union[Unset, list[str]] = UNSET
    if not isinstance(vector_in, Unset):
        json_vector_in = vector_in

    params["vector__in"] = json_vector_in

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v2/affects/{affect_id}/cvss-scores".format(
            affect_id=affect_id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV2AffectsCvssScoresListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV2AffectsCvssScoresListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV2AffectsCvssScoresListResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV2AffectsCvssScoresListResponse200]:
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
    comment: Union[Unset, str] = UNSET,
    comment_in: Union[Unset, list[str]] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_version: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    issuer: Union[Unset, OsidbApiV2AffectsCvssScoresListIssuer] = UNSET,
    issuer_in: Union[Unset, list[OsidbApiV2AffectsCvssScoresListIssuerInItem]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    score: Union[Unset, float] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    vector: Union[Unset, str] = UNSET,
    vector_in: Union[Unset, list[str]] = UNSET,
) -> Response[OsidbApiV2AffectsCvssScoresListResponse200]:
    """
    Args:
        affect_id (UUID):
        comment (Union[Unset, str]):
        comment_in (Union[Unset, list[str]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_version (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        issuer (Union[Unset, OsidbApiV2AffectsCvssScoresListIssuer]):
        issuer_in (Union[Unset, list[OsidbApiV2AffectsCvssScoresListIssuerInItem]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        score (Union[Unset, float]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        uuid_in (Union[Unset, list[UUID]]):
        vector (Union[Unset, str]):
        vector_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2AffectsCvssScoresListResponse200]
    """

    kwargs = _get_kwargs(
        affect_id=affect_id,
        client=client,
        comment=comment,
        comment_in=comment_in,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cvss_version=cvss_version,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        issuer=issuer,
        issuer_in=issuer_in,
        limit=limit,
        offset=offset,
        score=score,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
        uuid_in=uuid_in,
        vector=vector,
        vector_in=vector_in,
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
    affect_id: UUID,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, str] = UNSET,
    comment_in: Union[Unset, list[str]] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_version: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    issuer: Union[Unset, OsidbApiV2AffectsCvssScoresListIssuer] = UNSET,
    issuer_in: Union[Unset, list[OsidbApiV2AffectsCvssScoresListIssuerInItem]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    score: Union[Unset, float] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    vector: Union[Unset, str] = UNSET,
    vector_in: Union[Unset, list[str]] = UNSET,
) -> Optional[OsidbApiV2AffectsCvssScoresListResponse200]:
    """
    Args:
        affect_id (UUID):
        comment (Union[Unset, str]):
        comment_in (Union[Unset, list[str]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_version (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        issuer (Union[Unset, OsidbApiV2AffectsCvssScoresListIssuer]):
        issuer_in (Union[Unset, list[OsidbApiV2AffectsCvssScoresListIssuerInItem]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        score (Union[Unset, float]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        uuid_in (Union[Unset, list[UUID]]):
        vector (Union[Unset, str]):
        vector_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2AffectsCvssScoresListResponse200
    """

    return sync_detailed(
        affect_id=affect_id,
        client=client,
        comment=comment,
        comment_in=comment_in,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cvss_version=cvss_version,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        issuer=issuer,
        issuer_in=issuer_in,
        limit=limit,
        offset=offset,
        score=score,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
        uuid_in=uuid_in,
        vector=vector,
        vector_in=vector_in,
    ).parsed


async def asyncio_detailed(
    affect_id: UUID,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, str] = UNSET,
    comment_in: Union[Unset, list[str]] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_version: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    issuer: Union[Unset, OsidbApiV2AffectsCvssScoresListIssuer] = UNSET,
    issuer_in: Union[Unset, list[OsidbApiV2AffectsCvssScoresListIssuerInItem]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    score: Union[Unset, float] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    vector: Union[Unset, str] = UNSET,
    vector_in: Union[Unset, list[str]] = UNSET,
) -> Response[OsidbApiV2AffectsCvssScoresListResponse200]:
    """
    Args:
        affect_id (UUID):
        comment (Union[Unset, str]):
        comment_in (Union[Unset, list[str]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_version (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        issuer (Union[Unset, OsidbApiV2AffectsCvssScoresListIssuer]):
        issuer_in (Union[Unset, list[OsidbApiV2AffectsCvssScoresListIssuerInItem]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        score (Union[Unset, float]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        uuid_in (Union[Unset, list[UUID]]):
        vector (Union[Unset, str]):
        vector_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2AffectsCvssScoresListResponse200]
    """

    kwargs = _get_kwargs(
        affect_id=affect_id,
        client=client,
        comment=comment,
        comment_in=comment_in,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cvss_version=cvss_version,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        issuer=issuer,
        issuer_in=issuer_in,
        limit=limit,
        offset=offset,
        score=score,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
        uuid_in=uuid_in,
        vector=vector,
        vector_in=vector_in,
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
    affect_id: UUID,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, str] = UNSET,
    comment_in: Union[Unset, list[str]] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_version: Union[Unset, str] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    issuer: Union[Unset, OsidbApiV2AffectsCvssScoresListIssuer] = UNSET,
    issuer_in: Union[Unset, list[OsidbApiV2AffectsCvssScoresListIssuerInItem]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    score: Union[Unset, float] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    vector: Union[Unset, str] = UNSET,
    vector_in: Union[Unset, list[str]] = UNSET,
) -> Optional[OsidbApiV2AffectsCvssScoresListResponse200]:
    """
    Args:
        affect_id (UUID):
        comment (Union[Unset, str]):
        comment_in (Union[Unset, list[str]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_version (Union[Unset, str]):
        exclude_fields (Union[Unset, list[str]]):
        include_fields (Union[Unset, list[str]]):
        issuer (Union[Unset, OsidbApiV2AffectsCvssScoresListIssuer]):
        issuer_in (Union[Unset, list[OsidbApiV2AffectsCvssScoresListIssuerInItem]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        score (Union[Unset, float]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        uuid_in (Union[Unset, list[UUID]]):
        vector (Union[Unset, str]):
        vector_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2AffectsCvssScoresListResponse200
    """

    return (
        await asyncio_detailed(
            affect_id=affect_id,
            client=client,
            comment=comment,
            comment_in=comment_in,
            created_dt=created_dt,
            created_dt_date=created_dt_date,
            created_dt_date_gte=created_dt_date_gte,
            created_dt_date_lte=created_dt_date_lte,
            created_dt_gt=created_dt_gt,
            created_dt_gte=created_dt_gte,
            created_dt_lt=created_dt_lt,
            created_dt_lte=created_dt_lte,
            cvss_version=cvss_version,
            exclude_fields=exclude_fields,
            include_fields=include_fields,
            issuer=issuer,
            issuer_in=issuer_in,
            limit=limit,
            offset=offset,
            score=score,
            updated_dt=updated_dt,
            updated_dt_date=updated_dt_date,
            updated_dt_date_gte=updated_dt_date_gte,
            updated_dt_date_lte=updated_dt_date_lte,
            updated_dt_gt=updated_dt_gt,
            updated_dt_gte=updated_dt_gte,
            updated_dt_lt=updated_dt_lt,
            updated_dt_lte=updated_dt_lte,
            uuid=uuid,
            uuid_in=uuid_in,
            vector=vector,
            vector_in=vector_in,
        )
    ).parsed
