import datetime
from typing import Any, Dict, List, Optional, Union

import requests

from ...client import AuthenticatedClient
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
from ...models.osidb_api_v1_affects_list_flaw_type import OsidbApiV1AffectsListFlawType
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
from ...models.osidb_api_v1_affects_list_type import OsidbApiV1AffectsListType
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
    "cvss2": str,
    "cvss2_score": float,
    "cvss2_score__gt": float,
    "cvss2_score__gte": float,
    "cvss2_score__lt": float,
    "cvss2_score__lte": float,
    "cvss3": str,
    "cvss3_score": float,
    "cvss3_score__gt": float,
    "cvss3_score__gte": float,
    "cvss3_score__lt": float,
    "cvss3_score__lte": float,
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
    "cvss_scores__uuid": str,
    "cvss_scores__vector": str,
    "embargoed": bool,
    "exclude_fields": List[str],
    "flaw__component": str,
    "flaw__created_dt": datetime.datetime,
    "flaw__created_dt__date": datetime.date,
    "flaw__created_dt__date__gte": datetime.date,
    "flaw__created_dt__date__lte": datetime.date,
    "flaw__created_dt__gt": datetime.datetime,
    "flaw__created_dt__gte": datetime.datetime,
    "flaw__created_dt__lt": datetime.datetime,
    "flaw__created_dt__lte": datetime.datetime,
    "flaw__cve_id": str,
    "flaw__cvss2": str,
    "flaw__cvss2_score": float,
    "flaw__cvss2_score__gt": float,
    "flaw__cvss2_score__gte": float,
    "flaw__cvss2_score__lt": float,
    "flaw__cvss2_score__lte": float,
    "flaw__cvss3": str,
    "flaw__cvss3_score": float,
    "flaw__cvss3_score__gt": float,
    "flaw__cvss3_score__gte": float,
    "flaw__cvss3_score__lt": float,
    "flaw__cvss3_score__lte": float,
    "flaw__cwe_id": str,
    "flaw__embargoed": bool,
    "flaw__impact": OsidbApiV1AffectsListFlawImpact,
    "flaw__is_major_incident": bool,
    "flaw__nvd_cvss2": str,
    "flaw__nvd_cvss3": str,
    "flaw__reported_dt": datetime.datetime,
    "flaw__reported_dt__date": datetime.date,
    "flaw__reported_dt__date__gte": datetime.date,
    "flaw__reported_dt__date__lte": datetime.date,
    "flaw__reported_dt__gt": datetime.datetime,
    "flaw__reported_dt__gte": datetime.datetime,
    "flaw__reported_dt__lt": datetime.datetime,
    "flaw__reported_dt__lte": datetime.datetime,
    "flaw__source": OsidbApiV1AffectsListFlawSource,
    "flaw__type": OsidbApiV1AffectsListFlawType,
    "flaw__unembargo_dt": datetime.datetime,
    "flaw__updated_dt": datetime.datetime,
    "flaw__updated_dt__date": datetime.date,
    "flaw__updated_dt__date__gte": datetime.date,
    "flaw__updated_dt__date__lte": datetime.date,
    "flaw__updated_dt__gt": datetime.datetime,
    "flaw__updated_dt__gte": datetime.datetime,
    "flaw__updated_dt__lt": datetime.datetime,
    "flaw__updated_dt__lte": datetime.datetime,
    "flaw__uuid": str,
    "impact": OsidbApiV1AffectsListImpact,
    "include_fields": List[str],
    "include_meta_attr": List[str],
    "limit": int,
    "offset": int,
    "order": List[OsidbApiV1AffectsListOrderItem],
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
    "trackers__uuid": str,
    "type": OsidbApiV1AffectsListType,
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
    affectedness: Union[Unset, None, OsidbApiV1AffectsListAffectedness] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss2: Union[Unset, None, str] = UNSET,
    cvss2_score: Union[Unset, None, float] = UNSET,
    cvss2_score_gt: Union[Unset, None, float] = UNSET,
    cvss2_score_gte: Union[Unset, None, float] = UNSET,
    cvss2_score_lt: Union[Unset, None, float] = UNSET,
    cvss2_score_lte: Union[Unset, None, float] = UNSET,
    cvss3: Union[Unset, None, str] = UNSET,
    cvss3_score: Union[Unset, None, float] = UNSET,
    cvss3_score_gt: Union[Unset, None, float] = UNSET,
    cvss3_score_gte: Union[Unset, None, float] = UNSET,
    cvss3_score_lt: Union[Unset, None, float] = UNSET,
    cvss3_score_lte: Union[Unset, None, float] = UNSET,
    cvss_scores_comment: Union[Unset, None, str] = UNSET,
    cvss_scores_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, None, str] = UNSET,
    cvss_scores_issuer: Union[
        Unset, None, OsidbApiV1AffectsListCvssScoresIssuer
    ] = UNSET,
    cvss_scores_score: Union[Unset, None, float] = UNSET,
    cvss_scores_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_uuid: Union[Unset, None, str] = UNSET,
    cvss_scores_vector: Union[Unset, None, str] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_component: Union[Unset, None, str] = UNSET,
    flaw_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, None, str] = UNSET,
    flaw_cvss2: Union[Unset, None, str] = UNSET,
    flaw_cvss2_score: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    flaw_cvss3: Union[Unset, None, str] = UNSET,
    flaw_cvss3_score: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    flaw_cwe_id: Union[Unset, None, str] = UNSET,
    flaw_embargoed: Union[Unset, None, bool] = UNSET,
    flaw_impact: Union[Unset, None, OsidbApiV1AffectsListFlawImpact] = UNSET,
    flaw_is_major_incident: Union[Unset, None, bool] = UNSET,
    flaw_nvd_cvss2: Union[Unset, None, str] = UNSET,
    flaw_nvd_cvss3: Union[Unset, None, str] = UNSET,
    flaw_reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, None, OsidbApiV1AffectsListFlawSource] = UNSET,
    flaw_type: Union[Unset, None, OsidbApiV1AffectsListFlawType] = UNSET,
    flaw_unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_uuid: Union[Unset, None, str] = UNSET,
    impact: Union[Unset, None, OsidbApiV1AffectsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, None, str] = UNSET,
    ps_module: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, OsidbApiV1AffectsListResolution] = UNSET,
    trackers_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_embargoed: Union[Unset, None, bool] = UNSET,
    trackers_external_system_id: Union[Unset, None, str] = UNSET,
    trackers_ps_update_stream: Union[Unset, None, str] = UNSET,
    trackers_resolution: Union[Unset, None, str] = UNSET,
    trackers_status: Union[Unset, None, str] = UNSET,
    trackers_type: Union[Unset, None, OsidbApiV1AffectsListTrackersType] = UNSET,
    trackers_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_uuid: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1AffectsListType] = UNSET,
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
    url = "{}/osidb/api/v1/affects".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_affectedness: Union[Unset, None, str] = UNSET
    if not isinstance(affectedness, Unset):

        json_affectedness = (
            OsidbApiV1AffectsListAffectedness(affectedness).value
            if affectedness
            else None
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

    json_cvss_scores_created_dt: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_created_dt, Unset):
        json_cvss_scores_created_dt = (
            cvss_scores_created_dt.isoformat() if cvss_scores_created_dt else None
        )

    json_cvss_scores_created_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_created_dt_date, Unset):
        json_cvss_scores_created_dt_date = (
            cvss_scores_created_dt_date.isoformat()
            if cvss_scores_created_dt_date
            else None
        )

    json_cvss_scores_created_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_created_dt_date_gte, Unset):
        json_cvss_scores_created_dt_date_gte = (
            cvss_scores_created_dt_date_gte.isoformat()
            if cvss_scores_created_dt_date_gte
            else None
        )

    json_cvss_scores_created_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_created_dt_date_lte, Unset):
        json_cvss_scores_created_dt_date_lte = (
            cvss_scores_created_dt_date_lte.isoformat()
            if cvss_scores_created_dt_date_lte
            else None
        )

    json_cvss_scores_created_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_created_dt_gt, Unset):
        json_cvss_scores_created_dt_gt = (
            cvss_scores_created_dt_gt.isoformat() if cvss_scores_created_dt_gt else None
        )

    json_cvss_scores_created_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_created_dt_gte, Unset):
        json_cvss_scores_created_dt_gte = (
            cvss_scores_created_dt_gte.isoformat()
            if cvss_scores_created_dt_gte
            else None
        )

    json_cvss_scores_created_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_created_dt_lt, Unset):
        json_cvss_scores_created_dt_lt = (
            cvss_scores_created_dt_lt.isoformat() if cvss_scores_created_dt_lt else None
        )

    json_cvss_scores_created_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_created_dt_lte, Unset):
        json_cvss_scores_created_dt_lte = (
            cvss_scores_created_dt_lte.isoformat()
            if cvss_scores_created_dt_lte
            else None
        )

    json_cvss_scores_issuer: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_issuer, Unset):

        json_cvss_scores_issuer = (
            OsidbApiV1AffectsListCvssScoresIssuer(cvss_scores_issuer).value
            if cvss_scores_issuer
            else None
        )

    json_cvss_scores_updated_dt: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_updated_dt, Unset):
        json_cvss_scores_updated_dt = (
            cvss_scores_updated_dt.isoformat() if cvss_scores_updated_dt else None
        )

    json_cvss_scores_updated_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_date, Unset):
        json_cvss_scores_updated_dt_date = (
            cvss_scores_updated_dt_date.isoformat()
            if cvss_scores_updated_dt_date
            else None
        )

    json_cvss_scores_updated_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_date_gte, Unset):
        json_cvss_scores_updated_dt_date_gte = (
            cvss_scores_updated_dt_date_gte.isoformat()
            if cvss_scores_updated_dt_date_gte
            else None
        )

    json_cvss_scores_updated_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_date_lte, Unset):
        json_cvss_scores_updated_dt_date_lte = (
            cvss_scores_updated_dt_date_lte.isoformat()
            if cvss_scores_updated_dt_date_lte
            else None
        )

    json_cvss_scores_updated_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_gt, Unset):
        json_cvss_scores_updated_dt_gt = (
            cvss_scores_updated_dt_gt.isoformat() if cvss_scores_updated_dt_gt else None
        )

    json_cvss_scores_updated_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_gte, Unset):
        json_cvss_scores_updated_dt_gte = (
            cvss_scores_updated_dt_gte.isoformat()
            if cvss_scores_updated_dt_gte
            else None
        )

    json_cvss_scores_updated_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_lt, Unset):
        json_cvss_scores_updated_dt_lt = (
            cvss_scores_updated_dt_lt.isoformat() if cvss_scores_updated_dt_lt else None
        )

    json_cvss_scores_updated_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(cvss_scores_updated_dt_lte, Unset):
        json_cvss_scores_updated_dt_lte = (
            cvss_scores_updated_dt_lte.isoformat()
            if cvss_scores_updated_dt_lte
            else None
        )

    json_exclude_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        if exclude_fields is None:
            json_exclude_fields = None
        else:
            json_exclude_fields = exclude_fields

    json_flaw_created_dt: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_created_dt, Unset):
        json_flaw_created_dt = flaw_created_dt.isoformat() if flaw_created_dt else None

    json_flaw_created_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_created_dt_date, Unset):
        json_flaw_created_dt_date = (
            flaw_created_dt_date.isoformat() if flaw_created_dt_date else None
        )

    json_flaw_created_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_created_dt_date_gte, Unset):
        json_flaw_created_dt_date_gte = (
            flaw_created_dt_date_gte.isoformat() if flaw_created_dt_date_gte else None
        )

    json_flaw_created_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_created_dt_date_lte, Unset):
        json_flaw_created_dt_date_lte = (
            flaw_created_dt_date_lte.isoformat() if flaw_created_dt_date_lte else None
        )

    json_flaw_created_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_created_dt_gt, Unset):
        json_flaw_created_dt_gt = (
            flaw_created_dt_gt.isoformat() if flaw_created_dt_gt else None
        )

    json_flaw_created_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_created_dt_gte, Unset):
        json_flaw_created_dt_gte = (
            flaw_created_dt_gte.isoformat() if flaw_created_dt_gte else None
        )

    json_flaw_created_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_created_dt_lt, Unset):
        json_flaw_created_dt_lt = (
            flaw_created_dt_lt.isoformat() if flaw_created_dt_lt else None
        )

    json_flaw_created_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_created_dt_lte, Unset):
        json_flaw_created_dt_lte = (
            flaw_created_dt_lte.isoformat() if flaw_created_dt_lte else None
        )

    json_flaw_impact: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_impact, Unset):

        json_flaw_impact = (
            OsidbApiV1AffectsListFlawImpact(flaw_impact).value if flaw_impact else None
        )

    json_flaw_reported_dt: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_reported_dt, Unset):
        json_flaw_reported_dt = (
            flaw_reported_dt.isoformat() if flaw_reported_dt else None
        )

    json_flaw_reported_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_reported_dt_date, Unset):
        json_flaw_reported_dt_date = (
            flaw_reported_dt_date.isoformat() if flaw_reported_dt_date else None
        )

    json_flaw_reported_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_reported_dt_date_gte, Unset):
        json_flaw_reported_dt_date_gte = (
            flaw_reported_dt_date_gte.isoformat() if flaw_reported_dt_date_gte else None
        )

    json_flaw_reported_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_reported_dt_date_lte, Unset):
        json_flaw_reported_dt_date_lte = (
            flaw_reported_dt_date_lte.isoformat() if flaw_reported_dt_date_lte else None
        )

    json_flaw_reported_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_reported_dt_gt, Unset):
        json_flaw_reported_dt_gt = (
            flaw_reported_dt_gt.isoformat() if flaw_reported_dt_gt else None
        )

    json_flaw_reported_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_reported_dt_gte, Unset):
        json_flaw_reported_dt_gte = (
            flaw_reported_dt_gte.isoformat() if flaw_reported_dt_gte else None
        )

    json_flaw_reported_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_reported_dt_lt, Unset):
        json_flaw_reported_dt_lt = (
            flaw_reported_dt_lt.isoformat() if flaw_reported_dt_lt else None
        )

    json_flaw_reported_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_reported_dt_lte, Unset):
        json_flaw_reported_dt_lte = (
            flaw_reported_dt_lte.isoformat() if flaw_reported_dt_lte else None
        )

    json_flaw_source: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_source, Unset):

        json_flaw_source = (
            OsidbApiV1AffectsListFlawSource(flaw_source).value if flaw_source else None
        )

    json_flaw_type: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_type, Unset):

        json_flaw_type = (
            OsidbApiV1AffectsListFlawType(flaw_type).value if flaw_type else None
        )

    json_flaw_unembargo_dt: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_unembargo_dt, Unset):
        json_flaw_unembargo_dt = (
            flaw_unembargo_dt.isoformat() if flaw_unembargo_dt else None
        )

    json_flaw_updated_dt: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_updated_dt, Unset):
        json_flaw_updated_dt = flaw_updated_dt.isoformat() if flaw_updated_dt else None

    json_flaw_updated_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_updated_dt_date, Unset):
        json_flaw_updated_dt_date = (
            flaw_updated_dt_date.isoformat() if flaw_updated_dt_date else None
        )

    json_flaw_updated_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_updated_dt_date_gte, Unset):
        json_flaw_updated_dt_date_gte = (
            flaw_updated_dt_date_gte.isoformat() if flaw_updated_dt_date_gte else None
        )

    json_flaw_updated_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_updated_dt_date_lte, Unset):
        json_flaw_updated_dt_date_lte = (
            flaw_updated_dt_date_lte.isoformat() if flaw_updated_dt_date_lte else None
        )

    json_flaw_updated_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_updated_dt_gt, Unset):
        json_flaw_updated_dt_gt = (
            flaw_updated_dt_gt.isoformat() if flaw_updated_dt_gt else None
        )

    json_flaw_updated_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_updated_dt_gte, Unset):
        json_flaw_updated_dt_gte = (
            flaw_updated_dt_gte.isoformat() if flaw_updated_dt_gte else None
        )

    json_flaw_updated_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_updated_dt_lt, Unset):
        json_flaw_updated_dt_lt = (
            flaw_updated_dt_lt.isoformat() if flaw_updated_dt_lt else None
        )

    json_flaw_updated_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(flaw_updated_dt_lte, Unset):
        json_flaw_updated_dt_lte = (
            flaw_updated_dt_lte.isoformat() if flaw_updated_dt_lte else None
        )

    json_impact: Union[Unset, None, str] = UNSET
    if not isinstance(impact, Unset):

        json_impact = OsidbApiV1AffectsListImpact(impact).value if impact else None

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

                    order_item = OsidbApiV1AffectsListOrderItem(order_item_data).value

                json_order.append(order_item)

    json_resolution: Union[Unset, None, str] = UNSET
    if not isinstance(resolution, Unset):

        json_resolution = (
            OsidbApiV1AffectsListResolution(resolution).value if resolution else None
        )

    json_trackers_created_dt: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_created_dt, Unset):
        json_trackers_created_dt = (
            trackers_created_dt.isoformat() if trackers_created_dt else None
        )

    json_trackers_created_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_created_dt_date, Unset):
        json_trackers_created_dt_date = (
            trackers_created_dt_date.isoformat() if trackers_created_dt_date else None
        )

    json_trackers_created_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_created_dt_date_gte, Unset):
        json_trackers_created_dt_date_gte = (
            trackers_created_dt_date_gte.isoformat()
            if trackers_created_dt_date_gte
            else None
        )

    json_trackers_created_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_created_dt_date_lte, Unset):
        json_trackers_created_dt_date_lte = (
            trackers_created_dt_date_lte.isoformat()
            if trackers_created_dt_date_lte
            else None
        )

    json_trackers_created_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_created_dt_gt, Unset):
        json_trackers_created_dt_gt = (
            trackers_created_dt_gt.isoformat() if trackers_created_dt_gt else None
        )

    json_trackers_created_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_created_dt_gte, Unset):
        json_trackers_created_dt_gte = (
            trackers_created_dt_gte.isoformat() if trackers_created_dt_gte else None
        )

    json_trackers_created_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_created_dt_lt, Unset):
        json_trackers_created_dt_lt = (
            trackers_created_dt_lt.isoformat() if trackers_created_dt_lt else None
        )

    json_trackers_created_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_created_dt_lte, Unset):
        json_trackers_created_dt_lte = (
            trackers_created_dt_lte.isoformat() if trackers_created_dt_lte else None
        )

    json_trackers_type: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_type, Unset):

        json_trackers_type = (
            OsidbApiV1AffectsListTrackersType(trackers_type).value
            if trackers_type
            else None
        )

    json_trackers_updated_dt: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_updated_dt, Unset):
        json_trackers_updated_dt = (
            trackers_updated_dt.isoformat() if trackers_updated_dt else None
        )

    json_trackers_updated_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_updated_dt_date, Unset):
        json_trackers_updated_dt_date = (
            trackers_updated_dt_date.isoformat() if trackers_updated_dt_date else None
        )

    json_trackers_updated_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_updated_dt_date_gte, Unset):
        json_trackers_updated_dt_date_gte = (
            trackers_updated_dt_date_gte.isoformat()
            if trackers_updated_dt_date_gte
            else None
        )

    json_trackers_updated_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_updated_dt_date_lte, Unset):
        json_trackers_updated_dt_date_lte = (
            trackers_updated_dt_date_lte.isoformat()
            if trackers_updated_dt_date_lte
            else None
        )

    json_trackers_updated_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_updated_dt_gt, Unset):
        json_trackers_updated_dt_gt = (
            trackers_updated_dt_gt.isoformat() if trackers_updated_dt_gt else None
        )

    json_trackers_updated_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_updated_dt_gte, Unset):
        json_trackers_updated_dt_gte = (
            trackers_updated_dt_gte.isoformat() if trackers_updated_dt_gte else None
        )

    json_trackers_updated_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_updated_dt_lt, Unset):
        json_trackers_updated_dt_lt = (
            trackers_updated_dt_lt.isoformat() if trackers_updated_dt_lt else None
        )

    json_trackers_updated_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(trackers_updated_dt_lte, Unset):
        json_trackers_updated_dt_lte = (
            trackers_updated_dt_lte.isoformat() if trackers_updated_dt_lte else None
        )

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):

        json_type = OsidbApiV1AffectsListType(type).value if type else None

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
        "affectedness": json_affectedness,
        "created_dt": json_created_dt,
        "created_dt__date": json_created_dt_date,
        "created_dt__date__gte": json_created_dt_date_gte,
        "created_dt__date__lte": json_created_dt_date_lte,
        "created_dt__gt": json_created_dt_gt,
        "created_dt__gte": json_created_dt_gte,
        "created_dt__lt": json_created_dt_lt,
        "created_dt__lte": json_created_dt_lte,
        "cvss2": cvss2,
        "cvss2_score": cvss2_score,
        "cvss2_score__gt": cvss2_score_gt,
        "cvss2_score__gte": cvss2_score_gte,
        "cvss2_score__lt": cvss2_score_lt,
        "cvss2_score__lte": cvss2_score_lte,
        "cvss3": cvss3,
        "cvss3_score": cvss3_score,
        "cvss3_score__gt": cvss3_score_gt,
        "cvss3_score__gte": cvss3_score_gte,
        "cvss3_score__lt": cvss3_score_lt,
        "cvss3_score__lte": cvss3_score_lte,
        "cvss_scores__comment": cvss_scores_comment,
        "cvss_scores__created_dt": json_cvss_scores_created_dt,
        "cvss_scores__created_dt__date": json_cvss_scores_created_dt_date,
        "cvss_scores__created_dt__date__gte": json_cvss_scores_created_dt_date_gte,
        "cvss_scores__created_dt__date__lte": json_cvss_scores_created_dt_date_lte,
        "cvss_scores__created_dt__gt": json_cvss_scores_created_dt_gt,
        "cvss_scores__created_dt__gte": json_cvss_scores_created_dt_gte,
        "cvss_scores__created_dt__lt": json_cvss_scores_created_dt_lt,
        "cvss_scores__created_dt__lte": json_cvss_scores_created_dt_lte,
        "cvss_scores__cvss_version": cvss_scores_cvss_version,
        "cvss_scores__issuer": json_cvss_scores_issuer,
        "cvss_scores__score": cvss_scores_score,
        "cvss_scores__updated_dt": json_cvss_scores_updated_dt,
        "cvss_scores__updated_dt__date": json_cvss_scores_updated_dt_date,
        "cvss_scores__updated_dt__date__gte": json_cvss_scores_updated_dt_date_gte,
        "cvss_scores__updated_dt__date__lte": json_cvss_scores_updated_dt_date_lte,
        "cvss_scores__updated_dt__gt": json_cvss_scores_updated_dt_gt,
        "cvss_scores__updated_dt__gte": json_cvss_scores_updated_dt_gte,
        "cvss_scores__updated_dt__lt": json_cvss_scores_updated_dt_lt,
        "cvss_scores__updated_dt__lte": json_cvss_scores_updated_dt_lte,
        "cvss_scores__uuid": cvss_scores_uuid,
        "cvss_scores__vector": cvss_scores_vector,
        "embargoed": embargoed,
        "exclude_fields": json_exclude_fields,
        "flaw__component": flaw_component,
        "flaw__created_dt": json_flaw_created_dt,
        "flaw__created_dt__date": json_flaw_created_dt_date,
        "flaw__created_dt__date__gte": json_flaw_created_dt_date_gte,
        "flaw__created_dt__date__lte": json_flaw_created_dt_date_lte,
        "flaw__created_dt__gt": json_flaw_created_dt_gt,
        "flaw__created_dt__gte": json_flaw_created_dt_gte,
        "flaw__created_dt__lt": json_flaw_created_dt_lt,
        "flaw__created_dt__lte": json_flaw_created_dt_lte,
        "flaw__cve_id": flaw_cve_id,
        "flaw__cvss2": flaw_cvss2,
        "flaw__cvss2_score": flaw_cvss2_score,
        "flaw__cvss2_score__gt": flaw_cvss2_score_gt,
        "flaw__cvss2_score__gte": flaw_cvss2_score_gte,
        "flaw__cvss2_score__lt": flaw_cvss2_score_lt,
        "flaw__cvss2_score__lte": flaw_cvss2_score_lte,
        "flaw__cvss3": flaw_cvss3,
        "flaw__cvss3_score": flaw_cvss3_score,
        "flaw__cvss3_score__gt": flaw_cvss3_score_gt,
        "flaw__cvss3_score__gte": flaw_cvss3_score_gte,
        "flaw__cvss3_score__lt": flaw_cvss3_score_lt,
        "flaw__cvss3_score__lte": flaw_cvss3_score_lte,
        "flaw__cwe_id": flaw_cwe_id,
        "flaw__embargoed": flaw_embargoed,
        "flaw__impact": json_flaw_impact,
        "flaw__is_major_incident": flaw_is_major_incident,
        "flaw__nvd_cvss2": flaw_nvd_cvss2,
        "flaw__nvd_cvss3": flaw_nvd_cvss3,
        "flaw__reported_dt": json_flaw_reported_dt,
        "flaw__reported_dt__date": json_flaw_reported_dt_date,
        "flaw__reported_dt__date__gte": json_flaw_reported_dt_date_gte,
        "flaw__reported_dt__date__lte": json_flaw_reported_dt_date_lte,
        "flaw__reported_dt__gt": json_flaw_reported_dt_gt,
        "flaw__reported_dt__gte": json_flaw_reported_dt_gte,
        "flaw__reported_dt__lt": json_flaw_reported_dt_lt,
        "flaw__reported_dt__lte": json_flaw_reported_dt_lte,
        "flaw__source": json_flaw_source,
        "flaw__type": json_flaw_type,
        "flaw__unembargo_dt": json_flaw_unembargo_dt,
        "flaw__updated_dt": json_flaw_updated_dt,
        "flaw__updated_dt__date": json_flaw_updated_dt_date,
        "flaw__updated_dt__date__gte": json_flaw_updated_dt_date_gte,
        "flaw__updated_dt__date__lte": json_flaw_updated_dt_date_lte,
        "flaw__updated_dt__gt": json_flaw_updated_dt_gt,
        "flaw__updated_dt__gte": json_flaw_updated_dt_gte,
        "flaw__updated_dt__lt": json_flaw_updated_dt_lt,
        "flaw__updated_dt__lte": json_flaw_updated_dt_lte,
        "flaw__uuid": flaw_uuid,
        "impact": json_impact,
        "include_fields": json_include_fields,
        "include_meta_attr": json_include_meta_attr,
        "limit": limit,
        "offset": offset,
        "order": json_order,
        "ps_component": ps_component,
        "ps_module": ps_module,
        "resolution": json_resolution,
        "trackers__created_dt": json_trackers_created_dt,
        "trackers__created_dt__date": json_trackers_created_dt_date,
        "trackers__created_dt__date__gte": json_trackers_created_dt_date_gte,
        "trackers__created_dt__date__lte": json_trackers_created_dt_date_lte,
        "trackers__created_dt__gt": json_trackers_created_dt_gt,
        "trackers__created_dt__gte": json_trackers_created_dt_gte,
        "trackers__created_dt__lt": json_trackers_created_dt_lt,
        "trackers__created_dt__lte": json_trackers_created_dt_lte,
        "trackers__embargoed": trackers_embargoed,
        "trackers__external_system_id": trackers_external_system_id,
        "trackers__ps_update_stream": trackers_ps_update_stream,
        "trackers__resolution": trackers_resolution,
        "trackers__status": trackers_status,
        "trackers__type": json_trackers_type,
        "trackers__updated_dt": json_trackers_updated_dt,
        "trackers__updated_dt__date": json_trackers_updated_dt_date,
        "trackers__updated_dt__date__gte": json_trackers_updated_dt_date_gte,
        "trackers__updated_dt__date__lte": json_trackers_updated_dt_date_lte,
        "trackers__updated_dt__gt": json_trackers_updated_dt_gt,
        "trackers__updated_dt__gte": json_trackers_updated_dt_gte,
        "trackers__updated_dt__lt": json_trackers_updated_dt_lt,
        "trackers__updated_dt__lte": json_trackers_updated_dt_lte,
        "trackers__uuid": trackers_uuid,
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
) -> Optional[OsidbApiV1AffectsListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1AffectsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1AffectsListResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1AffectsListResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    affectedness: Union[Unset, None, OsidbApiV1AffectsListAffectedness] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss2: Union[Unset, None, str] = UNSET,
    cvss2_score: Union[Unset, None, float] = UNSET,
    cvss2_score_gt: Union[Unset, None, float] = UNSET,
    cvss2_score_gte: Union[Unset, None, float] = UNSET,
    cvss2_score_lt: Union[Unset, None, float] = UNSET,
    cvss2_score_lte: Union[Unset, None, float] = UNSET,
    cvss3: Union[Unset, None, str] = UNSET,
    cvss3_score: Union[Unset, None, float] = UNSET,
    cvss3_score_gt: Union[Unset, None, float] = UNSET,
    cvss3_score_gte: Union[Unset, None, float] = UNSET,
    cvss3_score_lt: Union[Unset, None, float] = UNSET,
    cvss3_score_lte: Union[Unset, None, float] = UNSET,
    cvss_scores_comment: Union[Unset, None, str] = UNSET,
    cvss_scores_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, None, str] = UNSET,
    cvss_scores_issuer: Union[
        Unset, None, OsidbApiV1AffectsListCvssScoresIssuer
    ] = UNSET,
    cvss_scores_score: Union[Unset, None, float] = UNSET,
    cvss_scores_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_uuid: Union[Unset, None, str] = UNSET,
    cvss_scores_vector: Union[Unset, None, str] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_component: Union[Unset, None, str] = UNSET,
    flaw_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, None, str] = UNSET,
    flaw_cvss2: Union[Unset, None, str] = UNSET,
    flaw_cvss2_score: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    flaw_cvss3: Union[Unset, None, str] = UNSET,
    flaw_cvss3_score: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    flaw_cwe_id: Union[Unset, None, str] = UNSET,
    flaw_embargoed: Union[Unset, None, bool] = UNSET,
    flaw_impact: Union[Unset, None, OsidbApiV1AffectsListFlawImpact] = UNSET,
    flaw_is_major_incident: Union[Unset, None, bool] = UNSET,
    flaw_nvd_cvss2: Union[Unset, None, str] = UNSET,
    flaw_nvd_cvss3: Union[Unset, None, str] = UNSET,
    flaw_reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, None, OsidbApiV1AffectsListFlawSource] = UNSET,
    flaw_type: Union[Unset, None, OsidbApiV1AffectsListFlawType] = UNSET,
    flaw_unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_uuid: Union[Unset, None, str] = UNSET,
    impact: Union[Unset, None, OsidbApiV1AffectsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, None, str] = UNSET,
    ps_module: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, OsidbApiV1AffectsListResolution] = UNSET,
    trackers_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_embargoed: Union[Unset, None, bool] = UNSET,
    trackers_external_system_id: Union[Unset, None, str] = UNSET,
    trackers_ps_update_stream: Union[Unset, None, str] = UNSET,
    trackers_resolution: Union[Unset, None, str] = UNSET,
    trackers_status: Union[Unset, None, str] = UNSET,
    trackers_type: Union[Unset, None, OsidbApiV1AffectsListTrackersType] = UNSET,
    trackers_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_uuid: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1AffectsListType] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1AffectsListResponse200]:
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
        cvss2=cvss2,
        cvss2_score=cvss2_score,
        cvss2_score_gt=cvss2_score_gt,
        cvss2_score_gte=cvss2_score_gte,
        cvss2_score_lt=cvss2_score_lt,
        cvss2_score_lte=cvss2_score_lte,
        cvss3=cvss3,
        cvss3_score=cvss3_score,
        cvss3_score_gt=cvss3_score_gt,
        cvss3_score_gte=cvss3_score_gte,
        cvss3_score_lt=cvss3_score_lt,
        cvss3_score_lte=cvss3_score_lte,
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
        flaw_component=flaw_component,
        flaw_created_dt=flaw_created_dt,
        flaw_created_dt_date=flaw_created_dt_date,
        flaw_created_dt_date_gte=flaw_created_dt_date_gte,
        flaw_created_dt_date_lte=flaw_created_dt_date_lte,
        flaw_created_dt_gt=flaw_created_dt_gt,
        flaw_created_dt_gte=flaw_created_dt_gte,
        flaw_created_dt_lt=flaw_created_dt_lt,
        flaw_created_dt_lte=flaw_created_dt_lte,
        flaw_cve_id=flaw_cve_id,
        flaw_cvss2=flaw_cvss2,
        flaw_cvss2_score=flaw_cvss2_score,
        flaw_cvss2_score_gt=flaw_cvss2_score_gt,
        flaw_cvss2_score_gte=flaw_cvss2_score_gte,
        flaw_cvss2_score_lt=flaw_cvss2_score_lt,
        flaw_cvss2_score_lte=flaw_cvss2_score_lte,
        flaw_cvss3=flaw_cvss3,
        flaw_cvss3_score=flaw_cvss3_score,
        flaw_cvss3_score_gt=flaw_cvss3_score_gt,
        flaw_cvss3_score_gte=flaw_cvss3_score_gte,
        flaw_cvss3_score_lt=flaw_cvss3_score_lt,
        flaw_cvss3_score_lte=flaw_cvss3_score_lte,
        flaw_cwe_id=flaw_cwe_id,
        flaw_embargoed=flaw_embargoed,
        flaw_impact=flaw_impact,
        flaw_is_major_incident=flaw_is_major_incident,
        flaw_nvd_cvss2=flaw_nvd_cvss2,
        flaw_nvd_cvss3=flaw_nvd_cvss3,
        flaw_reported_dt=flaw_reported_dt,
        flaw_reported_dt_date=flaw_reported_dt_date,
        flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
        flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
        flaw_reported_dt_gt=flaw_reported_dt_gt,
        flaw_reported_dt_gte=flaw_reported_dt_gte,
        flaw_reported_dt_lt=flaw_reported_dt_lt,
        flaw_reported_dt_lte=flaw_reported_dt_lte,
        flaw_source=flaw_source,
        flaw_type=flaw_type,
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
    affectedness: Union[Unset, None, OsidbApiV1AffectsListAffectedness] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss2: Union[Unset, None, str] = UNSET,
    cvss2_score: Union[Unset, None, float] = UNSET,
    cvss2_score_gt: Union[Unset, None, float] = UNSET,
    cvss2_score_gte: Union[Unset, None, float] = UNSET,
    cvss2_score_lt: Union[Unset, None, float] = UNSET,
    cvss2_score_lte: Union[Unset, None, float] = UNSET,
    cvss3: Union[Unset, None, str] = UNSET,
    cvss3_score: Union[Unset, None, float] = UNSET,
    cvss3_score_gt: Union[Unset, None, float] = UNSET,
    cvss3_score_gte: Union[Unset, None, float] = UNSET,
    cvss3_score_lt: Union[Unset, None, float] = UNSET,
    cvss3_score_lte: Union[Unset, None, float] = UNSET,
    cvss_scores_comment: Union[Unset, None, str] = UNSET,
    cvss_scores_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, None, str] = UNSET,
    cvss_scores_issuer: Union[
        Unset, None, OsidbApiV1AffectsListCvssScoresIssuer
    ] = UNSET,
    cvss_scores_score: Union[Unset, None, float] = UNSET,
    cvss_scores_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_uuid: Union[Unset, None, str] = UNSET,
    cvss_scores_vector: Union[Unset, None, str] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_component: Union[Unset, None, str] = UNSET,
    flaw_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, None, str] = UNSET,
    flaw_cvss2: Union[Unset, None, str] = UNSET,
    flaw_cvss2_score: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    flaw_cvss3: Union[Unset, None, str] = UNSET,
    flaw_cvss3_score: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    flaw_cwe_id: Union[Unset, None, str] = UNSET,
    flaw_embargoed: Union[Unset, None, bool] = UNSET,
    flaw_impact: Union[Unset, None, OsidbApiV1AffectsListFlawImpact] = UNSET,
    flaw_is_major_incident: Union[Unset, None, bool] = UNSET,
    flaw_nvd_cvss2: Union[Unset, None, str] = UNSET,
    flaw_nvd_cvss3: Union[Unset, None, str] = UNSET,
    flaw_reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, None, OsidbApiV1AffectsListFlawSource] = UNSET,
    flaw_type: Union[Unset, None, OsidbApiV1AffectsListFlawType] = UNSET,
    flaw_unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_uuid: Union[Unset, None, str] = UNSET,
    impact: Union[Unset, None, OsidbApiV1AffectsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, None, str] = UNSET,
    ps_module: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, OsidbApiV1AffectsListResolution] = UNSET,
    trackers_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_embargoed: Union[Unset, None, bool] = UNSET,
    trackers_external_system_id: Union[Unset, None, str] = UNSET,
    trackers_ps_update_stream: Union[Unset, None, str] = UNSET,
    trackers_resolution: Union[Unset, None, str] = UNSET,
    trackers_status: Union[Unset, None, str] = UNSET,
    trackers_type: Union[Unset, None, OsidbApiV1AffectsListTrackersType] = UNSET,
    trackers_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_uuid: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1AffectsListType] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1AffectsListResponse200]:
    """ """

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
        cvss2=cvss2,
        cvss2_score=cvss2_score,
        cvss2_score_gt=cvss2_score_gt,
        cvss2_score_gte=cvss2_score_gte,
        cvss2_score_lt=cvss2_score_lt,
        cvss2_score_lte=cvss2_score_lte,
        cvss3=cvss3,
        cvss3_score=cvss3_score,
        cvss3_score_gt=cvss3_score_gt,
        cvss3_score_gte=cvss3_score_gte,
        cvss3_score_lt=cvss3_score_lt,
        cvss3_score_lte=cvss3_score_lte,
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
        flaw_component=flaw_component,
        flaw_created_dt=flaw_created_dt,
        flaw_created_dt_date=flaw_created_dt_date,
        flaw_created_dt_date_gte=flaw_created_dt_date_gte,
        flaw_created_dt_date_lte=flaw_created_dt_date_lte,
        flaw_created_dt_gt=flaw_created_dt_gt,
        flaw_created_dt_gte=flaw_created_dt_gte,
        flaw_created_dt_lt=flaw_created_dt_lt,
        flaw_created_dt_lte=flaw_created_dt_lte,
        flaw_cve_id=flaw_cve_id,
        flaw_cvss2=flaw_cvss2,
        flaw_cvss2_score=flaw_cvss2_score,
        flaw_cvss2_score_gt=flaw_cvss2_score_gt,
        flaw_cvss2_score_gte=flaw_cvss2_score_gte,
        flaw_cvss2_score_lt=flaw_cvss2_score_lt,
        flaw_cvss2_score_lte=flaw_cvss2_score_lte,
        flaw_cvss3=flaw_cvss3,
        flaw_cvss3_score=flaw_cvss3_score,
        flaw_cvss3_score_gt=flaw_cvss3_score_gt,
        flaw_cvss3_score_gte=flaw_cvss3_score_gte,
        flaw_cvss3_score_lt=flaw_cvss3_score_lt,
        flaw_cvss3_score_lte=flaw_cvss3_score_lte,
        flaw_cwe_id=flaw_cwe_id,
        flaw_embargoed=flaw_embargoed,
        flaw_impact=flaw_impact,
        flaw_is_major_incident=flaw_is_major_incident,
        flaw_nvd_cvss2=flaw_nvd_cvss2,
        flaw_nvd_cvss3=flaw_nvd_cvss3,
        flaw_reported_dt=flaw_reported_dt,
        flaw_reported_dt_date=flaw_reported_dt_date,
        flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
        flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
        flaw_reported_dt_gt=flaw_reported_dt_gt,
        flaw_reported_dt_gte=flaw_reported_dt_gte,
        flaw_reported_dt_lt=flaw_reported_dt_lt,
        flaw_reported_dt_lte=flaw_reported_dt_lte,
        flaw_source=flaw_source,
        flaw_type=flaw_type,
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
    affectedness: Union[Unset, None, OsidbApiV1AffectsListAffectedness] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss2: Union[Unset, None, str] = UNSET,
    cvss2_score: Union[Unset, None, float] = UNSET,
    cvss2_score_gt: Union[Unset, None, float] = UNSET,
    cvss2_score_gte: Union[Unset, None, float] = UNSET,
    cvss2_score_lt: Union[Unset, None, float] = UNSET,
    cvss2_score_lte: Union[Unset, None, float] = UNSET,
    cvss3: Union[Unset, None, str] = UNSET,
    cvss3_score: Union[Unset, None, float] = UNSET,
    cvss3_score_gt: Union[Unset, None, float] = UNSET,
    cvss3_score_gte: Union[Unset, None, float] = UNSET,
    cvss3_score_lt: Union[Unset, None, float] = UNSET,
    cvss3_score_lte: Union[Unset, None, float] = UNSET,
    cvss_scores_comment: Union[Unset, None, str] = UNSET,
    cvss_scores_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, None, str] = UNSET,
    cvss_scores_issuer: Union[
        Unset, None, OsidbApiV1AffectsListCvssScoresIssuer
    ] = UNSET,
    cvss_scores_score: Union[Unset, None, float] = UNSET,
    cvss_scores_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_uuid: Union[Unset, None, str] = UNSET,
    cvss_scores_vector: Union[Unset, None, str] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_component: Union[Unset, None, str] = UNSET,
    flaw_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, None, str] = UNSET,
    flaw_cvss2: Union[Unset, None, str] = UNSET,
    flaw_cvss2_score: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    flaw_cvss3: Union[Unset, None, str] = UNSET,
    flaw_cvss3_score: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    flaw_cwe_id: Union[Unset, None, str] = UNSET,
    flaw_embargoed: Union[Unset, None, bool] = UNSET,
    flaw_impact: Union[Unset, None, OsidbApiV1AffectsListFlawImpact] = UNSET,
    flaw_is_major_incident: Union[Unset, None, bool] = UNSET,
    flaw_nvd_cvss2: Union[Unset, None, str] = UNSET,
    flaw_nvd_cvss3: Union[Unset, None, str] = UNSET,
    flaw_reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, None, OsidbApiV1AffectsListFlawSource] = UNSET,
    flaw_type: Union[Unset, None, OsidbApiV1AffectsListFlawType] = UNSET,
    flaw_unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_uuid: Union[Unset, None, str] = UNSET,
    impact: Union[Unset, None, OsidbApiV1AffectsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, None, str] = UNSET,
    ps_module: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, OsidbApiV1AffectsListResolution] = UNSET,
    trackers_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_embargoed: Union[Unset, None, bool] = UNSET,
    trackers_external_system_id: Union[Unset, None, str] = UNSET,
    trackers_ps_update_stream: Union[Unset, None, str] = UNSET,
    trackers_resolution: Union[Unset, None, str] = UNSET,
    trackers_status: Union[Unset, None, str] = UNSET,
    trackers_type: Union[Unset, None, OsidbApiV1AffectsListTrackersType] = UNSET,
    trackers_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_uuid: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1AffectsListType] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1AffectsListResponse200]:
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
        cvss2=cvss2,
        cvss2_score=cvss2_score,
        cvss2_score_gt=cvss2_score_gt,
        cvss2_score_gte=cvss2_score_gte,
        cvss2_score_lt=cvss2_score_lt,
        cvss2_score_lte=cvss2_score_lte,
        cvss3=cvss3,
        cvss3_score=cvss3_score,
        cvss3_score_gt=cvss3_score_gt,
        cvss3_score_gte=cvss3_score_gte,
        cvss3_score_lt=cvss3_score_lt,
        cvss3_score_lte=cvss3_score_lte,
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
        flaw_component=flaw_component,
        flaw_created_dt=flaw_created_dt,
        flaw_created_dt_date=flaw_created_dt_date,
        flaw_created_dt_date_gte=flaw_created_dt_date_gte,
        flaw_created_dt_date_lte=flaw_created_dt_date_lte,
        flaw_created_dt_gt=flaw_created_dt_gt,
        flaw_created_dt_gte=flaw_created_dt_gte,
        flaw_created_dt_lt=flaw_created_dt_lt,
        flaw_created_dt_lte=flaw_created_dt_lte,
        flaw_cve_id=flaw_cve_id,
        flaw_cvss2=flaw_cvss2,
        flaw_cvss2_score=flaw_cvss2_score,
        flaw_cvss2_score_gt=flaw_cvss2_score_gt,
        flaw_cvss2_score_gte=flaw_cvss2_score_gte,
        flaw_cvss2_score_lt=flaw_cvss2_score_lt,
        flaw_cvss2_score_lte=flaw_cvss2_score_lte,
        flaw_cvss3=flaw_cvss3,
        flaw_cvss3_score=flaw_cvss3_score,
        flaw_cvss3_score_gt=flaw_cvss3_score_gt,
        flaw_cvss3_score_gte=flaw_cvss3_score_gte,
        flaw_cvss3_score_lt=flaw_cvss3_score_lt,
        flaw_cvss3_score_lte=flaw_cvss3_score_lte,
        flaw_cwe_id=flaw_cwe_id,
        flaw_embargoed=flaw_embargoed,
        flaw_impact=flaw_impact,
        flaw_is_major_incident=flaw_is_major_incident,
        flaw_nvd_cvss2=flaw_nvd_cvss2,
        flaw_nvd_cvss3=flaw_nvd_cvss3,
        flaw_reported_dt=flaw_reported_dt,
        flaw_reported_dt_date=flaw_reported_dt_date,
        flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
        flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
        flaw_reported_dt_gt=flaw_reported_dt_gt,
        flaw_reported_dt_gte=flaw_reported_dt_gte,
        flaw_reported_dt_lt=flaw_reported_dt_lt,
        flaw_reported_dt_lte=flaw_reported_dt_lte,
        flaw_source=flaw_source,
        flaw_type=flaw_type,
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
    affectedness: Union[Unset, None, OsidbApiV1AffectsListAffectedness] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss2: Union[Unset, None, str] = UNSET,
    cvss2_score: Union[Unset, None, float] = UNSET,
    cvss2_score_gt: Union[Unset, None, float] = UNSET,
    cvss2_score_gte: Union[Unset, None, float] = UNSET,
    cvss2_score_lt: Union[Unset, None, float] = UNSET,
    cvss2_score_lte: Union[Unset, None, float] = UNSET,
    cvss3: Union[Unset, None, str] = UNSET,
    cvss3_score: Union[Unset, None, float] = UNSET,
    cvss3_score_gt: Union[Unset, None, float] = UNSET,
    cvss3_score_gte: Union[Unset, None, float] = UNSET,
    cvss3_score_lt: Union[Unset, None, float] = UNSET,
    cvss3_score_lte: Union[Unset, None, float] = UNSET,
    cvss_scores_comment: Union[Unset, None, str] = UNSET,
    cvss_scores_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, None, str] = UNSET,
    cvss_scores_issuer: Union[
        Unset, None, OsidbApiV1AffectsListCvssScoresIssuer
    ] = UNSET,
    cvss_scores_score: Union[Unset, None, float] = UNSET,
    cvss_scores_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    cvss_scores_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cvss_scores_uuid: Union[Unset, None, str] = UNSET,
    cvss_scores_vector: Union[Unset, None, str] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_component: Union[Unset, None, str] = UNSET,
    flaw_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, None, str] = UNSET,
    flaw_cvss2: Union[Unset, None, str] = UNSET,
    flaw_cvss2_score: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_gt: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_gte: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_lt: Union[Unset, None, float] = UNSET,
    flaw_cvss2_score_lte: Union[Unset, None, float] = UNSET,
    flaw_cvss3: Union[Unset, None, str] = UNSET,
    flaw_cvss3_score: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_gt: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_gte: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_lt: Union[Unset, None, float] = UNSET,
    flaw_cvss3_score_lte: Union[Unset, None, float] = UNSET,
    flaw_cwe_id: Union[Unset, None, str] = UNSET,
    flaw_embargoed: Union[Unset, None, bool] = UNSET,
    flaw_impact: Union[Unset, None, OsidbApiV1AffectsListFlawImpact] = UNSET,
    flaw_is_major_incident: Union[Unset, None, bool] = UNSET,
    flaw_nvd_cvss2: Union[Unset, None, str] = UNSET,
    flaw_nvd_cvss3: Union[Unset, None, str] = UNSET,
    flaw_reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, None, OsidbApiV1AffectsListFlawSource] = UNSET,
    flaw_type: Union[Unset, None, OsidbApiV1AffectsListFlawType] = UNSET,
    flaw_unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    flaw_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    flaw_uuid: Union[Unset, None, str] = UNSET,
    impact: Union[Unset, None, OsidbApiV1AffectsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, None, str] = UNSET,
    ps_module: Union[Unset, None, str] = UNSET,
    resolution: Union[Unset, None, OsidbApiV1AffectsListResolution] = UNSET,
    trackers_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    trackers_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_embargoed: Union[Unset, None, bool] = UNSET,
    trackers_external_system_id: Union[Unset, None, str] = UNSET,
    trackers_ps_update_stream: Union[Unset, None, str] = UNSET,
    trackers_resolution: Union[Unset, None, str] = UNSET,
    trackers_status: Union[Unset, None, str] = UNSET,
    trackers_type: Union[Unset, None, OsidbApiV1AffectsListTrackersType] = UNSET,
    trackers_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    trackers_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    trackers_uuid: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, OsidbApiV1AffectsListType] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1AffectsListResponse200]:
    """ """

    return (
        await async_detailed(
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
            cvss2=cvss2,
            cvss2_score=cvss2_score,
            cvss2_score_gt=cvss2_score_gt,
            cvss2_score_gte=cvss2_score_gte,
            cvss2_score_lt=cvss2_score_lt,
            cvss2_score_lte=cvss2_score_lte,
            cvss3=cvss3,
            cvss3_score=cvss3_score,
            cvss3_score_gt=cvss3_score_gt,
            cvss3_score_gte=cvss3_score_gte,
            cvss3_score_lt=cvss3_score_lt,
            cvss3_score_lte=cvss3_score_lte,
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
            flaw_component=flaw_component,
            flaw_created_dt=flaw_created_dt,
            flaw_created_dt_date=flaw_created_dt_date,
            flaw_created_dt_date_gte=flaw_created_dt_date_gte,
            flaw_created_dt_date_lte=flaw_created_dt_date_lte,
            flaw_created_dt_gt=flaw_created_dt_gt,
            flaw_created_dt_gte=flaw_created_dt_gte,
            flaw_created_dt_lt=flaw_created_dt_lt,
            flaw_created_dt_lte=flaw_created_dt_lte,
            flaw_cve_id=flaw_cve_id,
            flaw_cvss2=flaw_cvss2,
            flaw_cvss2_score=flaw_cvss2_score,
            flaw_cvss2_score_gt=flaw_cvss2_score_gt,
            flaw_cvss2_score_gte=flaw_cvss2_score_gte,
            flaw_cvss2_score_lt=flaw_cvss2_score_lt,
            flaw_cvss2_score_lte=flaw_cvss2_score_lte,
            flaw_cvss3=flaw_cvss3,
            flaw_cvss3_score=flaw_cvss3_score,
            flaw_cvss3_score_gt=flaw_cvss3_score_gt,
            flaw_cvss3_score_gte=flaw_cvss3_score_gte,
            flaw_cvss3_score_lt=flaw_cvss3_score_lt,
            flaw_cvss3_score_lte=flaw_cvss3_score_lte,
            flaw_cwe_id=flaw_cwe_id,
            flaw_embargoed=flaw_embargoed,
            flaw_impact=flaw_impact,
            flaw_is_major_incident=flaw_is_major_incident,
            flaw_nvd_cvss2=flaw_nvd_cvss2,
            flaw_nvd_cvss3=flaw_nvd_cvss3,
            flaw_reported_dt=flaw_reported_dt,
            flaw_reported_dt_date=flaw_reported_dt_date,
            flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
            flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
            flaw_reported_dt_gt=flaw_reported_dt_gt,
            flaw_reported_dt_gte=flaw_reported_dt_gte,
            flaw_reported_dt_lt=flaw_reported_dt_lt,
            flaw_reported_dt_lte=flaw_reported_dt_lte,
            flaw_source=flaw_source,
            flaw_type=flaw_type,
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
