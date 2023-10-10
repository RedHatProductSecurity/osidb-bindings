from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.flaw_post import FlawPost
from ...models.osidb_api_v1_flaws_create_response_201 import (
    OsidbApiV1FlawsCreateResponse201,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}
REQUEST_BODY_TYPE = FlawPost


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: FlawPost,
    multipart_data: FlawPost,
    json_body: FlawPost,
    bugzilla_api_key: str,
    jira_api_key: str,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    headers["bugzilla-api-key"] = bugzilla_api_key
    headers["jira-api-key"] = jira_api_key

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
) -> Optional[OsidbApiV1FlawsCreateResponse201]:
    if response.status_code == 201:
        _response_201 = response.json()
        response_201: OsidbApiV1FlawsCreateResponse201
        if isinstance(_response_201, Unset):
            response_201 = UNSET
        else:
            response_201 = OsidbApiV1FlawsCreateResponse201.from_dict(_response_201)

        return response_201
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsCreateResponse201]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: FlawPost,
    multipart_data: FlawPost,
    json_body: FlawPost,
    bugzilla_api_key: str,
    jira_api_key: str,
) -> Response[OsidbApiV1FlawsCreateResponse201]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        bugzilla_api_key=bugzilla_api_key,
        jira_api_key=jira_api_key,
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
    form_data: FlawPost,
    multipart_data: FlawPost,
    json_body: FlawPost,
    bugzilla_api_key: str,
    jira_api_key: str,
) -> Optional[OsidbApiV1FlawsCreateResponse201]:
    """ """

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        bugzilla_api_key=bugzilla_api_key,
        jira_api_key=jira_api_key,
    ).parsed


async def async_detailed(
    *,
    client: AuthenticatedClient,
    form_data: FlawPost,
    multipart_data: FlawPost,
    json_body: FlawPost,
    bugzilla_api_key: str,
    jira_api_key: str,
) -> Response[OsidbApiV1FlawsCreateResponse201]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        bugzilla_api_key=bugzilla_api_key,
        jira_api_key=jira_api_key,
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
    form_data: FlawPost,
    multipart_data: FlawPost,
    json_body: FlawPost,
    bugzilla_api_key: str,
    jira_api_key: str,
) -> Optional[OsidbApiV1FlawsCreateResponse201]:
    """ """

    return (
        await async_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
            bugzilla_api_key=bugzilla_api_key,
            jira_api_key=jira_api_key,
        )
    ).parsed
