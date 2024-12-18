from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.workflows_api_v1_workflows_adjust_create_response_200 import (
    WorkflowsApiV1WorkflowsAdjustCreateResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/workflows/api/v1/workflows/{id}/adjust".format(
            id=id,
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[WorkflowsApiV1WorkflowsAdjustCreateResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: WorkflowsApiV1WorkflowsAdjustCreateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = WorkflowsApiV1WorkflowsAdjustCreateResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[WorkflowsApiV1WorkflowsAdjustCreateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[WorkflowsApiV1WorkflowsAdjustCreateResponse200]:
    """workflow adjustion API endpoint

    adjust workflow classification of flaw identified by UUID or CVE
    and return its workflow:state classification (new if changed and old otherwise)

    adjust operation is idempotent so when the classification
    is already adjusted running it results in no operation

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowsApiV1WorkflowsAdjustCreateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = requests.post(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[WorkflowsApiV1WorkflowsAdjustCreateResponse200]:
    """workflow adjustion API endpoint

    adjust workflow classification of flaw identified by UUID or CVE
    and return its workflow:state classification (new if changed and old otherwise)

    adjust operation is idempotent so when the classification
    is already adjusted running it results in no operation

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowsApiV1WorkflowsAdjustCreateResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[WorkflowsApiV1WorkflowsAdjustCreateResponse200]:
    """workflow adjustion API endpoint

    adjust workflow classification of flaw identified by UUID or CVE
    and return its workflow:state classification (new if changed and old otherwise)

    adjust operation is idempotent so when the classification
    is already adjusted running it results in no operation

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowsApiV1WorkflowsAdjustCreateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with client.get_async_session().post(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(client=client, response=resp)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[WorkflowsApiV1WorkflowsAdjustCreateResponse200]:
    """workflow adjustion API endpoint

    adjust workflow classification of flaw identified by UUID or CVE
    and return its workflow:state classification (new if changed and old otherwise)

    adjust operation is idempotent so when the classification
    is already adjusted running it results in no operation

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowsApiV1WorkflowsAdjustCreateResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
