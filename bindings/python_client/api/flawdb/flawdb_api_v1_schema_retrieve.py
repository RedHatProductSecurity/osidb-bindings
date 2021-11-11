from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.flawdb_api_v1_schema_retrieve_format import FlawdbApiV1SchemaRetrieveFormat
from ...models.flawdb_api_v1_schema_retrieve_lang import FlawdbApiV1SchemaRetrieveLang
from ...models.flawdb_api_v1_schema_retrieve_response_200 import FlawdbApiV1SchemaRetrieveResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, None, FlawdbApiV1SchemaRetrieveLang] = UNSET,
) -> Dict[str, Any]:
    url = "/flawdb/api/v1/schema/"

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = (
            format_.value
            if isinstance(format_, FlawdbApiV1SchemaRetrieveFormat)
            else FlawdbApiV1SchemaRetrieveFormat(format_).value
            if format_
            else None
        )

    json_lang: Union[Unset, None, str] = UNSET
    if not isinstance(lang, Unset):
        json_lang = (
            lang.value
            if isinstance(lang, FlawdbApiV1SchemaRetrieveLang)
            else FlawdbApiV1SchemaRetrieveLang(lang).value
            if lang
            else None
        )

    params: Dict[str, Any] = {
        "format": json_format_,
        "lang": json_lang,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[FlawdbApiV1SchemaRetrieveResponse200]:
    if response.status_code == 200:
        response_200 = FlawdbApiV1SchemaRetrieveResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[FlawdbApiV1SchemaRetrieveResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, None, FlawdbApiV1SchemaRetrieveLang] = UNSET,
) -> Response[FlawdbApiV1SchemaRetrieveResponse200]:
    kwargs = _get_kwargs(
        client=client,
        format_=format_,
        lang=lang,
    )

    response = client.get_session().get(
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, None, FlawdbApiV1SchemaRetrieveLang] = UNSET,
) -> Optional[FlawdbApiV1SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json"""

    return sync_detailed(
        client=client,
        format_=format_,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, None, FlawdbApiV1SchemaRetrieveLang] = UNSET,
) -> Response[FlawdbApiV1SchemaRetrieveResponse200]:
    kwargs = _get_kwargs(
        client=client,
        format_=format_,
        lang=lang,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, FlawdbApiV1SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, None, FlawdbApiV1SchemaRetrieveLang] = UNSET,
) -> Optional[FlawdbApiV1SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json"""

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
            lang=lang,
        )
    ).parsed
