from typing import Any, Dict, List, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_flaws_retrieve_response_200 import (
    OsidbApiV1FlawsRetrieveResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "exclude_fields": List[str],
    "flaw_meta_type": List[str],
    "include_fields": List[str],
    "include_meta_attr": List[str],
    "tracker_ids": List[str],
}


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws/{id}".format(
        client.base_url,
        id=id,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_exclude_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        if exclude_fields is None:
            json_exclude_fields = None
        else:
            json_exclude_fields = exclude_fields

    json_flaw_meta_type: Union[Unset, None, List[str]] = UNSET
    if not isinstance(flaw_meta_type, Unset):
        if flaw_meta_type is None:
            json_flaw_meta_type = None
        else:
            json_flaw_meta_type = flaw_meta_type

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

    json_tracker_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tracker_ids, Unset):
        if tracker_ids is None:
            json_tracker_ids = None
        else:
            json_tracker_ids = tracker_ids

    params: Dict[str, Any] = {
        "exclude_fields": json_exclude_fields,
        "flaw_meta_type": json_flaw_meta_type,
        "include_fields": json_include_fields,
        "include_meta_attr": json_include_meta_attr,
        "tracker_ids": json_tracker_ids,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1FlawsRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsRetrieveResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsRetrieveResponse200]:
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
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
) -> Response[OsidbApiV1FlawsRetrieveResponse200]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        exclude_fields=exclude_fields,
        flaw_meta_type=flaw_meta_type,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        tracker_ids=tracker_ids,
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
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
) -> Optional[OsidbApiV1FlawsRetrieveResponse200]:
    """ """

    return sync_detailed(
        id=id,
        client=client,
        exclude_fields=exclude_fields,
        flaw_meta_type=flaw_meta_type,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        tracker_ids=tracker_ids,
    ).parsed


async def async_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
) -> Response[OsidbApiV1FlawsRetrieveResponse200]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        exclude_fields=exclude_fields,
        flaw_meta_type=flaw_meta_type,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        tracker_ids=tracker_ids,
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
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
) -> Optional[OsidbApiV1FlawsRetrieveResponse200]:
    """ """

    return (
        await async_detailed(
            id=id,
            client=client,
            exclude_fields=exclude_fields,
            flaw_meta_type=flaw_meta_type,
            include_fields=include_fields,
            include_meta_attr=include_meta_attr,
            tracker_ids=tracker_ids,
        )
    ).parsed
