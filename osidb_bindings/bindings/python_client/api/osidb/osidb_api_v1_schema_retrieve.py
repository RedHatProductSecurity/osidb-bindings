from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_schema_retrieve_format import OsidbApiV1SchemaRetrieveFormat
from ...models.osidb_api_v1_schema_retrieve_lang import OsidbApiV1SchemaRetrieveLang
from ...models.osidb_api_v1_schema_retrieve_response_200 import (
    OsidbApiV1SchemaRetrieveResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "format": OsidbApiV1SchemaRetrieveFormat,
    "lang": OsidbApiV1SchemaRetrieveLang,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, OsidbApiV1SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, OsidbApiV1SchemaRetrieveLang] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = OsidbApiV1SchemaRetrieveFormat(format_).value

    params["format"] = json_format_

    json_lang: Union[Unset, str] = UNSET
    if not isinstance(lang, Unset):
        json_lang = OsidbApiV1SchemaRetrieveLang(lang).value

    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/schema/",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1SchemaRetrieveResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1SchemaRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1SchemaRetrieveResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1SchemaRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, OsidbApiV1SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, OsidbApiV1SchemaRetrieveLang] = UNSET,
) -> Response[OsidbApiV1SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        format_ (Union[Unset, OsidbApiV1SchemaRetrieveFormat]):
        lang (Union[Unset, OsidbApiV1SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1SchemaRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        format_=format_,
        lang=lang,
    )

    response = requests.get(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, OsidbApiV1SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, OsidbApiV1SchemaRetrieveLang] = UNSET,
) -> Optional[OsidbApiV1SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        format_ (Union[Unset, OsidbApiV1SchemaRetrieveFormat]):
        lang (Union[Unset, OsidbApiV1SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1SchemaRetrieveResponse200
    """

    return sync_detailed(
        client=client,
        format_=format_,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, OsidbApiV1SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, OsidbApiV1SchemaRetrieveLang] = UNSET,
) -> Response[OsidbApiV1SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        format_ (Union[Unset, OsidbApiV1SchemaRetrieveFormat]):
        lang (Union[Unset, OsidbApiV1SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1SchemaRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        format_=format_,
        lang=lang,
    )

    async with client.get_async_session().get(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(client=client, response=resp)


async def asyncio(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, OsidbApiV1SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, OsidbApiV1SchemaRetrieveLang] = UNSET,
) -> Optional[OsidbApiV1SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        format_ (Union[Unset, OsidbApiV1SchemaRetrieveFormat]):
        lang (Union[Unset, OsidbApiV1SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1SchemaRetrieveResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
            lang=lang,
        )
    ).parsed
