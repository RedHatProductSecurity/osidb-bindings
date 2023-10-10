from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_flaws_acknowledgments_destroy_response_200 import (
    OsidbApiV1FlawsAcknowledgmentsDestroyResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    flaw_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws/{flaw_id}/acknowledgments/{id}".format(
        client.base_url,
        flaw_id=flaw_id,
        id=id,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsAcknowledgmentsDestroyResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsAcknowledgmentsDestroyResponse200.from_dict(
                _response_200
            )

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    flaw_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        id=id,
        client=client,
    )

    response = requests.delete(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    flaw_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    """Destroy the instance and proxy the delete to Bugzilla"""

    return sync_detailed(
        flaw_id=flaw_id,
        id=id,
        client=client,
    ).parsed


async def async_detailed(
    flaw_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        id=id,
        client=client,
    )

    async with client.get_async_session().delete(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(response=resp)


async def async_(
    flaw_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1FlawsAcknowledgmentsDestroyResponse200]:
    """Destroy the instance and proxy the delete to Bugzilla"""

    return (
        await async_detailed(
            flaw_id=flaw_id,
            id=id,
            client=client,
        )
    ).parsed
