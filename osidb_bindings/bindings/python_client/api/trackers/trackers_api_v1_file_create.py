from typing import Any, Dict, List, Optional

import requests

from ...client import AuthenticatedClient
from ...models.flaw_uuid_list import FlawUUIDList
from ...models.tracker_suggestion import TrackerSuggestion
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}
REQUEST_BODY_TYPE = FlawUUIDList


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: FlawUUIDList,
    multipart_data: FlawUUIDList,
    json_body: FlawUUIDList,
) -> Dict[str, Any]:
    url = "{}/trackers/api/v1/file".format(
        client.base_url,
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
) -> Optional[List[TrackerSuggestion]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        if _response_200 is UNSET:
            response_200 = UNSET
        else:
            for response_200_item_data in _response_200 or []:
                _response_200_item = response_200_item_data
                response_200_item: TrackerSuggestion
                if isinstance(_response_200_item, Unset):
                    response_200_item = UNSET
                else:
                    response_200_item = TrackerSuggestion.from_dict(_response_200_item)

                response_200.append(response_200_item)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[List[TrackerSuggestion]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: FlawUUIDList,
    multipart_data: FlawUUIDList,
    json_body: FlawUUIDList,
) -> Response[List[TrackerSuggestion]]:
    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    form_data: FlawUUIDList,
    multipart_data: FlawUUIDList,
    json_body: FlawUUIDList,
) -> Optional[List[TrackerSuggestion]]:
    """Given a list of flaws, generates a list of suggested trackers to file."""

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def async_detailed(
    *,
    client: AuthenticatedClient,
    form_data: FlawUUIDList,
    multipart_data: FlawUUIDList,
    json_body: FlawUUIDList,
) -> Response[List[TrackerSuggestion]]:
    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    form_data: FlawUUIDList,
    multipart_data: FlawUUIDList,
    json_body: FlawUUIDList,
) -> Optional[List[TrackerSuggestion]]:
    """Given a list of flaws, generates a list of suggested trackers to file."""

    return (
        await async_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
