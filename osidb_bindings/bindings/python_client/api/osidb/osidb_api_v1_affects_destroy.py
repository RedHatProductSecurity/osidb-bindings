from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_affects_destroy_response_204 import (
    OsidbApiV1AffectsDestroyResponse204,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/affects/{uuid}".format(
        client.base_url,
        uuid=uuid,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1AffectsDestroyResponse204]:
    if response.status_code == 204:
        _response_204 = response.json()
        response_204: OsidbApiV1AffectsDestroyResponse204
        if isinstance(_response_204, Unset):
            response_204 = UNSET
        else:
            response_204 = OsidbApiV1AffectsDestroyResponse204.from_dict(_response_204)

        return response_204
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1AffectsDestroyResponse204]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[OsidbApiV1AffectsDestroyResponse204]:
    kwargs = _get_kwargs(
        uuid=uuid,
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
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[OsidbApiV1AffectsDestroyResponse204]:
    """ """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed
