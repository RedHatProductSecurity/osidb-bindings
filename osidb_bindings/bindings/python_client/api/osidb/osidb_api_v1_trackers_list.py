from typing import Any, Dict, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_trackers_list_response_200 import OsidbApiV1TrackersListResponse200
from ...models.osidb_api_v1_trackers_list_type import OsidbApiV1TrackersListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    external_system_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    ps_update_stream: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1TrackersListType] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/trackers".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):

        json_type = OsidbApiV1TrackersListType(type).value if type else None

    params: Dict[str, Any] = {
        "external_system_id": external_system_id,
        "limit": limit,
        "offset": offset,
        "ps_update_stream": ps_update_stream,
        "resolution": resolution,
        "status": status,
        "type": json_type,
        "uuid": uuid,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(*, response: requests.Response) -> Optional[OsidbApiV1TrackersListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1TrackersListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1TrackersListResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: requests.Response) -> Response[OsidbApiV1TrackersListResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    external_system_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    ps_update_stream: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1TrackersListType] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1TrackersListResponse200]:
    kwargs = _get_kwargs(
        client=client,
        external_system_id=external_system_id,
        limit=limit,
        offset=offset,
        ps_update_stream=ps_update_stream,
        resolution=resolution,
        status=status,
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
    external_system_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    ps_update_stream: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1TrackersListType] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1TrackersListResponse200]:
    """ """

    return sync_detailed(
        client=client,
        external_system_id=external_system_id,
        limit=limit,
        offset=offset,
        ps_update_stream=ps_update_stream,
        resolution=resolution,
        status=status,
        type=type,
        uuid=uuid,
    ).parsed
