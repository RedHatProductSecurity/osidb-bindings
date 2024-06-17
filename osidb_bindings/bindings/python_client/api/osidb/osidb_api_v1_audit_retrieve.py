from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_audit_retrieve_response_200 import (
    OsidbApiV1AuditRetrieveResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    pgh_slug: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/audit/{pgh_slug}".format(
        client.base_url,
        pgh_slug=pgh_slug,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1AuditRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1AuditRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AuditRetrieveResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1AuditRetrieveResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    pgh_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV1AuditRetrieveResponse200]:
    kwargs = _get_kwargs(
        pgh_slug=pgh_slug,
        client=client,
    )

    response = requests.get(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    pgh_slug: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1AuditRetrieveResponse200]:
    """basic view of audit history events"""

    return sync_detailed(
        pgh_slug=pgh_slug,
        client=client,
    ).parsed


async def async_detailed(
    pgh_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV1AuditRetrieveResponse200]:
    kwargs = _get_kwargs(
        pgh_slug=pgh_slug,
        client=client,
    )

    async with client.get_async_session().get(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(response=resp)


async def async_(
    pgh_slug: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1AuditRetrieveResponse200]:
    """basic view of audit history events"""

    return (
        await async_detailed(
            pgh_slug=pgh_slug,
            client=client,
        )
    ).parsed
