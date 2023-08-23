from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.osim_api_v1_workflows_adjust_create_response_200 import (
    OsimApiV1WorkflowsAdjustCreateResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/osim/api/v1/workflows/{id}/adjust".format(
        client.base_url,
        id=id,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsimApiV1WorkflowsAdjustCreateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsimApiV1WorkflowsAdjustCreateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsimApiV1WorkflowsAdjustCreateResponse200.from_dict(
                _response_200
            )

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsimApiV1WorkflowsAdjustCreateResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsimApiV1WorkflowsAdjustCreateResponse200]:
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

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsimApiV1WorkflowsAdjustCreateResponse200]:
    """workflow adjustion API endpoint

    adjust workflow classification of flaw identified by UUID or CVE
    and return its workflow:state classification (new if changed and old otherwise)

    adjust operation is idempotent so when the classification
    is already adjusted running it results in no operation"""

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def async_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsimApiV1WorkflowsAdjustCreateResponse200]:
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

    return _build_response(response=resp)


async def async_(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsimApiV1WorkflowsAdjustCreateResponse200]:
    """workflow adjustion API endpoint

    adjust workflow classification of flaw identified by UUID or CVE
    and return its workflow:state classification (new if changed and old otherwise)

    adjust operation is idempotent so when the classification
    is already adjusted running it results in no operation"""

    return (
        await async_detailed(
            id=id,
            client=client,
        )
    ).parsed
