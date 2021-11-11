from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.bzimport_api_v1_jobs_create_format import BzimportApiV1JobsCreateFormat
from ...models.job import Job
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: Job,
    multipart_data: Job,
    json_body: Job,
    format_: Union[Unset, None, BzimportApiV1JobsCreateFormat] = UNSET,
) -> Dict[str, Any]:
    url = "/bzimport/api/v1/jobs"

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = (
            format_.value
            if isinstance(format_, BzimportApiV1JobsCreateFormat)
            else BzimportApiV1JobsCreateFormat(format_).value
            if format_
            else None
        )

    params: Dict[str, Any] = {
        "format": json_format_,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "url": url,
        "data": form_data.to_dict(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Job]:
    if response.status_code == 200:
        response_200 = Job.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Job]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: Job,
    multipart_data: Job,
    json_body: Job,
    format_: Union[Unset, None, BzimportApiV1JobsCreateFormat] = UNSET,
) -> Response[Job]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    )

    response = client.get_session().post(
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    form_data: Job,
    multipart_data: Job,
    json_body: Job,
    format_: Union[Unset, None, BzimportApiV1JobsCreateFormat] = UNSET,
) -> Optional[Job]:
    """HTTP POST /jobs"""

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: Job,
    multipart_data: Job,
    json_body: Job,
    format_: Union[Unset, None, BzimportApiV1JobsCreateFormat] = UNSET,
) -> Response[Job]:
    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: Job,
    multipart_data: Job,
    json_body: Job,
    format_: Union[Unset, None, BzimportApiV1JobsCreateFormat] = UNSET,
) -> Optional[Job]:
    """HTTP POST /jobs"""

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
            format_=format_,
        )
    ).parsed
