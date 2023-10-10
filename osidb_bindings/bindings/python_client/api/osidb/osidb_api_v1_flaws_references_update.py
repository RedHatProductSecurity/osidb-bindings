from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.flaw_reference_put import FlawReferencePut
from ...models.osidb_api_v1_flaws_references_update_response_200 import (
    OsidbApiV1FlawsReferencesUpdateResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}
REQUEST_BODY_TYPE = FlawReferencePut


def _get_kwargs(
    flaw_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: FlawReferencePut,
    multipart_data: FlawReferencePut,
    json_body: FlawReferencePut,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws/{flaw_id}/references/{id}".format(
        client.base_url,
        flaw_id=flaw_id,
        id=id,
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
) -> Optional[OsidbApiV1FlawsReferencesUpdateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsReferencesUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsReferencesUpdateResponse200.from_dict(
                _response_200
            )

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsReferencesUpdateResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    flaw_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: FlawReferencePut,
    multipart_data: FlawReferencePut,
    json_body: FlawReferencePut,
) -> Response[OsidbApiV1FlawsReferencesUpdateResponse200]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        id=id,
        client=client,
        form_data=form_data,
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
    flaw_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: FlawReferencePut,
    multipart_data: FlawReferencePut,
    json_body: FlawReferencePut,
) -> Optional[OsidbApiV1FlawsReferencesUpdateResponse200]:
    """ """

    return sync_detailed(
        flaw_id=flaw_id,
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def async_detailed(
    flaw_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: FlawReferencePut,
    multipart_data: FlawReferencePut,
    json_body: FlawReferencePut,
) -> Response[OsidbApiV1FlawsReferencesUpdateResponse200]:
    kwargs = _get_kwargs(
        flaw_id=flaw_id,
        id=id,
        client=client,
        form_data=form_data,
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
    flaw_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: FlawReferencePut,
    multipart_data: FlawReferencePut,
    json_body: FlawReferencePut,
) -> Optional[OsidbApiV1FlawsReferencesUpdateResponse200]:
    """ """

    return (
        await async_detailed(
            flaw_id=flaw_id,
            id=id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
