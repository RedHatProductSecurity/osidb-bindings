import datetime
from typing import Any, Dict, List, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_flaws_cvss_scores_list_issuer import (
    OsidbApiV1FlawsCvssScoresListIssuer,
)
from ...models.osidb_api_v1_flaws_cvss_scores_list_response_200 import (
    OsidbApiV1FlawsCvssScoresListResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "comment": str,
    "created_dt": datetime.datetime,
    "created_dt__date": datetime.date,
    "created_dt__date__gte": datetime.date,
    "created_dt__date__lte": datetime.date,
    "created_dt__gt": datetime.datetime,
    "created_dt__gte": datetime.datetime,
    "created_dt__lt": datetime.datetime,
    "created_dt__lte": datetime.datetime,
    "cvss_version": str,
    "exclude_fields": List[str],
    "include_fields": List[str],
    "issuer": OsidbApiV1FlawsCvssScoresListIssuer,
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
    "uuid": str,
    "vector": str,
}


def _get_kwargs(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, None, str] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_version: Union[Unset, None, str] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    issuer: Union[Unset, None, OsidbApiV1FlawsCvssScoresListIssuer] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    score: Union[Unset, None, float] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
    vector: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws/{flaw_id}/cvss_scores".format(
        client.base_url,
        flaw_id=flaw_id,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_created_dt: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt, Unset):
        json_created_dt = created_dt.isoformat() if created_dt else None

    json_created_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_date, Unset):
        json_created_dt_date = created_dt_date.isoformat() if created_dt_date else None

    json_created_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_date_gte, Unset):
        json_created_dt_date_gte = (
            created_dt_date_gte.isoformat() if created_dt_date_gte else None
        )

    json_created_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_date_lte, Unset):
        json_created_dt_date_lte = (
            created_dt_date_lte.isoformat() if created_dt_date_lte else None
        )

    json_created_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_gt, Unset):
        json_created_dt_gt = created_dt_gt.isoformat() if created_dt_gt else None

    json_created_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_gte, Unset):
        json_created_dt_gte = created_dt_gte.isoformat() if created_dt_gte else None

    json_created_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_lt, Unset):
        json_created_dt_lt = created_dt_lt.isoformat() if created_dt_lt else None

    json_created_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_lte, Unset):
        json_created_dt_lte = created_dt_lte.isoformat() if created_dt_lte else None

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

    json_issuer: Union[Unset, None, str] = UNSET
    if not isinstance(issuer, Unset):

        json_issuer = (
            OsidbApiV1FlawsCvssScoresListIssuer(issuer).value if issuer else None
        )

    json_updated_dt: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt, Unset):
        json_updated_dt = updated_dt.isoformat() if updated_dt else None

    json_updated_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_date, Unset):
        json_updated_dt_date = updated_dt_date.isoformat() if updated_dt_date else None

    json_updated_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_date_gte, Unset):
        json_updated_dt_date_gte = (
            updated_dt_date_gte.isoformat() if updated_dt_date_gte else None
        )

    json_updated_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_date_lte, Unset):
        json_updated_dt_date_lte = (
            updated_dt_date_lte.isoformat() if updated_dt_date_lte else None
        )

    json_updated_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_gt, Unset):
        json_updated_dt_gt = updated_dt_gt.isoformat() if updated_dt_gt else None

    json_updated_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_gte, Unset):
        json_updated_dt_gte = updated_dt_gte.isoformat() if updated_dt_gte else None

    json_updated_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_lt, Unset):
        json_updated_dt_lt = updated_dt_lt.isoformat() if updated_dt_lt else None

    json_updated_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_lte, Unset):
        json_updated_dt_lte = updated_dt_lte.isoformat() if updated_dt_lte else None

    params: Dict[str, Any] = {
        "comment": comment,
        "created_dt": json_created_dt,
        "created_dt__date": json_created_dt_date,
        "created_dt__date__gte": json_created_dt_date_gte,
        "created_dt__date__lte": json_created_dt_date_lte,
        "created_dt__gt": json_created_dt_gt,
        "created_dt__gte": json_created_dt_gte,
        "created_dt__lt": json_created_dt_lt,
        "created_dt__lte": json_created_dt_lte,
        "cvss_version": cvss_version,
        "exclude_fields": json_exclude_fields,
        "include_fields": json_include_fields,
        "issuer": json_issuer,
        "limit": limit,
        "offset": offset,
        "score": score,
        "updated_dt": json_updated_dt,
        "updated_dt__date": json_updated_dt_date,
        "updated_dt__date__gte": json_updated_dt_date_gte,
        "updated_dt__date__lte": json_updated_dt_date_lte,
        "updated_dt__gt": json_updated_dt_gt,
        "updated_dt__gte": json_updated_dt_gte,
        "updated_dt__lt": json_updated_dt_lt,
        "updated_dt__lte": json_updated_dt_lte,
        "uuid": uuid,
        "vector": vector,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1FlawsCvssScoresListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsCvssScoresListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsCvssScoresListResponse200.from_dict(
                _response_200
            )

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsCvssScoresListResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, None, str] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_version: Union[Unset, None, str] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    issuer: Union[Unset, None, OsidbApiV1FlawsCvssScoresListIssuer] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    score: Union[Unset, None, float] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
    vector: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1FlawsCvssScoresListResponse200]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
        comment=comment,
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
        vector=vector,
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
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, None, str] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_version: Union[Unset, None, str] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    issuer: Union[Unset, None, OsidbApiV1FlawsCvssScoresListIssuer] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    score: Union[Unset, None, float] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
    vector: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1FlawsCvssScoresListResponse200]:
    """ """

    return sync_detailed(
        flaw_id=flaw_id,
        client=client,
        comment=comment,
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
        vector=vector,
    ).parsed


async def async_detailed(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, None, str] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_version: Union[Unset, None, str] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    issuer: Union[Unset, None, OsidbApiV1FlawsCvssScoresListIssuer] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    score: Union[Unset, None, float] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
    vector: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1FlawsCvssScoresListResponse200]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
        comment=comment,
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
        vector=vector,
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
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    comment: Union[Unset, None, str] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_version: Union[Unset, None, str] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    issuer: Union[Unset, None, OsidbApiV1FlawsCvssScoresListIssuer] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    score: Union[Unset, None, float] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
    vector: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1FlawsCvssScoresListResponse200]:
    """ """

    return (
        await async_detailed(
            flaw_id=flaw_id,
            client=client,
            comment=comment,
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
            vector=vector,
        )
    ).parsed
