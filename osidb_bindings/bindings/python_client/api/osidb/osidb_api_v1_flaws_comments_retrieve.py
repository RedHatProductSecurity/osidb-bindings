from typing import Any, Dict, List, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_flaws_comments_retrieve_response_200 import (
    OsidbApiV1FlawsCommentsRetrieveResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "exclude_fields": List[str],
    "include_fields": List[str],
    "include_meta_attr": List[str],
}


def _get_kwargs(
    flaw_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws/{flaw_id}/comments/{comment_id}".format(
        client.base_url,
        flaw_id=flaw_id,
        comment_id=comment_id,
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

    params: Dict[str, Any] = {
        "exclude_fields": json_exclude_fields,
        "include_fields": json_include_fields,
        "include_meta_attr": json_include_meta_attr,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1FlawsCommentsRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsCommentsRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsCommentsRetrieveResponse200.from_dict(
                _response_200
            )

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsCommentsRetrieveResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    flaw_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
) -> Response[OsidbApiV1FlawsCommentsRetrieveResponse200]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        comment_id=comment_id,
        client=client,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
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
    flaw_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
) -> Optional[OsidbApiV1FlawsCommentsRetrieveResponse200]:
    """Retrieve a single existing comments for a given flaw. Beware that freshly created comments are not guaranteed to keep their original UUIDs, especially if multiple comments are created simultaneously."""

    return sync_detailed(
        flaw_id=flaw_id,
        comment_id=comment_id,
        client=client,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
    ).parsed


async def async_detailed(
    flaw_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
) -> Response[OsidbApiV1FlawsCommentsRetrieveResponse200]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        comment_id=comment_id,
        client=client,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
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
    flaw_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
) -> Optional[OsidbApiV1FlawsCommentsRetrieveResponse200]:
    """Retrieve a single existing comments for a given flaw. Beware that freshly created comments are not guaranteed to keep their original UUIDs, especially if multiple comments are created simultaneously."""

    return (
        await async_detailed(
            flaw_id=flaw_id,
            comment_id=comment_id,
            client=client,
            exclude_fields=exclude_fields,
            include_fields=include_fields,
            include_meta_attr=include_meta_attr,
        )
    ).parsed
