import datetime
from typing import Any, Dict, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_audit_list_response_200 import (
    OsidbApiV1AuditListResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "limit": int,
    "offset": int,
    "pgh_created_at": datetime.datetime,
    "pgh_label": str,
    "pgh_obj_model": str,
    "pgh_slug": str,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    pgh_created_at: Union[Unset, None, datetime.datetime] = UNSET,
    pgh_label: Union[Unset, None, str] = UNSET,
    pgh_obj_model: Union[Unset, None, str] = UNSET,
    pgh_slug: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/audit".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_pgh_created_at: Union[Unset, None, str] = UNSET
    if not isinstance(pgh_created_at, Unset):
        json_pgh_created_at = pgh_created_at.isoformat() if pgh_created_at else None

    params: Dict[str, Any] = {
        "limit": limit,
        "offset": offset,
        "pgh_created_at": json_pgh_created_at,
        "pgh_label": pgh_label,
        "pgh_obj_model": pgh_obj_model,
        "pgh_slug": pgh_slug,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1AuditListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1AuditListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AuditListResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1AuditListResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    pgh_created_at: Union[Unset, None, datetime.datetime] = UNSET,
    pgh_label: Union[Unset, None, str] = UNSET,
    pgh_obj_model: Union[Unset, None, str] = UNSET,
    pgh_slug: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1AuditListResponse200]:
    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        pgh_created_at=pgh_created_at,
        pgh_label=pgh_label,
        pgh_obj_model=pgh_obj_model,
        pgh_slug=pgh_slug,
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
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    pgh_created_at: Union[Unset, None, datetime.datetime] = UNSET,
    pgh_label: Union[Unset, None, str] = UNSET,
    pgh_obj_model: Union[Unset, None, str] = UNSET,
    pgh_slug: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1AuditListResponse200]:
    """basic view of audit history events"""

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        pgh_created_at=pgh_created_at,
        pgh_label=pgh_label,
        pgh_obj_model=pgh_obj_model,
        pgh_slug=pgh_slug,
    ).parsed


async def async_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    pgh_created_at: Union[Unset, None, datetime.datetime] = UNSET,
    pgh_label: Union[Unset, None, str] = UNSET,
    pgh_obj_model: Union[Unset, None, str] = UNSET,
    pgh_slug: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1AuditListResponse200]:
    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        pgh_created_at=pgh_created_at,
        pgh_label=pgh_label,
        pgh_obj_model=pgh_obj_model,
        pgh_slug=pgh_slug,
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
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    pgh_created_at: Union[Unset, None, datetime.datetime] = UNSET,
    pgh_label: Union[Unset, None, str] = UNSET,
    pgh_obj_model: Union[Unset, None, str] = UNSET,
    pgh_slug: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1AuditListResponse200]:
    """basic view of audit history events"""

    return (
        await async_detailed(
            client=client,
            limit=limit,
            offset=offset,
            pgh_created_at=pgh_created_at,
            pgh_label=pgh_label,
            pgh_obj_model=pgh_obj_model,
            pgh_slug=pgh_slug,
        )
    ).parsed
