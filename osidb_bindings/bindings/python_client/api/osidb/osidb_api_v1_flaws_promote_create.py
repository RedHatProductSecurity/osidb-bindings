from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_flaws_promote_create_response_200 import (
    OsidbApiV1FlawsPromoteCreateResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws/{flaw_id}/promote".format(
        client.base_url,
        flaw_id=flaw_id,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1FlawsPromoteCreateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsPromoteCreateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsPromoteCreateResponse200.from_dict(
                _response_200
            )

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsPromoteCreateResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV1FlawsPromoteCreateResponse200]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
    )

    response = requests.post(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1FlawsPromoteCreateResponse200]:
    """workflow promotion API endpoint

    try to adjust workflow classification of flaw to the next state available
    return its workflow:state classification or errors if not possible to promote"""

    return sync_detailed(
        flaw_id=flaw_id,
        client=client,
    ).parsed


async def async_detailed(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV1FlawsPromoteCreateResponse200]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
    )

    async with client.get_async_session().post(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(response=resp)


async def async_(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1FlawsPromoteCreateResponse200]:
    """workflow promotion API endpoint

    try to adjust workflow classification of flaw to the next state available
    return its workflow:state classification or errors if not possible to promote"""

    return (
        await async_detailed(
            flaw_id=flaw_id,
            client=client,
        )
    ).parsed
