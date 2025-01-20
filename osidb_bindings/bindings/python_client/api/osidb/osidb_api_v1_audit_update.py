from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.audit import Audit
from ...models.osidb_api_v1_audit_update_response_200 import (
    OsidbApiV1AuditUpdateResponse200,
)
from ...types import UNSET, Response, Unset, check_nested_instance

QUERY_PARAMS = {}

REQUEST_BODY_TYPE = Audit


def _get_kwargs(
    pgh_slug: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        Audit,
        Audit,
        Audit,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/audit/{pgh_slug}".format(
            pgh_slug=pgh_slug,
        ),
    }

    if check_nested_instance(body, Audit):
        _json_body: dict[str, Any] = UNSET
        if not isinstance(body, Unset):
            _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1AuditUpdateResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1AuditUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AuditUpdateResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1AuditUpdateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pgh_slug: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        Audit,
        Audit,
        Audit,
    ],
) -> Response[OsidbApiV1AuditUpdateResponse200]:
    """basic view of audit history events

    Args:
        pgh_slug (str): The unique identifier across all event tables.
        body (Audit):
        body (Audit):
        body (Audit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AuditUpdateResponse200]
    """

    kwargs = _get_kwargs(
        pgh_slug=pgh_slug,
        client=client,
        body=body,
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
    pgh_slug: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        Audit,
        Audit,
        Audit,
    ],
) -> Optional[OsidbApiV1AuditUpdateResponse200]:
    """basic view of audit history events

    Args:
        pgh_slug (str): The unique identifier across all event tables.
        body (Audit):
        body (Audit):
        body (Audit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AuditUpdateResponse200
    """

    return sync_detailed(
        pgh_slug=pgh_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pgh_slug: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        Audit,
        Audit,
        Audit,
    ],
) -> Response[OsidbApiV1AuditUpdateResponse200]:
    """basic view of audit history events

    Args:
        pgh_slug (str): The unique identifier across all event tables.
        body (Audit):
        body (Audit):
        body (Audit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1AuditUpdateResponse200]
    """

    kwargs = _get_kwargs(
        pgh_slug=pgh_slug,
        client=client,
        body=body,
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
    pgh_slug: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        Audit,
        Audit,
        Audit,
    ],
) -> Optional[OsidbApiV1AuditUpdateResponse200]:
    """basic view of audit history events

    Args:
        pgh_slug (str): The unique identifier across all event tables.
        body (Audit):
        body (Audit):
        body (Audit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1AuditUpdateResponse200
    """

    return (
        await asyncio_detailed(
            pgh_slug=pgh_slug,
            client=client,
            body=body,
        )
    ).parsed
