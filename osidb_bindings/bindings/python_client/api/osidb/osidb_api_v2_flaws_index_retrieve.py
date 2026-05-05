from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v2_flaws_index_retrieve_id_type import (
    OsidbApiV2FlawsIndexRetrieveIdType,
)
from ...models.osidb_api_v2_flaws_index_retrieve_response_200 import (
    OsidbApiV2FlawsIndexRetrieveResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "id_type": OsidbApiV2FlawsIndexRetrieveIdType,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id_type: Union[Unset, OsidbApiV2FlawsIndexRetrieveIdType] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    json_id_type: Union[Unset, str] = UNSET
    if not isinstance(id_type, Unset):
        json_id_type = OsidbApiV2FlawsIndexRetrieveIdType(id_type).value

    params["id_type"] = json_id_type

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v2/flaws/index",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV2FlawsIndexRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV2FlawsIndexRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV2FlawsIndexRetrieveResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV2FlawsIndexRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id_type: Union[Unset, OsidbApiV2FlawsIndexRetrieveIdType] = UNSET,
) -> Response[OsidbApiV2FlawsIndexRetrieveResponse200]:
    """Simple API endpoint to return ID and local update time pairs

    Args:
        id_type (Union[Unset, OsidbApiV2FlawsIndexRetrieveIdType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2FlawsIndexRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        id_type=id_type,
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
    *,
    client: AuthenticatedClient,
    id_type: Union[Unset, OsidbApiV2FlawsIndexRetrieveIdType] = UNSET,
) -> Optional[OsidbApiV2FlawsIndexRetrieveResponse200]:
    """Simple API endpoint to return ID and local update time pairs

    Args:
        id_type (Union[Unset, OsidbApiV2FlawsIndexRetrieveIdType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2FlawsIndexRetrieveResponse200
    """

    return sync_detailed(
        client=client,
        id_type=id_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id_type: Union[Unset, OsidbApiV2FlawsIndexRetrieveIdType] = UNSET,
) -> Response[OsidbApiV2FlawsIndexRetrieveResponse200]:
    """Simple API endpoint to return ID and local update time pairs

    Args:
        id_type (Union[Unset, OsidbApiV2FlawsIndexRetrieveIdType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2FlawsIndexRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        id_type=id_type,
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
    *,
    client: AuthenticatedClient,
    id_type: Union[Unset, OsidbApiV2FlawsIndexRetrieveIdType] = UNSET,
) -> Optional[OsidbApiV2FlawsIndexRetrieveResponse200]:
    """Simple API endpoint to return ID and local update time pairs

    Args:
        id_type (Union[Unset, OsidbApiV2FlawsIndexRetrieveIdType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2FlawsIndexRetrieveResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            id_type=id_type,
        )
    ).parsed
