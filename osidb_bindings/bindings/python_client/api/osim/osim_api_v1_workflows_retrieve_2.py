from typing import Any, Dict, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.osim_api_v1_workflows_retrieve_2_response_200 import (
    OsimApiV1WorkflowsRetrieve2Response200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "verbose": bool,
}


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    verbose: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osim/api/v1/workflows/{id}".format(
        client.base_url,
        id=id,
    )

    headers: Dict[str, Any] = client.get_headers()

    params: Dict[str, Any] = {
        "verbose": verbose,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsimApiV1WorkflowsRetrieve2Response200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsimApiV1WorkflowsRetrieve2Response200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsimApiV1WorkflowsRetrieve2Response200.from_dict(
                _response_200
            )

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsimApiV1WorkflowsRetrieve2Response200]:
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
    verbose: Union[Unset, None, bool] = UNSET,
) -> Response[OsimApiV1WorkflowsRetrieve2Response200]:
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

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    verbose: Union[Unset, None, bool] = UNSET,
) -> Optional[OsimApiV1WorkflowsRetrieve2Response200]:
    """workflow classification API endpoint

    for flaw identified by UUID or CVE returns its workflow:state classification

    params:

        verbose - return also workflows with flaw classification
                  which represents the reasoning of the result"""

    return sync_detailed(
        id=id,
        client=client,
        verbose=verbose,
    ).parsed


async def async_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    verbose: Union[Unset, None, bool] = UNSET,
) -> Response[OsimApiV1WorkflowsRetrieve2Response200]:
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

    return _build_response(response=resp)


async def async_(
    id: str,
    *,
    client: AuthenticatedClient,
    verbose: Union[Unset, None, bool] = UNSET,
) -> Optional[OsimApiV1WorkflowsRetrieve2Response200]:
    """workflow classification API endpoint

    for flaw identified by UUID or CVE returns its workflow:state classification

    params:

        verbose - return also workflows with flaw classification
                  which represents the reasoning of the result"""

    return (
        await async_detailed(
            id=id,
            client=client,
            verbose=verbose,
        )
    ).parsed
