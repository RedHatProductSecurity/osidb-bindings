import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_affects_list_affectedness import (
    OsidbApiV1AffectsListAffectedness,
)
from ...models.osidb_api_v1_affects_list_cvss_scores_issuer import (
    OsidbApiV1AffectsListCvssScoresIssuer,
)
from ...models.osidb_api_v1_affects_list_flaw_impact import (
    OsidbApiV1AffectsListFlawImpact,
)
from ...models.osidb_api_v1_affects_list_flaw_source import (
    OsidbApiV1AffectsListFlawSource,
)
from ...models.osidb_api_v1_affects_list_impact import OsidbApiV1AffectsListImpact
from ...models.osidb_api_v1_affects_list_order_item import (
    OsidbApiV1AffectsListOrderItem,
)
from ...models.osidb_api_v1_affects_list_resolution import (
    OsidbApiV1AffectsListResolution,
)
from ...models.osidb_api_v1_affects_list_response_200 import (
    OsidbApiV1AffectsListResponse200,
)
from ...models.osidb_api_v1_affects_list_trackers_type import (
    OsidbApiV1AffectsListTrackersType,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "affectedness": OsidbApiV1AffectsListAffectedness,
    "created_dt": datetime.datetime,
    "created_dt__date": datetime.date,
    "created_dt__date__gte": datetime.date,
    "created_dt__date__lte": datetime.date,
    "created_dt__gt": datetime.datetime,
    "created_dt__gte": datetime.datetime,
    "created_dt__lt": datetime.datetime,
    "created_dt__lte": datetime.datetime,
    "cvss_scores__comment": str,
    "cvss_scores__created_dt": datetime.datetime,
    "cvss_scores__created_dt__date": datetime.date,
    "cvss_scores__created_dt__date__gte": datetime.date,
    "cvss_scores__created_dt__date__lte": datetime.date,
    "cvss_scores__created_dt__gt": datetime.datetime,
    "cvss_scores__created_dt__gte": datetime.datetime,
    "cvss_scores__created_dt__lt": datetime.datetime,
    "cvss_scores__created_dt__lte": datetime.datetime,
    "cvss_scores__cvss_version": str,
    "cvss_scores__issuer": OsidbApiV1AffectsListCvssScoresIssuer,
    "cvss_scores__score": float,
    "cvss_scores__updated_dt": datetime.datetime,
    "cvss_scores__updated_dt__date": datetime.date,
    "cvss_scores__updated_dt__date__gte": datetime.date,
    "cvss_scores__updated_dt__date__lte": datetime.date,
    "cvss_scores__updated_dt__gt": datetime.datetime,
    "cvss_scores__updated_dt__gte": datetime.datetime,
    "cvss_scores__updated_dt__lt": datetime.datetime,
    "cvss_scores__updated_dt__lte": datetime.datetime,
    "cvss_scores__uuid": UUID,
    "cvss_scores__vector": str,
    "embargoed": bool,
    "exclude_fields": list[str],
    "flaw__components": list[str],
    "flaw__created_dt": datetime.datetime,
    "flaw__created_dt__date": datetime.date,
    "flaw__created_dt__date__gte": datetime.date,
    "flaw__created_dt__date__lte": datetime.date,
    "flaw__created_dt__gt": datetime.datetime,
    "flaw__created_dt__gte": datetime.datetime,
    "flaw__created_dt__lt": datetime.datetime,
    "flaw__created_dt__lte": datetime.datetime,
    "flaw__cve_id": str,
    "flaw__cwe_id": str,
    "flaw__embargoed": bool,
    "flaw__impact": OsidbApiV1AffectsListFlawImpact,
    "flaw__reported_dt": datetime.datetime,
    "flaw__reported_dt__date": datetime.date,
    "flaw__reported_dt__date__gte": datetime.date,
    "flaw__reported_dt__date__lte": datetime.date,
    "flaw__reported_dt__gt": datetime.datetime,
    "flaw__reported_dt__gte": datetime.datetime,
    "flaw__reported_dt__lt": datetime.datetime,
    "flaw__reported_dt__lte": datetime.datetime,
    "flaw__source": OsidbApiV1AffectsListFlawSource,
    "flaw__unembargo_dt": datetime.datetime,
    "flaw__updated_dt": datetime.datetime,
    "flaw__updated_dt__date": datetime.date,
    "flaw__updated_dt__date__gte": datetime.date,
    "flaw__updated_dt__date__lte": datetime.date,
    "flaw__updated_dt__gt": datetime.datetime,
    "flaw__updated_dt__gte": datetime.datetime,
    "flaw__updated_dt__lt": datetime.datetime,
    "flaw__updated_dt__lte": datetime.datetime,
    "flaw__uuid": UUID,
    "impact": OsidbApiV1AffectsListImpact,
    "include_fields": list[str],
    "include_meta_attr": list[str],
    "limit": int,
    "offset": int,
    "order": list[OsidbApiV1AffectsListOrderItem],
    "ps_component": str,
    "ps_module": str,
    "resolution": OsidbApiV1AffectsListResolution,
    "trackers__created_dt": datetime.datetime,
    "trackers__created_dt__date": datetime.date,
    "trackers__created_dt__date__gte": datetime.date,
    "trackers__created_dt__date__lte": datetime.date,
    "trackers__created_dt__gt": datetime.datetime,
    "trackers__created_dt__gte": datetime.datetime,
    "trackers__created_dt__lt": datetime.datetime,
    "trackers__created_dt__lte": datetime.datetime,
    "trackers__embargoed": bool,
    "trackers__external_system_id": str,
    "trackers__ps_update_stream": str,
    "trackers__resolution": str,
    "trackers__status": str,
    "trackers__type": OsidbApiV1AffectsListTrackersType,
    "trackers__updated_dt": datetime.datetime,
    "trackers__updated_dt__date": datetime.date,
    "trackers__updated_dt__date__gte": datetime.date,
    "trackers__updated_dt__date__lte": datetime.date,
    "trackers__updated_dt__gt": datetime.datetime,
    "trackers__updated_dt__gte": datetime.datetime,
    "trackers__updated_dt__lt": datetime.datetime,
    "trackers__updated_dt__lte": datetime.datetime,
    "trackers__uuid": UUID,
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
    affectedness: Union[Unset, OsidbApiV1AffectsListAffectedness] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_comment: Union[Unset, str] = UNSET,
    cvss_scores_created_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, str] = UNSET,
    cvss_scores_issuer: Union[Unset, OsidbApiV1AffectsListCvssScoresIssuer] = UNSET,
    cvss_scores_score: Union[Unset, float] = UNSET,
    cvss_scores_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_uuid: Union[Unset, UUID] = UNSET,
    cvss_scores_vector: Union[Unset, str] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_components: Union[Unset, list[str]] = UNSET,
    flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, str] = UNSET,
    flaw_cwe_id: Union[Unset, str] = UNSET,
    flaw_embargoed: Union[Unset, bool] = UNSET,
    flaw_impact: Union[Unset, OsidbApiV1AffectsListFlawImpact] = UNSET,
    flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, OsidbApiV1AffectsListFlawSource] = UNSET,
    flaw_unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_uuid: Union[Unset, UUID] = UNSET,
    impact: Union[Unset, OsidbApiV1AffectsListImpact] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, str] = UNSET,
    ps_module: Union[Unset, str] = UNSET,
    resolution: Union[Unset, OsidbApiV1AffectsListResolution] = UNSET,
    trackers_created_dt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_date: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    trackers_embargoed: Union[Unset, bool] = UNSET,
    trackers_external_system_id: Union[Unset, str] = UNSET,
    trackers_ps_update_stream: Union[Unset, str] = UNSET,
    trackers_resolution: Union[Unset, str] = UNSET,
    trackers_status: Union[Unset, str] = UNSET,
    trackers_type: Union[Unset, OsidbApiV1AffectsListTrackersType] = UNSET,
    trackers_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    trackers_uuid: Union[Unset, UUID] = UNSET,
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

    json_affectedness: Union[Unset, str] = UNSET
    if not isinstance(affectedness, Unset):
        json_affectedness = OsidbApiV1AffectsListAffectedness(affectedness).value

    params["affectedness"] = json_affectedness

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

    params["cvss_scores__comment"] = cvss_scores_comment

    json_cvss_scores_created_dt: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_created_dt, Unset):
        json_cvss_scores_created_dt = cvss_scores_created_dt.isoformat()

    params["cvss_scores__created_dt"] = json_cvss_scores_created_dt

    json_cvss_scores_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_created_dt_date, Unset):
        json_cvss_scores_created_dt_date = cvss_scores_created_dt_date.isoformat()

    params["cvss_scores__created_dt__date"] = json_cvss_scores_created_dt_date

    json_cvss_scores_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_created_dt_date_gte, Unset):
        json_cvss_scores_created_dt_date_gte = (
            cvss_scores_created_dt_date_gte.isoformat()
        )

    params["cvss_scores__created_dt__date__gte"] = json_cvss_scores_created_dt_date_gte

    json_cvss_scores_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_created_dt_date_lte, Unset):
        json_cvss_scores_created_dt_date_lte = (
            cvss_scores_created_dt_date_lte.isoformat()
        )

    params["cvss_scores__created_dt__date__lte"] = json_cvss_scores_created_dt_date_lte

    json_cvss_scores_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_created_dt_gt, Unset):
        json_cvss_scores_created_dt_gt = cvss_scores_created_dt_gt.isoformat()

    params["cvss_scores__created_dt__gt"] = json_cvss_scores_created_dt_gt

    json_cvss_scores_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_created_dt_gte, Unset):
        json_cvss_scores_created_dt_gte = cvss_scores_created_dt_gte.isoformat()

    params["cvss_scores__created_dt__gte"] = json_cvss_scores_created_dt_gte

    json_cvss_scores_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_created_dt_lt, Unset):
        json_cvss_scores_created_dt_lt = cvss_scores_created_dt_lt.isoformat()

    params["cvss_scores__created_dt__lt"] = json_cvss_scores_created_dt_lt

    json_cvss_scores_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_created_dt_lte, Unset):
        json_cvss_scores_created_dt_lte = cvss_scores_created_dt_lte.isoformat()

    params["cvss_scores__created_dt__lte"] = json_cvss_scores_created_dt_lte

    params["cvss_scores__cvss_version"] = cvss_scores_cvss_version

    json_cvss_scores_issuer: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_issuer, Unset):
        json_cvss_scores_issuer = OsidbApiV1AffectsListCvssScoresIssuer(
            cvss_scores_issuer
        ).value

    params["cvss_scores__issuer"] = json_cvss_scores_issuer

    params["cvss_scores__score"] = cvss_scores_score

    json_cvss_scores_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_updated_dt, Unset):
        json_cvss_scores_updated_dt = cvss_scores_updated_dt.isoformat()

    params["cvss_scores__updated_dt"] = json_cvss_scores_updated_dt

    json_cvss_scores_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_date, Unset):
        json_cvss_scores_updated_dt_date = cvss_scores_updated_dt_date.isoformat()

    params["cvss_scores__updated_dt__date"] = json_cvss_scores_updated_dt_date

    json_cvss_scores_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_date_gte, Unset):
        json_cvss_scores_updated_dt_date_gte = (
            cvss_scores_updated_dt_date_gte.isoformat()
        )

    params["cvss_scores__updated_dt__date__gte"] = json_cvss_scores_updated_dt_date_gte

    json_cvss_scores_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_date_lte, Unset):
        json_cvss_scores_updated_dt_date_lte = (
            cvss_scores_updated_dt_date_lte.isoformat()
        )

    params["cvss_scores__updated_dt__date__lte"] = json_cvss_scores_updated_dt_date_lte

    json_cvss_scores_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_gt, Unset):
        json_cvss_scores_updated_dt_gt = cvss_scores_updated_dt_gt.isoformat()

    params["cvss_scores__updated_dt__gt"] = json_cvss_scores_updated_dt_gt

    json_cvss_scores_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_gte, Unset):
        json_cvss_scores_updated_dt_gte = cvss_scores_updated_dt_gte.isoformat()

    params["cvss_scores__updated_dt__gte"] = json_cvss_scores_updated_dt_gte

    json_cvss_scores_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_lt, Unset):
        json_cvss_scores_updated_dt_lt = cvss_scores_updated_dt_lt.isoformat()

    params["cvss_scores__updated_dt__lt"] = json_cvss_scores_updated_dt_lt

    json_cvss_scores_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_lte, Unset):
        json_cvss_scores_updated_dt_lte = cvss_scores_updated_dt_lte.isoformat()

    params["cvss_scores__updated_dt__lte"] = json_cvss_scores_updated_dt_lte

    json_cvss_scores_uuid: Union[Unset, str] = UNSET
    if not isinstance(cvss_scores_uuid, Unset):
        json_cvss_scores_uuid = str(cvss_scores_uuid)

    params["cvss_scores__uuid"] = json_cvss_scores_uuid

    params["cvss_scores__vector"] = cvss_scores_vector

    params["embargoed"] = embargoed

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    json_flaw_components: Union[Unset, list[str]] = UNSET
    if not isinstance(flaw_components, Unset):
        json_flaw_components = flaw_components

    params["flaw__components"] = json_flaw_components

    json_flaw_created_dt: Union[Unset, str] = UNSET
    if not isinstance(flaw_created_dt, Unset):
        json_flaw_created_dt = flaw_created_dt.isoformat()

    params["flaw__created_dt"] = json_flaw_created_dt

    json_flaw_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(flaw_created_dt_date, Unset):
        json_flaw_created_dt_date = flaw_created_dt_date.isoformat()

    params["flaw__created_dt__date"] = json_flaw_created_dt_date

    json_flaw_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(flaw_created_dt_date_gte, Unset):
        json_flaw_created_dt_date_gte = flaw_created_dt_date_gte.isoformat()

    params["flaw__created_dt__date__gte"] = json_flaw_created_dt_date_gte

    json_flaw_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(flaw_created_dt_date_lte, Unset):
        json_flaw_created_dt_date_lte = flaw_created_dt_date_lte.isoformat()

    params["flaw__created_dt__date__lte"] = json_flaw_created_dt_date_lte

    json_flaw_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(flaw_created_dt_gt, Unset):
        json_flaw_created_dt_gt = flaw_created_dt_gt.isoformat()

    params["flaw__created_dt__gt"] = json_flaw_created_dt_gt

    json_flaw_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(flaw_created_dt_gte, Unset):
        json_flaw_created_dt_gte = flaw_created_dt_gte.isoformat()

    params["flaw__created_dt__gte"] = json_flaw_created_dt_gte

    json_flaw_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(flaw_created_dt_lt, Unset):
        json_flaw_created_dt_lt = flaw_created_dt_lt.isoformat()

    params["flaw__created_dt__lt"] = json_flaw_created_dt_lt

    json_flaw_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(flaw_created_dt_lte, Unset):
        json_flaw_created_dt_lte = flaw_created_dt_lte.isoformat()

    params["flaw__created_dt__lte"] = json_flaw_created_dt_lte

    params["flaw__cve_id"] = flaw_cve_id

    params["flaw__cwe_id"] = flaw_cwe_id

    params["flaw__embargoed"] = flaw_embargoed

    json_flaw_impact: Union[Unset, str] = UNSET
    if not isinstance(flaw_impact, Unset):
        json_flaw_impact = OsidbApiV1AffectsListFlawImpact(flaw_impact).value

    params["flaw__impact"] = json_flaw_impact

    json_flaw_reported_dt: Union[Unset, str] = UNSET
    if not isinstance(flaw_reported_dt, Unset):
        json_flaw_reported_dt = flaw_reported_dt.isoformat()

    params["flaw__reported_dt"] = json_flaw_reported_dt

    json_flaw_reported_dt_date: Union[Unset, str] = UNSET
    if not isinstance(flaw_reported_dt_date, Unset):
        json_flaw_reported_dt_date = flaw_reported_dt_date.isoformat()

    params["flaw__reported_dt__date"] = json_flaw_reported_dt_date

    json_flaw_reported_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(flaw_reported_dt_date_gte, Unset):
        json_flaw_reported_dt_date_gte = flaw_reported_dt_date_gte.isoformat()

    params["flaw__reported_dt__date__gte"] = json_flaw_reported_dt_date_gte

    json_flaw_reported_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(flaw_reported_dt_date_lte, Unset):
        json_flaw_reported_dt_date_lte = flaw_reported_dt_date_lte.isoformat()

    params["flaw__reported_dt__date__lte"] = json_flaw_reported_dt_date_lte

    json_flaw_reported_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(flaw_reported_dt_gt, Unset):
        json_flaw_reported_dt_gt = flaw_reported_dt_gt.isoformat()

    params["flaw__reported_dt__gt"] = json_flaw_reported_dt_gt

    json_flaw_reported_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(flaw_reported_dt_gte, Unset):
        json_flaw_reported_dt_gte = flaw_reported_dt_gte.isoformat()

    params["flaw__reported_dt__gte"] = json_flaw_reported_dt_gte

    json_flaw_reported_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(flaw_reported_dt_lt, Unset):
        json_flaw_reported_dt_lt = flaw_reported_dt_lt.isoformat()

    params["flaw__reported_dt__lt"] = json_flaw_reported_dt_lt

    json_flaw_reported_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(flaw_reported_dt_lte, Unset):
        json_flaw_reported_dt_lte = flaw_reported_dt_lte.isoformat()

    params["flaw__reported_dt__lte"] = json_flaw_reported_dt_lte

    json_flaw_source: Union[Unset, str] = UNSET
    if not isinstance(flaw_source, Unset):
        json_flaw_source = OsidbApiV1AffectsListFlawSource(flaw_source).value

    params["flaw__source"] = json_flaw_source

    json_flaw_unembargo_dt: Union[Unset, str] = UNSET
    if not isinstance(flaw_unembargo_dt, Unset):
        json_flaw_unembargo_dt = flaw_unembargo_dt.isoformat()

    params["flaw__unembargo_dt"] = json_flaw_unembargo_dt

    json_flaw_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(flaw_updated_dt, Unset):
        json_flaw_updated_dt = flaw_updated_dt.isoformat()

    params["flaw__updated_dt"] = json_flaw_updated_dt

    json_flaw_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(flaw_updated_dt_date, Unset):
        json_flaw_updated_dt_date = flaw_updated_dt_date.isoformat()

    params["flaw__updated_dt__date"] = json_flaw_updated_dt_date

    json_flaw_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(flaw_updated_dt_date_gte, Unset):
        json_flaw_updated_dt_date_gte = flaw_updated_dt_date_gte.isoformat()

    params["flaw__updated_dt__date__gte"] = json_flaw_updated_dt_date_gte

    json_flaw_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(flaw_updated_dt_date_lte, Unset):
        json_flaw_updated_dt_date_lte = flaw_updated_dt_date_lte.isoformat()

    params["flaw__updated_dt__date__lte"] = json_flaw_updated_dt_date_lte

    json_flaw_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(flaw_updated_dt_gt, Unset):
        json_flaw_updated_dt_gt = flaw_updated_dt_gt.isoformat()

    params["flaw__updated_dt__gt"] = json_flaw_updated_dt_gt

    json_flaw_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(flaw_updated_dt_gte, Unset):
        json_flaw_updated_dt_gte = flaw_updated_dt_gte.isoformat()

    params["flaw__updated_dt__gte"] = json_flaw_updated_dt_gte

    json_flaw_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(flaw_updated_dt_lt, Unset):
        json_flaw_updated_dt_lt = flaw_updated_dt_lt.isoformat()

    params["flaw__updated_dt__lt"] = json_flaw_updated_dt_lt

    json_flaw_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(flaw_updated_dt_lte, Unset):
        json_flaw_updated_dt_lte = flaw_updated_dt_lte.isoformat()

    params["flaw__updated_dt__lte"] = json_flaw_updated_dt_lte

    json_flaw_uuid: Union[Unset, str] = UNSET
    if not isinstance(flaw_uuid, Unset):
        json_flaw_uuid = str(flaw_uuid)

    params["flaw__uuid"] = json_flaw_uuid

    json_impact: Union[Unset, str] = UNSET
    if not isinstance(impact, Unset):
        json_impact = OsidbApiV1AffectsListImpact(impact).value

    params["impact"] = json_impact

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
                order_item = OsidbApiV1AffectsListOrderItem(order_item_data).value

            json_order.append(order_item)

    params["order"] = json_order

    params["ps_component"] = ps_component

    params["ps_module"] = ps_module

    json_resolution: Union[Unset, str] = UNSET
    if not isinstance(resolution, Unset):
        json_resolution = OsidbApiV1AffectsListResolution(resolution).value

    params["resolution"] = json_resolution

    json_trackers_created_dt: Union[Unset, str] = UNSET
    if not isinstance(trackers_created_dt, Unset):
        json_trackers_created_dt = trackers_created_dt.isoformat()

    params["trackers__created_dt"] = json_trackers_created_dt

    json_trackers_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(trackers_created_dt_date, Unset):
        json_trackers_created_dt_date = trackers_created_dt_date.isoformat()

    params["trackers__created_dt__date"] = json_trackers_created_dt_date

    json_trackers_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(trackers_created_dt_date_gte, Unset):
        json_trackers_created_dt_date_gte = trackers_created_dt_date_gte.isoformat()

    params["trackers__created_dt__date__gte"] = json_trackers_created_dt_date_gte

    json_trackers_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(trackers_created_dt_date_lte, Unset):
        json_trackers_created_dt_date_lte = trackers_created_dt_date_lte.isoformat()

    params["trackers__created_dt__date__lte"] = json_trackers_created_dt_date_lte

    json_trackers_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(trackers_created_dt_gt, Unset):
        json_trackers_created_dt_gt = trackers_created_dt_gt.isoformat()

    params["trackers__created_dt__gt"] = json_trackers_created_dt_gt

    json_trackers_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(trackers_created_dt_gte, Unset):
        json_trackers_created_dt_gte = trackers_created_dt_gte.isoformat()

    params["trackers__created_dt__gte"] = json_trackers_created_dt_gte

    json_trackers_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(trackers_created_dt_lt, Unset):
        json_trackers_created_dt_lt = trackers_created_dt_lt.isoformat()

    params["trackers__created_dt__lt"] = json_trackers_created_dt_lt

    json_trackers_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(trackers_created_dt_lte, Unset):
        json_trackers_created_dt_lte = trackers_created_dt_lte.isoformat()

    params["trackers__created_dt__lte"] = json_trackers_created_dt_lte

    params["trackers__embargoed"] = trackers_embargoed

    params["trackers__external_system_id"] = trackers_external_system_id

    params["trackers__ps_update_stream"] = trackers_ps_update_stream

    params["trackers__resolution"] = trackers_resolution

    params["trackers__status"] = trackers_status

    json_trackers_type: Union[Unset, str] = UNSET
    if not isinstance(trackers_type, Unset):
        json_trackers_type = OsidbApiV1AffectsListTrackersType(trackers_type).value

    params["trackers__type"] = json_trackers_type

    json_trackers_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(trackers_updated_dt, Unset):
        json_trackers_updated_dt = trackers_updated_dt.isoformat()

    params["trackers__updated_dt"] = json_trackers_updated_dt

    json_trackers_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(trackers_updated_dt_date, Unset):
        json_trackers_updated_dt_date = trackers_updated_dt_date.isoformat()

    params["trackers__updated_dt__date"] = json_trackers_updated_dt_date

    json_trackers_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(trackers_updated_dt_date_gte, Unset):
        json_trackers_updated_dt_date_gte = trackers_updated_dt_date_gte.isoformat()

    params["trackers__updated_dt__date__gte"] = json_trackers_updated_dt_date_gte

    json_trackers_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(trackers_updated_dt_date_lte, Unset):
        json_trackers_updated_dt_date_lte = trackers_updated_dt_date_lte.isoformat()

    params["trackers__updated_dt__date__lte"] = json_trackers_updated_dt_date_lte

    json_trackers_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(trackers_updated_dt_gt, Unset):
        json_trackers_updated_dt_gt = trackers_updated_dt_gt.isoformat()

    params["trackers__updated_dt__gt"] = json_trackers_updated_dt_gt

    json_trackers_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(trackers_updated_dt_gte, Unset):
        json_trackers_updated_dt_gte = trackers_updated_dt_gte.isoformat()

    params["trackers__updated_dt__gte"] = json_trackers_updated_dt_gte

    json_trackers_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(trackers_updated_dt_lt, Unset):
        json_trackers_updated_dt_lt = trackers_updated_dt_lt.isoformat()

    params["trackers__updated_dt__lt"] = json_trackers_updated_dt_lt

    json_trackers_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(trackers_updated_dt_lte, Unset):
        json_trackers_updated_dt_lte = trackers_updated_dt_lte.isoformat()

    params["trackers__updated_dt__lte"] = json_trackers_updated_dt_lte

    json_trackers_uuid: Union[Unset, str] = UNSET
    if not isinstance(trackers_uuid, Unset):
        json_trackers_uuid = str(trackers_uuid)

    params["trackers__uuid"] = json_trackers_uuid

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
        "url": f"{client.base_url}/osidb/api/v1/affects",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1AffectsListResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1AffectsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AffectsListResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1AffectsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    affectedness: Union[Unset, OsidbApiV1AffectsListAffectedness] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_comment: Union[Unset, str] = UNSET,
    cvss_scores_created_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, str] = UNSET,
    cvss_scores_issuer: Union[Unset, OsidbApiV1AffectsListCvssScoresIssuer] = UNSET,
    cvss_scores_score: Union[Unset, float] = UNSET,
    cvss_scores_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_uuid: Union[Unset, UUID] = UNSET,
    cvss_scores_vector: Union[Unset, str] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_components: Union[Unset, list[str]] = UNSET,
    flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, str] = UNSET,
    flaw_cwe_id: Union[Unset, str] = UNSET,
    flaw_embargoed: Union[Unset, bool] = UNSET,
    flaw_impact: Union[Unset, OsidbApiV1AffectsListFlawImpact] = UNSET,
    flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, OsidbApiV1AffectsListFlawSource] = UNSET,
    flaw_unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_uuid: Union[Unset, UUID] = UNSET,
    impact: Union[Unset, OsidbApiV1AffectsListImpact] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, str] = UNSET,
    ps_module: Union[Unset, str] = UNSET,
    resolution: Union[Unset, OsidbApiV1AffectsListResolution] = UNSET,
    trackers_created_dt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_date: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    trackers_embargoed: Union[Unset, bool] = UNSET,
    trackers_external_system_id: Union[Unset, str] = UNSET,
    trackers_ps_update_stream: Union[Unset, str] = UNSET,
    trackers_resolution: Union[Unset, str] = UNSET,
    trackers_status: Union[Unset, str] = UNSET,
    trackers_type: Union[Unset, OsidbApiV1AffectsListTrackersType] = UNSET,
    trackers_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    trackers_uuid: Union[Unset, UUID] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[OsidbApiV1AffectsListResponse200]:
    """
    Args:
        affectedness (Union[Unset, OsidbApiV1AffectsListAffectedness]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_comment (Union[Unset, str]):
        cvss_scores_created_dt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_date (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_cvss_version (Union[Unset, str]):
        cvss_scores_issuer (Union[Unset, OsidbApiV1AffectsListCvssScoresIssuer]):
        cvss_scores_score (Union[Unset, float]):
        cvss_scores_updated_dt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_date (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_uuid (Union[Unset, UUID]):
        cvss_scores_vector (Union[Unset, str]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_components (Union[Unset, list[str]]):
        flaw_created_dt (Union[Unset, datetime.datetime]):
        flaw_created_dt_date (Union[Unset, datetime.date]):
        flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_cve_id (Union[Unset, str]):
        flaw_cwe_id (Union[Unset, str]):
        flaw_embargoed (Union[Unset, bool]):
        flaw_impact (Union[Unset, OsidbApiV1AffectsListFlawImpact]):
        flaw_reported_dt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_date (Union[Unset, datetime.date]):
        flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        flaw_source (Union[Unset, OsidbApiV1AffectsListFlawSource]):
        flaw_unembargo_dt (Union[Unset, datetime.datetime]):
        flaw_updated_dt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_date (Union[Unset, datetime.date]):
        flaw_updated_dt_date_gte (Union[Unset, datetime.date]):
        flaw_updated_dt_date_lte (Union[Unset, datetime.date]):
        flaw_updated_dt_gt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_gte (Union[Unset, datetime.datetime]):
        flaw_updated_dt_lt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_lte (Union[Unset, datetime.datetime]):
        flaw_uuid (Union[Unset, UUID]):
        impact (Union[Unset, OsidbApiV1AffectsListImpact]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1AffectsListOrderItem]]):
        ps_component (Union[Unset, str]):
        ps_module (Union[Unset, str]):
        resolution (Union[Unset, OsidbApiV1AffectsListResolution]):
        trackers_created_dt (Union[Unset, datetime.datetime]):
        trackers_created_dt_date (Union[Unset, datetime.date]):
        trackers_created_dt_date_gte (Union[Unset, datetime.date]):
        trackers_created_dt_date_lte (Union[Unset, datetime.date]):
        trackers_created_dt_gt (Union[Unset, datetime.datetime]):
        trackers_created_dt_gte (Union[Unset, datetime.datetime]):
        trackers_created_dt_lt (Union[Unset, datetime.datetime]):
        trackers_created_dt_lte (Union[Unset, datetime.datetime]):
        trackers_embargoed (Union[Unset, bool]):
        trackers_external_system_id (Union[Unset, str]):
        trackers_ps_update_stream (Union[Unset, str]):
        trackers_resolution (Union[Unset, str]):
        trackers_status (Union[Unset, str]):
        trackers_type (Union[Unset, OsidbApiV1AffectsListTrackersType]):
        trackers_updated_dt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_date (Union[Unset, datetime.date]):
        trackers_updated_dt_date_gte (Union[Unset, datetime.date]):
        trackers_updated_dt_date_lte (Union[Unset, datetime.date]):
        trackers_updated_dt_gt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_gte (Union[Unset, datetime.datetime]):
        trackers_updated_dt_lt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_lte (Union[Unset, datetime.datetime]):
        trackers_uuid (Union[Unset, UUID]):
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
        Response[OsidbApiV1AffectsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        affectedness=affectedness,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cvss_scores_comment=cvss_scores_comment,
        cvss_scores_created_dt=cvss_scores_created_dt,
        cvss_scores_created_dt_date=cvss_scores_created_dt_date,
        cvss_scores_created_dt_date_gte=cvss_scores_created_dt_date_gte,
        cvss_scores_created_dt_date_lte=cvss_scores_created_dt_date_lte,
        cvss_scores_created_dt_gt=cvss_scores_created_dt_gt,
        cvss_scores_created_dt_gte=cvss_scores_created_dt_gte,
        cvss_scores_created_dt_lt=cvss_scores_created_dt_lt,
        cvss_scores_created_dt_lte=cvss_scores_created_dt_lte,
        cvss_scores_cvss_version=cvss_scores_cvss_version,
        cvss_scores_issuer=cvss_scores_issuer,
        cvss_scores_score=cvss_scores_score,
        cvss_scores_updated_dt=cvss_scores_updated_dt,
        cvss_scores_updated_dt_date=cvss_scores_updated_dt_date,
        cvss_scores_updated_dt_date_gte=cvss_scores_updated_dt_date_gte,
        cvss_scores_updated_dt_date_lte=cvss_scores_updated_dt_date_lte,
        cvss_scores_updated_dt_gt=cvss_scores_updated_dt_gt,
        cvss_scores_updated_dt_gte=cvss_scores_updated_dt_gte,
        cvss_scores_updated_dt_lt=cvss_scores_updated_dt_lt,
        cvss_scores_updated_dt_lte=cvss_scores_updated_dt_lte,
        cvss_scores_uuid=cvss_scores_uuid,
        cvss_scores_vector=cvss_scores_vector,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        flaw_components=flaw_components,
        flaw_created_dt=flaw_created_dt,
        flaw_created_dt_date=flaw_created_dt_date,
        flaw_created_dt_date_gte=flaw_created_dt_date_gte,
        flaw_created_dt_date_lte=flaw_created_dt_date_lte,
        flaw_created_dt_gt=flaw_created_dt_gt,
        flaw_created_dt_gte=flaw_created_dt_gte,
        flaw_created_dt_lt=flaw_created_dt_lt,
        flaw_created_dt_lte=flaw_created_dt_lte,
        flaw_cve_id=flaw_cve_id,
        flaw_cwe_id=flaw_cwe_id,
        flaw_embargoed=flaw_embargoed,
        flaw_impact=flaw_impact,
        flaw_reported_dt=flaw_reported_dt,
        flaw_reported_dt_date=flaw_reported_dt_date,
        flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
        flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
        flaw_reported_dt_gt=flaw_reported_dt_gt,
        flaw_reported_dt_gte=flaw_reported_dt_gte,
        flaw_reported_dt_lt=flaw_reported_dt_lt,
        flaw_reported_dt_lte=flaw_reported_dt_lte,
        flaw_source=flaw_source,
        flaw_unembargo_dt=flaw_unembargo_dt,
        flaw_updated_dt=flaw_updated_dt,
        flaw_updated_dt_date=flaw_updated_dt_date,
        flaw_updated_dt_date_gte=flaw_updated_dt_date_gte,
        flaw_updated_dt_date_lte=flaw_updated_dt_date_lte,
        flaw_updated_dt_gt=flaw_updated_dt_gt,
        flaw_updated_dt_gte=flaw_updated_dt_gte,
        flaw_updated_dt_lt=flaw_updated_dt_lt,
        flaw_updated_dt_lte=flaw_updated_dt_lte,
        flaw_uuid=flaw_uuid,
        impact=impact,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        order=order,
        ps_component=ps_component,
        ps_module=ps_module,
        resolution=resolution,
        trackers_created_dt=trackers_created_dt,
        trackers_created_dt_date=trackers_created_dt_date,
        trackers_created_dt_date_gte=trackers_created_dt_date_gte,
        trackers_created_dt_date_lte=trackers_created_dt_date_lte,
        trackers_created_dt_gt=trackers_created_dt_gt,
        trackers_created_dt_gte=trackers_created_dt_gte,
        trackers_created_dt_lt=trackers_created_dt_lt,
        trackers_created_dt_lte=trackers_created_dt_lte,
        trackers_embargoed=trackers_embargoed,
        trackers_external_system_id=trackers_external_system_id,
        trackers_ps_update_stream=trackers_ps_update_stream,
        trackers_resolution=trackers_resolution,
        trackers_status=trackers_status,
        trackers_type=trackers_type,
        trackers_updated_dt=trackers_updated_dt,
        trackers_updated_dt_date=trackers_updated_dt_date,
        trackers_updated_dt_date_gte=trackers_updated_dt_date_gte,
        trackers_updated_dt_date_lte=trackers_updated_dt_date_lte,
        trackers_updated_dt_gt=trackers_updated_dt_gt,
        trackers_updated_dt_gte=trackers_updated_dt_gte,
        trackers_updated_dt_lt=trackers_updated_dt_lt,
        trackers_updated_dt_lte=trackers_updated_dt_lte,
        trackers_uuid=trackers_uuid,
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
    affectedness: Union[Unset, OsidbApiV1AffectsListAffectedness] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_comment: Union[Unset, str] = UNSET,
    cvss_scores_created_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, str] = UNSET,
    cvss_scores_issuer: Union[Unset, OsidbApiV1AffectsListCvssScoresIssuer] = UNSET,
    cvss_scores_score: Union[Unset, float] = UNSET,
    cvss_scores_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_uuid: Union[Unset, UUID] = UNSET,
    cvss_scores_vector: Union[Unset, str] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_components: Union[Unset, list[str]] = UNSET,
    flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, str] = UNSET,
    flaw_cwe_id: Union[Unset, str] = UNSET,
    flaw_embargoed: Union[Unset, bool] = UNSET,
    flaw_impact: Union[Unset, OsidbApiV1AffectsListFlawImpact] = UNSET,
    flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, OsidbApiV1AffectsListFlawSource] = UNSET,
    flaw_unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_uuid: Union[Unset, UUID] = UNSET,
    impact: Union[Unset, OsidbApiV1AffectsListImpact] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, str] = UNSET,
    ps_module: Union[Unset, str] = UNSET,
    resolution: Union[Unset, OsidbApiV1AffectsListResolution] = UNSET,
    trackers_created_dt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_date: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    trackers_embargoed: Union[Unset, bool] = UNSET,
    trackers_external_system_id: Union[Unset, str] = UNSET,
    trackers_ps_update_stream: Union[Unset, str] = UNSET,
    trackers_resolution: Union[Unset, str] = UNSET,
    trackers_status: Union[Unset, str] = UNSET,
    trackers_type: Union[Unset, OsidbApiV1AffectsListTrackersType] = UNSET,
    trackers_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    trackers_uuid: Union[Unset, UUID] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[OsidbApiV1AffectsListResponse200]:
    """
    Args:
        affectedness (Union[Unset, OsidbApiV1AffectsListAffectedness]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_comment (Union[Unset, str]):
        cvss_scores_created_dt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_date (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_cvss_version (Union[Unset, str]):
        cvss_scores_issuer (Union[Unset, OsidbApiV1AffectsListCvssScoresIssuer]):
        cvss_scores_score (Union[Unset, float]):
        cvss_scores_updated_dt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_date (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_uuid (Union[Unset, UUID]):
        cvss_scores_vector (Union[Unset, str]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_components (Union[Unset, list[str]]):
        flaw_created_dt (Union[Unset, datetime.datetime]):
        flaw_created_dt_date (Union[Unset, datetime.date]):
        flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_cve_id (Union[Unset, str]):
        flaw_cwe_id (Union[Unset, str]):
        flaw_embargoed (Union[Unset, bool]):
        flaw_impact (Union[Unset, OsidbApiV1AffectsListFlawImpact]):
        flaw_reported_dt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_date (Union[Unset, datetime.date]):
        flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        flaw_source (Union[Unset, OsidbApiV1AffectsListFlawSource]):
        flaw_unembargo_dt (Union[Unset, datetime.datetime]):
        flaw_updated_dt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_date (Union[Unset, datetime.date]):
        flaw_updated_dt_date_gte (Union[Unset, datetime.date]):
        flaw_updated_dt_date_lte (Union[Unset, datetime.date]):
        flaw_updated_dt_gt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_gte (Union[Unset, datetime.datetime]):
        flaw_updated_dt_lt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_lte (Union[Unset, datetime.datetime]):
        flaw_uuid (Union[Unset, UUID]):
        impact (Union[Unset, OsidbApiV1AffectsListImpact]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1AffectsListOrderItem]]):
        ps_component (Union[Unset, str]):
        ps_module (Union[Unset, str]):
        resolution (Union[Unset, OsidbApiV1AffectsListResolution]):
        trackers_created_dt (Union[Unset, datetime.datetime]):
        trackers_created_dt_date (Union[Unset, datetime.date]):
        trackers_created_dt_date_gte (Union[Unset, datetime.date]):
        trackers_created_dt_date_lte (Union[Unset, datetime.date]):
        trackers_created_dt_gt (Union[Unset, datetime.datetime]):
        trackers_created_dt_gte (Union[Unset, datetime.datetime]):
        trackers_created_dt_lt (Union[Unset, datetime.datetime]):
        trackers_created_dt_lte (Union[Unset, datetime.datetime]):
        trackers_embargoed (Union[Unset, bool]):
        trackers_external_system_id (Union[Unset, str]):
        trackers_ps_update_stream (Union[Unset, str]):
        trackers_resolution (Union[Unset, str]):
        trackers_status (Union[Unset, str]):
        trackers_type (Union[Unset, OsidbApiV1AffectsListTrackersType]):
        trackers_updated_dt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_date (Union[Unset, datetime.date]):
        trackers_updated_dt_date_gte (Union[Unset, datetime.date]):
        trackers_updated_dt_date_lte (Union[Unset, datetime.date]):
        trackers_updated_dt_gt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_gte (Union[Unset, datetime.datetime]):
        trackers_updated_dt_lt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_lte (Union[Unset, datetime.datetime]):
        trackers_uuid (Union[Unset, UUID]):
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
        OsidbApiV1AffectsListResponse200
    """

    return sync_detailed(
        client=client,
        affectedness=affectedness,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cvss_scores_comment=cvss_scores_comment,
        cvss_scores_created_dt=cvss_scores_created_dt,
        cvss_scores_created_dt_date=cvss_scores_created_dt_date,
        cvss_scores_created_dt_date_gte=cvss_scores_created_dt_date_gte,
        cvss_scores_created_dt_date_lte=cvss_scores_created_dt_date_lte,
        cvss_scores_created_dt_gt=cvss_scores_created_dt_gt,
        cvss_scores_created_dt_gte=cvss_scores_created_dt_gte,
        cvss_scores_created_dt_lt=cvss_scores_created_dt_lt,
        cvss_scores_created_dt_lte=cvss_scores_created_dt_lte,
        cvss_scores_cvss_version=cvss_scores_cvss_version,
        cvss_scores_issuer=cvss_scores_issuer,
        cvss_scores_score=cvss_scores_score,
        cvss_scores_updated_dt=cvss_scores_updated_dt,
        cvss_scores_updated_dt_date=cvss_scores_updated_dt_date,
        cvss_scores_updated_dt_date_gte=cvss_scores_updated_dt_date_gte,
        cvss_scores_updated_dt_date_lte=cvss_scores_updated_dt_date_lte,
        cvss_scores_updated_dt_gt=cvss_scores_updated_dt_gt,
        cvss_scores_updated_dt_gte=cvss_scores_updated_dt_gte,
        cvss_scores_updated_dt_lt=cvss_scores_updated_dt_lt,
        cvss_scores_updated_dt_lte=cvss_scores_updated_dt_lte,
        cvss_scores_uuid=cvss_scores_uuid,
        cvss_scores_vector=cvss_scores_vector,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        flaw_components=flaw_components,
        flaw_created_dt=flaw_created_dt,
        flaw_created_dt_date=flaw_created_dt_date,
        flaw_created_dt_date_gte=flaw_created_dt_date_gte,
        flaw_created_dt_date_lte=flaw_created_dt_date_lte,
        flaw_created_dt_gt=flaw_created_dt_gt,
        flaw_created_dt_gte=flaw_created_dt_gte,
        flaw_created_dt_lt=flaw_created_dt_lt,
        flaw_created_dt_lte=flaw_created_dt_lte,
        flaw_cve_id=flaw_cve_id,
        flaw_cwe_id=flaw_cwe_id,
        flaw_embargoed=flaw_embargoed,
        flaw_impact=flaw_impact,
        flaw_reported_dt=flaw_reported_dt,
        flaw_reported_dt_date=flaw_reported_dt_date,
        flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
        flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
        flaw_reported_dt_gt=flaw_reported_dt_gt,
        flaw_reported_dt_gte=flaw_reported_dt_gte,
        flaw_reported_dt_lt=flaw_reported_dt_lt,
        flaw_reported_dt_lte=flaw_reported_dt_lte,
        flaw_source=flaw_source,
        flaw_unembargo_dt=flaw_unembargo_dt,
        flaw_updated_dt=flaw_updated_dt,
        flaw_updated_dt_date=flaw_updated_dt_date,
        flaw_updated_dt_date_gte=flaw_updated_dt_date_gte,
        flaw_updated_dt_date_lte=flaw_updated_dt_date_lte,
        flaw_updated_dt_gt=flaw_updated_dt_gt,
        flaw_updated_dt_gte=flaw_updated_dt_gte,
        flaw_updated_dt_lt=flaw_updated_dt_lt,
        flaw_updated_dt_lte=flaw_updated_dt_lte,
        flaw_uuid=flaw_uuid,
        impact=impact,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        order=order,
        ps_component=ps_component,
        ps_module=ps_module,
        resolution=resolution,
        trackers_created_dt=trackers_created_dt,
        trackers_created_dt_date=trackers_created_dt_date,
        trackers_created_dt_date_gte=trackers_created_dt_date_gte,
        trackers_created_dt_date_lte=trackers_created_dt_date_lte,
        trackers_created_dt_gt=trackers_created_dt_gt,
        trackers_created_dt_gte=trackers_created_dt_gte,
        trackers_created_dt_lt=trackers_created_dt_lt,
        trackers_created_dt_lte=trackers_created_dt_lte,
        trackers_embargoed=trackers_embargoed,
        trackers_external_system_id=trackers_external_system_id,
        trackers_ps_update_stream=trackers_ps_update_stream,
        trackers_resolution=trackers_resolution,
        trackers_status=trackers_status,
        trackers_type=trackers_type,
        trackers_updated_dt=trackers_updated_dt,
        trackers_updated_dt_date=trackers_updated_dt_date,
        trackers_updated_dt_date_gte=trackers_updated_dt_date_gte,
        trackers_updated_dt_date_lte=trackers_updated_dt_date_lte,
        trackers_updated_dt_gt=trackers_updated_dt_gt,
        trackers_updated_dt_gte=trackers_updated_dt_gte,
        trackers_updated_dt_lt=trackers_updated_dt_lt,
        trackers_updated_dt_lte=trackers_updated_dt_lte,
        trackers_uuid=trackers_uuid,
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
    affectedness: Union[Unset, OsidbApiV1AffectsListAffectedness] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_comment: Union[Unset, str] = UNSET,
    cvss_scores_created_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, str] = UNSET,
    cvss_scores_issuer: Union[Unset, OsidbApiV1AffectsListCvssScoresIssuer] = UNSET,
    cvss_scores_score: Union[Unset, float] = UNSET,
    cvss_scores_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_uuid: Union[Unset, UUID] = UNSET,
    cvss_scores_vector: Union[Unset, str] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_components: Union[Unset, list[str]] = UNSET,
    flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, str] = UNSET,
    flaw_cwe_id: Union[Unset, str] = UNSET,
    flaw_embargoed: Union[Unset, bool] = UNSET,
    flaw_impact: Union[Unset, OsidbApiV1AffectsListFlawImpact] = UNSET,
    flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, OsidbApiV1AffectsListFlawSource] = UNSET,
    flaw_unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_uuid: Union[Unset, UUID] = UNSET,
    impact: Union[Unset, OsidbApiV1AffectsListImpact] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, str] = UNSET,
    ps_module: Union[Unset, str] = UNSET,
    resolution: Union[Unset, OsidbApiV1AffectsListResolution] = UNSET,
    trackers_created_dt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_date: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    trackers_embargoed: Union[Unset, bool] = UNSET,
    trackers_external_system_id: Union[Unset, str] = UNSET,
    trackers_ps_update_stream: Union[Unset, str] = UNSET,
    trackers_resolution: Union[Unset, str] = UNSET,
    trackers_status: Union[Unset, str] = UNSET,
    trackers_type: Union[Unset, OsidbApiV1AffectsListTrackersType] = UNSET,
    trackers_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    trackers_uuid: Union[Unset, UUID] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Response[OsidbApiV1AffectsListResponse200]:
    """
    Args:
        affectedness (Union[Unset, OsidbApiV1AffectsListAffectedness]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_comment (Union[Unset, str]):
        cvss_scores_created_dt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_date (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_cvss_version (Union[Unset, str]):
        cvss_scores_issuer (Union[Unset, OsidbApiV1AffectsListCvssScoresIssuer]):
        cvss_scores_score (Union[Unset, float]):
        cvss_scores_updated_dt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_date (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_uuid (Union[Unset, UUID]):
        cvss_scores_vector (Union[Unset, str]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_components (Union[Unset, list[str]]):
        flaw_created_dt (Union[Unset, datetime.datetime]):
        flaw_created_dt_date (Union[Unset, datetime.date]):
        flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_cve_id (Union[Unset, str]):
        flaw_cwe_id (Union[Unset, str]):
        flaw_embargoed (Union[Unset, bool]):
        flaw_impact (Union[Unset, OsidbApiV1AffectsListFlawImpact]):
        flaw_reported_dt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_date (Union[Unset, datetime.date]):
        flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        flaw_source (Union[Unset, OsidbApiV1AffectsListFlawSource]):
        flaw_unembargo_dt (Union[Unset, datetime.datetime]):
        flaw_updated_dt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_date (Union[Unset, datetime.date]):
        flaw_updated_dt_date_gte (Union[Unset, datetime.date]):
        flaw_updated_dt_date_lte (Union[Unset, datetime.date]):
        flaw_updated_dt_gt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_gte (Union[Unset, datetime.datetime]):
        flaw_updated_dt_lt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_lte (Union[Unset, datetime.datetime]):
        flaw_uuid (Union[Unset, UUID]):
        impact (Union[Unset, OsidbApiV1AffectsListImpact]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1AffectsListOrderItem]]):
        ps_component (Union[Unset, str]):
        ps_module (Union[Unset, str]):
        resolution (Union[Unset, OsidbApiV1AffectsListResolution]):
        trackers_created_dt (Union[Unset, datetime.datetime]):
        trackers_created_dt_date (Union[Unset, datetime.date]):
        trackers_created_dt_date_gte (Union[Unset, datetime.date]):
        trackers_created_dt_date_lte (Union[Unset, datetime.date]):
        trackers_created_dt_gt (Union[Unset, datetime.datetime]):
        trackers_created_dt_gte (Union[Unset, datetime.datetime]):
        trackers_created_dt_lt (Union[Unset, datetime.datetime]):
        trackers_created_dt_lte (Union[Unset, datetime.datetime]):
        trackers_embargoed (Union[Unset, bool]):
        trackers_external_system_id (Union[Unset, str]):
        trackers_ps_update_stream (Union[Unset, str]):
        trackers_resolution (Union[Unset, str]):
        trackers_status (Union[Unset, str]):
        trackers_type (Union[Unset, OsidbApiV1AffectsListTrackersType]):
        trackers_updated_dt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_date (Union[Unset, datetime.date]):
        trackers_updated_dt_date_gte (Union[Unset, datetime.date]):
        trackers_updated_dt_date_lte (Union[Unset, datetime.date]):
        trackers_updated_dt_gt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_gte (Union[Unset, datetime.datetime]):
        trackers_updated_dt_lt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_lte (Union[Unset, datetime.datetime]):
        trackers_uuid (Union[Unset, UUID]):
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
        Response[OsidbApiV1AffectsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        affectedness=affectedness,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cvss_scores_comment=cvss_scores_comment,
        cvss_scores_created_dt=cvss_scores_created_dt,
        cvss_scores_created_dt_date=cvss_scores_created_dt_date,
        cvss_scores_created_dt_date_gte=cvss_scores_created_dt_date_gte,
        cvss_scores_created_dt_date_lte=cvss_scores_created_dt_date_lte,
        cvss_scores_created_dt_gt=cvss_scores_created_dt_gt,
        cvss_scores_created_dt_gte=cvss_scores_created_dt_gte,
        cvss_scores_created_dt_lt=cvss_scores_created_dt_lt,
        cvss_scores_created_dt_lte=cvss_scores_created_dt_lte,
        cvss_scores_cvss_version=cvss_scores_cvss_version,
        cvss_scores_issuer=cvss_scores_issuer,
        cvss_scores_score=cvss_scores_score,
        cvss_scores_updated_dt=cvss_scores_updated_dt,
        cvss_scores_updated_dt_date=cvss_scores_updated_dt_date,
        cvss_scores_updated_dt_date_gte=cvss_scores_updated_dt_date_gte,
        cvss_scores_updated_dt_date_lte=cvss_scores_updated_dt_date_lte,
        cvss_scores_updated_dt_gt=cvss_scores_updated_dt_gt,
        cvss_scores_updated_dt_gte=cvss_scores_updated_dt_gte,
        cvss_scores_updated_dt_lt=cvss_scores_updated_dt_lt,
        cvss_scores_updated_dt_lte=cvss_scores_updated_dt_lte,
        cvss_scores_uuid=cvss_scores_uuid,
        cvss_scores_vector=cvss_scores_vector,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        flaw_components=flaw_components,
        flaw_created_dt=flaw_created_dt,
        flaw_created_dt_date=flaw_created_dt_date,
        flaw_created_dt_date_gte=flaw_created_dt_date_gte,
        flaw_created_dt_date_lte=flaw_created_dt_date_lte,
        flaw_created_dt_gt=flaw_created_dt_gt,
        flaw_created_dt_gte=flaw_created_dt_gte,
        flaw_created_dt_lt=flaw_created_dt_lt,
        flaw_created_dt_lte=flaw_created_dt_lte,
        flaw_cve_id=flaw_cve_id,
        flaw_cwe_id=flaw_cwe_id,
        flaw_embargoed=flaw_embargoed,
        flaw_impact=flaw_impact,
        flaw_reported_dt=flaw_reported_dt,
        flaw_reported_dt_date=flaw_reported_dt_date,
        flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
        flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
        flaw_reported_dt_gt=flaw_reported_dt_gt,
        flaw_reported_dt_gte=flaw_reported_dt_gte,
        flaw_reported_dt_lt=flaw_reported_dt_lt,
        flaw_reported_dt_lte=flaw_reported_dt_lte,
        flaw_source=flaw_source,
        flaw_unembargo_dt=flaw_unembargo_dt,
        flaw_updated_dt=flaw_updated_dt,
        flaw_updated_dt_date=flaw_updated_dt_date,
        flaw_updated_dt_date_gte=flaw_updated_dt_date_gte,
        flaw_updated_dt_date_lte=flaw_updated_dt_date_lte,
        flaw_updated_dt_gt=flaw_updated_dt_gt,
        flaw_updated_dt_gte=flaw_updated_dt_gte,
        flaw_updated_dt_lt=flaw_updated_dt_lt,
        flaw_updated_dt_lte=flaw_updated_dt_lte,
        flaw_uuid=flaw_uuid,
        impact=impact,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        order=order,
        ps_component=ps_component,
        ps_module=ps_module,
        resolution=resolution,
        trackers_created_dt=trackers_created_dt,
        trackers_created_dt_date=trackers_created_dt_date,
        trackers_created_dt_date_gte=trackers_created_dt_date_gte,
        trackers_created_dt_date_lte=trackers_created_dt_date_lte,
        trackers_created_dt_gt=trackers_created_dt_gt,
        trackers_created_dt_gte=trackers_created_dt_gte,
        trackers_created_dt_lt=trackers_created_dt_lt,
        trackers_created_dt_lte=trackers_created_dt_lte,
        trackers_embargoed=trackers_embargoed,
        trackers_external_system_id=trackers_external_system_id,
        trackers_ps_update_stream=trackers_ps_update_stream,
        trackers_resolution=trackers_resolution,
        trackers_status=trackers_status,
        trackers_type=trackers_type,
        trackers_updated_dt=trackers_updated_dt,
        trackers_updated_dt_date=trackers_updated_dt_date,
        trackers_updated_dt_date_gte=trackers_updated_dt_date_gte,
        trackers_updated_dt_date_lte=trackers_updated_dt_date_lte,
        trackers_updated_dt_gt=trackers_updated_dt_gt,
        trackers_updated_dt_gte=trackers_updated_dt_gte,
        trackers_updated_dt_lt=trackers_updated_dt_lt,
        trackers_updated_dt_lte=trackers_updated_dt_lte,
        trackers_uuid=trackers_uuid,
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
    affectedness: Union[Unset, OsidbApiV1AffectsListAffectedness] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_comment: Union[Unset, str] = UNSET,
    cvss_scores_created_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, str] = UNSET,
    cvss_scores_issuer: Union[Unset, OsidbApiV1AffectsListCvssScoresIssuer] = UNSET,
    cvss_scores_score: Union[Unset, float] = UNSET,
    cvss_scores_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_uuid: Union[Unset, UUID] = UNSET,
    cvss_scores_vector: Union[Unset, str] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_components: Union[Unset, list[str]] = UNSET,
    flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, str] = UNSET,
    flaw_cwe_id: Union[Unset, str] = UNSET,
    flaw_embargoed: Union[Unset, bool] = UNSET,
    flaw_impact: Union[Unset, OsidbApiV1AffectsListFlawImpact] = UNSET,
    flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, OsidbApiV1AffectsListFlawSource] = UNSET,
    flaw_unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_uuid: Union[Unset, UUID] = UNSET,
    impact: Union[Unset, OsidbApiV1AffectsListImpact] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, str] = UNSET,
    ps_module: Union[Unset, str] = UNSET,
    resolution: Union[Unset, OsidbApiV1AffectsListResolution] = UNSET,
    trackers_created_dt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_date: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    trackers_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    trackers_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    trackers_embargoed: Union[Unset, bool] = UNSET,
    trackers_external_system_id: Union[Unset, str] = UNSET,
    trackers_ps_update_stream: Union[Unset, str] = UNSET,
    trackers_resolution: Union[Unset, str] = UNSET,
    trackers_status: Union[Unset, str] = UNSET,
    trackers_type: Union[Unset, OsidbApiV1AffectsListTrackersType] = UNSET,
    trackers_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    trackers_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    trackers_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    trackers_uuid: Union[Unset, UUID] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
) -> Optional[OsidbApiV1AffectsListResponse200]:
    """
    Args:
        affectedness (Union[Unset, OsidbApiV1AffectsListAffectedness]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_comment (Union[Unset, str]):
        cvss_scores_created_dt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_date (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_cvss_version (Union[Unset, str]):
        cvss_scores_issuer (Union[Unset, OsidbApiV1AffectsListCvssScoresIssuer]):
        cvss_scores_score (Union[Unset, float]):
        cvss_scores_updated_dt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_date (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_updated_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_updated_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_uuid (Union[Unset, UUID]):
        cvss_scores_vector (Union[Unset, str]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_components (Union[Unset, list[str]]):
        flaw_created_dt (Union[Unset, datetime.datetime]):
        flaw_created_dt_date (Union[Unset, datetime.date]):
        flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_cve_id (Union[Unset, str]):
        flaw_cwe_id (Union[Unset, str]):
        flaw_embargoed (Union[Unset, bool]):
        flaw_impact (Union[Unset, OsidbApiV1AffectsListFlawImpact]):
        flaw_reported_dt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_date (Union[Unset, datetime.date]):
        flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        flaw_source (Union[Unset, OsidbApiV1AffectsListFlawSource]):
        flaw_unembargo_dt (Union[Unset, datetime.datetime]):
        flaw_updated_dt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_date (Union[Unset, datetime.date]):
        flaw_updated_dt_date_gte (Union[Unset, datetime.date]):
        flaw_updated_dt_date_lte (Union[Unset, datetime.date]):
        flaw_updated_dt_gt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_gte (Union[Unset, datetime.datetime]):
        flaw_updated_dt_lt (Union[Unset, datetime.datetime]):
        flaw_updated_dt_lte (Union[Unset, datetime.datetime]):
        flaw_uuid (Union[Unset, UUID]):
        impact (Union[Unset, OsidbApiV1AffectsListImpact]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1AffectsListOrderItem]]):
        ps_component (Union[Unset, str]):
        ps_module (Union[Unset, str]):
        resolution (Union[Unset, OsidbApiV1AffectsListResolution]):
        trackers_created_dt (Union[Unset, datetime.datetime]):
        trackers_created_dt_date (Union[Unset, datetime.date]):
        trackers_created_dt_date_gte (Union[Unset, datetime.date]):
        trackers_created_dt_date_lte (Union[Unset, datetime.date]):
        trackers_created_dt_gt (Union[Unset, datetime.datetime]):
        trackers_created_dt_gte (Union[Unset, datetime.datetime]):
        trackers_created_dt_lt (Union[Unset, datetime.datetime]):
        trackers_created_dt_lte (Union[Unset, datetime.datetime]):
        trackers_embargoed (Union[Unset, bool]):
        trackers_external_system_id (Union[Unset, str]):
        trackers_ps_update_stream (Union[Unset, str]):
        trackers_resolution (Union[Unset, str]):
        trackers_status (Union[Unset, str]):
        trackers_type (Union[Unset, OsidbApiV1AffectsListTrackersType]):
        trackers_updated_dt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_date (Union[Unset, datetime.date]):
        trackers_updated_dt_date_gte (Union[Unset, datetime.date]):
        trackers_updated_dt_date_lte (Union[Unset, datetime.date]):
        trackers_updated_dt_gt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_gte (Union[Unset, datetime.datetime]):
        trackers_updated_dt_lt (Union[Unset, datetime.datetime]):
        trackers_updated_dt_lte (Union[Unset, datetime.datetime]):
        trackers_uuid (Union[Unset, UUID]):
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
        OsidbApiV1AffectsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            affectedness=affectedness,
            created_dt=created_dt,
            created_dt_date=created_dt_date,
            created_dt_date_gte=created_dt_date_gte,
            created_dt_date_lte=created_dt_date_lte,
            created_dt_gt=created_dt_gt,
            created_dt_gte=created_dt_gte,
            created_dt_lt=created_dt_lt,
            created_dt_lte=created_dt_lte,
            cvss_scores_comment=cvss_scores_comment,
            cvss_scores_created_dt=cvss_scores_created_dt,
            cvss_scores_created_dt_date=cvss_scores_created_dt_date,
            cvss_scores_created_dt_date_gte=cvss_scores_created_dt_date_gte,
            cvss_scores_created_dt_date_lte=cvss_scores_created_dt_date_lte,
            cvss_scores_created_dt_gt=cvss_scores_created_dt_gt,
            cvss_scores_created_dt_gte=cvss_scores_created_dt_gte,
            cvss_scores_created_dt_lt=cvss_scores_created_dt_lt,
            cvss_scores_created_dt_lte=cvss_scores_created_dt_lte,
            cvss_scores_cvss_version=cvss_scores_cvss_version,
            cvss_scores_issuer=cvss_scores_issuer,
            cvss_scores_score=cvss_scores_score,
            cvss_scores_updated_dt=cvss_scores_updated_dt,
            cvss_scores_updated_dt_date=cvss_scores_updated_dt_date,
            cvss_scores_updated_dt_date_gte=cvss_scores_updated_dt_date_gte,
            cvss_scores_updated_dt_date_lte=cvss_scores_updated_dt_date_lte,
            cvss_scores_updated_dt_gt=cvss_scores_updated_dt_gt,
            cvss_scores_updated_dt_gte=cvss_scores_updated_dt_gte,
            cvss_scores_updated_dt_lt=cvss_scores_updated_dt_lt,
            cvss_scores_updated_dt_lte=cvss_scores_updated_dt_lte,
            cvss_scores_uuid=cvss_scores_uuid,
            cvss_scores_vector=cvss_scores_vector,
            embargoed=embargoed,
            exclude_fields=exclude_fields,
            flaw_components=flaw_components,
            flaw_created_dt=flaw_created_dt,
            flaw_created_dt_date=flaw_created_dt_date,
            flaw_created_dt_date_gte=flaw_created_dt_date_gte,
            flaw_created_dt_date_lte=flaw_created_dt_date_lte,
            flaw_created_dt_gt=flaw_created_dt_gt,
            flaw_created_dt_gte=flaw_created_dt_gte,
            flaw_created_dt_lt=flaw_created_dt_lt,
            flaw_created_dt_lte=flaw_created_dt_lte,
            flaw_cve_id=flaw_cve_id,
            flaw_cwe_id=flaw_cwe_id,
            flaw_embargoed=flaw_embargoed,
            flaw_impact=flaw_impact,
            flaw_reported_dt=flaw_reported_dt,
            flaw_reported_dt_date=flaw_reported_dt_date,
            flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
            flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
            flaw_reported_dt_gt=flaw_reported_dt_gt,
            flaw_reported_dt_gte=flaw_reported_dt_gte,
            flaw_reported_dt_lt=flaw_reported_dt_lt,
            flaw_reported_dt_lte=flaw_reported_dt_lte,
            flaw_source=flaw_source,
            flaw_unembargo_dt=flaw_unembargo_dt,
            flaw_updated_dt=flaw_updated_dt,
            flaw_updated_dt_date=flaw_updated_dt_date,
            flaw_updated_dt_date_gte=flaw_updated_dt_date_gte,
            flaw_updated_dt_date_lte=flaw_updated_dt_date_lte,
            flaw_updated_dt_gt=flaw_updated_dt_gt,
            flaw_updated_dt_gte=flaw_updated_dt_gte,
            flaw_updated_dt_lt=flaw_updated_dt_lt,
            flaw_updated_dt_lte=flaw_updated_dt_lte,
            flaw_uuid=flaw_uuid,
            impact=impact,
            include_fields=include_fields,
            include_meta_attr=include_meta_attr,
            limit=limit,
            offset=offset,
            order=order,
            ps_component=ps_component,
            ps_module=ps_module,
            resolution=resolution,
            trackers_created_dt=trackers_created_dt,
            trackers_created_dt_date=trackers_created_dt_date,
            trackers_created_dt_date_gte=trackers_created_dt_date_gte,
            trackers_created_dt_date_lte=trackers_created_dt_date_lte,
            trackers_created_dt_gt=trackers_created_dt_gt,
            trackers_created_dt_gte=trackers_created_dt_gte,
            trackers_created_dt_lt=trackers_created_dt_lt,
            trackers_created_dt_lte=trackers_created_dt_lte,
            trackers_embargoed=trackers_embargoed,
            trackers_external_system_id=trackers_external_system_id,
            trackers_ps_update_stream=trackers_ps_update_stream,
            trackers_resolution=trackers_resolution,
            trackers_status=trackers_status,
            trackers_type=trackers_type,
            trackers_updated_dt=trackers_updated_dt,
            trackers_updated_dt_date=trackers_updated_dt_date,
            trackers_updated_dt_date_gte=trackers_updated_dt_date_gte,
            trackers_updated_dt_date_lte=trackers_updated_dt_date_lte,
            trackers_updated_dt_gt=trackers_updated_dt_gt,
            trackers_updated_dt_gte=trackers_updated_dt_gte,
            trackers_updated_dt_lt=trackers_updated_dt_lt,
            trackers_updated_dt_lte=trackers_updated_dt_lte,
            trackers_uuid=trackers_uuid,
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
