from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.taskman_api_v1_task_retrieve_response_200 import (
    TaskmanApiV1TaskRetrieveResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    task_key: str,
    *,
    client: AuthenticatedClient,
    jira_api_key: str,
) -> Dict[str, Any]:
    url = "{}/taskman/api/v1/task/{task_key}".format(
        client.base_url,
        task_key=task_key,
    )

    headers: Dict[str, Any] = client.get_headers()

    headers["jira-api-key"] = jira_api_key

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[TaskmanApiV1TaskRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: TaskmanApiV1TaskRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = TaskmanApiV1TaskRetrieveResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[TaskmanApiV1TaskRetrieveResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    task_key: str,
    *,
    client: AuthenticatedClient,
    jira_api_key: str,
) -> Response[TaskmanApiV1TaskRetrieveResponse200]:
    kwargs = _get_kwargs(
        task_key=task_key,
        client=client,
        jira_api_key=jira_api_key,
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
    task_key: str,
    *,
    client: AuthenticatedClient,
    jira_api_key: str,
) -> Optional[TaskmanApiV1TaskRetrieveResponse200]:
    """Get a task from Jira given a task key"""

    return sync_detailed(
        task_key=task_key,
        client=client,
        jira_api_key=jira_api_key,
    ).parsed


async def async_detailed(
    task_key: str,
    *,
    client: AuthenticatedClient,
    jira_api_key: str,
) -> Response[TaskmanApiV1TaskRetrieveResponse200]:
    kwargs = _get_kwargs(
        task_key=task_key,
        client=client,
        jira_api_key=jira_api_key,
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
    task_key: str,
    *,
    client: AuthenticatedClient,
    jira_api_key: str,
) -> Optional[TaskmanApiV1TaskRetrieveResponse200]:
    """Get a task from Jira given a task key"""

    return (
        await async_detailed(
            task_key=task_key,
            client=client,
            jira_api_key=jira_api_key,
        )
    ).parsed
