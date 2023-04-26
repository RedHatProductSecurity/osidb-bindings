from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.taskman_api_v1_task_flaw_update_response_204 import (
    TaskmanApiV1TaskFlawUpdateResponse204,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    jira_authentication: str,
) -> Dict[str, Any]:
    url = "{}/taskman/api/v1/task/flaw/{flaw_uuid}".format(
        client.base_url,
        flaw_uuid=flaw_uuid,
    )

    headers: Dict[str, Any] = client.get_headers()

    headers["jira-authentication"] = jira_authentication

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[TaskmanApiV1TaskFlawUpdateResponse204]:
    if response.status_code == 204:
        _response_204 = response.json()
        response_204: TaskmanApiV1TaskFlawUpdateResponse204
        if isinstance(_response_204, Unset):
            response_204 = UNSET
        else:
            response_204 = TaskmanApiV1TaskFlawUpdateResponse204.from_dict(
                _response_204
            )

        return response_204
    return None


def _build_response(
    *, response: requests.Response
) -> Response[TaskmanApiV1TaskFlawUpdateResponse204]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    jira_authentication: str,
) -> Response[TaskmanApiV1TaskFlawUpdateResponse204]:
    kwargs = _get_kwargs(
        flaw_uuid=flaw_uuid,
        client=client,
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
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    jira_authentication: str,
) -> Optional[TaskmanApiV1TaskFlawUpdateResponse204]:
    """Update a task in Jira from a Flaw"""

    return sync_detailed(
        flaw_uuid=flaw_uuid,
        client=client,
        jira_authentication=jira_authentication,
    ).parsed
