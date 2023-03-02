from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_flaws_destroy_response_204 import (
    OsidbApiV1FlawsDestroyResponse204,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws/{id}".format(
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
) -> Optional[OsidbApiV1FlawsDestroyResponse204]:
    if response.status_code == 204:
        _response_204 = response.json()
        response_204: OsidbApiV1FlawsDestroyResponse204
        if isinstance(_response_204, Unset):
            response_204 = UNSET
        else:
            response_204 = OsidbApiV1FlawsDestroyResponse204.from_dict(_response_204)

        return response_204
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsDestroyResponse204]:
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
) -> Response[OsidbApiV1FlawsDestroyResponse204]:
    kwargs = _get_kwargs(
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
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1FlawsDestroyResponse204]:
    """ """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


QUERY_PARAMS = {}
