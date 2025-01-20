from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.flaw import Flaw
from ...models.osidb_api_v1_flaws_update_response_200 import (
    OsidbApiV1FlawsUpdateResponse200,
)
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {
    "create_jira_task": bool,
}

REQUEST_BODY_TYPE = Flaw


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        Flaw,
        Flaw,
        Flaw,
    ],
    create_jira_task: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["create_jira_task"] = create_jira_task

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/flaws/{id}".format(
            id=id,
        ),
        "params": params,
    }

    if check_nested_instance(body, Flaw):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1FlawsUpdateResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsUpdateResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1FlawsUpdateResponse200]:
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
    body: Union[
        Flaw,
        Flaw,
        Flaw,
    ],
    create_jira_task: Union[Unset, bool] = UNSET,
) -> Response[OsidbApiV1FlawsUpdateResponse200]:
    """
    Args:
        id (str):
        create_jira_task (Union[Unset, bool]):
        bugzilla_api_key (str):
        jira_api_key (str):
        body (Flaw): serialize flaw model
        body (Flaw): serialize flaw model
        body (Flaw): serialize flaw model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsUpdateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        body=body,
        create_jira_task=create_jira_task,
    )

    response = requests.put(
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
    body: Union[
        Flaw,
        Flaw,
        Flaw,
    ],
    create_jira_task: Union[Unset, bool] = UNSET,
) -> Optional[OsidbApiV1FlawsUpdateResponse200]:
    """
    Args:
        id (str):
        create_jira_task (Union[Unset, bool]):
        bugzilla_api_key (str):
        jira_api_key (str):
        body (Flaw): serialize flaw model
        body (Flaw): serialize flaw model
        body (Flaw): serialize flaw model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsUpdateResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        create_jira_task=create_jira_task,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        Flaw,
        Flaw,
        Flaw,
    ],
    create_jira_task: Union[Unset, bool] = UNSET,
) -> Response[OsidbApiV1FlawsUpdateResponse200]:
    """
    Args:
        id (str):
        create_jira_task (Union[Unset, bool]):
        bugzilla_api_key (str):
        jira_api_key (str):
        body (Flaw): serialize flaw model
        body (Flaw): serialize flaw model
        body (Flaw): serialize flaw model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsUpdateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        body=body,
        create_jira_task=create_jira_task,
    )

    async with client.get_async_session().put(
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
    body: Union[
        Flaw,
        Flaw,
        Flaw,
    ],
    create_jira_task: Union[Unset, bool] = UNSET,
) -> Optional[OsidbApiV1FlawsUpdateResponse200]:
    """
    Args:
        id (str):
        create_jira_task (Union[Unset, bool]):
        bugzilla_api_key (str):
        jira_api_key (str):
        body (Flaw): serialize flaw model
        body (Flaw): serialize flaw model
        body (Flaw): serialize flaw model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsUpdateResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            create_jira_task=create_jira_task,
        )
    ).parsed
