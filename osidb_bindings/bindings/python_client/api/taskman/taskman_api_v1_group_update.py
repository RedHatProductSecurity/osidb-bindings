from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.taskman_api_v1_group_update_response_204 import (
    TaskmanApiV1GroupUpdateResponse204,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "task_key": str,
}


def _get_kwargs(
    group_key: str,
    *,
    client: AuthenticatedClient,
    task_key: str,
    jira_authentication: str,
) -> Dict[str, Any]:
    url = "{}/taskman/api/v1/group/{group_key}".format(
        client.base_url,
        group_key=group_key,
    )

    headers: Dict[str, Any] = client.get_headers()

    headers["jira-authentication"] = jira_authentication

    params: Dict[str, Any] = {
        "task_key": task_key,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[TaskmanApiV1GroupUpdateResponse204]:
    if response.status_code == 204:
        _response_204 = response.json()
        response_204: TaskmanApiV1GroupUpdateResponse204
        if isinstance(_response_204, Unset):
            response_204 = UNSET
        else:
            response_204 = TaskmanApiV1GroupUpdateResponse204.from_dict(_response_204)

        return response_204
    return None


def _build_response(
    *, response: requests.Response
) -> Response[TaskmanApiV1GroupUpdateResponse204]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    group_key: str,
    *,
    client: AuthenticatedClient,
    task_key: str,
    jira_authentication: str,
) -> Response[TaskmanApiV1GroupUpdateResponse204]:
    kwargs = _get_kwargs(
        group_key=group_key,
        client=client,
        task_key=task_key,
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
    group_key: str,
    *,
    client: AuthenticatedClient,
    task_key: str,
    jira_authentication: str,
) -> Optional[TaskmanApiV1GroupUpdateResponse204]:
    """Add a task into a group"""

    return sync_detailed(
        group_key=group_key,
        client=client,
        task_key=task_key,
        jira_authentication=jira_authentication,
    ).parsed
