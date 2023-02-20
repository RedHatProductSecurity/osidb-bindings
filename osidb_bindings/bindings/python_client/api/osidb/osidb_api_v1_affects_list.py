from typing import Any, Dict, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_affects_list_affectedness import (
    OsidbApiV1AffectsListAffectedness,
)
from ...models.osidb_api_v1_affects_list_impact import OsidbApiV1AffectsListImpact
from ...models.osidb_api_v1_affects_list_resolution import (
    OsidbApiV1AffectsListResolution,
)
from ...models.osidb_api_v1_affects_list_response_200 import (
    OsidbApiV1AffectsListResponse200,
)
from ...models.osidb_api_v1_affects_list_type import OsidbApiV1AffectsListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    affectedness: Union[Unset, None, OsidbApiV1AffectsListAffectedness] = UNSET,
    flaw: Union[Unset, None, str] = UNSET,
    impact: Union[Unset, None, OsidbApiV1AffectsListImpact] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    ps_component: Union[Unset, None, str] = UNSET,
    ps_module: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, OsidbApiV1AffectsListResolution] = UNSET,
    type: Union[Unset, None, OsidbApiV1AffectsListType] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/affects".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_affectedness: Union[Unset, None, str] = UNSET
    if not isinstance(affectedness, Unset):

        json_affectedness = (
            OsidbApiV1AffectsListAffectedness(affectedness).value
            if affectedness
            else None
        )

    json_impact: Union[Unset, None, str] = UNSET
    if not isinstance(impact, Unset):

        json_impact = OsidbApiV1AffectsListImpact(impact).value if impact else None

    json_resolution: Union[Unset, None, str] = UNSET
    if not isinstance(resolution, Unset):

        json_resolution = (
            OsidbApiV1AffectsListResolution(resolution).value if resolution else None
        )

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):

        json_type = OsidbApiV1AffectsListType(type).value if type else None

    params: Dict[str, Any] = {
        "affectedness": json_affectedness,
        "flaw": flaw,
        "impact": json_impact,
        "limit": limit,
        "offset": offset,
        "ps_component": ps_component,
        "ps_module": ps_module,
        "resolution": json_resolution,
        "type": json_type,
        "uuid": uuid,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1AffectsListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1AffectsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AffectsListResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1AffectsListResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    affectedness: Union[Unset, None, OsidbApiV1AffectsListAffectedness] = UNSET,
    flaw: Union[Unset, None, str] = UNSET,
    impact: Union[Unset, None, OsidbApiV1AffectsListImpact] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    ps_component: Union[Unset, None, str] = UNSET,
    ps_module: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, OsidbApiV1AffectsListResolution] = UNSET,
    type: Union[Unset, None, OsidbApiV1AffectsListType] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1AffectsListResponse200]:
    kwargs = _get_kwargs(
        client=client,
        affectedness=affectedness,
        flaw=flaw,
        impact=impact,
        limit=limit,
        offset=offset,
        ps_component=ps_component,
        ps_module=ps_module,
        resolution=resolution,
        type=type,
        uuid=uuid,
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
    *,
    client: AuthenticatedClient,
    affectedness: Union[Unset, None, OsidbApiV1AffectsListAffectedness] = UNSET,
    flaw: Union[Unset, None, str] = UNSET,
    impact: Union[Unset, None, OsidbApiV1AffectsListImpact] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    ps_component: Union[Unset, None, str] = UNSET,
    ps_module: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, OsidbApiV1AffectsListResolution] = UNSET,
    type: Union[Unset, None, OsidbApiV1AffectsListType] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1AffectsListResponse200]:
    """ """

    return sync_detailed(
        client=client,
        affectedness=affectedness,
        flaw=flaw,
        impact=impact,
        limit=limit,
        offset=offset,
        ps_component=ps_component,
        ps_module=ps_module,
        resolution=resolution,
        type=type,
        uuid=uuid,
    ).parsed
