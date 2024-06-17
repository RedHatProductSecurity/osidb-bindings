from typing import Any, Dict, List, Optional

import requests

from ...client import AuthenticatedClient
from ...models.affect_bulk_put import AffectBulkPut
from ...models.osidb_api_v1_affects_bulk_update_response_200 import (
    OsidbApiV1AffectsBulkUpdateResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    multipart_data: List[AffectBulkPut],
    json_body: List[AffectBulkPut],
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/affects/bulk".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_json_body: List[Dict[str, Any]] = UNSET
    if not isinstance(json_body, Unset):
        json_json_body = []
        for json_body_item_data in json_body:
            json_body_item: Dict[str, Any] = UNSET
            if not isinstance(json_body_item_data, Unset):
                json_body_item = json_body_item_data.to_dict()

            json_json_body.append(json_body_item)

    multipart_multipart_data: List[Dict[str, Any]] = UNSET
    if not isinstance(multipart_data, Unset):
        multipart_multipart_data = []
        for multipart_data_item_data in multipart_data:
            multipart_data_item: Dict[str, Any] = UNSET
            if not isinstance(multipart_data_item_data, Unset):
                multipart_data_item = multipart_data_item_data.to_dict()

            multipart_multipart_data.append(multipart_data_item)

    return {
        "url": url,
        "headers": headers,
        "json": form_data.to_dict(),
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1AffectsBulkUpdateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1AffectsBulkUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AffectsBulkUpdateResponse200.from_dict(
                _response_200
            )

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1AffectsBulkUpdateResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: List[AffectBulkPut],
    json_body: List[AffectBulkPut],
) -> Response[OsidbApiV1AffectsBulkUpdateResponse200]:
    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = requests.put(
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
    multipart_data: List[AffectBulkPut],
    json_body: List[AffectBulkPut],
) -> Optional[OsidbApiV1AffectsBulkUpdateResponse200]:
    """Bulk update endpoint. Expects a list of dict Affect objects."""

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def async_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: List[AffectBulkPut],
    json_body: List[AffectBulkPut],
) -> Response[OsidbApiV1AffectsBulkUpdateResponse200]:
    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with client.get_async_session().put(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(response=resp)


async def async_(
    *,
    client: AuthenticatedClient,
    multipart_data: List[AffectBulkPut],
    json_body: List[AffectBulkPut],
) -> Optional[OsidbApiV1AffectsBulkUpdateResponse200]:
    """Bulk update endpoint. Expects a list of dict Affect objects."""

    return (
        await async_detailed(
            client=client,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
