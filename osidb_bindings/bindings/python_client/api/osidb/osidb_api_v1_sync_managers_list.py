import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_sync_managers_list_order_item import (
    OsidbApiV1SyncManagersListOrderItem,
)
from ...models.osidb_api_v1_sync_managers_list_response_200 import (
    OsidbApiV1SyncManagersListResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "last_consecutive_failures": int,
    "last_consecutive_failures__gt": int,
    "last_consecutive_failures__gte": int,
    "last_consecutive_failures__lt": int,
    "last_consecutive_failures__lte": int,
    "last_consecutive_reschedules": int,
    "last_consecutive_reschedules__gt": int,
    "last_consecutive_reschedules__gte": int,
    "last_consecutive_reschedules__lt": int,
    "last_consecutive_reschedules__lte": int,
    "last_failed_dt": datetime.datetime,
    "last_failed_dt__date": datetime.date,
    "last_failed_dt__date__gte": datetime.date,
    "last_failed_dt__date__lte": datetime.date,
    "last_failed_dt__gt": datetime.datetime,
    "last_failed_dt__gte": datetime.datetime,
    "last_failed_dt__lt": datetime.datetime,
    "last_failed_dt__lte": datetime.datetime,
    "last_finished_dt": datetime.datetime,
    "last_finished_dt__date": datetime.date,
    "last_finished_dt__date__gte": datetime.date,
    "last_finished_dt__date__lte": datetime.date,
    "last_finished_dt__gt": datetime.datetime,
    "last_finished_dt__gte": datetime.datetime,
    "last_finished_dt__lt": datetime.datetime,
    "last_finished_dt__lte": datetime.datetime,
    "last_rescheduled_dt": datetime.datetime,
    "last_rescheduled_dt__date": datetime.date,
    "last_rescheduled_dt__date__gte": datetime.date,
    "last_rescheduled_dt__date__lte": datetime.date,
    "last_rescheduled_dt__gt": datetime.datetime,
    "last_rescheduled_dt__gte": datetime.datetime,
    "last_rescheduled_dt__lt": datetime.datetime,
    "last_rescheduled_dt__lte": datetime.datetime,
    "last_scheduled_dt": datetime.datetime,
    "last_scheduled_dt__date": datetime.date,
    "last_scheduled_dt__date__gte": datetime.date,
    "last_scheduled_dt__date__lte": datetime.date,
    "last_scheduled_dt__gt": datetime.datetime,
    "last_scheduled_dt__gte": datetime.datetime,
    "last_scheduled_dt__lt": datetime.datetime,
    "last_scheduled_dt__lte": datetime.datetime,
    "last_started_dt": datetime.datetime,
    "last_started_dt__date": datetime.date,
    "last_started_dt__date__gte": datetime.date,
    "last_started_dt__date__lte": datetime.date,
    "last_started_dt__gt": datetime.datetime,
    "last_started_dt__gte": datetime.datetime,
    "last_started_dt__lt": datetime.datetime,
    "last_started_dt__lte": datetime.datetime,
    "limit": int,
    "name": str,
    "name__in": list[str],
    "offset": int,
    "order": list[OsidbApiV1SyncManagersListOrderItem],
    "permanently_failed": bool,
    "sync_id": str,
    "sync_id__in": list[str],
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    last_consecutive_failures: Union[Unset, int] = UNSET,
    last_consecutive_failures_gt: Union[Unset, int] = UNSET,
    last_consecutive_failures_gte: Union[Unset, int] = UNSET,
    last_consecutive_failures_lt: Union[Unset, int] = UNSET,
    last_consecutive_failures_lte: Union[Unset, int] = UNSET,
    last_consecutive_reschedules: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_gt: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_gte: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_lt: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_lte: Union[Unset, int] = UNSET,
    last_failed_dt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_date: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_date: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_date: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_date: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_date: Union[Unset, datetime.date] = UNSET,
    last_started_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_started_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_started_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1SyncManagersListOrderItem]] = UNSET,
    permanently_failed: Union[Unset, bool] = UNSET,
    sync_id: Union[Unset, str] = UNSET,
    sync_id_in: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["last_consecutive_failures"] = last_consecutive_failures

    params["last_consecutive_failures__gt"] = last_consecutive_failures_gt

    params["last_consecutive_failures__gte"] = last_consecutive_failures_gte

    params["last_consecutive_failures__lt"] = last_consecutive_failures_lt

    params["last_consecutive_failures__lte"] = last_consecutive_failures_lte

    params["last_consecutive_reschedules"] = last_consecutive_reschedules

    params["last_consecutive_reschedules__gt"] = last_consecutive_reschedules_gt

    params["last_consecutive_reschedules__gte"] = last_consecutive_reschedules_gte

    params["last_consecutive_reschedules__lt"] = last_consecutive_reschedules_lt

    params["last_consecutive_reschedules__lte"] = last_consecutive_reschedules_lte

    json_last_failed_dt: Union[Unset, str] = UNSET
    if not isinstance(last_failed_dt, Unset):
        json_last_failed_dt = last_failed_dt.isoformat()

    params["last_failed_dt"] = json_last_failed_dt

    json_last_failed_dt_date: Union[Unset, str] = UNSET
    if not isinstance(last_failed_dt_date, Unset):
        json_last_failed_dt_date = last_failed_dt_date.isoformat()

    params["last_failed_dt__date"] = json_last_failed_dt_date

    json_last_failed_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(last_failed_dt_date_gte, Unset):
        json_last_failed_dt_date_gte = last_failed_dt_date_gte.isoformat()

    params["last_failed_dt__date__gte"] = json_last_failed_dt_date_gte

    json_last_failed_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(last_failed_dt_date_lte, Unset):
        json_last_failed_dt_date_lte = last_failed_dt_date_lte.isoformat()

    params["last_failed_dt__date__lte"] = json_last_failed_dt_date_lte

    json_last_failed_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(last_failed_dt_gt, Unset):
        json_last_failed_dt_gt = last_failed_dt_gt.isoformat()

    params["last_failed_dt__gt"] = json_last_failed_dt_gt

    json_last_failed_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(last_failed_dt_gte, Unset):
        json_last_failed_dt_gte = last_failed_dt_gte.isoformat()

    params["last_failed_dt__gte"] = json_last_failed_dt_gte

    json_last_failed_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(last_failed_dt_lt, Unset):
        json_last_failed_dt_lt = last_failed_dt_lt.isoformat()

    params["last_failed_dt__lt"] = json_last_failed_dt_lt

    json_last_failed_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(last_failed_dt_lte, Unset):
        json_last_failed_dt_lte = last_failed_dt_lte.isoformat()

    params["last_failed_dt__lte"] = json_last_failed_dt_lte

    json_last_finished_dt: Union[Unset, str] = UNSET
    if not isinstance(last_finished_dt, Unset):
        json_last_finished_dt = last_finished_dt.isoformat()

    params["last_finished_dt"] = json_last_finished_dt

    json_last_finished_dt_date: Union[Unset, str] = UNSET
    if not isinstance(last_finished_dt_date, Unset):
        json_last_finished_dt_date = last_finished_dt_date.isoformat()

    params["last_finished_dt__date"] = json_last_finished_dt_date

    json_last_finished_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(last_finished_dt_date_gte, Unset):
        json_last_finished_dt_date_gte = last_finished_dt_date_gte.isoformat()

    params["last_finished_dt__date__gte"] = json_last_finished_dt_date_gte

    json_last_finished_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(last_finished_dt_date_lte, Unset):
        json_last_finished_dt_date_lte = last_finished_dt_date_lte.isoformat()

    params["last_finished_dt__date__lte"] = json_last_finished_dt_date_lte

    json_last_finished_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(last_finished_dt_gt, Unset):
        json_last_finished_dt_gt = last_finished_dt_gt.isoformat()

    params["last_finished_dt__gt"] = json_last_finished_dt_gt

    json_last_finished_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(last_finished_dt_gte, Unset):
        json_last_finished_dt_gte = last_finished_dt_gte.isoformat()

    params["last_finished_dt__gte"] = json_last_finished_dt_gte

    json_last_finished_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(last_finished_dt_lt, Unset):
        json_last_finished_dt_lt = last_finished_dt_lt.isoformat()

    params["last_finished_dt__lt"] = json_last_finished_dt_lt

    json_last_finished_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(last_finished_dt_lte, Unset):
        json_last_finished_dt_lte = last_finished_dt_lte.isoformat()

    params["last_finished_dt__lte"] = json_last_finished_dt_lte

    json_last_rescheduled_dt: Union[Unset, str] = UNSET
    if not isinstance(last_rescheduled_dt, Unset):
        json_last_rescheduled_dt = last_rescheduled_dt.isoformat()

    params["last_rescheduled_dt"] = json_last_rescheduled_dt

    json_last_rescheduled_dt_date: Union[Unset, str] = UNSET
    if not isinstance(last_rescheduled_dt_date, Unset):
        json_last_rescheduled_dt_date = last_rescheduled_dt_date.isoformat()

    params["last_rescheduled_dt__date"] = json_last_rescheduled_dt_date

    json_last_rescheduled_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(last_rescheduled_dt_date_gte, Unset):
        json_last_rescheduled_dt_date_gte = last_rescheduled_dt_date_gte.isoformat()

    params["last_rescheduled_dt__date__gte"] = json_last_rescheduled_dt_date_gte

    json_last_rescheduled_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(last_rescheduled_dt_date_lte, Unset):
        json_last_rescheduled_dt_date_lte = last_rescheduled_dt_date_lte.isoformat()

    params["last_rescheduled_dt__date__lte"] = json_last_rescheduled_dt_date_lte

    json_last_rescheduled_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(last_rescheduled_dt_gt, Unset):
        json_last_rescheduled_dt_gt = last_rescheduled_dt_gt.isoformat()

    params["last_rescheduled_dt__gt"] = json_last_rescheduled_dt_gt

    json_last_rescheduled_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(last_rescheduled_dt_gte, Unset):
        json_last_rescheduled_dt_gte = last_rescheduled_dt_gte.isoformat()

    params["last_rescheduled_dt__gte"] = json_last_rescheduled_dt_gte

    json_last_rescheduled_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(last_rescheduled_dt_lt, Unset):
        json_last_rescheduled_dt_lt = last_rescheduled_dt_lt.isoformat()

    params["last_rescheduled_dt__lt"] = json_last_rescheduled_dt_lt

    json_last_rescheduled_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(last_rescheduled_dt_lte, Unset):
        json_last_rescheduled_dt_lte = last_rescheduled_dt_lte.isoformat()

    params["last_rescheduled_dt__lte"] = json_last_rescheduled_dt_lte

    json_last_scheduled_dt: Union[Unset, str] = UNSET
    if not isinstance(last_scheduled_dt, Unset):
        json_last_scheduled_dt = last_scheduled_dt.isoformat()

    params["last_scheduled_dt"] = json_last_scheduled_dt

    json_last_scheduled_dt_date: Union[Unset, str] = UNSET
    if not isinstance(last_scheduled_dt_date, Unset):
        json_last_scheduled_dt_date = last_scheduled_dt_date.isoformat()

    params["last_scheduled_dt__date"] = json_last_scheduled_dt_date

    json_last_scheduled_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(last_scheduled_dt_date_gte, Unset):
        json_last_scheduled_dt_date_gte = last_scheduled_dt_date_gte.isoformat()

    params["last_scheduled_dt__date__gte"] = json_last_scheduled_dt_date_gte

    json_last_scheduled_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(last_scheduled_dt_date_lte, Unset):
        json_last_scheduled_dt_date_lte = last_scheduled_dt_date_lte.isoformat()

    params["last_scheduled_dt__date__lte"] = json_last_scheduled_dt_date_lte

    json_last_scheduled_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(last_scheduled_dt_gt, Unset):
        json_last_scheduled_dt_gt = last_scheduled_dt_gt.isoformat()

    params["last_scheduled_dt__gt"] = json_last_scheduled_dt_gt

    json_last_scheduled_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(last_scheduled_dt_gte, Unset):
        json_last_scheduled_dt_gte = last_scheduled_dt_gte.isoformat()

    params["last_scheduled_dt__gte"] = json_last_scheduled_dt_gte

    json_last_scheduled_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(last_scheduled_dt_lt, Unset):
        json_last_scheduled_dt_lt = last_scheduled_dt_lt.isoformat()

    params["last_scheduled_dt__lt"] = json_last_scheduled_dt_lt

    json_last_scheduled_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(last_scheduled_dt_lte, Unset):
        json_last_scheduled_dt_lte = last_scheduled_dt_lte.isoformat()

    params["last_scheduled_dt__lte"] = json_last_scheduled_dt_lte

    json_last_started_dt: Union[Unset, str] = UNSET
    if not isinstance(last_started_dt, Unset):
        json_last_started_dt = last_started_dt.isoformat()

    params["last_started_dt"] = json_last_started_dt

    json_last_started_dt_date: Union[Unset, str] = UNSET
    if not isinstance(last_started_dt_date, Unset):
        json_last_started_dt_date = last_started_dt_date.isoformat()

    params["last_started_dt__date"] = json_last_started_dt_date

    json_last_started_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(last_started_dt_date_gte, Unset):
        json_last_started_dt_date_gte = last_started_dt_date_gte.isoformat()

    params["last_started_dt__date__gte"] = json_last_started_dt_date_gte

    json_last_started_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(last_started_dt_date_lte, Unset):
        json_last_started_dt_date_lte = last_started_dt_date_lte.isoformat()

    params["last_started_dt__date__lte"] = json_last_started_dt_date_lte

    json_last_started_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(last_started_dt_gt, Unset):
        json_last_started_dt_gt = last_started_dt_gt.isoformat()

    params["last_started_dt__gt"] = json_last_started_dt_gt

    json_last_started_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(last_started_dt_gte, Unset):
        json_last_started_dt_gte = last_started_dt_gte.isoformat()

    params["last_started_dt__gte"] = json_last_started_dt_gte

    json_last_started_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(last_started_dt_lt, Unset):
        json_last_started_dt_lt = last_started_dt_lt.isoformat()

    params["last_started_dt__lt"] = json_last_started_dt_lt

    json_last_started_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(last_started_dt_lte, Unset):
        json_last_started_dt_lte = last_started_dt_lte.isoformat()

    params["last_started_dt__lte"] = json_last_started_dt_lte

    params["limit"] = limit

    params["name"] = name

    json_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(name_in, Unset):
        json_name_in = name_in

    params["name__in"] = json_name_in

    params["offset"] = offset

    json_order: Union[Unset, list[str]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item: str = UNSET
            if not isinstance(order_item_data, Unset):
                order_item = OsidbApiV1SyncManagersListOrderItem(order_item_data).value

            json_order.append(order_item)

    params["order"] = json_order

    params["permanently_failed"] = permanently_failed

    params["sync_id"] = sync_id

    json_sync_id_in: Union[Unset, list[str]] = UNSET
    if not isinstance(sync_id_in, Unset):
        json_sync_id_in = sync_id_in

    params["sync_id__in"] = json_sync_id_in

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/sync-managers",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1SyncManagersListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1SyncManagersListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1SyncManagersListResponse200.from_dict(
                _response_200
            )

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1SyncManagersListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    last_consecutive_failures: Union[Unset, int] = UNSET,
    last_consecutive_failures_gt: Union[Unset, int] = UNSET,
    last_consecutive_failures_gte: Union[Unset, int] = UNSET,
    last_consecutive_failures_lt: Union[Unset, int] = UNSET,
    last_consecutive_failures_lte: Union[Unset, int] = UNSET,
    last_consecutive_reschedules: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_gt: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_gte: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_lt: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_lte: Union[Unset, int] = UNSET,
    last_failed_dt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_date: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_date: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_date: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_date: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_date: Union[Unset, datetime.date] = UNSET,
    last_started_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_started_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_started_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1SyncManagersListOrderItem]] = UNSET,
    permanently_failed: Union[Unset, bool] = UNSET,
    sync_id: Union[Unset, str] = UNSET,
    sync_id_in: Union[Unset, list[str]] = UNSET,
) -> Response[OsidbApiV1SyncManagersListResponse200]:
    """Read-only view for sync managers

    Args:
        last_consecutive_failures (Union[Unset, int]):
        last_consecutive_failures_gt (Union[Unset, int]):
        last_consecutive_failures_gte (Union[Unset, int]):
        last_consecutive_failures_lt (Union[Unset, int]):
        last_consecutive_failures_lte (Union[Unset, int]):
        last_consecutive_reschedules (Union[Unset, int]):
        last_consecutive_reschedules_gt (Union[Unset, int]):
        last_consecutive_reschedules_gte (Union[Unset, int]):
        last_consecutive_reschedules_lt (Union[Unset, int]):
        last_consecutive_reschedules_lte (Union[Unset, int]):
        last_failed_dt (Union[Unset, datetime.datetime]):
        last_failed_dt_date (Union[Unset, datetime.date]):
        last_failed_dt_date_gte (Union[Unset, datetime.date]):
        last_failed_dt_date_lte (Union[Unset, datetime.date]):
        last_failed_dt_gt (Union[Unset, datetime.datetime]):
        last_failed_dt_gte (Union[Unset, datetime.datetime]):
        last_failed_dt_lt (Union[Unset, datetime.datetime]):
        last_failed_dt_lte (Union[Unset, datetime.datetime]):
        last_finished_dt (Union[Unset, datetime.datetime]):
        last_finished_dt_date (Union[Unset, datetime.date]):
        last_finished_dt_date_gte (Union[Unset, datetime.date]):
        last_finished_dt_date_lte (Union[Unset, datetime.date]):
        last_finished_dt_gt (Union[Unset, datetime.datetime]):
        last_finished_dt_gte (Union[Unset, datetime.datetime]):
        last_finished_dt_lt (Union[Unset, datetime.datetime]):
        last_finished_dt_lte (Union[Unset, datetime.datetime]):
        last_rescheduled_dt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_date (Union[Unset, datetime.date]):
        last_rescheduled_dt_date_gte (Union[Unset, datetime.date]):
        last_rescheduled_dt_date_lte (Union[Unset, datetime.date]):
        last_rescheduled_dt_gt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_gte (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_lt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_lte (Union[Unset, datetime.datetime]):
        last_scheduled_dt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_date (Union[Unset, datetime.date]):
        last_scheduled_dt_date_gte (Union[Unset, datetime.date]):
        last_scheduled_dt_date_lte (Union[Unset, datetime.date]):
        last_scheduled_dt_gt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_gte (Union[Unset, datetime.datetime]):
        last_scheduled_dt_lt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_lte (Union[Unset, datetime.datetime]):
        last_started_dt (Union[Unset, datetime.datetime]):
        last_started_dt_date (Union[Unset, datetime.date]):
        last_started_dt_date_gte (Union[Unset, datetime.date]):
        last_started_dt_date_lte (Union[Unset, datetime.date]):
        last_started_dt_gt (Union[Unset, datetime.datetime]):
        last_started_dt_gte (Union[Unset, datetime.datetime]):
        last_started_dt_lt (Union[Unset, datetime.datetime]):
        last_started_dt_lte (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1SyncManagersListOrderItem]]):
        permanently_failed (Union[Unset, bool]):
        sync_id (Union[Unset, str]):
        sync_id_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1SyncManagersListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        last_consecutive_failures=last_consecutive_failures,
        last_consecutive_failures_gt=last_consecutive_failures_gt,
        last_consecutive_failures_gte=last_consecutive_failures_gte,
        last_consecutive_failures_lt=last_consecutive_failures_lt,
        last_consecutive_failures_lte=last_consecutive_failures_lte,
        last_consecutive_reschedules=last_consecutive_reschedules,
        last_consecutive_reschedules_gt=last_consecutive_reschedules_gt,
        last_consecutive_reschedules_gte=last_consecutive_reschedules_gte,
        last_consecutive_reschedules_lt=last_consecutive_reschedules_lt,
        last_consecutive_reschedules_lte=last_consecutive_reschedules_lte,
        last_failed_dt=last_failed_dt,
        last_failed_dt_date=last_failed_dt_date,
        last_failed_dt_date_gte=last_failed_dt_date_gte,
        last_failed_dt_date_lte=last_failed_dt_date_lte,
        last_failed_dt_gt=last_failed_dt_gt,
        last_failed_dt_gte=last_failed_dt_gte,
        last_failed_dt_lt=last_failed_dt_lt,
        last_failed_dt_lte=last_failed_dt_lte,
        last_finished_dt=last_finished_dt,
        last_finished_dt_date=last_finished_dt_date,
        last_finished_dt_date_gte=last_finished_dt_date_gte,
        last_finished_dt_date_lte=last_finished_dt_date_lte,
        last_finished_dt_gt=last_finished_dt_gt,
        last_finished_dt_gte=last_finished_dt_gte,
        last_finished_dt_lt=last_finished_dt_lt,
        last_finished_dt_lte=last_finished_dt_lte,
        last_rescheduled_dt=last_rescheduled_dt,
        last_rescheduled_dt_date=last_rescheduled_dt_date,
        last_rescheduled_dt_date_gte=last_rescheduled_dt_date_gte,
        last_rescheduled_dt_date_lte=last_rescheduled_dt_date_lte,
        last_rescheduled_dt_gt=last_rescheduled_dt_gt,
        last_rescheduled_dt_gte=last_rescheduled_dt_gte,
        last_rescheduled_dt_lt=last_rescheduled_dt_lt,
        last_rescheduled_dt_lte=last_rescheduled_dt_lte,
        last_scheduled_dt=last_scheduled_dt,
        last_scheduled_dt_date=last_scheduled_dt_date,
        last_scheduled_dt_date_gte=last_scheduled_dt_date_gte,
        last_scheduled_dt_date_lte=last_scheduled_dt_date_lte,
        last_scheduled_dt_gt=last_scheduled_dt_gt,
        last_scheduled_dt_gte=last_scheduled_dt_gte,
        last_scheduled_dt_lt=last_scheduled_dt_lt,
        last_scheduled_dt_lte=last_scheduled_dt_lte,
        last_started_dt=last_started_dt,
        last_started_dt_date=last_started_dt_date,
        last_started_dt_date_gte=last_started_dt_date_gte,
        last_started_dt_date_lte=last_started_dt_date_lte,
        last_started_dt_gt=last_started_dt_gt,
        last_started_dt_gte=last_started_dt_gte,
        last_started_dt_lt=last_started_dt_lt,
        last_started_dt_lte=last_started_dt_lte,
        limit=limit,
        name=name,
        name_in=name_in,
        offset=offset,
        order=order,
        permanently_failed=permanently_failed,
        sync_id=sync_id,
        sync_id_in=sync_id_in,
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
    last_consecutive_failures: Union[Unset, int] = UNSET,
    last_consecutive_failures_gt: Union[Unset, int] = UNSET,
    last_consecutive_failures_gte: Union[Unset, int] = UNSET,
    last_consecutive_failures_lt: Union[Unset, int] = UNSET,
    last_consecutive_failures_lte: Union[Unset, int] = UNSET,
    last_consecutive_reschedules: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_gt: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_gte: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_lt: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_lte: Union[Unset, int] = UNSET,
    last_failed_dt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_date: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_date: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_date: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_date: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_date: Union[Unset, datetime.date] = UNSET,
    last_started_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_started_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_started_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1SyncManagersListOrderItem]] = UNSET,
    permanently_failed: Union[Unset, bool] = UNSET,
    sync_id: Union[Unset, str] = UNSET,
    sync_id_in: Union[Unset, list[str]] = UNSET,
) -> Optional[OsidbApiV1SyncManagersListResponse200]:
    """Read-only view for sync managers

    Args:
        last_consecutive_failures (Union[Unset, int]):
        last_consecutive_failures_gt (Union[Unset, int]):
        last_consecutive_failures_gte (Union[Unset, int]):
        last_consecutive_failures_lt (Union[Unset, int]):
        last_consecutive_failures_lte (Union[Unset, int]):
        last_consecutive_reschedules (Union[Unset, int]):
        last_consecutive_reschedules_gt (Union[Unset, int]):
        last_consecutive_reschedules_gte (Union[Unset, int]):
        last_consecutive_reschedules_lt (Union[Unset, int]):
        last_consecutive_reschedules_lte (Union[Unset, int]):
        last_failed_dt (Union[Unset, datetime.datetime]):
        last_failed_dt_date (Union[Unset, datetime.date]):
        last_failed_dt_date_gte (Union[Unset, datetime.date]):
        last_failed_dt_date_lte (Union[Unset, datetime.date]):
        last_failed_dt_gt (Union[Unset, datetime.datetime]):
        last_failed_dt_gte (Union[Unset, datetime.datetime]):
        last_failed_dt_lt (Union[Unset, datetime.datetime]):
        last_failed_dt_lte (Union[Unset, datetime.datetime]):
        last_finished_dt (Union[Unset, datetime.datetime]):
        last_finished_dt_date (Union[Unset, datetime.date]):
        last_finished_dt_date_gte (Union[Unset, datetime.date]):
        last_finished_dt_date_lte (Union[Unset, datetime.date]):
        last_finished_dt_gt (Union[Unset, datetime.datetime]):
        last_finished_dt_gte (Union[Unset, datetime.datetime]):
        last_finished_dt_lt (Union[Unset, datetime.datetime]):
        last_finished_dt_lte (Union[Unset, datetime.datetime]):
        last_rescheduled_dt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_date (Union[Unset, datetime.date]):
        last_rescheduled_dt_date_gte (Union[Unset, datetime.date]):
        last_rescheduled_dt_date_lte (Union[Unset, datetime.date]):
        last_rescheduled_dt_gt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_gte (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_lt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_lte (Union[Unset, datetime.datetime]):
        last_scheduled_dt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_date (Union[Unset, datetime.date]):
        last_scheduled_dt_date_gte (Union[Unset, datetime.date]):
        last_scheduled_dt_date_lte (Union[Unset, datetime.date]):
        last_scheduled_dt_gt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_gte (Union[Unset, datetime.datetime]):
        last_scheduled_dt_lt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_lte (Union[Unset, datetime.datetime]):
        last_started_dt (Union[Unset, datetime.datetime]):
        last_started_dt_date (Union[Unset, datetime.date]):
        last_started_dt_date_gte (Union[Unset, datetime.date]):
        last_started_dt_date_lte (Union[Unset, datetime.date]):
        last_started_dt_gt (Union[Unset, datetime.datetime]):
        last_started_dt_gte (Union[Unset, datetime.datetime]):
        last_started_dt_lt (Union[Unset, datetime.datetime]):
        last_started_dt_lte (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1SyncManagersListOrderItem]]):
        permanently_failed (Union[Unset, bool]):
        sync_id (Union[Unset, str]):
        sync_id_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1SyncManagersListResponse200
    """

    return sync_detailed(
        client=client,
        last_consecutive_failures=last_consecutive_failures,
        last_consecutive_failures_gt=last_consecutive_failures_gt,
        last_consecutive_failures_gte=last_consecutive_failures_gte,
        last_consecutive_failures_lt=last_consecutive_failures_lt,
        last_consecutive_failures_lte=last_consecutive_failures_lte,
        last_consecutive_reschedules=last_consecutive_reschedules,
        last_consecutive_reschedules_gt=last_consecutive_reschedules_gt,
        last_consecutive_reschedules_gte=last_consecutive_reschedules_gte,
        last_consecutive_reschedules_lt=last_consecutive_reschedules_lt,
        last_consecutive_reschedules_lte=last_consecutive_reschedules_lte,
        last_failed_dt=last_failed_dt,
        last_failed_dt_date=last_failed_dt_date,
        last_failed_dt_date_gte=last_failed_dt_date_gte,
        last_failed_dt_date_lte=last_failed_dt_date_lte,
        last_failed_dt_gt=last_failed_dt_gt,
        last_failed_dt_gte=last_failed_dt_gte,
        last_failed_dt_lt=last_failed_dt_lt,
        last_failed_dt_lte=last_failed_dt_lte,
        last_finished_dt=last_finished_dt,
        last_finished_dt_date=last_finished_dt_date,
        last_finished_dt_date_gte=last_finished_dt_date_gte,
        last_finished_dt_date_lte=last_finished_dt_date_lte,
        last_finished_dt_gt=last_finished_dt_gt,
        last_finished_dt_gte=last_finished_dt_gte,
        last_finished_dt_lt=last_finished_dt_lt,
        last_finished_dt_lte=last_finished_dt_lte,
        last_rescheduled_dt=last_rescheduled_dt,
        last_rescheduled_dt_date=last_rescheduled_dt_date,
        last_rescheduled_dt_date_gte=last_rescheduled_dt_date_gte,
        last_rescheduled_dt_date_lte=last_rescheduled_dt_date_lte,
        last_rescheduled_dt_gt=last_rescheduled_dt_gt,
        last_rescheduled_dt_gte=last_rescheduled_dt_gte,
        last_rescheduled_dt_lt=last_rescheduled_dt_lt,
        last_rescheduled_dt_lte=last_rescheduled_dt_lte,
        last_scheduled_dt=last_scheduled_dt,
        last_scheduled_dt_date=last_scheduled_dt_date,
        last_scheduled_dt_date_gte=last_scheduled_dt_date_gte,
        last_scheduled_dt_date_lte=last_scheduled_dt_date_lte,
        last_scheduled_dt_gt=last_scheduled_dt_gt,
        last_scheduled_dt_gte=last_scheduled_dt_gte,
        last_scheduled_dt_lt=last_scheduled_dt_lt,
        last_scheduled_dt_lte=last_scheduled_dt_lte,
        last_started_dt=last_started_dt,
        last_started_dt_date=last_started_dt_date,
        last_started_dt_date_gte=last_started_dt_date_gte,
        last_started_dt_date_lte=last_started_dt_date_lte,
        last_started_dt_gt=last_started_dt_gt,
        last_started_dt_gte=last_started_dt_gte,
        last_started_dt_lt=last_started_dt_lt,
        last_started_dt_lte=last_started_dt_lte,
        limit=limit,
        name=name,
        name_in=name_in,
        offset=offset,
        order=order,
        permanently_failed=permanently_failed,
        sync_id=sync_id,
        sync_id_in=sync_id_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    last_consecutive_failures: Union[Unset, int] = UNSET,
    last_consecutive_failures_gt: Union[Unset, int] = UNSET,
    last_consecutive_failures_gte: Union[Unset, int] = UNSET,
    last_consecutive_failures_lt: Union[Unset, int] = UNSET,
    last_consecutive_failures_lte: Union[Unset, int] = UNSET,
    last_consecutive_reschedules: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_gt: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_gte: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_lt: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_lte: Union[Unset, int] = UNSET,
    last_failed_dt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_date: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_date: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_date: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_date: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_date: Union[Unset, datetime.date] = UNSET,
    last_started_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_started_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_started_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1SyncManagersListOrderItem]] = UNSET,
    permanently_failed: Union[Unset, bool] = UNSET,
    sync_id: Union[Unset, str] = UNSET,
    sync_id_in: Union[Unset, list[str]] = UNSET,
) -> Response[OsidbApiV1SyncManagersListResponse200]:
    """Read-only view for sync managers

    Args:
        last_consecutive_failures (Union[Unset, int]):
        last_consecutive_failures_gt (Union[Unset, int]):
        last_consecutive_failures_gte (Union[Unset, int]):
        last_consecutive_failures_lt (Union[Unset, int]):
        last_consecutive_failures_lte (Union[Unset, int]):
        last_consecutive_reschedules (Union[Unset, int]):
        last_consecutive_reschedules_gt (Union[Unset, int]):
        last_consecutive_reschedules_gte (Union[Unset, int]):
        last_consecutive_reschedules_lt (Union[Unset, int]):
        last_consecutive_reschedules_lte (Union[Unset, int]):
        last_failed_dt (Union[Unset, datetime.datetime]):
        last_failed_dt_date (Union[Unset, datetime.date]):
        last_failed_dt_date_gte (Union[Unset, datetime.date]):
        last_failed_dt_date_lte (Union[Unset, datetime.date]):
        last_failed_dt_gt (Union[Unset, datetime.datetime]):
        last_failed_dt_gte (Union[Unset, datetime.datetime]):
        last_failed_dt_lt (Union[Unset, datetime.datetime]):
        last_failed_dt_lte (Union[Unset, datetime.datetime]):
        last_finished_dt (Union[Unset, datetime.datetime]):
        last_finished_dt_date (Union[Unset, datetime.date]):
        last_finished_dt_date_gte (Union[Unset, datetime.date]):
        last_finished_dt_date_lte (Union[Unset, datetime.date]):
        last_finished_dt_gt (Union[Unset, datetime.datetime]):
        last_finished_dt_gte (Union[Unset, datetime.datetime]):
        last_finished_dt_lt (Union[Unset, datetime.datetime]):
        last_finished_dt_lte (Union[Unset, datetime.datetime]):
        last_rescheduled_dt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_date (Union[Unset, datetime.date]):
        last_rescheduled_dt_date_gte (Union[Unset, datetime.date]):
        last_rescheduled_dt_date_lte (Union[Unset, datetime.date]):
        last_rescheduled_dt_gt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_gte (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_lt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_lte (Union[Unset, datetime.datetime]):
        last_scheduled_dt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_date (Union[Unset, datetime.date]):
        last_scheduled_dt_date_gte (Union[Unset, datetime.date]):
        last_scheduled_dt_date_lte (Union[Unset, datetime.date]):
        last_scheduled_dt_gt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_gte (Union[Unset, datetime.datetime]):
        last_scheduled_dt_lt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_lte (Union[Unset, datetime.datetime]):
        last_started_dt (Union[Unset, datetime.datetime]):
        last_started_dt_date (Union[Unset, datetime.date]):
        last_started_dt_date_gte (Union[Unset, datetime.date]):
        last_started_dt_date_lte (Union[Unset, datetime.date]):
        last_started_dt_gt (Union[Unset, datetime.datetime]):
        last_started_dt_gte (Union[Unset, datetime.datetime]):
        last_started_dt_lt (Union[Unset, datetime.datetime]):
        last_started_dt_lte (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1SyncManagersListOrderItem]]):
        permanently_failed (Union[Unset, bool]):
        sync_id (Union[Unset, str]):
        sync_id_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1SyncManagersListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        last_consecutive_failures=last_consecutive_failures,
        last_consecutive_failures_gt=last_consecutive_failures_gt,
        last_consecutive_failures_gte=last_consecutive_failures_gte,
        last_consecutive_failures_lt=last_consecutive_failures_lt,
        last_consecutive_failures_lte=last_consecutive_failures_lte,
        last_consecutive_reschedules=last_consecutive_reschedules,
        last_consecutive_reschedules_gt=last_consecutive_reschedules_gt,
        last_consecutive_reschedules_gte=last_consecutive_reschedules_gte,
        last_consecutive_reschedules_lt=last_consecutive_reschedules_lt,
        last_consecutive_reschedules_lte=last_consecutive_reschedules_lte,
        last_failed_dt=last_failed_dt,
        last_failed_dt_date=last_failed_dt_date,
        last_failed_dt_date_gte=last_failed_dt_date_gte,
        last_failed_dt_date_lte=last_failed_dt_date_lte,
        last_failed_dt_gt=last_failed_dt_gt,
        last_failed_dt_gte=last_failed_dt_gte,
        last_failed_dt_lt=last_failed_dt_lt,
        last_failed_dt_lte=last_failed_dt_lte,
        last_finished_dt=last_finished_dt,
        last_finished_dt_date=last_finished_dt_date,
        last_finished_dt_date_gte=last_finished_dt_date_gte,
        last_finished_dt_date_lte=last_finished_dt_date_lte,
        last_finished_dt_gt=last_finished_dt_gt,
        last_finished_dt_gte=last_finished_dt_gte,
        last_finished_dt_lt=last_finished_dt_lt,
        last_finished_dt_lte=last_finished_dt_lte,
        last_rescheduled_dt=last_rescheduled_dt,
        last_rescheduled_dt_date=last_rescheduled_dt_date,
        last_rescheduled_dt_date_gte=last_rescheduled_dt_date_gte,
        last_rescheduled_dt_date_lte=last_rescheduled_dt_date_lte,
        last_rescheduled_dt_gt=last_rescheduled_dt_gt,
        last_rescheduled_dt_gte=last_rescheduled_dt_gte,
        last_rescheduled_dt_lt=last_rescheduled_dt_lt,
        last_rescheduled_dt_lte=last_rescheduled_dt_lte,
        last_scheduled_dt=last_scheduled_dt,
        last_scheduled_dt_date=last_scheduled_dt_date,
        last_scheduled_dt_date_gte=last_scheduled_dt_date_gte,
        last_scheduled_dt_date_lte=last_scheduled_dt_date_lte,
        last_scheduled_dt_gt=last_scheduled_dt_gt,
        last_scheduled_dt_gte=last_scheduled_dt_gte,
        last_scheduled_dt_lt=last_scheduled_dt_lt,
        last_scheduled_dt_lte=last_scheduled_dt_lte,
        last_started_dt=last_started_dt,
        last_started_dt_date=last_started_dt_date,
        last_started_dt_date_gte=last_started_dt_date_gte,
        last_started_dt_date_lte=last_started_dt_date_lte,
        last_started_dt_gt=last_started_dt_gt,
        last_started_dt_gte=last_started_dt_gte,
        last_started_dt_lt=last_started_dt_lt,
        last_started_dt_lte=last_started_dt_lte,
        limit=limit,
        name=name,
        name_in=name_in,
        offset=offset,
        order=order,
        permanently_failed=permanently_failed,
        sync_id=sync_id,
        sync_id_in=sync_id_in,
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
    last_consecutive_failures: Union[Unset, int] = UNSET,
    last_consecutive_failures_gt: Union[Unset, int] = UNSET,
    last_consecutive_failures_gte: Union[Unset, int] = UNSET,
    last_consecutive_failures_lt: Union[Unset, int] = UNSET,
    last_consecutive_failures_lte: Union[Unset, int] = UNSET,
    last_consecutive_reschedules: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_gt: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_gte: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_lt: Union[Unset, int] = UNSET,
    last_consecutive_reschedules_lte: Union[Unset, int] = UNSET,
    last_failed_dt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_date: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_failed_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_failed_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_date: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_finished_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_finished_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_date: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_rescheduled_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_rescheduled_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_date: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_scheduled_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_scheduled_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_date: Union[Unset, datetime.date] = UNSET,
    last_started_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    last_started_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    last_started_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    last_started_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1SyncManagersListOrderItem]] = UNSET,
    permanently_failed: Union[Unset, bool] = UNSET,
    sync_id: Union[Unset, str] = UNSET,
    sync_id_in: Union[Unset, list[str]] = UNSET,
) -> Optional[OsidbApiV1SyncManagersListResponse200]:
    """Read-only view for sync managers

    Args:
        last_consecutive_failures (Union[Unset, int]):
        last_consecutive_failures_gt (Union[Unset, int]):
        last_consecutive_failures_gte (Union[Unset, int]):
        last_consecutive_failures_lt (Union[Unset, int]):
        last_consecutive_failures_lte (Union[Unset, int]):
        last_consecutive_reschedules (Union[Unset, int]):
        last_consecutive_reschedules_gt (Union[Unset, int]):
        last_consecutive_reschedules_gte (Union[Unset, int]):
        last_consecutive_reschedules_lt (Union[Unset, int]):
        last_consecutive_reschedules_lte (Union[Unset, int]):
        last_failed_dt (Union[Unset, datetime.datetime]):
        last_failed_dt_date (Union[Unset, datetime.date]):
        last_failed_dt_date_gte (Union[Unset, datetime.date]):
        last_failed_dt_date_lte (Union[Unset, datetime.date]):
        last_failed_dt_gt (Union[Unset, datetime.datetime]):
        last_failed_dt_gte (Union[Unset, datetime.datetime]):
        last_failed_dt_lt (Union[Unset, datetime.datetime]):
        last_failed_dt_lte (Union[Unset, datetime.datetime]):
        last_finished_dt (Union[Unset, datetime.datetime]):
        last_finished_dt_date (Union[Unset, datetime.date]):
        last_finished_dt_date_gte (Union[Unset, datetime.date]):
        last_finished_dt_date_lte (Union[Unset, datetime.date]):
        last_finished_dt_gt (Union[Unset, datetime.datetime]):
        last_finished_dt_gte (Union[Unset, datetime.datetime]):
        last_finished_dt_lt (Union[Unset, datetime.datetime]):
        last_finished_dt_lte (Union[Unset, datetime.datetime]):
        last_rescheduled_dt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_date (Union[Unset, datetime.date]):
        last_rescheduled_dt_date_gte (Union[Unset, datetime.date]):
        last_rescheduled_dt_date_lte (Union[Unset, datetime.date]):
        last_rescheduled_dt_gt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_gte (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_lt (Union[Unset, datetime.datetime]):
        last_rescheduled_dt_lte (Union[Unset, datetime.datetime]):
        last_scheduled_dt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_date (Union[Unset, datetime.date]):
        last_scheduled_dt_date_gte (Union[Unset, datetime.date]):
        last_scheduled_dt_date_lte (Union[Unset, datetime.date]):
        last_scheduled_dt_gt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_gte (Union[Unset, datetime.datetime]):
        last_scheduled_dt_lt (Union[Unset, datetime.datetime]):
        last_scheduled_dt_lte (Union[Unset, datetime.datetime]):
        last_started_dt (Union[Unset, datetime.datetime]):
        last_started_dt_date (Union[Unset, datetime.date]):
        last_started_dt_date_gte (Union[Unset, datetime.date]):
        last_started_dt_date_lte (Union[Unset, datetime.date]):
        last_started_dt_gt (Union[Unset, datetime.datetime]):
        last_started_dt_gte (Union[Unset, datetime.datetime]):
        last_started_dt_lt (Union[Unset, datetime.datetime]):
        last_started_dt_lte (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1SyncManagersListOrderItem]]):
        permanently_failed (Union[Unset, bool]):
        sync_id (Union[Unset, str]):
        sync_id_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1SyncManagersListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            last_consecutive_failures=last_consecutive_failures,
            last_consecutive_failures_gt=last_consecutive_failures_gt,
            last_consecutive_failures_gte=last_consecutive_failures_gte,
            last_consecutive_failures_lt=last_consecutive_failures_lt,
            last_consecutive_failures_lte=last_consecutive_failures_lte,
            last_consecutive_reschedules=last_consecutive_reschedules,
            last_consecutive_reschedules_gt=last_consecutive_reschedules_gt,
            last_consecutive_reschedules_gte=last_consecutive_reschedules_gte,
            last_consecutive_reschedules_lt=last_consecutive_reschedules_lt,
            last_consecutive_reschedules_lte=last_consecutive_reschedules_lte,
            last_failed_dt=last_failed_dt,
            last_failed_dt_date=last_failed_dt_date,
            last_failed_dt_date_gte=last_failed_dt_date_gte,
            last_failed_dt_date_lte=last_failed_dt_date_lte,
            last_failed_dt_gt=last_failed_dt_gt,
            last_failed_dt_gte=last_failed_dt_gte,
            last_failed_dt_lt=last_failed_dt_lt,
            last_failed_dt_lte=last_failed_dt_lte,
            last_finished_dt=last_finished_dt,
            last_finished_dt_date=last_finished_dt_date,
            last_finished_dt_date_gte=last_finished_dt_date_gte,
            last_finished_dt_date_lte=last_finished_dt_date_lte,
            last_finished_dt_gt=last_finished_dt_gt,
            last_finished_dt_gte=last_finished_dt_gte,
            last_finished_dt_lt=last_finished_dt_lt,
            last_finished_dt_lte=last_finished_dt_lte,
            last_rescheduled_dt=last_rescheduled_dt,
            last_rescheduled_dt_date=last_rescheduled_dt_date,
            last_rescheduled_dt_date_gte=last_rescheduled_dt_date_gte,
            last_rescheduled_dt_date_lte=last_rescheduled_dt_date_lte,
            last_rescheduled_dt_gt=last_rescheduled_dt_gt,
            last_rescheduled_dt_gte=last_rescheduled_dt_gte,
            last_rescheduled_dt_lt=last_rescheduled_dt_lt,
            last_rescheduled_dt_lte=last_rescheduled_dt_lte,
            last_scheduled_dt=last_scheduled_dt,
            last_scheduled_dt_date=last_scheduled_dt_date,
            last_scheduled_dt_date_gte=last_scheduled_dt_date_gte,
            last_scheduled_dt_date_lte=last_scheduled_dt_date_lte,
            last_scheduled_dt_gt=last_scheduled_dt_gt,
            last_scheduled_dt_gte=last_scheduled_dt_gte,
            last_scheduled_dt_lt=last_scheduled_dt_lt,
            last_scheduled_dt_lte=last_scheduled_dt_lte,
            last_started_dt=last_started_dt,
            last_started_dt_date=last_started_dt_date,
            last_started_dt_date_gte=last_started_dt_date_gte,
            last_started_dt_date_lte=last_started_dt_date_lte,
            last_started_dt_gt=last_started_dt_gt,
            last_started_dt_gte=last_started_dt_gte,
            last_started_dt_lt=last_started_dt_lt,
            last_started_dt_lte=last_started_dt_lte,
            limit=limit,
            name=name,
            name_in=name_in,
            offset=offset,
            order=order,
            permanently_failed=permanently_failed,
            sync_id=sync_id,
            sync_id_in=sync_id_in,
        )
    ).parsed
