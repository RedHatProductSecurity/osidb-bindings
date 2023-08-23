from typing import Any, Dict, Optional

import requests

from ...client import Client
from ...models.auth_token_create_response_200 import AuthTokenCreateResponse200
from ...models.token_obtain_pair import TokenObtainPair
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}
REQUEST_BODY_TYPE = TokenObtainPair


def _get_kwargs(
    *,
    client: Client,
    form_data: TokenObtainPair,
    multipart_data: TokenObtainPair,
    json_body: TokenObtainPair,
) -> Dict[str, Any]:
    url = "{}/auth/token".format(
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
) -> Optional[AuthTokenCreateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: AuthTokenCreateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = AuthTokenCreateResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[AuthTokenCreateResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    form_data: TokenObtainPair,
    multipart_data: TokenObtainPair,
    json_body: TokenObtainPair,
) -> Response[AuthTokenCreateResponse200]:
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
    client: Client,
    form_data: TokenObtainPair,
    multipart_data: TokenObtainPair,
    json_body: TokenObtainPair,
) -> Optional[AuthTokenCreateResponse200]:
    """Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials."""

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def async_detailed(
    *,
    client: Client,
    form_data: TokenObtainPair,
    multipart_data: TokenObtainPair,
    json_body: TokenObtainPair,
) -> Response[AuthTokenCreateResponse200]:
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
    client: Client,
    form_data: TokenObtainPair,
    multipart_data: TokenObtainPair,
    json_body: TokenObtainPair,
) -> Optional[AuthTokenCreateResponse200]:
    """Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials."""

    return (
        await async_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
