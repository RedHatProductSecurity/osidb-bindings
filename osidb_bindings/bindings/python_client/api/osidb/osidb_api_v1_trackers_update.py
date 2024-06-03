from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_trackers_update_response_200 import (
    OsidbApiV1TrackersUpdateResponse200,
)
from ...models.tracker import Tracker
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}
REQUEST_BODY_TYPE = Tracker


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: Tracker,
    multipart_data: Tracker,
    json_body: Tracker,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/trackers/{uuid}".format(
        client.base_url,
        uuid=uuid,
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
        "json": form_data.to_dict(),
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1TrackersUpdateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1TrackersUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1TrackersUpdateResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1TrackersUpdateResponse200]:
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
    form_data: Tracker,
    multipart_data: Tracker,
    json_body: Tracker,
) -> Response[OsidbApiV1TrackersUpdateResponse200]:
    kwargs = _get_kwargs(
        uuid=uuid,
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
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: Tracker,
    multipart_data: Tracker,
    json_body: Tracker,
) -> Optional[OsidbApiV1TrackersUpdateResponse200]:
    """ """

    return sync_detailed(
        uuid=uuid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def async_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: Tracker,
    multipart_data: Tracker,
    json_body: Tracker,
) -> Response[OsidbApiV1TrackersUpdateResponse200]:
    kwargs = _get_kwargs(
        uuid=uuid,
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
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: Tracker,
    multipart_data: Tracker,
    json_body: Tracker,
) -> Optional[OsidbApiV1TrackersUpdateResponse200]:
    """ """

    return (
        await async_detailed(
            uuid=uuid,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
