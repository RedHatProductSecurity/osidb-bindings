import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_trackers_list_affects_affectedness import (
    OsidbApiV1TrackersListAffectsAffectedness,
)
from ...models.osidb_api_v1_trackers_list_affects_flaw_impact import (
    OsidbApiV1TrackersListAffectsFlawImpact,
)
from ...models.osidb_api_v1_trackers_list_affects_flaw_source import (
    OsidbApiV1TrackersListAffectsFlawSource,
)
from ...models.osidb_api_v1_trackers_list_affects_impact import (
    OsidbApiV1TrackersListAffectsImpact,
)
from ...models.osidb_api_v1_trackers_list_affects_resolution import (
    OsidbApiV1TrackersListAffectsResolution,
)
from ...models.osidb_api_v1_trackers_list_order_item import (
    OsidbApiV1TrackersListOrderItem,
)
from ...models.osidb_api_v1_trackers_list_response_200 import (
    OsidbApiV1TrackersListResponse200,
)
from ...models.osidb_api_v1_trackers_list_type import OsidbApiV1TrackersListType
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "affects__affectedness": OsidbApiV1TrackersListAffectsAffectedness,
    "affects__created_dt": datetime.datetime,
    "affects__created_dt__date": datetime.date,
    "affects__created_dt__date__gte": datetime.date,
    "affects__created_dt__date__lte": datetime.date,
    "affects__created_dt__gt": datetime.datetime,
    "affects__created_dt__gte": datetime.datetime,
    "affects__created_dt__lt": datetime.datetime,
    "affects__created_dt__lte": datetime.datetime,
    "affects__embargoed": bool,
    "affects__flaw__components": list[str],
    "affects__flaw__created_dt": datetime.datetime,
    "affects__flaw__created_dt__date": datetime.date,
    "affects__flaw__created_dt__date__gte": datetime.date,
    "affects__flaw__created_dt__date__lte": datetime.date,
    "affects__flaw__created_dt__gt": datetime.datetime,
    "affects__flaw__created_dt__gte": datetime.datetime,
    "affects__flaw__created_dt__lt": datetime.datetime,
    "affects__flaw__created_dt__lte": datetime.datetime,
    "affects__flaw__cve_id": str,
    "affects__flaw__cwe_id": str,
    "affects__flaw__embargoed": bool,
    "affects__flaw__impact": OsidbApiV1TrackersListAffectsFlawImpact,
    "affects__flaw__reported_dt": datetime.datetime,
    "affects__flaw__reported_dt__date": datetime.date,
    "affects__flaw__reported_dt__date__gte": datetime.date,
    "affects__flaw__reported_dt__date__lte": datetime.date,
    "affects__flaw__reported_dt__gt": datetime.datetime,
    "affects__flaw__reported_dt__gte": datetime.datetime,
    "affects__flaw__reported_dt__lt": datetime.datetime,
    "affects__flaw__reported_dt__lte": datetime.datetime,
    "affects__flaw__source": OsidbApiV1TrackersListAffectsFlawSource,
    "affects__flaw__unembargo_dt": datetime.datetime,
    "affects__flaw__updated_dt": datetime.datetime,
    "affects__flaw__updated_dt__date": datetime.date,
    "affects__flaw__updated_dt__date__gte": datetime.date,
    "affects__flaw__updated_dt__date__lte": datetime.date,
    "affects__flaw__updated_dt__gt": datetime.datetime,
    "affects__flaw__updated_dt__gte": datetime.datetime,
    "affects__flaw__updated_dt__lt": datetime.datetime,
    "affects__flaw__updated_dt__lte": datetime.datetime,
    "affects__flaw__uuid": UUID,
    "affects__impact": OsidbApiV1TrackersListAffectsImpact,
    "affects__ps_component": str,
    "affects__ps_module": str,
    "affects__resolution": OsidbApiV1TrackersListAffectsResolution,
    "affects__updated_dt": datetime.datetime,
    "affects__updated_dt__date": datetime.date,
    "affects__updated_dt__date__gte": datetime.date,
    "affects__updated_dt__date__lte": datetime.date,
    "affects__updated_dt__gt": datetime.datetime,
    "affects__updated_dt__gte": datetime.datetime,
    "affects__updated_dt__lt": datetime.datetime,
    "affects__updated_dt__lte": datetime.datetime,
    "affects__uuid": UUID,
    "created_dt": datetime.datetime,
    "created_dt__date": datetime.date,
    "created_dt__date__gte": datetime.date,
    "created_dt__date__lte": datetime.date,
    "created_dt__gt": datetime.datetime,
    "created_dt__gte": datetime.datetime,
    "created_dt__lt": datetime.datetime,
    "created_dt__lte": datetime.datetime,
    "embargoed": bool,
    "exclude_fields": list[str],
    "external_system_id": str,
    "include_fields": list[str],
    "include_meta_attr": list[str],
    "limit": int,
    "offset": int,
    "order": list[OsidbApiV1TrackersListOrderItem],
    "ps_update_stream": str,
    "resolution": str,
    "status": str,
    "type": OsidbApiV1TrackersListType,
    "updated_dt": datetime.datetime,
    "updated_dt__date": datetime.date,
    "updated_dt__date__gte": datetime.date,
    "updated_dt__date__lte": datetime.date,
    "updated_dt__gt": datetime.datetime,
    "updated_dt__gte": datetime.datetime,
    "updated_dt__lt": datetime.datetime,
    "updated_dt__lte": datetime.datetime,
    "uuid": UUID,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    affects_affectedness: Union[
        Unset, OsidbApiV1TrackersListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, bool] = UNSET,
    affects_flaw_components: Union[Unset, list[str]] = UNSET,
    affects_flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_cve_id: Union[Unset, str] = UNSET,
    affects_flaw_cwe_id: Union[Unset, str] = UNSET,
    affects_flaw_embargoed: Union[Unset, bool] = UNSET,
    affects_flaw_impact: Union[Unset, OsidbApiV1TrackersListAffectsFlawImpact] = UNSET,
    affects_flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_source: Union[Unset, OsidbApiV1TrackersListAffectsFlawSource] = UNSET,
    affects_flaw_unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_uuid: Union[Unset, UUID] = UNSET,
    affects_impact: Union[Unset, OsidbApiV1TrackersListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV1TrackersListAffectsResolution] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1TrackersListOrderItem]] = UNSET,
    ps_update_stream: Union[Unset, str] = UNSET,
    resolution: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, OsidbApiV1TrackersListType] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    json_affects_affectedness: Union[Unset, str] = UNSET
    if not isinstance(affects_affectedness, Unset):
        json_affects_affectedness = OsidbApiV1TrackersListAffectsAffectedness(
            affects_affectedness
        ).value

    params["affects__affectedness"] = json_affects_affectedness

    json_affects_created_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_created_dt, Unset):
        json_affects_created_dt = affects_created_dt.isoformat()

    params["affects__created_dt"] = json_affects_created_dt

    json_affects_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(affects_created_dt_date, Unset):
        json_affects_created_dt_date = affects_created_dt_date.isoformat()

    params["affects__created_dt__date"] = json_affects_created_dt_date

    json_affects_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_created_dt_date_gte, Unset):
        json_affects_created_dt_date_gte = affects_created_dt_date_gte.isoformat()

    params["affects__created_dt__date__gte"] = json_affects_created_dt_date_gte

    json_affects_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_created_dt_date_lte, Unset):
        json_affects_created_dt_date_lte = affects_created_dt_date_lte.isoformat()

    params["affects__created_dt__date__lte"] = json_affects_created_dt_date_lte

    json_affects_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(affects_created_dt_gt, Unset):
        json_affects_created_dt_gt = affects_created_dt_gt.isoformat()

    params["affects__created_dt__gt"] = json_affects_created_dt_gt

    json_affects_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_created_dt_gte, Unset):
        json_affects_created_dt_gte = affects_created_dt_gte.isoformat()

    params["affects__created_dt__gte"] = json_affects_created_dt_gte

    json_affects_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(affects_created_dt_lt, Unset):
        json_affects_created_dt_lt = affects_created_dt_lt.isoformat()

    params["affects__created_dt__lt"] = json_affects_created_dt_lt

    json_affects_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_created_dt_lte, Unset):
        json_affects_created_dt_lte = affects_created_dt_lte.isoformat()

    params["affects__created_dt__lte"] = json_affects_created_dt_lte

    params["affects__embargoed"] = affects_embargoed

    json_affects_flaw_components: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_flaw_components, Unset):
        json_affects_flaw_components = affects_flaw_components

    params["affects__flaw__components"] = json_affects_flaw_components

    json_affects_flaw_created_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_created_dt, Unset):
        json_affects_flaw_created_dt = affects_flaw_created_dt.isoformat()

    params["affects__flaw__created_dt"] = json_affects_flaw_created_dt

    json_affects_flaw_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_created_dt_date, Unset):
        json_affects_flaw_created_dt_date = affects_flaw_created_dt_date.isoformat()

    params["affects__flaw__created_dt__date"] = json_affects_flaw_created_dt_date

    json_affects_flaw_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_created_dt_date_gte, Unset):
        json_affects_flaw_created_dt_date_gte = (
            affects_flaw_created_dt_date_gte.isoformat()
        )

    params["affects__flaw__created_dt__date__gte"] = (
        json_affects_flaw_created_dt_date_gte
    )

    json_affects_flaw_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_created_dt_date_lte, Unset):
        json_affects_flaw_created_dt_date_lte = (
            affects_flaw_created_dt_date_lte.isoformat()
        )

    params["affects__flaw__created_dt__date__lte"] = (
        json_affects_flaw_created_dt_date_lte
    )

    json_affects_flaw_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_created_dt_gt, Unset):
        json_affects_flaw_created_dt_gt = affects_flaw_created_dt_gt.isoformat()

    params["affects__flaw__created_dt__gt"] = json_affects_flaw_created_dt_gt

    json_affects_flaw_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_created_dt_gte, Unset):
        json_affects_flaw_created_dt_gte = affects_flaw_created_dt_gte.isoformat()

    params["affects__flaw__created_dt__gte"] = json_affects_flaw_created_dt_gte

    json_affects_flaw_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_created_dt_lt, Unset):
        json_affects_flaw_created_dt_lt = affects_flaw_created_dt_lt.isoformat()

    params["affects__flaw__created_dt__lt"] = json_affects_flaw_created_dt_lt

    json_affects_flaw_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_created_dt_lte, Unset):
        json_affects_flaw_created_dt_lte = affects_flaw_created_dt_lte.isoformat()

    params["affects__flaw__created_dt__lte"] = json_affects_flaw_created_dt_lte

    params["affects__flaw__cve_id"] = affects_flaw_cve_id

    params["affects__flaw__cwe_id"] = affects_flaw_cwe_id

    params["affects__flaw__embargoed"] = affects_flaw_embargoed

    json_affects_flaw_impact: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_impact, Unset):
        json_affects_flaw_impact = OsidbApiV1TrackersListAffectsFlawImpact(
            affects_flaw_impact
        ).value

    params["affects__flaw__impact"] = json_affects_flaw_impact

    json_affects_flaw_reported_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_reported_dt, Unset):
        json_affects_flaw_reported_dt = affects_flaw_reported_dt.isoformat()

    params["affects__flaw__reported_dt"] = json_affects_flaw_reported_dt

    json_affects_flaw_reported_dt_date: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_date, Unset):
        json_affects_flaw_reported_dt_date = affects_flaw_reported_dt_date.isoformat()

    params["affects__flaw__reported_dt__date"] = json_affects_flaw_reported_dt_date

    json_affects_flaw_reported_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_date_gte, Unset):
        json_affects_flaw_reported_dt_date_gte = (
            affects_flaw_reported_dt_date_gte.isoformat()
        )

    params["affects__flaw__reported_dt__date__gte"] = (
        json_affects_flaw_reported_dt_date_gte
    )

    json_affects_flaw_reported_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_date_lte, Unset):
        json_affects_flaw_reported_dt_date_lte = (
            affects_flaw_reported_dt_date_lte.isoformat()
        )

    params["affects__flaw__reported_dt__date__lte"] = (
        json_affects_flaw_reported_dt_date_lte
    )

    json_affects_flaw_reported_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_gt, Unset):
        json_affects_flaw_reported_dt_gt = affects_flaw_reported_dt_gt.isoformat()

    params["affects__flaw__reported_dt__gt"] = json_affects_flaw_reported_dt_gt

    json_affects_flaw_reported_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_gte, Unset):
        json_affects_flaw_reported_dt_gte = affects_flaw_reported_dt_gte.isoformat()

    params["affects__flaw__reported_dt__gte"] = json_affects_flaw_reported_dt_gte

    json_affects_flaw_reported_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_lt, Unset):
        json_affects_flaw_reported_dt_lt = affects_flaw_reported_dt_lt.isoformat()

    params["affects__flaw__reported_dt__lt"] = json_affects_flaw_reported_dt_lt

    json_affects_flaw_reported_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_lte, Unset):
        json_affects_flaw_reported_dt_lte = affects_flaw_reported_dt_lte.isoformat()

    params["affects__flaw__reported_dt__lte"] = json_affects_flaw_reported_dt_lte

    json_affects_flaw_source: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_source, Unset):
        json_affects_flaw_source = OsidbApiV1TrackersListAffectsFlawSource(
            affects_flaw_source
        ).value

    params["affects__flaw__source"] = json_affects_flaw_source

    json_affects_flaw_unembargo_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_unembargo_dt, Unset):
        json_affects_flaw_unembargo_dt = affects_flaw_unembargo_dt.isoformat()

    params["affects__flaw__unembargo_dt"] = json_affects_flaw_unembargo_dt

    json_affects_flaw_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_updated_dt, Unset):
        json_affects_flaw_updated_dt = affects_flaw_updated_dt.isoformat()

    params["affects__flaw__updated_dt"] = json_affects_flaw_updated_dt

    json_affects_flaw_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_date, Unset):
        json_affects_flaw_updated_dt_date = affects_flaw_updated_dt_date.isoformat()

    params["affects__flaw__updated_dt__date"] = json_affects_flaw_updated_dt_date

    json_affects_flaw_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_date_gte, Unset):
        json_affects_flaw_updated_dt_date_gte = (
            affects_flaw_updated_dt_date_gte.isoformat()
        )

    params["affects__flaw__updated_dt__date__gte"] = (
        json_affects_flaw_updated_dt_date_gte
    )

    json_affects_flaw_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_date_lte, Unset):
        json_affects_flaw_updated_dt_date_lte = (
            affects_flaw_updated_dt_date_lte.isoformat()
        )

    params["affects__flaw__updated_dt__date__lte"] = (
        json_affects_flaw_updated_dt_date_lte
    )

    json_affects_flaw_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_gt, Unset):
        json_affects_flaw_updated_dt_gt = affects_flaw_updated_dt_gt.isoformat()

    params["affects__flaw__updated_dt__gt"] = json_affects_flaw_updated_dt_gt

    json_affects_flaw_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_gte, Unset):
        json_affects_flaw_updated_dt_gte = affects_flaw_updated_dt_gte.isoformat()

    params["affects__flaw__updated_dt__gte"] = json_affects_flaw_updated_dt_gte

    json_affects_flaw_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_lt, Unset):
        json_affects_flaw_updated_dt_lt = affects_flaw_updated_dt_lt.isoformat()

    params["affects__flaw__updated_dt__lt"] = json_affects_flaw_updated_dt_lt

    json_affects_flaw_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_lte, Unset):
        json_affects_flaw_updated_dt_lte = affects_flaw_updated_dt_lte.isoformat()

    params["affects__flaw__updated_dt__lte"] = json_affects_flaw_updated_dt_lte

    json_affects_flaw_uuid: Union[Unset, str] = UNSET
    if not isinstance(affects_flaw_uuid, Unset):
        json_affects_flaw_uuid = str(affects_flaw_uuid)

    params["affects__flaw__uuid"] = json_affects_flaw_uuid

    json_affects_impact: Union[Unset, str] = UNSET
    if not isinstance(affects_impact, Unset):
        json_affects_impact = OsidbApiV1TrackersListAffectsImpact(affects_impact).value

    params["affects__impact"] = json_affects_impact

    params["affects__ps_component"] = affects_ps_component

    params["affects__ps_module"] = affects_ps_module

    json_affects_resolution: Union[Unset, str] = UNSET
    if not isinstance(affects_resolution, Unset):
        json_affects_resolution = OsidbApiV1TrackersListAffectsResolution(
            affects_resolution
        ).value

    params["affects__resolution"] = json_affects_resolution

    json_affects_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_updated_dt, Unset):
        json_affects_updated_dt = affects_updated_dt.isoformat()

    params["affects__updated_dt"] = json_affects_updated_dt

    json_affects_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(affects_updated_dt_date, Unset):
        json_affects_updated_dt_date = affects_updated_dt_date.isoformat()

    params["affects__updated_dt__date"] = json_affects_updated_dt_date

    json_affects_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_updated_dt_date_gte, Unset):
        json_affects_updated_dt_date_gte = affects_updated_dt_date_gte.isoformat()

    params["affects__updated_dt__date__gte"] = json_affects_updated_dt_date_gte

    json_affects_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_updated_dt_date_lte, Unset):
        json_affects_updated_dt_date_lte = affects_updated_dt_date_lte.isoformat()

    params["affects__updated_dt__date__lte"] = json_affects_updated_dt_date_lte

    json_affects_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(affects_updated_dt_gt, Unset):
        json_affects_updated_dt_gt = affects_updated_dt_gt.isoformat()

    params["affects__updated_dt__gt"] = json_affects_updated_dt_gt

    json_affects_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_updated_dt_gte, Unset):
        json_affects_updated_dt_gte = affects_updated_dt_gte.isoformat()

    params["affects__updated_dt__gte"] = json_affects_updated_dt_gte

    json_affects_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(affects_updated_dt_lt, Unset):
        json_affects_updated_dt_lt = affects_updated_dt_lt.isoformat()

    params["affects__updated_dt__lt"] = json_affects_updated_dt_lt

    json_affects_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_updated_dt_lte, Unset):
        json_affects_updated_dt_lte = affects_updated_dt_lte.isoformat()

    params["affects__updated_dt__lte"] = json_affects_updated_dt_lte

    json_affects_uuid: Union[Unset, str] = UNSET
    if not isinstance(affects_uuid, Unset):
        json_affects_uuid = str(affects_uuid)

    params["affects__uuid"] = json_affects_uuid

    json_created_dt: Union[Unset, str] = UNSET
    if not isinstance(created_dt, Unset):
        json_created_dt = created_dt.isoformat()

    params["created_dt"] = json_created_dt

    json_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(created_dt_date, Unset):
        json_created_dt_date = created_dt_date.isoformat()

    params["created_dt__date"] = json_created_dt_date

    json_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(created_dt_date_gte, Unset):
        json_created_dt_date_gte = created_dt_date_gte.isoformat()

    params["created_dt__date__gte"] = json_created_dt_date_gte

    json_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(created_dt_date_lte, Unset):
        json_created_dt_date_lte = created_dt_date_lte.isoformat()

    params["created_dt__date__lte"] = json_created_dt_date_lte

    json_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(created_dt_gt, Unset):
        json_created_dt_gt = created_dt_gt.isoformat()

    params["created_dt__gt"] = json_created_dt_gt

    json_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(created_dt_gte, Unset):
        json_created_dt_gte = created_dt_gte.isoformat()

    params["created_dt__gte"] = json_created_dt_gte

    json_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(created_dt_lt, Unset):
        json_created_dt_lt = created_dt_lt.isoformat()

    params["created_dt__lt"] = json_created_dt_lt

    json_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(created_dt_lte, Unset):
        json_created_dt_lte = created_dt_lte.isoformat()

    params["created_dt__lte"] = json_created_dt_lte

    params["embargoed"] = embargoed

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    params["external_system_id"] = external_system_id

    json_include_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(include_fields, Unset):
        json_include_fields = include_fields

    params["include_fields"] = json_include_fields

    json_include_meta_attr: Union[Unset, list[str]] = UNSET
    if not isinstance(include_meta_attr, Unset):
        json_include_meta_attr = include_meta_attr

    params["include_meta_attr"] = json_include_meta_attr

    params["limit"] = limit

    params["offset"] = offset

    json_order: Union[Unset, list[str]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item: str = UNSET
            if not isinstance(order_item_data, Unset):
                order_item = OsidbApiV1TrackersListOrderItem(order_item_data).value

            json_order.append(order_item)

    params["order"] = json_order

    params["ps_update_stream"] = ps_update_stream

    params["resolution"] = resolution

    params["status"] = status

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = OsidbApiV1TrackersListType(type_).value

    params["type"] = json_type_

    json_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(updated_dt, Unset):
        json_updated_dt = updated_dt.isoformat()

    params["updated_dt"] = json_updated_dt

    json_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_date, Unset):
        json_updated_dt_date = updated_dt_date.isoformat()

    params["updated_dt__date"] = json_updated_dt_date

    json_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_date_gte, Unset):
        json_updated_dt_date_gte = updated_dt_date_gte.isoformat()

    params["updated_dt__date__gte"] = json_updated_dt_date_gte

    json_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_date_lte, Unset):
        json_updated_dt_date_lte = updated_dt_date_lte.isoformat()

    params["updated_dt__date__lte"] = json_updated_dt_date_lte

    json_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_gt, Unset):
        json_updated_dt_gt = updated_dt_gt.isoformat()

    params["updated_dt__gt"] = json_updated_dt_gt

    json_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_gte, Unset):
        json_updated_dt_gte = updated_dt_gte.isoformat()

    params["updated_dt__gte"] = json_updated_dt_gte

    json_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_lt, Unset):
        json_updated_dt_lt = updated_dt_lt.isoformat()

    params["updated_dt__lt"] = json_updated_dt_lt

    json_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(updated_dt_lte, Unset):
        json_updated_dt_lte = updated_dt_lte.isoformat()

    params["updated_dt__lte"] = json_updated_dt_lte

    json_uuid: Union[Unset, str] = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)

    params["uuid"] = json_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/trackers",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1TrackersListResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1TrackersListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1TrackersListResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1TrackersListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    affects_affectedness: Union[
        Unset, OsidbApiV1TrackersListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, bool] = UNSET,
    affects_flaw_components: Union[Unset, list[str]] = UNSET,
    affects_flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_cve_id: Union[Unset, str] = UNSET,
    affects_flaw_cwe_id: Union[Unset, str] = UNSET,
    affects_flaw_embargoed: Union[Unset, bool] = UNSET,
    affects_flaw_impact: Union[Unset, OsidbApiV1TrackersListAffectsFlawImpact] = UNSET,
    affects_flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_source: Union[Unset, OsidbApiV1TrackersListAffectsFlawSource] = UNSET,
    affects_flaw_unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_uuid: Union[Unset, UUID] = UNSET,
    affects_impact: Union[Unset, OsidbApiV1TrackersListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV1TrackersListAffectsResolution] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1TrackersListOrderItem]] = UNSET,
    ps_update_stream: Union[Unset, str] = UNSET,
    resolution: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, OsidbApiV1TrackersListType] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[OsidbApiV1TrackersListResponse200]:
    """
    Args:
        affects_affectedness (Union[Unset, OsidbApiV1TrackersListAffectsAffectedness]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_flaw_components (Union[Unset, list[str]]):
        affects_flaw_created_dt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_date (Union[Unset, datetime.date]):
        affects_flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_cve_id (Union[Unset, str]):
        affects_flaw_cwe_id (Union[Unset, str]):
        affects_flaw_embargoed (Union[Unset, bool]):
        affects_flaw_impact (Union[Unset, OsidbApiV1TrackersListAffectsFlawImpact]):
        affects_flaw_reported_dt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_date (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_source (Union[Unset, OsidbApiV1TrackersListAffectsFlawSource]):
        affects_flaw_unembargo_dt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_date (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_uuid (Union[Unset, UUID]):
        affects_impact (Union[Unset, OsidbApiV1TrackersListAffectsImpact]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_module (Union[Unset, str]):
        affects_resolution (Union[Unset, OsidbApiV1TrackersListAffectsResolution]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        external_system_id (Union[Unset, str]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1TrackersListOrderItem]]):
        ps_update_stream (Union[Unset, str]):
        resolution (Union[Unset, str]):
        status (Union[Unset, str]):
        type_ (Union[Unset, OsidbApiV1TrackersListType]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1TrackersListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        affects_affectedness=affects_affectedness,
        affects_created_dt=affects_created_dt,
        affects_created_dt_date=affects_created_dt_date,
        affects_created_dt_date_gte=affects_created_dt_date_gte,
        affects_created_dt_date_lte=affects_created_dt_date_lte,
        affects_created_dt_gt=affects_created_dt_gt,
        affects_created_dt_gte=affects_created_dt_gte,
        affects_created_dt_lt=affects_created_dt_lt,
        affects_created_dt_lte=affects_created_dt_lte,
        affects_embargoed=affects_embargoed,
        affects_flaw_components=affects_flaw_components,
        affects_flaw_created_dt=affects_flaw_created_dt,
        affects_flaw_created_dt_date=affects_flaw_created_dt_date,
        affects_flaw_created_dt_date_gte=affects_flaw_created_dt_date_gte,
        affects_flaw_created_dt_date_lte=affects_flaw_created_dt_date_lte,
        affects_flaw_created_dt_gt=affects_flaw_created_dt_gt,
        affects_flaw_created_dt_gte=affects_flaw_created_dt_gte,
        affects_flaw_created_dt_lt=affects_flaw_created_dt_lt,
        affects_flaw_created_dt_lte=affects_flaw_created_dt_lte,
        affects_flaw_cve_id=affects_flaw_cve_id,
        affects_flaw_cwe_id=affects_flaw_cwe_id,
        affects_flaw_embargoed=affects_flaw_embargoed,
        affects_flaw_impact=affects_flaw_impact,
        affects_flaw_reported_dt=affects_flaw_reported_dt,
        affects_flaw_reported_dt_date=affects_flaw_reported_dt_date,
        affects_flaw_reported_dt_date_gte=affects_flaw_reported_dt_date_gte,
        affects_flaw_reported_dt_date_lte=affects_flaw_reported_dt_date_lte,
        affects_flaw_reported_dt_gt=affects_flaw_reported_dt_gt,
        affects_flaw_reported_dt_gte=affects_flaw_reported_dt_gte,
        affects_flaw_reported_dt_lt=affects_flaw_reported_dt_lt,
        affects_flaw_reported_dt_lte=affects_flaw_reported_dt_lte,
        affects_flaw_source=affects_flaw_source,
        affects_flaw_unembargo_dt=affects_flaw_unembargo_dt,
        affects_flaw_updated_dt=affects_flaw_updated_dt,
        affects_flaw_updated_dt_date=affects_flaw_updated_dt_date,
        affects_flaw_updated_dt_date_gte=affects_flaw_updated_dt_date_gte,
        affects_flaw_updated_dt_date_lte=affects_flaw_updated_dt_date_lte,
        affects_flaw_updated_dt_gt=affects_flaw_updated_dt_gt,
        affects_flaw_updated_dt_gte=affects_flaw_updated_dt_gte,
        affects_flaw_updated_dt_lt=affects_flaw_updated_dt_lt,
        affects_flaw_updated_dt_lte=affects_flaw_updated_dt_lte,
        affects_flaw_uuid=affects_flaw_uuid,
        affects_impact=affects_impact,
        affects_ps_component=affects_ps_component,
        affects_ps_module=affects_ps_module,
        affects_resolution=affects_resolution,
        affects_updated_dt=affects_updated_dt,
        affects_updated_dt_date=affects_updated_dt_date,
        affects_updated_dt_date_gte=affects_updated_dt_date_gte,
        affects_updated_dt_date_lte=affects_updated_dt_date_lte,
        affects_updated_dt_gt=affects_updated_dt_gt,
        affects_updated_dt_gte=affects_updated_dt_gte,
        affects_updated_dt_lt=affects_updated_dt_lt,
        affects_updated_dt_lte=affects_updated_dt_lte,
        affects_uuid=affects_uuid,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        external_system_id=external_system_id,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        order=order,
        ps_update_stream=ps_update_stream,
        resolution=resolution,
        status=status,
        type_=type_,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
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
    affects_affectedness: Union[
        Unset, OsidbApiV1TrackersListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, bool] = UNSET,
    affects_flaw_components: Union[Unset, list[str]] = UNSET,
    affects_flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_cve_id: Union[Unset, str] = UNSET,
    affects_flaw_cwe_id: Union[Unset, str] = UNSET,
    affects_flaw_embargoed: Union[Unset, bool] = UNSET,
    affects_flaw_impact: Union[Unset, OsidbApiV1TrackersListAffectsFlawImpact] = UNSET,
    affects_flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_source: Union[Unset, OsidbApiV1TrackersListAffectsFlawSource] = UNSET,
    affects_flaw_unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_uuid: Union[Unset, UUID] = UNSET,
    affects_impact: Union[Unset, OsidbApiV1TrackersListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV1TrackersListAffectsResolution] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1TrackersListOrderItem]] = UNSET,
    ps_update_stream: Union[Unset, str] = UNSET,
    resolution: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, OsidbApiV1TrackersListType] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[OsidbApiV1TrackersListResponse200]:
    """
    Args:
        affects_affectedness (Union[Unset, OsidbApiV1TrackersListAffectsAffectedness]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_flaw_components (Union[Unset, list[str]]):
        affects_flaw_created_dt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_date (Union[Unset, datetime.date]):
        affects_flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_cve_id (Union[Unset, str]):
        affects_flaw_cwe_id (Union[Unset, str]):
        affects_flaw_embargoed (Union[Unset, bool]):
        affects_flaw_impact (Union[Unset, OsidbApiV1TrackersListAffectsFlawImpact]):
        affects_flaw_reported_dt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_date (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_source (Union[Unset, OsidbApiV1TrackersListAffectsFlawSource]):
        affects_flaw_unembargo_dt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_date (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_uuid (Union[Unset, UUID]):
        affects_impact (Union[Unset, OsidbApiV1TrackersListAffectsImpact]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_module (Union[Unset, str]):
        affects_resolution (Union[Unset, OsidbApiV1TrackersListAffectsResolution]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        external_system_id (Union[Unset, str]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1TrackersListOrderItem]]):
        ps_update_stream (Union[Unset, str]):
        resolution (Union[Unset, str]):
        status (Union[Unset, str]):
        type_ (Union[Unset, OsidbApiV1TrackersListType]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1TrackersListResponse200
    """

    return sync_detailed(
        client=client,
        affects_affectedness=affects_affectedness,
        affects_created_dt=affects_created_dt,
        affects_created_dt_date=affects_created_dt_date,
        affects_created_dt_date_gte=affects_created_dt_date_gte,
        affects_created_dt_date_lte=affects_created_dt_date_lte,
        affects_created_dt_gt=affects_created_dt_gt,
        affects_created_dt_gte=affects_created_dt_gte,
        affects_created_dt_lt=affects_created_dt_lt,
        affects_created_dt_lte=affects_created_dt_lte,
        affects_embargoed=affects_embargoed,
        affects_flaw_components=affects_flaw_components,
        affects_flaw_created_dt=affects_flaw_created_dt,
        affects_flaw_created_dt_date=affects_flaw_created_dt_date,
        affects_flaw_created_dt_date_gte=affects_flaw_created_dt_date_gte,
        affects_flaw_created_dt_date_lte=affects_flaw_created_dt_date_lte,
        affects_flaw_created_dt_gt=affects_flaw_created_dt_gt,
        affects_flaw_created_dt_gte=affects_flaw_created_dt_gte,
        affects_flaw_created_dt_lt=affects_flaw_created_dt_lt,
        affects_flaw_created_dt_lte=affects_flaw_created_dt_lte,
        affects_flaw_cve_id=affects_flaw_cve_id,
        affects_flaw_cwe_id=affects_flaw_cwe_id,
        affects_flaw_embargoed=affects_flaw_embargoed,
        affects_flaw_impact=affects_flaw_impact,
        affects_flaw_reported_dt=affects_flaw_reported_dt,
        affects_flaw_reported_dt_date=affects_flaw_reported_dt_date,
        affects_flaw_reported_dt_date_gte=affects_flaw_reported_dt_date_gte,
        affects_flaw_reported_dt_date_lte=affects_flaw_reported_dt_date_lte,
        affects_flaw_reported_dt_gt=affects_flaw_reported_dt_gt,
        affects_flaw_reported_dt_gte=affects_flaw_reported_dt_gte,
        affects_flaw_reported_dt_lt=affects_flaw_reported_dt_lt,
        affects_flaw_reported_dt_lte=affects_flaw_reported_dt_lte,
        affects_flaw_source=affects_flaw_source,
        affects_flaw_unembargo_dt=affects_flaw_unembargo_dt,
        affects_flaw_updated_dt=affects_flaw_updated_dt,
        affects_flaw_updated_dt_date=affects_flaw_updated_dt_date,
        affects_flaw_updated_dt_date_gte=affects_flaw_updated_dt_date_gte,
        affects_flaw_updated_dt_date_lte=affects_flaw_updated_dt_date_lte,
        affects_flaw_updated_dt_gt=affects_flaw_updated_dt_gt,
        affects_flaw_updated_dt_gte=affects_flaw_updated_dt_gte,
        affects_flaw_updated_dt_lt=affects_flaw_updated_dt_lt,
        affects_flaw_updated_dt_lte=affects_flaw_updated_dt_lte,
        affects_flaw_uuid=affects_flaw_uuid,
        affects_impact=affects_impact,
        affects_ps_component=affects_ps_component,
        affects_ps_module=affects_ps_module,
        affects_resolution=affects_resolution,
        affects_updated_dt=affects_updated_dt,
        affects_updated_dt_date=affects_updated_dt_date,
        affects_updated_dt_date_gte=affects_updated_dt_date_gte,
        affects_updated_dt_date_lte=affects_updated_dt_date_lte,
        affects_updated_dt_gt=affects_updated_dt_gt,
        affects_updated_dt_gte=affects_updated_dt_gte,
        affects_updated_dt_lt=affects_updated_dt_lt,
        affects_updated_dt_lte=affects_updated_dt_lte,
        affects_uuid=affects_uuid,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        external_system_id=external_system_id,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        order=order,
        ps_update_stream=ps_update_stream,
        resolution=resolution,
        status=status,
        type_=type_,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    affects_affectedness: Union[
        Unset, OsidbApiV1TrackersListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, bool] = UNSET,
    affects_flaw_components: Union[Unset, list[str]] = UNSET,
    affects_flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_cve_id: Union[Unset, str] = UNSET,
    affects_flaw_cwe_id: Union[Unset, str] = UNSET,
    affects_flaw_embargoed: Union[Unset, bool] = UNSET,
    affects_flaw_impact: Union[Unset, OsidbApiV1TrackersListAffectsFlawImpact] = UNSET,
    affects_flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_source: Union[Unset, OsidbApiV1TrackersListAffectsFlawSource] = UNSET,
    affects_flaw_unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_uuid: Union[Unset, UUID] = UNSET,
    affects_impact: Union[Unset, OsidbApiV1TrackersListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV1TrackersListAffectsResolution] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1TrackersListOrderItem]] = UNSET,
    ps_update_stream: Union[Unset, str] = UNSET,
    resolution: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, OsidbApiV1TrackersListType] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[OsidbApiV1TrackersListResponse200]:
    """
    Args:
        affects_affectedness (Union[Unset, OsidbApiV1TrackersListAffectsAffectedness]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_flaw_components (Union[Unset, list[str]]):
        affects_flaw_created_dt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_date (Union[Unset, datetime.date]):
        affects_flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_cve_id (Union[Unset, str]):
        affects_flaw_cwe_id (Union[Unset, str]):
        affects_flaw_embargoed (Union[Unset, bool]):
        affects_flaw_impact (Union[Unset, OsidbApiV1TrackersListAffectsFlawImpact]):
        affects_flaw_reported_dt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_date (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_source (Union[Unset, OsidbApiV1TrackersListAffectsFlawSource]):
        affects_flaw_unembargo_dt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_date (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_uuid (Union[Unset, UUID]):
        affects_impact (Union[Unset, OsidbApiV1TrackersListAffectsImpact]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_module (Union[Unset, str]):
        affects_resolution (Union[Unset, OsidbApiV1TrackersListAffectsResolution]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        external_system_id (Union[Unset, str]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1TrackersListOrderItem]]):
        ps_update_stream (Union[Unset, str]):
        resolution (Union[Unset, str]):
        status (Union[Unset, str]):
        type_ (Union[Unset, OsidbApiV1TrackersListType]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1TrackersListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        affects_affectedness=affects_affectedness,
        affects_created_dt=affects_created_dt,
        affects_created_dt_date=affects_created_dt_date,
        affects_created_dt_date_gte=affects_created_dt_date_gte,
        affects_created_dt_date_lte=affects_created_dt_date_lte,
        affects_created_dt_gt=affects_created_dt_gt,
        affects_created_dt_gte=affects_created_dt_gte,
        affects_created_dt_lt=affects_created_dt_lt,
        affects_created_dt_lte=affects_created_dt_lte,
        affects_embargoed=affects_embargoed,
        affects_flaw_components=affects_flaw_components,
        affects_flaw_created_dt=affects_flaw_created_dt,
        affects_flaw_created_dt_date=affects_flaw_created_dt_date,
        affects_flaw_created_dt_date_gte=affects_flaw_created_dt_date_gte,
        affects_flaw_created_dt_date_lte=affects_flaw_created_dt_date_lte,
        affects_flaw_created_dt_gt=affects_flaw_created_dt_gt,
        affects_flaw_created_dt_gte=affects_flaw_created_dt_gte,
        affects_flaw_created_dt_lt=affects_flaw_created_dt_lt,
        affects_flaw_created_dt_lte=affects_flaw_created_dt_lte,
        affects_flaw_cve_id=affects_flaw_cve_id,
        affects_flaw_cwe_id=affects_flaw_cwe_id,
        affects_flaw_embargoed=affects_flaw_embargoed,
        affects_flaw_impact=affects_flaw_impact,
        affects_flaw_reported_dt=affects_flaw_reported_dt,
        affects_flaw_reported_dt_date=affects_flaw_reported_dt_date,
        affects_flaw_reported_dt_date_gte=affects_flaw_reported_dt_date_gte,
        affects_flaw_reported_dt_date_lte=affects_flaw_reported_dt_date_lte,
        affects_flaw_reported_dt_gt=affects_flaw_reported_dt_gt,
        affects_flaw_reported_dt_gte=affects_flaw_reported_dt_gte,
        affects_flaw_reported_dt_lt=affects_flaw_reported_dt_lt,
        affects_flaw_reported_dt_lte=affects_flaw_reported_dt_lte,
        affects_flaw_source=affects_flaw_source,
        affects_flaw_unembargo_dt=affects_flaw_unembargo_dt,
        affects_flaw_updated_dt=affects_flaw_updated_dt,
        affects_flaw_updated_dt_date=affects_flaw_updated_dt_date,
        affects_flaw_updated_dt_date_gte=affects_flaw_updated_dt_date_gte,
        affects_flaw_updated_dt_date_lte=affects_flaw_updated_dt_date_lte,
        affects_flaw_updated_dt_gt=affects_flaw_updated_dt_gt,
        affects_flaw_updated_dt_gte=affects_flaw_updated_dt_gte,
        affects_flaw_updated_dt_lt=affects_flaw_updated_dt_lt,
        affects_flaw_updated_dt_lte=affects_flaw_updated_dt_lte,
        affects_flaw_uuid=affects_flaw_uuid,
        affects_impact=affects_impact,
        affects_ps_component=affects_ps_component,
        affects_ps_module=affects_ps_module,
        affects_resolution=affects_resolution,
        affects_updated_dt=affects_updated_dt,
        affects_updated_dt_date=affects_updated_dt_date,
        affects_updated_dt_date_gte=affects_updated_dt_date_gte,
        affects_updated_dt_date_lte=affects_updated_dt_date_lte,
        affects_updated_dt_gt=affects_updated_dt_gt,
        affects_updated_dt_gte=affects_updated_dt_gte,
        affects_updated_dt_lt=affects_updated_dt_lt,
        affects_updated_dt_lte=affects_updated_dt_lte,
        affects_uuid=affects_uuid,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        external_system_id=external_system_id,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        order=order,
        ps_update_stream=ps_update_stream,
        resolution=resolution,
        status=status,
        type_=type_,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
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
    affects_affectedness: Union[
        Unset, OsidbApiV1TrackersListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, bool] = UNSET,
    affects_flaw_components: Union[Unset, list[str]] = UNSET,
    affects_flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_cve_id: Union[Unset, str] = UNSET,
    affects_flaw_cwe_id: Union[Unset, str] = UNSET,
    affects_flaw_embargoed: Union[Unset, bool] = UNSET,
    affects_flaw_impact: Union[Unset, OsidbApiV1TrackersListAffectsFlawImpact] = UNSET,
    affects_flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_source: Union[Unset, OsidbApiV1TrackersListAffectsFlawSource] = UNSET,
    affects_flaw_unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_flaw_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_flaw_uuid: Union[Unset, UUID] = UNSET,
    affects_impact: Union[Unset, OsidbApiV1TrackersListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV1TrackersListAffectsResolution] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    external_system_id: Union[Unset, str] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1TrackersListOrderItem]] = UNSET,
    ps_update_stream: Union[Unset, str] = UNSET,
    resolution: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, OsidbApiV1TrackersListType] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[OsidbApiV1TrackersListResponse200]:
    """
    Args:
        affects_affectedness (Union[Unset, OsidbApiV1TrackersListAffectsAffectedness]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_flaw_components (Union[Unset, list[str]]):
        affects_flaw_created_dt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_date (Union[Unset, datetime.date]):
        affects_flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_cve_id (Union[Unset, str]):
        affects_flaw_cwe_id (Union[Unset, str]):
        affects_flaw_embargoed (Union[Unset, bool]):
        affects_flaw_impact (Union[Unset, OsidbApiV1TrackersListAffectsFlawImpact]):
        affects_flaw_reported_dt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_date (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_source (Union[Unset, OsidbApiV1TrackersListAffectsFlawSource]):
        affects_flaw_unembargo_dt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_date (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_flaw_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_flaw_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_flaw_uuid (Union[Unset, UUID]):
        affects_impact (Union[Unset, OsidbApiV1TrackersListAffectsImpact]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_module (Union[Unset, str]):
        affects_resolution (Union[Unset, OsidbApiV1TrackersListAffectsResolution]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        external_system_id (Union[Unset, str]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1TrackersListOrderItem]]):
        ps_update_stream (Union[Unset, str]):
        resolution (Union[Unset, str]):
        status (Union[Unset, str]):
        type_ (Union[Unset, OsidbApiV1TrackersListType]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1TrackersListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            affects_affectedness=affects_affectedness,
            affects_created_dt=affects_created_dt,
            affects_created_dt_date=affects_created_dt_date,
            affects_created_dt_date_gte=affects_created_dt_date_gte,
            affects_created_dt_date_lte=affects_created_dt_date_lte,
            affects_created_dt_gt=affects_created_dt_gt,
            affects_created_dt_gte=affects_created_dt_gte,
            affects_created_dt_lt=affects_created_dt_lt,
            affects_created_dt_lte=affects_created_dt_lte,
            affects_embargoed=affects_embargoed,
            affects_flaw_components=affects_flaw_components,
            affects_flaw_created_dt=affects_flaw_created_dt,
            affects_flaw_created_dt_date=affects_flaw_created_dt_date,
            affects_flaw_created_dt_date_gte=affects_flaw_created_dt_date_gte,
            affects_flaw_created_dt_date_lte=affects_flaw_created_dt_date_lte,
            affects_flaw_created_dt_gt=affects_flaw_created_dt_gt,
            affects_flaw_created_dt_gte=affects_flaw_created_dt_gte,
            affects_flaw_created_dt_lt=affects_flaw_created_dt_lt,
            affects_flaw_created_dt_lte=affects_flaw_created_dt_lte,
            affects_flaw_cve_id=affects_flaw_cve_id,
            affects_flaw_cwe_id=affects_flaw_cwe_id,
            affects_flaw_embargoed=affects_flaw_embargoed,
            affects_flaw_impact=affects_flaw_impact,
            affects_flaw_reported_dt=affects_flaw_reported_dt,
            affects_flaw_reported_dt_date=affects_flaw_reported_dt_date,
            affects_flaw_reported_dt_date_gte=affects_flaw_reported_dt_date_gte,
            affects_flaw_reported_dt_date_lte=affects_flaw_reported_dt_date_lte,
            affects_flaw_reported_dt_gt=affects_flaw_reported_dt_gt,
            affects_flaw_reported_dt_gte=affects_flaw_reported_dt_gte,
            affects_flaw_reported_dt_lt=affects_flaw_reported_dt_lt,
            affects_flaw_reported_dt_lte=affects_flaw_reported_dt_lte,
            affects_flaw_source=affects_flaw_source,
            affects_flaw_unembargo_dt=affects_flaw_unembargo_dt,
            affects_flaw_updated_dt=affects_flaw_updated_dt,
            affects_flaw_updated_dt_date=affects_flaw_updated_dt_date,
            affects_flaw_updated_dt_date_gte=affects_flaw_updated_dt_date_gte,
            affects_flaw_updated_dt_date_lte=affects_flaw_updated_dt_date_lte,
            affects_flaw_updated_dt_gt=affects_flaw_updated_dt_gt,
            affects_flaw_updated_dt_gte=affects_flaw_updated_dt_gte,
            affects_flaw_updated_dt_lt=affects_flaw_updated_dt_lt,
            affects_flaw_updated_dt_lte=affects_flaw_updated_dt_lte,
            affects_flaw_uuid=affects_flaw_uuid,
            affects_impact=affects_impact,
            affects_ps_component=affects_ps_component,
            affects_ps_module=affects_ps_module,
            affects_resolution=affects_resolution,
            affects_updated_dt=affects_updated_dt,
            affects_updated_dt_date=affects_updated_dt_date,
            affects_updated_dt_date_gte=affects_updated_dt_date_gte,
            affects_updated_dt_date_lte=affects_updated_dt_date_lte,
            affects_updated_dt_gt=affects_updated_dt_gt,
            affects_updated_dt_gte=affects_updated_dt_gte,
            affects_updated_dt_lt=affects_updated_dt_lt,
            affects_updated_dt_lte=affects_updated_dt_lte,
            affects_uuid=affects_uuid,
            created_dt=created_dt,
            created_dt_date=created_dt_date,
            created_dt_date_gte=created_dt_date_gte,
            created_dt_date_lte=created_dt_date_lte,
            created_dt_gt=created_dt_gt,
            created_dt_gte=created_dt_gte,
            created_dt_lt=created_dt_lt,
            created_dt_lte=created_dt_lte,
            embargoed=embargoed,
            exclude_fields=exclude_fields,
            external_system_id=external_system_id,
            include_fields=include_fields,
            include_meta_attr=include_meta_attr,
            limit=limit,
            offset=offset,
            order=order,
            ps_update_stream=ps_update_stream,
            resolution=resolution,
            status=status,
            type_=type_,
            updated_dt=updated_dt,
            updated_dt_date=updated_dt_date,
            updated_dt_date_gte=updated_dt_date_gte,
            updated_dt_date_lte=updated_dt_date_lte,
            updated_dt_gt=updated_dt_gt,
            updated_dt_gte=updated_dt_gte,
            updated_dt_lt=updated_dt_lt,
            updated_dt_lte=updated_dt_lte,
            uuid=uuid,
        )
    ).parsed
