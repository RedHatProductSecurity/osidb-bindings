from typing import Any, Dict, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.paginated_jiraffe_job_list import PaginatedJiraffeJobList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/jiraffe/api/v1/jobs".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    params: Dict[str, Any] = {
        "limit": limit,
        "offset": offset,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(*, response: requests.Response) -> Optional[PaginatedJiraffeJobList]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: PaginatedJiraffeJobList
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = PaginatedJiraffeJobList.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: requests.Response) -> Response[PaginatedJiraffeJobList]:
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
) -> Response[PaginatedJiraffeJobList]:
    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
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
) -> Optional[PaginatedJiraffeJobList]:
    """Fetch list of JiraffeJobs"""

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
    ).parsed
