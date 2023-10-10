from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.taskman_api_v1_task_flaw_update_response_200 import (
    TaskmanApiV1TaskFlawUpdateResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    jira_api_key: str,
) -> Dict[str, Any]:
    url = "{}/taskman/api/v1/task/flaw/{flaw_uuid}".format(
        client.base_url,
        flaw_uuid=flaw_uuid,
    )

    headers: Dict[str, Any] = client.get_headers()

    headers["jira-api-key"] = jira_api_key

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[TaskmanApiV1TaskFlawUpdateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: TaskmanApiV1TaskFlawUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = TaskmanApiV1TaskFlawUpdateResponse200.from_dict(
                _response_200
            )

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[TaskmanApiV1TaskFlawUpdateResponse200]:
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
    jira_api_key: str,
) -> Response[TaskmanApiV1TaskFlawUpdateResponse200]:
    kwargs = _get_kwargs(
        flaw_uuid=flaw_uuid,
        client=client,
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
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    jira_api_key: str,
) -> Optional[TaskmanApiV1TaskFlawUpdateResponse200]:
    """Update a task in Jira from a Flaw"""

    return sync_detailed(
        flaw_uuid=flaw_uuid,
        client=client,
        jira_api_key=jira_api_key,
    ).parsed


async def async_detailed(
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    jira_api_key: str,
) -> Response[TaskmanApiV1TaskFlawUpdateResponse200]:
    kwargs = _get_kwargs(
        flaw_uuid=flaw_uuid,
        client=client,
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
    flaw_uuid: str,
    *,
    client: AuthenticatedClient,
    jira_api_key: str,
) -> Optional[TaskmanApiV1TaskFlawUpdateResponse200]:
    """Update a task in Jira from a Flaw"""

    return (
        await async_detailed(
            flaw_uuid=flaw_uuid,
            client=client,
            jira_api_key=jira_api_key,
        )
    ).parsed
