import datetime
from typing import Any, Dict, List, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_trackers_list_affects_affectedness import (
    OsidbApiV1TrackersListAffectsAffectedness,
)
from ...models.osidb_api_v1_trackers_list_affects_flaw_impact import (
    OsidbApiV1TrackersListAffectsFlawImpact,
)
from ...models.osidb_api_v1_trackers_list_affects_flaw_source import (
    OsidbApiV1TrackersListAffectsFlawSource,
)
from ...models.osidb_api_v1_trackers_list_affects_flaw_type import (
    OsidbApiV1TrackersListAffectsFlawType,
)
from ...models.osidb_api_v1_trackers_list_affects_impact import (
    OsidbApiV1TrackersListAffectsImpact,
)
from ...models.osidb_api_v1_trackers_list_affects_resolution import (
    OsidbApiV1TrackersListAffectsResolution,
)
from ...models.osidb_api_v1_trackers_list_affects_type import (
    OsidbApiV1TrackersListAffectsType,
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
    "affects__cvss2": str,
    "affects__cvss2_score": float,
    "affects__cvss2_score__gt": float,
    "affects__cvss2_score__gte": float,
    "affects__cvss2_score__lt": float,
    "affects__cvss2_score__lte": float,
    "affects__cvss3": str,
    "affects__cvss3_score": float,
    "affects__cvss3_score__gt": float,
    "affects__cvss3_score__gte": float,
    "affects__cvss3_score__lt": float,
    "affects__cvss3_score__lte": float,
    "affects__embargoed": bool,
    "affects__flaw__component": str,
    "affects__flaw__created_dt": datetime.datetime,
    "affects__flaw__created_dt__date": datetime.date,
    "affects__flaw__created_dt__date__gte": datetime.date,
    "affects__flaw__created_dt__date__lte": datetime.date,
    "affects__flaw__created_dt__gt": datetime.datetime,
    "affects__flaw__created_dt__gte": datetime.datetime,
    "affects__flaw__created_dt__lt": datetime.datetime,
    "affects__flaw__created_dt__lte": datetime.datetime,
    "affects__flaw__cve_id": str,
    "affects__flaw__cvss2": str,
    "affects__flaw__cvss2_score": float,
    "affects__flaw__cvss2_score__gt": float,
    "affects__flaw__cvss2_score__gte": float,
    "affects__flaw__cvss2_score__lt": float,
    "affects__flaw__cvss2_score__lte": float,
    "affects__flaw__cvss3": str,
    "affects__flaw__cvss3_score": float,
    "affects__flaw__cvss3_score__gt": float,
    "affects__flaw__cvss3_score__gte": float,
    "affects__flaw__cvss3_score__lt": float,
    "affects__flaw__cvss3_score__lte": float,
    "affects__flaw__cwe_id": str,
    "affects__flaw__embargoed": bool,
    "affects__flaw__impact": OsidbApiV1TrackersListAffectsFlawImpact,
    "affects__flaw__is_major_incident": bool,
    "affects__flaw__nvd_cvss2": str,
    "affects__flaw__nvd_cvss3": str,
    "affects__flaw__reported_dt": datetime.datetime,
    "affects__flaw__reported_dt__date": datetime.date,
    "affects__flaw__reported_dt__date__gte": datetime.date,
    "affects__flaw__reported_dt__date__lte": datetime.date,
    "affects__flaw__reported_dt__gt": datetime.datetime,
    "affects__flaw__reported_dt__gte": datetime.datetime,
    "affects__flaw__reported_dt__lt": datetime.datetime,
    "affects__flaw__reported_dt__lte": datetime.datetime,
    "affects__flaw__source": OsidbApiV1TrackersListAffectsFlawSource,
    "affects__flaw__type": OsidbApiV1TrackersListAffectsFlawType,
    "affects__flaw__unembargo_dt": datetime.datetime,
    "affects__flaw__updated_dt": datetime.datetime,
    "affects__flaw__updated_dt__date": datetime.date,
    "affects__flaw__updated_dt__date__gte": datetime.date,
    "affects__flaw__updated_dt__date__lte": datetime.date,
    "affects__flaw__updated_dt__gt": datetime.datetime,
    "affects__flaw__updated_dt__gte": datetime.datetime,
    "affects__flaw__updated_dt__lt": datetime.datetime,
    "affects__flaw__updated_dt__lte": datetime.datetime,
    "affects__flaw__uuid": str,
    "affects__impact": OsidbApiV1TrackersListAffectsImpact,
    "affects__ps_component": str,
    "affects__ps_module": str,
    "affects__resolution": OsidbApiV1TrackersListAffectsResolution,
    "affects__type": OsidbApiV1TrackersListAffectsType,
    "affects__updated_dt": datetime.datetime,
    "affects__updated_dt__date": datetime.date,
    "affects__updated_dt__date__gte": datetime.date,
    "affects__updated_dt__date__lte": datetime.date,
    "affects__updated_dt__gt": datetime.datetime,
    "affects__updated_dt__gte": datetime.datetime,
    "affects__updated_dt__lt": datetime.datetime,
    "affects__updated_dt__lte": datetime.datetime,
    "affects__uuid": str,
    "created_dt": datetime.datetime,
    "created_dt__date": datetime.date,
    "created_dt__date__gte": datetime.date,
    "created_dt__date__lte": datetime.date,
    "created_dt__gt": datetime.datetime,
    "created_dt__gte": datetime.datetime,
    "created_dt__lt": datetime.datetime,
    "created_dt__lte": datetime.datetime,
    "embargoed": bool,
    "exclude_fields": List[str],
    "external_system_id": str,
    "include_fields": List[str],
    "include_meta_attr": List[str],
    "limit": int,
    "offset": int,
    "order": List[OsidbApiV1TrackersListOrderItem],
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
    "uuid": str,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    affects_affectedness: Union[
        Unset, None, OsidbApiV1TrackersListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_cvss2: Union[Unset, None, str] = UNSET,
    affects_cvss2_score: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    affects_cvss3: Union[Unset, None, str] = UNSET,
    affects_cvss3_score: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    affects_embargoed: Union[Unset, None, bool] = UNSET,
    affects_flaw_component: Union[Unset, None, str] = UNSET,
    affects_flaw_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_cve_id: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss2: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss2_score: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss3_score: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    affects_flaw_cwe_id: Union[Unset, None, str] = UNSET,
    affects_flaw_embargoed: Union[Unset, None, bool] = UNSET,
    affects_flaw_impact: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawImpact
    ] = UNSET,
    affects_flaw_is_major_incident: Union[Unset, None, bool] = UNSET,
    affects_flaw_nvd_cvss2: Union[Unset, None, str] = UNSET,
    affects_flaw_nvd_cvss3: Union[Unset, None, str] = UNSET,
    affects_flaw_reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_source: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawSource
    ] = UNSET,
    affects_flaw_type: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawType
    ] = UNSET,
    affects_flaw_unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_uuid: Union[Unset, None, str] = UNSET,
    affects_impact: Union[Unset, None, OsidbApiV1TrackersListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, None, str] = UNSET,
    affects_ps_module: Union[Unset, None, str] = UNSET,
    affects_resolution: Union[
        Unset, None, OsidbApiV1TrackersListAffectsResolution
    ] = UNSET,
    affects_type: Union[Unset, None, OsidbApiV1TrackersListAffectsType] = UNSET,
    affects_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, None, str] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    external_system_id: Union[Unset, None, str] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1TrackersListOrderItem]] = UNSET,
    ps_update_stream: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1TrackersListType] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/trackers".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_affects_affectedness: Union[Unset, None, str] = UNSET
    if not isinstance(affects_affectedness, Unset):

        json_affects_affectedness = (
            OsidbApiV1TrackersListAffectsAffectedness(affects_affectedness).value
            if affects_affectedness
            else None
        )

    json_affects_created_dt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_created_dt, Unset):
        json_affects_created_dt = (
            affects_created_dt.isoformat() if affects_created_dt else None
        )

    json_affects_created_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(affects_created_dt_date, Unset):
        json_affects_created_dt_date = (
            affects_created_dt_date.isoformat() if affects_created_dt_date else None
        )

    json_affects_created_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_created_dt_date_gte, Unset):
        json_affects_created_dt_date_gte = (
            affects_created_dt_date_gte.isoformat()
            if affects_created_dt_date_gte
            else None
        )

    json_affects_created_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_created_dt_date_lte, Unset):
        json_affects_created_dt_date_lte = (
            affects_created_dt_date_lte.isoformat()
            if affects_created_dt_date_lte
            else None
        )

    json_affects_created_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_created_dt_gt, Unset):
        json_affects_created_dt_gt = (
            affects_created_dt_gt.isoformat() if affects_created_dt_gt else None
        )

    json_affects_created_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_created_dt_gte, Unset):
        json_affects_created_dt_gte = (
            affects_created_dt_gte.isoformat() if affects_created_dt_gte else None
        )

    json_affects_created_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_created_dt_lt, Unset):
        json_affects_created_dt_lt = (
            affects_created_dt_lt.isoformat() if affects_created_dt_lt else None
        )

    json_affects_created_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_created_dt_lte, Unset):
        json_affects_created_dt_lte = (
            affects_created_dt_lte.isoformat() if affects_created_dt_lte else None
        )

    json_affects_flaw_created_dt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_created_dt, Unset):
        json_affects_flaw_created_dt = (
            affects_flaw_created_dt.isoformat() if affects_flaw_created_dt else None
        )

    json_affects_flaw_created_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_created_dt_date, Unset):
        json_affects_flaw_created_dt_date = (
            affects_flaw_created_dt_date.isoformat()
            if affects_flaw_created_dt_date
            else None
        )

    json_affects_flaw_created_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_created_dt_date_gte, Unset):
        json_affects_flaw_created_dt_date_gte = (
            affects_flaw_created_dt_date_gte.isoformat()
            if affects_flaw_created_dt_date_gte
            else None
        )

    json_affects_flaw_created_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_created_dt_date_lte, Unset):
        json_affects_flaw_created_dt_date_lte = (
            affects_flaw_created_dt_date_lte.isoformat()
            if affects_flaw_created_dt_date_lte
            else None
        )

    json_affects_flaw_created_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_created_dt_gt, Unset):
        json_affects_flaw_created_dt_gt = (
            affects_flaw_created_dt_gt.isoformat()
            if affects_flaw_created_dt_gt
            else None
        )

    json_affects_flaw_created_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_created_dt_gte, Unset):
        json_affects_flaw_created_dt_gte = (
            affects_flaw_created_dt_gte.isoformat()
            if affects_flaw_created_dt_gte
            else None
        )

    json_affects_flaw_created_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_created_dt_lt, Unset):
        json_affects_flaw_created_dt_lt = (
            affects_flaw_created_dt_lt.isoformat()
            if affects_flaw_created_dt_lt
            else None
        )

    json_affects_flaw_created_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_created_dt_lte, Unset):
        json_affects_flaw_created_dt_lte = (
            affects_flaw_created_dt_lte.isoformat()
            if affects_flaw_created_dt_lte
            else None
        )

    json_affects_flaw_impact: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_impact, Unset):

        json_affects_flaw_impact = (
            OsidbApiV1TrackersListAffectsFlawImpact(affects_flaw_impact).value
            if affects_flaw_impact
            else None
        )

    json_affects_flaw_reported_dt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_reported_dt, Unset):
        json_affects_flaw_reported_dt = (
            affects_flaw_reported_dt.isoformat() if affects_flaw_reported_dt else None
        )

    json_affects_flaw_reported_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_date, Unset):
        json_affects_flaw_reported_dt_date = (
            affects_flaw_reported_dt_date.isoformat()
            if affects_flaw_reported_dt_date
            else None
        )

    json_affects_flaw_reported_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_date_gte, Unset):
        json_affects_flaw_reported_dt_date_gte = (
            affects_flaw_reported_dt_date_gte.isoformat()
            if affects_flaw_reported_dt_date_gte
            else None
        )

    json_affects_flaw_reported_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_date_lte, Unset):
        json_affects_flaw_reported_dt_date_lte = (
            affects_flaw_reported_dt_date_lte.isoformat()
            if affects_flaw_reported_dt_date_lte
            else None
        )

    json_affects_flaw_reported_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_gt, Unset):
        json_affects_flaw_reported_dt_gt = (
            affects_flaw_reported_dt_gt.isoformat()
            if affects_flaw_reported_dt_gt
            else None
        )

    json_affects_flaw_reported_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_gte, Unset):
        json_affects_flaw_reported_dt_gte = (
            affects_flaw_reported_dt_gte.isoformat()
            if affects_flaw_reported_dt_gte
            else None
        )

    json_affects_flaw_reported_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_lt, Unset):
        json_affects_flaw_reported_dt_lt = (
            affects_flaw_reported_dt_lt.isoformat()
            if affects_flaw_reported_dt_lt
            else None
        )

    json_affects_flaw_reported_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_reported_dt_lte, Unset):
        json_affects_flaw_reported_dt_lte = (
            affects_flaw_reported_dt_lte.isoformat()
            if affects_flaw_reported_dt_lte
            else None
        )

    json_affects_flaw_source: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_source, Unset):

        json_affects_flaw_source = (
            OsidbApiV1TrackersListAffectsFlawSource(affects_flaw_source).value
            if affects_flaw_source
            else None
        )

    json_affects_flaw_type: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_type, Unset):

        json_affects_flaw_type = (
            OsidbApiV1TrackersListAffectsFlawType(affects_flaw_type).value
            if affects_flaw_type
            else None
        )

    json_affects_flaw_unembargo_dt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_unembargo_dt, Unset):
        json_affects_flaw_unembargo_dt = (
            affects_flaw_unembargo_dt.isoformat() if affects_flaw_unembargo_dt else None
        )

    json_affects_flaw_updated_dt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_updated_dt, Unset):
        json_affects_flaw_updated_dt = (
            affects_flaw_updated_dt.isoformat() if affects_flaw_updated_dt else None
        )

    json_affects_flaw_updated_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_date, Unset):
        json_affects_flaw_updated_dt_date = (
            affects_flaw_updated_dt_date.isoformat()
            if affects_flaw_updated_dt_date
            else None
        )

    json_affects_flaw_updated_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_date_gte, Unset):
        json_affects_flaw_updated_dt_date_gte = (
            affects_flaw_updated_dt_date_gte.isoformat()
            if affects_flaw_updated_dt_date_gte
            else None
        )

    json_affects_flaw_updated_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_date_lte, Unset):
        json_affects_flaw_updated_dt_date_lte = (
            affects_flaw_updated_dt_date_lte.isoformat()
            if affects_flaw_updated_dt_date_lte
            else None
        )

    json_affects_flaw_updated_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_gt, Unset):
        json_affects_flaw_updated_dt_gt = (
            affects_flaw_updated_dt_gt.isoformat()
            if affects_flaw_updated_dt_gt
            else None
        )

    json_affects_flaw_updated_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_gte, Unset):
        json_affects_flaw_updated_dt_gte = (
            affects_flaw_updated_dt_gte.isoformat()
            if affects_flaw_updated_dt_gte
            else None
        )

    json_affects_flaw_updated_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_lt, Unset):
        json_affects_flaw_updated_dt_lt = (
            affects_flaw_updated_dt_lt.isoformat()
            if affects_flaw_updated_dt_lt
            else None
        )

    json_affects_flaw_updated_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_flaw_updated_dt_lte, Unset):
        json_affects_flaw_updated_dt_lte = (
            affects_flaw_updated_dt_lte.isoformat()
            if affects_flaw_updated_dt_lte
            else None
        )

    json_affects_impact: Union[Unset, None, str] = UNSET
    if not isinstance(affects_impact, Unset):

        json_affects_impact = (
            OsidbApiV1TrackersListAffectsImpact(affects_impact).value
            if affects_impact
            else None
        )

    json_affects_resolution: Union[Unset, None, str] = UNSET
    if not isinstance(affects_resolution, Unset):

        json_affects_resolution = (
            OsidbApiV1TrackersListAffectsResolution(affects_resolution).value
            if affects_resolution
            else None
        )

    json_affects_type: Union[Unset, None, str] = UNSET
    if not isinstance(affects_type, Unset):

        json_affects_type = (
            OsidbApiV1TrackersListAffectsType(affects_type).value
            if affects_type
            else None
        )

    json_affects_updated_dt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_updated_dt, Unset):
        json_affects_updated_dt = (
            affects_updated_dt.isoformat() if affects_updated_dt else None
        )

    json_affects_updated_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(affects_updated_dt_date, Unset):
        json_affects_updated_dt_date = (
            affects_updated_dt_date.isoformat() if affects_updated_dt_date else None
        )

    json_affects_updated_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_updated_dt_date_gte, Unset):
        json_affects_updated_dt_date_gte = (
            affects_updated_dt_date_gte.isoformat()
            if affects_updated_dt_date_gte
            else None
        )

    json_affects_updated_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_updated_dt_date_lte, Unset):
        json_affects_updated_dt_date_lte = (
            affects_updated_dt_date_lte.isoformat()
            if affects_updated_dt_date_lte
            else None
        )

    json_affects_updated_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_updated_dt_gt, Unset):
        json_affects_updated_dt_gt = (
            affects_updated_dt_gt.isoformat() if affects_updated_dt_gt else None
        )

    json_affects_updated_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_updated_dt_gte, Unset):
        json_affects_updated_dt_gte = (
            affects_updated_dt_gte.isoformat() if affects_updated_dt_gte else None
        )

    json_affects_updated_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_updated_dt_lt, Unset):
        json_affects_updated_dt_lt = (
            affects_updated_dt_lt.isoformat() if affects_updated_dt_lt else None
        )

    json_affects_updated_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_updated_dt_lte, Unset):
        json_affects_updated_dt_lte = (
            affects_updated_dt_lte.isoformat() if affects_updated_dt_lte else None
        )

    json_created_dt: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt, Unset):
        json_created_dt = created_dt.isoformat() if created_dt else None

    json_created_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_date, Unset):
        json_created_dt_date = created_dt_date.isoformat() if created_dt_date else None

    json_created_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_date_gte, Unset):
        json_created_dt_date_gte = (
            created_dt_date_gte.isoformat() if created_dt_date_gte else None
        )

    json_created_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_date_lte, Unset):
        json_created_dt_date_lte = (
            created_dt_date_lte.isoformat() if created_dt_date_lte else None
        )

    json_created_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_gt, Unset):
        json_created_dt_gt = created_dt_gt.isoformat() if created_dt_gt else None

    json_created_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_gte, Unset):
        json_created_dt_gte = created_dt_gte.isoformat() if created_dt_gte else None

    json_created_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_lt, Unset):
        json_created_dt_lt = created_dt_lt.isoformat() if created_dt_lt else None

    json_created_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt_lte, Unset):
        json_created_dt_lte = created_dt_lte.isoformat() if created_dt_lte else None

    json_exclude_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        if exclude_fields is None:
            json_exclude_fields = None
        else:
            json_exclude_fields = exclude_fields

    json_include_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_fields, Unset):
        if include_fields is None:
            json_include_fields = None
        else:
            json_include_fields = include_fields

    json_include_meta_attr: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_meta_attr, Unset):
        if include_meta_attr is None:
            json_include_meta_attr = None
        else:
            json_include_meta_attr = include_meta_attr

    json_order: Union[Unset, None, List[str]] = UNSET
    if not isinstance(order, Unset):
        if order is None:
            json_order = None
        else:
            json_order = []
            for order_item_data in order:
                order_item: str = UNSET
                if not isinstance(order_item_data, Unset):

                    order_item = OsidbApiV1TrackersListOrderItem(order_item_data).value

                json_order.append(order_item)

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):

        json_type = OsidbApiV1TrackersListType(type).value if type else None

    json_updated_dt: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt, Unset):
        json_updated_dt = updated_dt.isoformat() if updated_dt else None

    json_updated_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_date, Unset):
        json_updated_dt_date = updated_dt_date.isoformat() if updated_dt_date else None

    json_updated_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_date_gte, Unset):
        json_updated_dt_date_gte = (
            updated_dt_date_gte.isoformat() if updated_dt_date_gte else None
        )

    json_updated_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_date_lte, Unset):
        json_updated_dt_date_lte = (
            updated_dt_date_lte.isoformat() if updated_dt_date_lte else None
        )

    json_updated_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_gt, Unset):
        json_updated_dt_gt = updated_dt_gt.isoformat() if updated_dt_gt else None

    json_updated_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_gte, Unset):
        json_updated_dt_gte = updated_dt_gte.isoformat() if updated_dt_gte else None

    json_updated_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_lt, Unset):
        json_updated_dt_lt = updated_dt_lt.isoformat() if updated_dt_lt else None

    json_updated_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt_lte, Unset):
        json_updated_dt_lte = updated_dt_lte.isoformat() if updated_dt_lte else None

    params: Dict[str, Any] = {
        "affects__affectedness": json_affects_affectedness,
        "affects__created_dt": json_affects_created_dt,
        "affects__created_dt__date": json_affects_created_dt_date,
        "affects__created_dt__date__gte": json_affects_created_dt_date_gte,
        "affects__created_dt__date__lte": json_affects_created_dt_date_lte,
        "affects__created_dt__gt": json_affects_created_dt_gt,
        "affects__created_dt__gte": json_affects_created_dt_gte,
        "affects__created_dt__lt": json_affects_created_dt_lt,
        "affects__created_dt__lte": json_affects_created_dt_lte,
        "affects__cvss2": affects_cvss2,
        "affects__cvss2_score": affects_cvss2_score,
        "affects__cvss2_score__gt": affects_cvss2_score_gt,
        "affects__cvss2_score__gte": affects_cvss2_score_gte,
        "affects__cvss2_score__lt": affects_cvss2_score_lt,
        "affects__cvss2_score__lte": affects_cvss2_score_lte,
        "affects__cvss3": affects_cvss3,
        "affects__cvss3_score": affects_cvss3_score,
        "affects__cvss3_score__gt": affects_cvss3_score_gt,
        "affects__cvss3_score__gte": affects_cvss3_score_gte,
        "affects__cvss3_score__lt": affects_cvss3_score_lt,
        "affects__cvss3_score__lte": affects_cvss3_score_lte,
        "affects__embargoed": affects_embargoed,
        "affects__flaw__component": affects_flaw_component,
        "affects__flaw__created_dt": json_affects_flaw_created_dt,
        "affects__flaw__created_dt__date": json_affects_flaw_created_dt_date,
        "affects__flaw__created_dt__date__gte": json_affects_flaw_created_dt_date_gte,
        "affects__flaw__created_dt__date__lte": json_affects_flaw_created_dt_date_lte,
        "affects__flaw__created_dt__gt": json_affects_flaw_created_dt_gt,
        "affects__flaw__created_dt__gte": json_affects_flaw_created_dt_gte,
        "affects__flaw__created_dt__lt": json_affects_flaw_created_dt_lt,
        "affects__flaw__created_dt__lte": json_affects_flaw_created_dt_lte,
        "affects__flaw__cve_id": affects_flaw_cve_id,
        "affects__flaw__cvss2": affects_flaw_cvss2,
        "affects__flaw__cvss2_score": affects_flaw_cvss2_score,
        "affects__flaw__cvss2_score__gt": affects_flaw_cvss2_score_gt,
        "affects__flaw__cvss2_score__gte": affects_flaw_cvss2_score_gte,
        "affects__flaw__cvss2_score__lt": affects_flaw_cvss2_score_lt,
        "affects__flaw__cvss2_score__lte": affects_flaw_cvss2_score_lte,
        "affects__flaw__cvss3": affects_flaw_cvss3,
        "affects__flaw__cvss3_score": affects_flaw_cvss3_score,
        "affects__flaw__cvss3_score__gt": affects_flaw_cvss3_score_gt,
        "affects__flaw__cvss3_score__gte": affects_flaw_cvss3_score_gte,
        "affects__flaw__cvss3_score__lt": affects_flaw_cvss3_score_lt,
        "affects__flaw__cvss3_score__lte": affects_flaw_cvss3_score_lte,
        "affects__flaw__cwe_id": affects_flaw_cwe_id,
        "affects__flaw__embargoed": affects_flaw_embargoed,
        "affects__flaw__impact": json_affects_flaw_impact,
        "affects__flaw__is_major_incident": affects_flaw_is_major_incident,
        "affects__flaw__nvd_cvss2": affects_flaw_nvd_cvss2,
        "affects__flaw__nvd_cvss3": affects_flaw_nvd_cvss3,
        "affects__flaw__reported_dt": json_affects_flaw_reported_dt,
        "affects__flaw__reported_dt__date": json_affects_flaw_reported_dt_date,
        "affects__flaw__reported_dt__date__gte": json_affects_flaw_reported_dt_date_gte,
        "affects__flaw__reported_dt__date__lte": json_affects_flaw_reported_dt_date_lte,
        "affects__flaw__reported_dt__gt": json_affects_flaw_reported_dt_gt,
        "affects__flaw__reported_dt__gte": json_affects_flaw_reported_dt_gte,
        "affects__flaw__reported_dt__lt": json_affects_flaw_reported_dt_lt,
        "affects__flaw__reported_dt__lte": json_affects_flaw_reported_dt_lte,
        "affects__flaw__source": json_affects_flaw_source,
        "affects__flaw__type": json_affects_flaw_type,
        "affects__flaw__unembargo_dt": json_affects_flaw_unembargo_dt,
        "affects__flaw__updated_dt": json_affects_flaw_updated_dt,
        "affects__flaw__updated_dt__date": json_affects_flaw_updated_dt_date,
        "affects__flaw__updated_dt__date__gte": json_affects_flaw_updated_dt_date_gte,
        "affects__flaw__updated_dt__date__lte": json_affects_flaw_updated_dt_date_lte,
        "affects__flaw__updated_dt__gt": json_affects_flaw_updated_dt_gt,
        "affects__flaw__updated_dt__gte": json_affects_flaw_updated_dt_gte,
        "affects__flaw__updated_dt__lt": json_affects_flaw_updated_dt_lt,
        "affects__flaw__updated_dt__lte": json_affects_flaw_updated_dt_lte,
        "affects__flaw__uuid": affects_flaw_uuid,
        "affects__impact": json_affects_impact,
        "affects__ps_component": affects_ps_component,
        "affects__ps_module": affects_ps_module,
        "affects__resolution": json_affects_resolution,
        "affects__type": json_affects_type,
        "affects__updated_dt": json_affects_updated_dt,
        "affects__updated_dt__date": json_affects_updated_dt_date,
        "affects__updated_dt__date__gte": json_affects_updated_dt_date_gte,
        "affects__updated_dt__date__lte": json_affects_updated_dt_date_lte,
        "affects__updated_dt__gt": json_affects_updated_dt_gt,
        "affects__updated_dt__gte": json_affects_updated_dt_gte,
        "affects__updated_dt__lt": json_affects_updated_dt_lt,
        "affects__updated_dt__lte": json_affects_updated_dt_lte,
        "affects__uuid": affects_uuid,
        "created_dt": json_created_dt,
        "created_dt__date": json_created_dt_date,
        "created_dt__date__gte": json_created_dt_date_gte,
        "created_dt__date__lte": json_created_dt_date_lte,
        "created_dt__gt": json_created_dt_gt,
        "created_dt__gte": json_created_dt_gte,
        "created_dt__lt": json_created_dt_lt,
        "created_dt__lte": json_created_dt_lte,
        "embargoed": embargoed,
        "exclude_fields": json_exclude_fields,
        "external_system_id": external_system_id,
        "include_fields": json_include_fields,
        "include_meta_attr": json_include_meta_attr,
        "limit": limit,
        "offset": offset,
        "order": json_order,
        "ps_update_stream": ps_update_stream,
        "resolution": resolution,
        "status": status,
        "type": json_type,
        "updated_dt": json_updated_dt,
        "updated_dt__date": json_updated_dt_date,
        "updated_dt__date__gte": json_updated_dt_date_gte,
        "updated_dt__date__lte": json_updated_dt_date_lte,
        "updated_dt__gt": json_updated_dt_gt,
        "updated_dt__gte": json_updated_dt_gte,
        "updated_dt__lt": json_updated_dt_lt,
        "updated_dt__lte": json_updated_dt_lte,
        "uuid": uuid,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1TrackersListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1TrackersListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1TrackersListResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1TrackersListResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    affects_affectedness: Union[
        Unset, None, OsidbApiV1TrackersListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_cvss2: Union[Unset, None, str] = UNSET,
    affects_cvss2_score: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    affects_cvss3: Union[Unset, None, str] = UNSET,
    affects_cvss3_score: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    affects_embargoed: Union[Unset, None, bool] = UNSET,
    affects_flaw_component: Union[Unset, None, str] = UNSET,
    affects_flaw_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_cve_id: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss2: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss2_score: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss3_score: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    affects_flaw_cwe_id: Union[Unset, None, str] = UNSET,
    affects_flaw_embargoed: Union[Unset, None, bool] = UNSET,
    affects_flaw_impact: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawImpact
    ] = UNSET,
    affects_flaw_is_major_incident: Union[Unset, None, bool] = UNSET,
    affects_flaw_nvd_cvss2: Union[Unset, None, str] = UNSET,
    affects_flaw_nvd_cvss3: Union[Unset, None, str] = UNSET,
    affects_flaw_reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_source: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawSource
    ] = UNSET,
    affects_flaw_type: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawType
    ] = UNSET,
    affects_flaw_unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_uuid: Union[Unset, None, str] = UNSET,
    affects_impact: Union[Unset, None, OsidbApiV1TrackersListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, None, str] = UNSET,
    affects_ps_module: Union[Unset, None, str] = UNSET,
    affects_resolution: Union[
        Unset, None, OsidbApiV1TrackersListAffectsResolution
    ] = UNSET,
    affects_type: Union[Unset, None, OsidbApiV1TrackersListAffectsType] = UNSET,
    affects_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, None, str] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    external_system_id: Union[Unset, None, str] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1TrackersListOrderItem]] = UNSET,
    ps_update_stream: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1TrackersListType] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1TrackersListResponse200]:
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
        affects_cvss2=affects_cvss2,
        affects_cvss2_score=affects_cvss2_score,
        affects_cvss2_score_gt=affects_cvss2_score_gt,
        affects_cvss2_score_gte=affects_cvss2_score_gte,
        affects_cvss2_score_lt=affects_cvss2_score_lt,
        affects_cvss2_score_lte=affects_cvss2_score_lte,
        affects_cvss3=affects_cvss3,
        affects_cvss3_score=affects_cvss3_score,
        affects_cvss3_score_gt=affects_cvss3_score_gt,
        affects_cvss3_score_gte=affects_cvss3_score_gte,
        affects_cvss3_score_lt=affects_cvss3_score_lt,
        affects_cvss3_score_lte=affects_cvss3_score_lte,
        affects_embargoed=affects_embargoed,
        affects_flaw_component=affects_flaw_component,
        affects_flaw_created_dt=affects_flaw_created_dt,
        affects_flaw_created_dt_date=affects_flaw_created_dt_date,
        affects_flaw_created_dt_date_gte=affects_flaw_created_dt_date_gte,
        affects_flaw_created_dt_date_lte=affects_flaw_created_dt_date_lte,
        affects_flaw_created_dt_gt=affects_flaw_created_dt_gt,
        affects_flaw_created_dt_gte=affects_flaw_created_dt_gte,
        affects_flaw_created_dt_lt=affects_flaw_created_dt_lt,
        affects_flaw_created_dt_lte=affects_flaw_created_dt_lte,
        affects_flaw_cve_id=affects_flaw_cve_id,
        affects_flaw_cvss2=affects_flaw_cvss2,
        affects_flaw_cvss2_score=affects_flaw_cvss2_score,
        affects_flaw_cvss2_score_gt=affects_flaw_cvss2_score_gt,
        affects_flaw_cvss2_score_gte=affects_flaw_cvss2_score_gte,
        affects_flaw_cvss2_score_lt=affects_flaw_cvss2_score_lt,
        affects_flaw_cvss2_score_lte=affects_flaw_cvss2_score_lte,
        affects_flaw_cvss3=affects_flaw_cvss3,
        affects_flaw_cvss3_score=affects_flaw_cvss3_score,
        affects_flaw_cvss3_score_gt=affects_flaw_cvss3_score_gt,
        affects_flaw_cvss3_score_gte=affects_flaw_cvss3_score_gte,
        affects_flaw_cvss3_score_lt=affects_flaw_cvss3_score_lt,
        affects_flaw_cvss3_score_lte=affects_flaw_cvss3_score_lte,
        affects_flaw_cwe_id=affects_flaw_cwe_id,
        affects_flaw_embargoed=affects_flaw_embargoed,
        affects_flaw_impact=affects_flaw_impact,
        affects_flaw_is_major_incident=affects_flaw_is_major_incident,
        affects_flaw_nvd_cvss2=affects_flaw_nvd_cvss2,
        affects_flaw_nvd_cvss3=affects_flaw_nvd_cvss3,
        affects_flaw_reported_dt=affects_flaw_reported_dt,
        affects_flaw_reported_dt_date=affects_flaw_reported_dt_date,
        affects_flaw_reported_dt_date_gte=affects_flaw_reported_dt_date_gte,
        affects_flaw_reported_dt_date_lte=affects_flaw_reported_dt_date_lte,
        affects_flaw_reported_dt_gt=affects_flaw_reported_dt_gt,
        affects_flaw_reported_dt_gte=affects_flaw_reported_dt_gte,
        affects_flaw_reported_dt_lt=affects_flaw_reported_dt_lt,
        affects_flaw_reported_dt_lte=affects_flaw_reported_dt_lte,
        affects_flaw_source=affects_flaw_source,
        affects_flaw_type=affects_flaw_type,
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
        affects_type=affects_type,
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
        type=type,
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

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    affects_affectedness: Union[
        Unset, None, OsidbApiV1TrackersListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_cvss2: Union[Unset, None, str] = UNSET,
    affects_cvss2_score: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    affects_cvss3: Union[Unset, None, str] = UNSET,
    affects_cvss3_score: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    affects_embargoed: Union[Unset, None, bool] = UNSET,
    affects_flaw_component: Union[Unset, None, str] = UNSET,
    affects_flaw_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_cve_id: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss2: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss2_score: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss3_score: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    affects_flaw_cwe_id: Union[Unset, None, str] = UNSET,
    affects_flaw_embargoed: Union[Unset, None, bool] = UNSET,
    affects_flaw_impact: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawImpact
    ] = UNSET,
    affects_flaw_is_major_incident: Union[Unset, None, bool] = UNSET,
    affects_flaw_nvd_cvss2: Union[Unset, None, str] = UNSET,
    affects_flaw_nvd_cvss3: Union[Unset, None, str] = UNSET,
    affects_flaw_reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_source: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawSource
    ] = UNSET,
    affects_flaw_type: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawType
    ] = UNSET,
    affects_flaw_unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_uuid: Union[Unset, None, str] = UNSET,
    affects_impact: Union[Unset, None, OsidbApiV1TrackersListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, None, str] = UNSET,
    affects_ps_module: Union[Unset, None, str] = UNSET,
    affects_resolution: Union[
        Unset, None, OsidbApiV1TrackersListAffectsResolution
    ] = UNSET,
    affects_type: Union[Unset, None, OsidbApiV1TrackersListAffectsType] = UNSET,
    affects_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, None, str] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    external_system_id: Union[Unset, None, str] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1TrackersListOrderItem]] = UNSET,
    ps_update_stream: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1TrackersListType] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1TrackersListResponse200]:
    """ """

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
        affects_cvss2=affects_cvss2,
        affects_cvss2_score=affects_cvss2_score,
        affects_cvss2_score_gt=affects_cvss2_score_gt,
        affects_cvss2_score_gte=affects_cvss2_score_gte,
        affects_cvss2_score_lt=affects_cvss2_score_lt,
        affects_cvss2_score_lte=affects_cvss2_score_lte,
        affects_cvss3=affects_cvss3,
        affects_cvss3_score=affects_cvss3_score,
        affects_cvss3_score_gt=affects_cvss3_score_gt,
        affects_cvss3_score_gte=affects_cvss3_score_gte,
        affects_cvss3_score_lt=affects_cvss3_score_lt,
        affects_cvss3_score_lte=affects_cvss3_score_lte,
        affects_embargoed=affects_embargoed,
        affects_flaw_component=affects_flaw_component,
        affects_flaw_created_dt=affects_flaw_created_dt,
        affects_flaw_created_dt_date=affects_flaw_created_dt_date,
        affects_flaw_created_dt_date_gte=affects_flaw_created_dt_date_gte,
        affects_flaw_created_dt_date_lte=affects_flaw_created_dt_date_lte,
        affects_flaw_created_dt_gt=affects_flaw_created_dt_gt,
        affects_flaw_created_dt_gte=affects_flaw_created_dt_gte,
        affects_flaw_created_dt_lt=affects_flaw_created_dt_lt,
        affects_flaw_created_dt_lte=affects_flaw_created_dt_lte,
        affects_flaw_cve_id=affects_flaw_cve_id,
        affects_flaw_cvss2=affects_flaw_cvss2,
        affects_flaw_cvss2_score=affects_flaw_cvss2_score,
        affects_flaw_cvss2_score_gt=affects_flaw_cvss2_score_gt,
        affects_flaw_cvss2_score_gte=affects_flaw_cvss2_score_gte,
        affects_flaw_cvss2_score_lt=affects_flaw_cvss2_score_lt,
        affects_flaw_cvss2_score_lte=affects_flaw_cvss2_score_lte,
        affects_flaw_cvss3=affects_flaw_cvss3,
        affects_flaw_cvss3_score=affects_flaw_cvss3_score,
        affects_flaw_cvss3_score_gt=affects_flaw_cvss3_score_gt,
        affects_flaw_cvss3_score_gte=affects_flaw_cvss3_score_gte,
        affects_flaw_cvss3_score_lt=affects_flaw_cvss3_score_lt,
        affects_flaw_cvss3_score_lte=affects_flaw_cvss3_score_lte,
        affects_flaw_cwe_id=affects_flaw_cwe_id,
        affects_flaw_embargoed=affects_flaw_embargoed,
        affects_flaw_impact=affects_flaw_impact,
        affects_flaw_is_major_incident=affects_flaw_is_major_incident,
        affects_flaw_nvd_cvss2=affects_flaw_nvd_cvss2,
        affects_flaw_nvd_cvss3=affects_flaw_nvd_cvss3,
        affects_flaw_reported_dt=affects_flaw_reported_dt,
        affects_flaw_reported_dt_date=affects_flaw_reported_dt_date,
        affects_flaw_reported_dt_date_gte=affects_flaw_reported_dt_date_gte,
        affects_flaw_reported_dt_date_lte=affects_flaw_reported_dt_date_lte,
        affects_flaw_reported_dt_gt=affects_flaw_reported_dt_gt,
        affects_flaw_reported_dt_gte=affects_flaw_reported_dt_gte,
        affects_flaw_reported_dt_lt=affects_flaw_reported_dt_lt,
        affects_flaw_reported_dt_lte=affects_flaw_reported_dt_lte,
        affects_flaw_source=affects_flaw_source,
        affects_flaw_type=affects_flaw_type,
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
        affects_type=affects_type,
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
        type=type,
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


async def async_detailed(
    *,
    client: AuthenticatedClient,
    affects_affectedness: Union[
        Unset, None, OsidbApiV1TrackersListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_cvss2: Union[Unset, None, str] = UNSET,
    affects_cvss2_score: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    affects_cvss3: Union[Unset, None, str] = UNSET,
    affects_cvss3_score: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    affects_embargoed: Union[Unset, None, bool] = UNSET,
    affects_flaw_component: Union[Unset, None, str] = UNSET,
    affects_flaw_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_cve_id: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss2: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss2_score: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss3_score: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    affects_flaw_cwe_id: Union[Unset, None, str] = UNSET,
    affects_flaw_embargoed: Union[Unset, None, bool] = UNSET,
    affects_flaw_impact: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawImpact
    ] = UNSET,
    affects_flaw_is_major_incident: Union[Unset, None, bool] = UNSET,
    affects_flaw_nvd_cvss2: Union[Unset, None, str] = UNSET,
    affects_flaw_nvd_cvss3: Union[Unset, None, str] = UNSET,
    affects_flaw_reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_source: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawSource
    ] = UNSET,
    affects_flaw_type: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawType
    ] = UNSET,
    affects_flaw_unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_uuid: Union[Unset, None, str] = UNSET,
    affects_impact: Union[Unset, None, OsidbApiV1TrackersListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, None, str] = UNSET,
    affects_ps_module: Union[Unset, None, str] = UNSET,
    affects_resolution: Union[
        Unset, None, OsidbApiV1TrackersListAffectsResolution
    ] = UNSET,
    affects_type: Union[Unset, None, OsidbApiV1TrackersListAffectsType] = UNSET,
    affects_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, None, str] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    external_system_id: Union[Unset, None, str] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1TrackersListOrderItem]] = UNSET,
    ps_update_stream: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1TrackersListType] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1TrackersListResponse200]:
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
        affects_cvss2=affects_cvss2,
        affects_cvss2_score=affects_cvss2_score,
        affects_cvss2_score_gt=affects_cvss2_score_gt,
        affects_cvss2_score_gte=affects_cvss2_score_gte,
        affects_cvss2_score_lt=affects_cvss2_score_lt,
        affects_cvss2_score_lte=affects_cvss2_score_lte,
        affects_cvss3=affects_cvss3,
        affects_cvss3_score=affects_cvss3_score,
        affects_cvss3_score_gt=affects_cvss3_score_gt,
        affects_cvss3_score_gte=affects_cvss3_score_gte,
        affects_cvss3_score_lt=affects_cvss3_score_lt,
        affects_cvss3_score_lte=affects_cvss3_score_lte,
        affects_embargoed=affects_embargoed,
        affects_flaw_component=affects_flaw_component,
        affects_flaw_created_dt=affects_flaw_created_dt,
        affects_flaw_created_dt_date=affects_flaw_created_dt_date,
        affects_flaw_created_dt_date_gte=affects_flaw_created_dt_date_gte,
        affects_flaw_created_dt_date_lte=affects_flaw_created_dt_date_lte,
        affects_flaw_created_dt_gt=affects_flaw_created_dt_gt,
        affects_flaw_created_dt_gte=affects_flaw_created_dt_gte,
        affects_flaw_created_dt_lt=affects_flaw_created_dt_lt,
        affects_flaw_created_dt_lte=affects_flaw_created_dt_lte,
        affects_flaw_cve_id=affects_flaw_cve_id,
        affects_flaw_cvss2=affects_flaw_cvss2,
        affects_flaw_cvss2_score=affects_flaw_cvss2_score,
        affects_flaw_cvss2_score_gt=affects_flaw_cvss2_score_gt,
        affects_flaw_cvss2_score_gte=affects_flaw_cvss2_score_gte,
        affects_flaw_cvss2_score_lt=affects_flaw_cvss2_score_lt,
        affects_flaw_cvss2_score_lte=affects_flaw_cvss2_score_lte,
        affects_flaw_cvss3=affects_flaw_cvss3,
        affects_flaw_cvss3_score=affects_flaw_cvss3_score,
        affects_flaw_cvss3_score_gt=affects_flaw_cvss3_score_gt,
        affects_flaw_cvss3_score_gte=affects_flaw_cvss3_score_gte,
        affects_flaw_cvss3_score_lt=affects_flaw_cvss3_score_lt,
        affects_flaw_cvss3_score_lte=affects_flaw_cvss3_score_lte,
        affects_flaw_cwe_id=affects_flaw_cwe_id,
        affects_flaw_embargoed=affects_flaw_embargoed,
        affects_flaw_impact=affects_flaw_impact,
        affects_flaw_is_major_incident=affects_flaw_is_major_incident,
        affects_flaw_nvd_cvss2=affects_flaw_nvd_cvss2,
        affects_flaw_nvd_cvss3=affects_flaw_nvd_cvss3,
        affects_flaw_reported_dt=affects_flaw_reported_dt,
        affects_flaw_reported_dt_date=affects_flaw_reported_dt_date,
        affects_flaw_reported_dt_date_gte=affects_flaw_reported_dt_date_gte,
        affects_flaw_reported_dt_date_lte=affects_flaw_reported_dt_date_lte,
        affects_flaw_reported_dt_gt=affects_flaw_reported_dt_gt,
        affects_flaw_reported_dt_gte=affects_flaw_reported_dt_gte,
        affects_flaw_reported_dt_lt=affects_flaw_reported_dt_lt,
        affects_flaw_reported_dt_lte=affects_flaw_reported_dt_lte,
        affects_flaw_source=affects_flaw_source,
        affects_flaw_type=affects_flaw_type,
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
        affects_type=affects_type,
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
        type=type,
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

    return _build_response(response=resp)


async def async_(
    *,
    client: AuthenticatedClient,
    affects_affectedness: Union[
        Unset, None, OsidbApiV1TrackersListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_cvss2: Union[Unset, None, str] = UNSET,
    affects_cvss2_score: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    affects_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    affects_cvss3: Union[Unset, None, str] = UNSET,
    affects_cvss3_score: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    affects_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    affects_embargoed: Union[Unset, None, bool] = UNSET,
    affects_flaw_component: Union[Unset, None, str] = UNSET,
    affects_flaw_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_cve_id: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss2: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss2_score: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3: Union[Unset, None, str] = UNSET,
    affects_flaw_cvss3_score: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    affects_flaw_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    affects_flaw_cwe_id: Union[Unset, None, str] = UNSET,
    affects_flaw_embargoed: Union[Unset, None, bool] = UNSET,
    affects_flaw_impact: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawImpact
    ] = UNSET,
    affects_flaw_is_major_incident: Union[Unset, None, bool] = UNSET,
    affects_flaw_nvd_cvss2: Union[Unset, None, str] = UNSET,
    affects_flaw_nvd_cvss3: Union[Unset, None, str] = UNSET,
    affects_flaw_reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_source: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawSource
    ] = UNSET,
    affects_flaw_type: Union[
        Unset, None, OsidbApiV1TrackersListAffectsFlawType
    ] = UNSET,
    affects_flaw_unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_flaw_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_flaw_uuid: Union[Unset, None, str] = UNSET,
    affects_impact: Union[Unset, None, OsidbApiV1TrackersListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, None, str] = UNSET,
    affects_ps_module: Union[Unset, None, str] = UNSET,
    affects_resolution: Union[
        Unset, None, OsidbApiV1TrackersListAffectsResolution
    ] = UNSET,
    affects_type: Union[Unset, None, OsidbApiV1TrackersListAffectsType] = UNSET,
    affects_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, None, str] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    external_system_id: Union[Unset, None, str] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1TrackersListOrderItem]] = UNSET,
    ps_update_stream: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1TrackersListType] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1TrackersListResponse200]:
    """ """

    return (
        await async_detailed(
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
            affects_cvss2=affects_cvss2,
            affects_cvss2_score=affects_cvss2_score,
            affects_cvss2_score_gt=affects_cvss2_score_gt,
            affects_cvss2_score_gte=affects_cvss2_score_gte,
            affects_cvss2_score_lt=affects_cvss2_score_lt,
            affects_cvss2_score_lte=affects_cvss2_score_lte,
            affects_cvss3=affects_cvss3,
            affects_cvss3_score=affects_cvss3_score,
            affects_cvss3_score_gt=affects_cvss3_score_gt,
            affects_cvss3_score_gte=affects_cvss3_score_gte,
            affects_cvss3_score_lt=affects_cvss3_score_lt,
            affects_cvss3_score_lte=affects_cvss3_score_lte,
            affects_embargoed=affects_embargoed,
            affects_flaw_component=affects_flaw_component,
            affects_flaw_created_dt=affects_flaw_created_dt,
            affects_flaw_created_dt_date=affects_flaw_created_dt_date,
            affects_flaw_created_dt_date_gte=affects_flaw_created_dt_date_gte,
            affects_flaw_created_dt_date_lte=affects_flaw_created_dt_date_lte,
            affects_flaw_created_dt_gt=affects_flaw_created_dt_gt,
            affects_flaw_created_dt_gte=affects_flaw_created_dt_gte,
            affects_flaw_created_dt_lt=affects_flaw_created_dt_lt,
            affects_flaw_created_dt_lte=affects_flaw_created_dt_lte,
            affects_flaw_cve_id=affects_flaw_cve_id,
            affects_flaw_cvss2=affects_flaw_cvss2,
            affects_flaw_cvss2_score=affects_flaw_cvss2_score,
            affects_flaw_cvss2_score_gt=affects_flaw_cvss2_score_gt,
            affects_flaw_cvss2_score_gte=affects_flaw_cvss2_score_gte,
            affects_flaw_cvss2_score_lt=affects_flaw_cvss2_score_lt,
            affects_flaw_cvss2_score_lte=affects_flaw_cvss2_score_lte,
            affects_flaw_cvss3=affects_flaw_cvss3,
            affects_flaw_cvss3_score=affects_flaw_cvss3_score,
            affects_flaw_cvss3_score_gt=affects_flaw_cvss3_score_gt,
            affects_flaw_cvss3_score_gte=affects_flaw_cvss3_score_gte,
            affects_flaw_cvss3_score_lt=affects_flaw_cvss3_score_lt,
            affects_flaw_cvss3_score_lte=affects_flaw_cvss3_score_lte,
            affects_flaw_cwe_id=affects_flaw_cwe_id,
            affects_flaw_embargoed=affects_flaw_embargoed,
            affects_flaw_impact=affects_flaw_impact,
            affects_flaw_is_major_incident=affects_flaw_is_major_incident,
            affects_flaw_nvd_cvss2=affects_flaw_nvd_cvss2,
            affects_flaw_nvd_cvss3=affects_flaw_nvd_cvss3,
            affects_flaw_reported_dt=affects_flaw_reported_dt,
            affects_flaw_reported_dt_date=affects_flaw_reported_dt_date,
            affects_flaw_reported_dt_date_gte=affects_flaw_reported_dt_date_gte,
            affects_flaw_reported_dt_date_lte=affects_flaw_reported_dt_date_lte,
            affects_flaw_reported_dt_gt=affects_flaw_reported_dt_gt,
            affects_flaw_reported_dt_gte=affects_flaw_reported_dt_gte,
            affects_flaw_reported_dt_lt=affects_flaw_reported_dt_lt,
            affects_flaw_reported_dt_lte=affects_flaw_reported_dt_lte,
            affects_flaw_source=affects_flaw_source,
            affects_flaw_type=affects_flaw_type,
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
            affects_type=affects_type,
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
            type=type,
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
