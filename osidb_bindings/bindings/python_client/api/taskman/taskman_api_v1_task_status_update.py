from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.taskman_api_v1_task_status_update_response_204 import (
    TaskmanApiV1TaskStatusUpdateResponse204,
)
from ...models.taskman_api_v1_task_status_update_status import (
    TaskmanApiV1TaskStatusUpdateStatus,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "status": TaskmanApiV1TaskStatusUpdateStatus,
}


def _get_kwargs(
    task_key: str,
    *,
    client: AuthenticatedClient,
    status: TaskmanApiV1TaskStatusUpdateStatus,
    jira_authentication: str,
) -> Dict[str, Any]:
    url = "{}/taskman/api/v1/task/{task_key}/status".format(
        client.base_url,
        task_key=task_key,
    )

    headers: Dict[str, Any] = client.get_headers()

    headers["jira-authentication"] = jira_authentication

    json_status: str = UNSET
    if not isinstance(status, Unset):

        json_status = TaskmanApiV1TaskStatusUpdateStatus(status).value

    params: Dict[str, Any] = {
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
) -> Optional[TaskmanApiV1TaskStatusUpdateResponse204]:
    if response.status_code == 204:
        _response_204 = response.json()
        response_204: TaskmanApiV1TaskStatusUpdateResponse204
        if isinstance(_response_204, Unset):
            response_204 = UNSET
        else:
            response_204 = TaskmanApiV1TaskStatusUpdateResponse204.from_dict(
                _response_204
            )

        return response_204
    return None


def _build_response(
    *, response: requests.Response
) -> Response[TaskmanApiV1TaskStatusUpdateResponse204]:
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
    status: TaskmanApiV1TaskStatusUpdateStatus,
    jira_authentication: str,
) -> Response[TaskmanApiV1TaskStatusUpdateResponse204]:
    kwargs = _get_kwargs(
        task_key=task_key,
        client=client,
        status=status,
        jira_authentication=jira_authentication,
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
    status: TaskmanApiV1TaskStatusUpdateStatus,
    jira_authentication: str,
) -> Optional[TaskmanApiV1TaskStatusUpdateResponse204]:
    """Change a task workflow status"""

    return sync_detailed(
        task_key=task_key,
        client=client,
        status=status,
        jira_authentication=jira_authentication,
    ).parsed
