from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.flaw_comment_post import FlawCommentPost
from ...models.osidb_api_v1_flaws_comments_create_response_201 import (
    OsidbApiV1FlawsCommentsCreateResponse201,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}
REQUEST_BODY_TYPE = FlawCommentPost


def _get_kwargs(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    form_data: FlawCommentPost,
    multipart_data: FlawCommentPost,
    json_body: FlawCommentPost,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws/{flaw_id}/comments".format(
        client.base_url,
        flaw_id=flaw_id,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_json_body: Dict[str, Any] = UNSET
    if not isinstance(json_body, Unset):
        json_body.to_dict()

    multipart_multipart_data: Dict[str, Any] = UNSET
    if not isinstance(multipart_data, Unset):
        multipart_data.to_multipart()

    return {
        "url": url,
        "headers": headers,
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1FlawsCommentsCreateResponse201]:
    if response.status_code == 201:
        _response_201 = response.json()
        response_201: OsidbApiV1FlawsCommentsCreateResponse201
        if isinstance(_response_201, Unset):
            response_201 = UNSET
        else:
            response_201 = OsidbApiV1FlawsCommentsCreateResponse201.from_dict(
                _response_201
            )

        return response_201
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsCommentsCreateResponse201]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    form_data: FlawCommentPost,
    multipart_data: FlawCommentPost,
    json_body: FlawCommentPost,
) -> Response[OsidbApiV1FlawsCommentsCreateResponse201]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
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
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    form_data: FlawCommentPost,
    multipart_data: FlawCommentPost,
    json_body: FlawCommentPost,
) -> Optional[OsidbApiV1FlawsCommentsCreateResponse201]:
    """Create a new comment for a given flaw. Beware that freshly created comments are not guaranteed to keep their original UUIDs, especially if multiple comments are created simultaneously."""

    return sync_detailed(
        flaw_id=flaw_id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def async_detailed(
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    form_data: FlawCommentPost,
    multipart_data: FlawCommentPost,
    json_body: FlawCommentPost,
) -> Response[OsidbApiV1FlawsCommentsCreateResponse201]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
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
    flaw_id: str,
    *,
    client: AuthenticatedClient,
    form_data: FlawCommentPost,
    multipart_data: FlawCommentPost,
    json_body: FlawCommentPost,
) -> Optional[OsidbApiV1FlawsCommentsCreateResponse201]:
    """Create a new comment for a given flaw. Beware that freshly created comments are not guaranteed to keep their original UUIDs, especially if multiple comments are created simultaneously."""

    return (
        await async_detailed(
            flaw_id=flaw_id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
