from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.affect_cvss_post import AffectCVSSPost
from ...models.osidb_api_v1_affects_cvss_scores_create_response_201 import (
    OsidbApiV1AffectsCvssScoresCreateResponse201,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}
REQUEST_BODY_TYPE = AffectCVSSPost


def _get_kwargs(
    affect_id: str,
    *,
    client: AuthenticatedClient,
    form_data: AffectCVSSPost,
    multipart_data: AffectCVSSPost,
    json_body: AffectCVSSPost,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/affects/{affect_id}/cvss_scores".format(
        client.base_url,
        affect_id=affect_id,
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
) -> Optional[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    if response.status_code == 201:
        _response_201 = response.json()
        response_201: OsidbApiV1AffectsCvssScoresCreateResponse201
        if isinstance(_response_201, Unset):
            response_201 = UNSET
        else:
            response_201 = OsidbApiV1AffectsCvssScoresCreateResponse201.from_dict(
                _response_201
            )

        return response_201
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    affect_id: str,
    *,
    client: AuthenticatedClient,
    form_data: AffectCVSSPost,
    multipart_data: AffectCVSSPost,
    json_body: AffectCVSSPost,
) -> Response[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    kwargs = _get_kwargs(
        affect_id=affect_id,
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
    affect_id: str,
    *,
    client: AuthenticatedClient,
    form_data: AffectCVSSPost,
    multipart_data: AffectCVSSPost,
    json_body: AffectCVSSPost,
) -> Optional[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    """ """

    return sync_detailed(
        affect_id=affect_id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def async_detailed(
    affect_id: str,
    *,
    client: AuthenticatedClient,
    form_data: AffectCVSSPost,
    multipart_data: AffectCVSSPost,
    json_body: AffectCVSSPost,
) -> Response[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    kwargs = _get_kwargs(
        affect_id=affect_id,
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
    affect_id: str,
    *,
    client: AuthenticatedClient,
    form_data: AffectCVSSPost,
    multipart_data: AffectCVSSPost,
    json_body: AffectCVSSPost,
) -> Optional[OsidbApiV1AffectsCvssScoresCreateResponse201]:
    """ """

    return (
        await async_detailed(
            affect_id=affect_id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
