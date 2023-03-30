from typing import Any, Dict, List, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_trackers_list_response_200 import (
    OsidbApiV1TrackersListResponse200,
)
from ...models.osidb_api_v1_trackers_list_type import OsidbApiV1TrackersListType
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "exclude_fields": List[str],
    "external_system_id": str,
    "include_fields": List[str],
    "include_meta_attr": List[str],
    "limit": int,
    "offset": int,
    "ps_update_stream": str,
    "resolution": str,
    "status": str,
    "type": OsidbApiV1TrackersListType,
    "uuid": str,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    external_system_id: Union[Unset, None, str] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
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

    json_exclude_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        if exclude_fields is None:
            json_exclude_fields = None
        else:
            json_exclude_fields = exclude_fields

    json_include_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_fields, Unset):
        if include_fields is None:
            json_include_fields = None
        else:
            json_include_fields = include_fields

    json_include_meta_attr: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_meta_attr, Unset):
        if include_meta_attr is None:
            json_include_meta_attr = None
        else:
            json_include_meta_attr = include_meta_attr

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):

        json_type = OsidbApiV1TrackersListType(type).value if type else None

    params: Dict[str, Any] = {
        "exclude_fields": json_exclude_fields,
        "external_system_id": external_system_id,
        "include_fields": json_include_fields,
        "include_meta_attr": json_include_meta_attr,
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


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1TrackersListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1TrackersListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1TrackersListResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1TrackersListResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    external_system_id: Union[Unset, None, str] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
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
        exclude_fields=exclude_fields,
        external_system_id=external_system_id,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
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
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    external_system_id: Union[Unset, None, str] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
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
        exclude_fields=exclude_fields,
        external_system_id=external_system_id,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        ps_update_stream=ps_update_stream,
        resolution=resolution,
        status=status,
        type=type,
        uuid=uuid,
    ).parsed
