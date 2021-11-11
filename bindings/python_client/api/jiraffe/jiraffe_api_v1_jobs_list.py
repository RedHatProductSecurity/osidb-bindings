from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.jiraffe_api_v1_jobs_list_format import JiraffeApiV1JobsListFormat
from ...models.paginated_jiraffe_job_list import PaginatedJiraffeJobList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, JiraffeApiV1JobsListFormat] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "/jiraffe/api/v1/jobs"

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = (
            format_.value
            if isinstance(format_, JiraffeApiV1JobsListFormat)
            else JiraffeApiV1JobsListFormat(format_).value
            if format_
            else None
        )

    params: Dict[str, Any] = {
        "format": json_format_,
        "limit": limit,
        "offset": offset,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedJiraffeJobList]:
    if response.status_code == 200:
        response_200 = PaginatedJiraffeJobList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedJiraffeJobList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, JiraffeApiV1JobsListFormat] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedJiraffeJobList]:
    kwargs = _get_kwargs(
        client=client,
        format_=format_,
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
    format_: Union[Unset, None, JiraffeApiV1JobsListFormat] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedJiraffeJobList]:
    """Fetch list of JiraffeJobs"""

    return sync_detailed(
        client=client,
        format_=format_,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, JiraffeApiV1JobsListFormat] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedJiraffeJobList]:
    kwargs = _get_kwargs(
        client=client,
        format_=format_,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, JiraffeApiV1JobsListFormat] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedJiraffeJobList]:
    """Fetch list of JiraffeJobs"""

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
            limit=limit,
            offset=offset,
        )
    ).parsed
