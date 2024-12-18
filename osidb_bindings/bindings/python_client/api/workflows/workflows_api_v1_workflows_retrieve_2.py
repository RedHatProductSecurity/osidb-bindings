from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.workflows_api_v1_workflows_retrieve_2_response_200 import (
    WorkflowsApiV1WorkflowsRetrieve2Response200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "verbose": bool,
}


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    verbose: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["verbose"] = verbose

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/workflows/api/v1/workflows/{id}".format(
            id=id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[WorkflowsApiV1WorkflowsRetrieve2Response200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: WorkflowsApiV1WorkflowsRetrieve2Response200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = WorkflowsApiV1WorkflowsRetrieve2Response200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[WorkflowsApiV1WorkflowsRetrieve2Response200]:
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
    verbose: Union[Unset, bool] = UNSET,
) -> Response[WorkflowsApiV1WorkflowsRetrieve2Response200]:
    """workflow classification API endpoint

    for flaw identified by UUID or CVE returns its workflow:state classification

    params:

        verbose - return also workflows with flaw classification
                  which represents the reasoning of the result

    Args:
        id (str):
        verbose (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowsApiV1WorkflowsRetrieve2Response200]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        verbose=verbose,
    )

    response = requests.get(
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
    verbose: Union[Unset, bool] = UNSET,
) -> Optional[WorkflowsApiV1WorkflowsRetrieve2Response200]:
    """workflow classification API endpoint

    for flaw identified by UUID or CVE returns its workflow:state classification

    params:

        verbose - return also workflows with flaw classification
                  which represents the reasoning of the result

    Args:
        id (str):
        verbose (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowsApiV1WorkflowsRetrieve2Response200
    """

    return sync_detailed(
        id=id,
        client=client,
        verbose=verbose,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    verbose: Union[Unset, bool] = UNSET,
) -> Response[WorkflowsApiV1WorkflowsRetrieve2Response200]:
    """workflow classification API endpoint

    for flaw identified by UUID or CVE returns its workflow:state classification

    params:

        verbose - return also workflows with flaw classification
                  which represents the reasoning of the result

    Args:
        id (str):
        verbose (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowsApiV1WorkflowsRetrieve2Response200]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        verbose=verbose,
    )

    async with client.get_async_session().get(
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
    verbose: Union[Unset, bool] = UNSET,
) -> Optional[WorkflowsApiV1WorkflowsRetrieve2Response200]:
    """workflow classification API endpoint

    for flaw identified by UUID or CVE returns its workflow:state classification

    params:

        verbose - return also workflows with flaw classification
                  which represents the reasoning of the result

    Args:
        id (str):
        verbose (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowsApiV1WorkflowsRetrieve2Response200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            verbose=verbose,
        )
    ).parsed
