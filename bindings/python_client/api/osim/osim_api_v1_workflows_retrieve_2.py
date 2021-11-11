from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...models.osim_api_v1_workflows_retrieve_2_format import OsimApiV1WorkflowsRetrieve2Format
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, OsimApiV1WorkflowsRetrieve2Format] = UNSET,
    verbose: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "/osim/api/v1/workflows/{id}".format(
        id=id,
    )

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = (
            format_.value
            if isinstance(format_, OsimApiV1WorkflowsRetrieve2Format)
            else OsimApiV1WorkflowsRetrieve2Format(format_).value
            if format_
            else None
        )

    params: Dict[str, Any] = {
        "format": json_format_,
        "verbose": verbose,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, OsimApiV1WorkflowsRetrieve2Format] = UNSET,
    verbose: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        format_=format_,
        verbose=verbose,
    )

    response = client.get_session().get(
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, OsimApiV1WorkflowsRetrieve2Format] = UNSET,
    verbose: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        format_=format_,
        verbose=verbose,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
