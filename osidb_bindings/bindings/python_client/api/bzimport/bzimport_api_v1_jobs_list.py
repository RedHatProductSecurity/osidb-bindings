from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_job_list import PaginatedJobList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "/bzimport/api/v1/jobs"

    params: Dict[str, Any] = {
        "limit": limit,
        "offset": offset,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedJobList]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: PaginatedJobList
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = PaginatedJobList.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedJobList]:
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
) -> Response[PaginatedJobList]:
    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
    )

    response = client.get_session().get(
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedJobList]:
    """HTTP get /jobs"""

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedJobList]:
    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedJobList]:
    """HTTP get /jobs"""

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
