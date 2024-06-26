from typing import Any, Dict, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.flaw import Flaw
from ...models.osidb_api_v1_flaws_update_response_200 import (
    OsidbApiV1FlawsUpdateResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "create_jira_task": bool,
}
REQUEST_BODY_TYPE = Flaw


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
    create_jira_task: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws/{id}".format(
        client.base_url,
        id=id,
    )

    headers: Dict[str, Any] = client.get_headers()

    params: Dict[str, Any] = {
        "create_jira_task": create_jira_task,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

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
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1FlawsUpdateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsUpdateResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsUpdateResponse200]:
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
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
    create_jira_task: Union[Unset, None, bool] = UNSET,
) -> Response[OsidbApiV1FlawsUpdateResponse200]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        create_jira_task=create_jira_task,
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
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
    create_jira_task: Union[Unset, None, bool] = UNSET,
) -> Optional[OsidbApiV1FlawsUpdateResponse200]:
    """ """

    return sync_detailed(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        create_jira_task=create_jira_task,
    ).parsed


async def async_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
    create_jira_task: Union[Unset, None, bool] = UNSET,
) -> Response[OsidbApiV1FlawsUpdateResponse200]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        create_jira_task=create_jira_task,
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
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: Flaw,
    multipart_data: Flaw,
    json_body: Flaw,
    create_jira_task: Union[Unset, None, bool] = UNSET,
) -> Optional[OsidbApiV1FlawsUpdateResponse200]:
    """ """

    return (
        await async_detailed(
            id=id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
            create_jira_task=create_jira_task,
        )
    ).parsed
