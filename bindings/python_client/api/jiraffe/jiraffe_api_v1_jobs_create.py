from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.jiraffe_api_v1_jobs_create_format import JiraffeApiV1JobsCreateFormat
from ...models.jiraffe_job import JiraffeJob
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: JiraffeJob,
    multipart_data: JiraffeJob,
    json_body: JiraffeJob,
    format_: Union[Unset, None, JiraffeApiV1JobsCreateFormat] = UNSET,
) -> Dict[str, Any]:
    url = "/jiraffe/api/v1/jobs"

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = (
            format_.value
            if isinstance(format_, JiraffeApiV1JobsCreateFormat)
            else JiraffeApiV1JobsCreateFormat(format_).value
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


def _parse_response(*, response: httpx.Response) -> Optional[JiraffeJob]:
    if response.status_code == 200:
        response_200 = JiraffeJob.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[JiraffeJob]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: JiraffeJob,
    multipart_data: JiraffeJob,
    json_body: JiraffeJob,
    format_: Union[Unset, None, JiraffeApiV1JobsCreateFormat] = UNSET,
) -> Response[JiraffeJob]:
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
    form_data: JiraffeJob,
    multipart_data: JiraffeJob,
    json_body: JiraffeJob,
    format_: Union[Unset, None, JiraffeApiV1JobsCreateFormat] = UNSET,
) -> Optional[JiraffeJob]:
    """Create a JiraffeJob"""

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
    form_data: JiraffeJob,
    multipart_data: JiraffeJob,
    json_body: JiraffeJob,
    format_: Union[Unset, None, JiraffeApiV1JobsCreateFormat] = UNSET,
) -> Response[JiraffeJob]:
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
    form_data: JiraffeJob,
    multipart_data: JiraffeJob,
    json_body: JiraffeJob,
    format_: Union[Unset, None, JiraffeApiV1JobsCreateFormat] = UNSET,
) -> Optional[JiraffeJob]:
    """Create a JiraffeJob"""

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
            format_=format_,
        )
    ).parsed
