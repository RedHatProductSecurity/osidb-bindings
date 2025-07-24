from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_available_flaws_retrieve_response_204 import (
    OsidbApiV1AvailableFlawsRetrieveResponse204,
)
from ...models.osidb_api_v1_available_flaws_retrieve_response_400 import (
    OsidbApiV1AvailableFlawsRetrieveResponse400,
)
from ...models.osidb_api_v1_available_flaws_retrieve_response_404 import (
    OsidbApiV1AvailableFlawsRetrieveResponse404,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    cve_id: str,
    *,
    client: AuthenticatedClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/available-flaws/{cve_id}".format(
            cve_id=cve_id,
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[
    Union[
        OsidbApiV1AvailableFlawsRetrieveResponse204,
        OsidbApiV1AvailableFlawsRetrieveResponse400,
        OsidbApiV1AvailableFlawsRetrieveResponse404,
    ]
]:
    if response.status_code == 204:
        _response_204 = response.json()
        response_204: OsidbApiV1AvailableFlawsRetrieveResponse204
        if isinstance(_response_204, Unset):
            response_204 = UNSET
        else:
            response_204 = OsidbApiV1AvailableFlawsRetrieveResponse204.from_dict(
                _response_204
            )

        return response_204
    if response.status_code == 400:
        _response_400 = response.json()
        response_400: OsidbApiV1AvailableFlawsRetrieveResponse400
        if isinstance(_response_400, Unset):
            response_400 = UNSET
        else:
            response_400 = OsidbApiV1AvailableFlawsRetrieveResponse400.from_dict(
                _response_400
            )

        return response_400
    if response.status_code == 404:
        _response_404 = response.json()
        response_404: OsidbApiV1AvailableFlawsRetrieveResponse404
        if isinstance(_response_404, Unset):
            response_404 = UNSET
        else:
            response_404 = OsidbApiV1AvailableFlawsRetrieveResponse404.from_dict(
                _response_404
            )

        return response_404


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[
    Union[
        OsidbApiV1AvailableFlawsRetrieveResponse204,
        OsidbApiV1AvailableFlawsRetrieveResponse400,
        OsidbApiV1AvailableFlawsRetrieveResponse404,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cve_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        OsidbApiV1AvailableFlawsRetrieveResponse204,
        OsidbApiV1AvailableFlawsRetrieveResponse400,
        OsidbApiV1AvailableFlawsRetrieveResponse404,
    ]
]:
    r"""Report whether a flaw is available for public consumption purposes
    based on the following criteria:
    1) The work on the flaw is done, or the flaw is public:
        - 204 status (yes, flaw is available for public consumption)
    2) The work on the flaw is not done yet, or the flaw doesn't exist in the DB:
        - 404 status (no, flaw is unavailable for public consumption)
    3) Invalid CVE ID:
        - 400 status

    The intention is that this API is consumed by an agent that publishes pages
    with information about individual CVEs. As long as this API returns 404,
    the agent waits and doesn't publish the CVE page. Once this API first returns 204,
    the agent stops polling this API and publishes the CVE page. The consumers of such
    CVE pages are then informed about the CVE in such a way that the general affectedness
    (\"Does the CVE affect products shipped by the organization that publishes the CVE
    page, or not?\") most likely doesn't change. So this is to prevent public confusion
    during the early stages of security analysis where the preliminary analysis might
    switch between \"this CVE affects our products\" and \"this CVE doesn't affect our products\".

    Args:
        cve_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OsidbApiV1AvailableFlawsRetrieveResponse204, OsidbApiV1AvailableFlawsRetrieveResponse400, OsidbApiV1AvailableFlawsRetrieveResponse404]]
    """

    kwargs = _get_kwargs(
        cve_id=cve_id,
        client=client,
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
    cve_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        OsidbApiV1AvailableFlawsRetrieveResponse204,
        OsidbApiV1AvailableFlawsRetrieveResponse400,
        OsidbApiV1AvailableFlawsRetrieveResponse404,
    ]
]:
    r"""Report whether a flaw is available for public consumption purposes
    based on the following criteria:
    1) The work on the flaw is done, or the flaw is public:
        - 204 status (yes, flaw is available for public consumption)
    2) The work on the flaw is not done yet, or the flaw doesn't exist in the DB:
        - 404 status (no, flaw is unavailable for public consumption)
    3) Invalid CVE ID:
        - 400 status

    The intention is that this API is consumed by an agent that publishes pages
    with information about individual CVEs. As long as this API returns 404,
    the agent waits and doesn't publish the CVE page. Once this API first returns 204,
    the agent stops polling this API and publishes the CVE page. The consumers of such
    CVE pages are then informed about the CVE in such a way that the general affectedness
    (\"Does the CVE affect products shipped by the organization that publishes the CVE
    page, or not?\") most likely doesn't change. So this is to prevent public confusion
    during the early stages of security analysis where the preliminary analysis might
    switch between \"this CVE affects our products\" and \"this CVE doesn't affect our products\".

    Args:
        cve_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OsidbApiV1AvailableFlawsRetrieveResponse204, OsidbApiV1AvailableFlawsRetrieveResponse400, OsidbApiV1AvailableFlawsRetrieveResponse404]
    """

    return sync_detailed(
        cve_id=cve_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cve_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        OsidbApiV1AvailableFlawsRetrieveResponse204,
        OsidbApiV1AvailableFlawsRetrieveResponse400,
        OsidbApiV1AvailableFlawsRetrieveResponse404,
    ]
]:
    r"""Report whether a flaw is available for public consumption purposes
    based on the following criteria:
    1) The work on the flaw is done, or the flaw is public:
        - 204 status (yes, flaw is available for public consumption)
    2) The work on the flaw is not done yet, or the flaw doesn't exist in the DB:
        - 404 status (no, flaw is unavailable for public consumption)
    3) Invalid CVE ID:
        - 400 status

    The intention is that this API is consumed by an agent that publishes pages
    with information about individual CVEs. As long as this API returns 404,
    the agent waits and doesn't publish the CVE page. Once this API first returns 204,
    the agent stops polling this API and publishes the CVE page. The consumers of such
    CVE pages are then informed about the CVE in such a way that the general affectedness
    (\"Does the CVE affect products shipped by the organization that publishes the CVE
    page, or not?\") most likely doesn't change. So this is to prevent public confusion
    during the early stages of security analysis where the preliminary analysis might
    switch between \"this CVE affects our products\" and \"this CVE doesn't affect our products\".

    Args:
        cve_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OsidbApiV1AvailableFlawsRetrieveResponse204, OsidbApiV1AvailableFlawsRetrieveResponse400, OsidbApiV1AvailableFlawsRetrieveResponse404]]
    """

    kwargs = _get_kwargs(
        cve_id=cve_id,
        client=client,
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
    cve_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        OsidbApiV1AvailableFlawsRetrieveResponse204,
        OsidbApiV1AvailableFlawsRetrieveResponse400,
        OsidbApiV1AvailableFlawsRetrieveResponse404,
    ]
]:
    r"""Report whether a flaw is available for public consumption purposes
    based on the following criteria:
    1) The work on the flaw is done, or the flaw is public:
        - 204 status (yes, flaw is available for public consumption)
    2) The work on the flaw is not done yet, or the flaw doesn't exist in the DB:
        - 404 status (no, flaw is unavailable for public consumption)
    3) Invalid CVE ID:
        - 400 status

    The intention is that this API is consumed by an agent that publishes pages
    with information about individual CVEs. As long as this API returns 404,
    the agent waits and doesn't publish the CVE page. Once this API first returns 204,
    the agent stops polling this API and publishes the CVE page. The consumers of such
    CVE pages are then informed about the CVE in such a way that the general affectedness
    (\"Does the CVE affect products shipped by the organization that publishes the CVE
    page, or not?\") most likely doesn't change. So this is to prevent public confusion
    during the early stages of security analysis where the preliminary analysis might
    switch between \"this CVE affects our products\" and \"this CVE doesn't affect our products\".

    Args:
        cve_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OsidbApiV1AvailableFlawsRetrieveResponse204, OsidbApiV1AvailableFlawsRetrieveResponse400, OsidbApiV1AvailableFlawsRetrieveResponse404]
    """

    return (
        await asyncio_detailed(
            cve_id=cve_id,
            client=client,
        )
    ).parsed
