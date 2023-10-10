from typing import Any, Dict, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.taskman_api_v1_task_status_update_reason import (
    TaskmanApiV1TaskStatusUpdateReason,
)
from ...models.taskman_api_v1_task_status_update_resolution import (
    TaskmanApiV1TaskStatusUpdateResolution,
)
from ...models.taskman_api_v1_task_status_update_response_200 import (
    TaskmanApiV1TaskStatusUpdateResponse200,
)
from ...models.taskman_api_v1_task_status_update_status import (
    TaskmanApiV1TaskStatusUpdateStatus,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "reason": TaskmanApiV1TaskStatusUpdateReason,
    "resolution": TaskmanApiV1TaskStatusUpdateResolution,
    "status": TaskmanApiV1TaskStatusUpdateStatus,
}


def _get_kwargs(
    task_key: str,
    *,
    client: AuthenticatedClient,
    reason: Union[Unset, None, TaskmanApiV1TaskStatusUpdateReason] = UNSET,
    resolution: Union[Unset, None, TaskmanApiV1TaskStatusUpdateResolution] = UNSET,
    status: TaskmanApiV1TaskStatusUpdateStatus,
    jira_api_key: str,
) -> Dict[str, Any]:
    url = "{}/taskman/api/v1/task/{task_key}/status".format(
        client.base_url,
        task_key=task_key,
    )

    headers: Dict[str, Any] = client.get_headers()

    headers["jira-api-key"] = jira_api_key

    json_reason: Union[Unset, None, str] = UNSET
    if not isinstance(reason, Unset):

        json_reason = (
            TaskmanApiV1TaskStatusUpdateReason(reason).value if reason else None
        )

    json_resolution: Union[Unset, None, str] = UNSET
    if not isinstance(resolution, Unset):

        json_resolution = (
            TaskmanApiV1TaskStatusUpdateResolution(resolution).value
            if resolution
            else None
        )

    json_status: str = UNSET
    if not isinstance(status, Unset):

        json_status = TaskmanApiV1TaskStatusUpdateStatus(status).value

    params: Dict[str, Any] = {
        "reason": json_reason,
        "resolution": json_resolution,
        "status": json_status,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[TaskmanApiV1TaskStatusUpdateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: TaskmanApiV1TaskStatusUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = TaskmanApiV1TaskStatusUpdateResponse200.from_dict(
                _response_200
            )

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[TaskmanApiV1TaskStatusUpdateResponse200]:
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
    reason: Union[Unset, None, TaskmanApiV1TaskStatusUpdateReason] = UNSET,
    resolution: Union[Unset, None, TaskmanApiV1TaskStatusUpdateResolution] = UNSET,
    status: TaskmanApiV1TaskStatusUpdateStatus,
    jira_api_key: str,
) -> Response[TaskmanApiV1TaskStatusUpdateResponse200]:
    kwargs = _get_kwargs(
        task_key=task_key,
        client=client,
        reason=reason,
        resolution=resolution,
        status=status,
        jira_api_key=jira_api_key,
    )

    response = requests.put(
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
    reason: Union[Unset, None, TaskmanApiV1TaskStatusUpdateReason] = UNSET,
    resolution: Union[Unset, None, TaskmanApiV1TaskStatusUpdateResolution] = UNSET,
    status: TaskmanApiV1TaskStatusUpdateStatus,
    jira_api_key: str,
) -> Optional[TaskmanApiV1TaskStatusUpdateResponse200]:
    """Change a task workflow status"""

    return sync_detailed(
        task_key=task_key,
        client=client,
        reason=reason,
        resolution=resolution,
        status=status,
        jira_api_key=jira_api_key,
    ).parsed


async def async_detailed(
    task_key: str,
    *,
    client: AuthenticatedClient,
    reason: Union[Unset, None, TaskmanApiV1TaskStatusUpdateReason] = UNSET,
    resolution: Union[Unset, None, TaskmanApiV1TaskStatusUpdateResolution] = UNSET,
    status: TaskmanApiV1TaskStatusUpdateStatus,
    jira_api_key: str,
) -> Response[TaskmanApiV1TaskStatusUpdateResponse200]:
    kwargs = _get_kwargs(
        task_key=task_key,
        client=client,
        reason=reason,
        resolution=resolution,
        status=status,
        jira_api_key=jira_api_key,
    )

    async with client.get_async_session().put(
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
    reason: Union[Unset, None, TaskmanApiV1TaskStatusUpdateReason] = UNSET,
    resolution: Union[Unset, None, TaskmanApiV1TaskStatusUpdateResolution] = UNSET,
    status: TaskmanApiV1TaskStatusUpdateStatus,
    jira_api_key: str,
) -> Optional[TaskmanApiV1TaskStatusUpdateResponse200]:
    """Change a task workflow status"""

    return (
        await async_detailed(
            task_key=task_key,
            client=client,
            reason=reason,
            resolution=resolution,
            status=status,
            jira_api_key=jira_api_key,
        )
    ).parsed
