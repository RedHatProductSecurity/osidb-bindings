import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v2_affects_list_affectedness import (
    OsidbApiV2AffectsListAffectedness,
)
from ...models.osidb_api_v2_affects_list_affectedness_in_item import (
    OsidbApiV2AffectsListAffectednessInItem,
)
from ...models.osidb_api_v2_affects_list_cvss_scores_issuer import (
    OsidbApiV2AffectsListCvssScoresIssuer,
)
from ...models.osidb_api_v2_affects_list_cvss_scores_issuer_in_item import (
    OsidbApiV2AffectsListCvssScoresIssuerInItem,
)
from ...models.osidb_api_v2_affects_list_flaw_impact import (
    OsidbApiV2AffectsListFlawImpact,
)
from ...models.osidb_api_v2_affects_list_flaw_impact_in_item import (
    OsidbApiV2AffectsListFlawImpactInItem,
)
from ...models.osidb_api_v2_affects_list_flaw_source import (
    OsidbApiV2AffectsListFlawSource,
)
from ...models.osidb_api_v2_affects_list_flaw_source_in_item import (
    OsidbApiV2AffectsListFlawSourceInItem,
)
from ...models.osidb_api_v2_affects_list_flaw_visibility import (
    OsidbApiV2AffectsListFlawVisibility,
)
from ...models.osidb_api_v2_affects_list_flaw_workflow_state_item import (
    OsidbApiV2AffectsListFlawWorkflowStateItem,
)
from ...models.osidb_api_v2_affects_list_impact import OsidbApiV2AffectsListImpact
from ...models.osidb_api_v2_affects_list_impact_in_item import (
    OsidbApiV2AffectsListImpactInItem,
)
from ...models.osidb_api_v2_affects_list_order_item import (
    OsidbApiV2AffectsListOrderItem,
)
from ...models.osidb_api_v2_affects_list_resolution import (
    OsidbApiV2AffectsListResolution,
)
from ...models.osidb_api_v2_affects_list_resolution_in_item import (
    OsidbApiV2AffectsListResolutionInItem,
)
from ...models.osidb_api_v2_affects_list_response_200 import (
    OsidbApiV2AffectsListResponse200,
)
from ...models.osidb_api_v2_affects_list_tracker_type import (
    OsidbApiV2AffectsListTrackerType,
)
from ...models.osidb_api_v2_affects_list_tracker_type_in_item import (
    OsidbApiV2AffectsListTrackerTypeInItem,
)
from ...models.osidb_api_v2_affects_list_tracker_visibility import (
    OsidbApiV2AffectsListTrackerVisibility,
)
from ...models.osidb_api_v2_affects_list_visibility import (
    OsidbApiV2AffectsListVisibility,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "affectedness": OsidbApiV2AffectsListAffectedness,
    "affectedness__in": list[OsidbApiV2AffectsListAffectednessInItem],
    "created_dt": datetime.datetime,
    "created_dt__date": datetime.date,
    "created_dt__date__gte": datetime.date,
    "created_dt__date__lte": datetime.date,
    "created_dt__gt": datetime.datetime,
    "created_dt__gte": datetime.datetime,
    "created_dt__lt": datetime.datetime,
    "created_dt__lte": datetime.datetime,
    "cve_id": str,
    "cve_id__in": list[str],
    "cvss_scores__comment": str,
    "cvss_scores__comment__in": list[str],
    "cvss_scores__created_dt": datetime.datetime,
    "cvss_scores__created_dt__date": datetime.date,
    "cvss_scores__created_dt__date__gte": datetime.date,
    "cvss_scores__created_dt__date__lte": datetime.date,
    "cvss_scores__created_dt__gt": datetime.datetime,
    "cvss_scores__created_dt__gte": datetime.datetime,
    "cvss_scores__created_dt__lt": datetime.datetime,
    "cvss_scores__created_dt__lte": datetime.datetime,
    "cvss_scores__cvss_version": str,
    "cvss_scores__issuer": OsidbApiV2AffectsListCvssScoresIssuer,
    "cvss_scores__issuer__in": list[OsidbApiV2AffectsListCvssScoresIssuerInItem],
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
    "cvss_scores__uuid__in": list[UUID],
    "cvss_scores__vector": str,
    "cvss_scores__vector__in": list[str],
    "embargoed": bool,
    "exclude_fields": list[str],
    "flaw__components": list[str],
    "flaw__components__in": list[str],
    "flaw__created_dt": datetime.datetime,
    "flaw__created_dt__date": datetime.date,
    "flaw__created_dt__date__gte": datetime.date,
    "flaw__created_dt__date__lte": datetime.date,
    "flaw__created_dt__gt": datetime.datetime,
    "flaw__created_dt__gte": datetime.datetime,
    "flaw__created_dt__lt": datetime.datetime,
    "flaw__created_dt__lte": datetime.datetime,
    "flaw__cve_id": str,
    "flaw__cve_id__in": list[str],
    "flaw__cwe_id": str,
    "flaw__cwe_id__in": list[str],
    "flaw__embargoed": bool,
    "flaw__impact": OsidbApiV2AffectsListFlawImpact,
    "flaw__impact__in": list[OsidbApiV2AffectsListFlawImpactInItem],
    "flaw__reported_dt": datetime.datetime,
    "flaw__reported_dt__date": datetime.date,
    "flaw__reported_dt__date__gte": datetime.date,
    "flaw__reported_dt__date__lte": datetime.date,
    "flaw__reported_dt__gt": datetime.datetime,
    "flaw__reported_dt__gte": datetime.datetime,
    "flaw__reported_dt__lt": datetime.datetime,
    "flaw__reported_dt__lte": datetime.datetime,
    "flaw__source": OsidbApiV2AffectsListFlawSource,
    "flaw__source__in": list[OsidbApiV2AffectsListFlawSourceInItem],
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
    "flaw__uuid__in": list[UUID],
    "flaw__visibility": OsidbApiV2AffectsListFlawVisibility,
    "flaw__workflow_state": list[OsidbApiV2AffectsListFlawWorkflowStateItem],
    "impact": OsidbApiV2AffectsListImpact,
    "impact__in": list[OsidbApiV2AffectsListImpactInItem],
    "include_fields": list[str],
    "include_history": bool,
    "include_meta_attr": list[str],
    "limit": int,
    "offset": int,
    "order": list[OsidbApiV2AffectsListOrderItem],
    "ps_component": str,
    "ps_component__in": list[str],
    "ps_module": str,
    "ps_module__in": list[str],
    "ps_update_stream": str,
    "ps_update_stream__in": list[str],
    "purl": str,
    "purl__in": list[str],
    "resolution": OsidbApiV2AffectsListResolution,
    "resolution__in": list[OsidbApiV2AffectsListResolutionInItem],
    "subpackage_purls": str,
    "subpackage_purls__in": list[str],
    "subpackage_purls__isempty": bool,
    "tracker__created_dt": datetime.datetime,
    "tracker__created_dt__date": datetime.date,
    "tracker__created_dt__date__gte": datetime.date,
    "tracker__created_dt__date__lte": datetime.date,
    "tracker__created_dt__gt": datetime.datetime,
    "tracker__created_dt__gte": datetime.datetime,
    "tracker__created_dt__lt": datetime.datetime,
    "tracker__created_dt__lte": datetime.datetime,
    "tracker__embargoed": bool,
    "tracker__external_system_id": str,
    "tracker__external_system_id__in": list[str],
    "tracker__isnull": bool,
    "tracker__ps_update_stream": str,
    "tracker__ps_update_stream__in": list[str],
    "tracker__resolution": str,
    "tracker__resolution__in": list[str],
    "tracker__status": str,
    "tracker__status__in": list[str],
    "tracker__type": OsidbApiV2AffectsListTrackerType,
    "tracker__type__in": list[OsidbApiV2AffectsListTrackerTypeInItem],
    "tracker__updated_dt": datetime.datetime,
    "tracker__updated_dt__date": datetime.date,
    "tracker__updated_dt__date__gte": datetime.date,
    "tracker__updated_dt__date__lte": datetime.date,
    "tracker__updated_dt__gt": datetime.datetime,
    "tracker__updated_dt__gte": datetime.datetime,
    "tracker__updated_dt__lt": datetime.datetime,
    "tracker__updated_dt__lte": datetime.datetime,
    "tracker__uuid": UUID,
    "tracker__uuid__in": list[UUID],
    "tracker__visibility": OsidbApiV2AffectsListTrackerVisibility,
    "updated_dt": datetime.datetime,
    "updated_dt__date": datetime.date,
    "updated_dt__date__gte": datetime.date,
    "updated_dt__date__lte": datetime.date,
    "updated_dt__gt": datetime.datetime,
    "updated_dt__gte": datetime.datetime,
    "updated_dt__lt": datetime.datetime,
    "updated_dt__lte": datetime.datetime,
    "uuid": UUID,
    "uuid__in": list[UUID],
    "visibility": OsidbApiV2AffectsListVisibility,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    affectedness: Union[Unset, OsidbApiV2AffectsListAffectedness] = UNSET,
    affectedness_in: Union[
        Unset, list[OsidbApiV2AffectsListAffectednessInItem]
    ] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cve_id: Union[Unset, str] = UNSET,
    cve_id_in: Union[Unset, list[str]] = UNSET,
    cvss_scores_comment: Union[Unset, str] = UNSET,
    cvss_scores_comment_in: Union[Unset, list[str]] = UNSET,
    cvss_scores_created_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, str] = UNSET,
    cvss_scores_issuer: Union[Unset, OsidbApiV2AffectsListCvssScoresIssuer] = UNSET,
    cvss_scores_issuer_in: Union[
        Unset, list[OsidbApiV2AffectsListCvssScoresIssuerInItem]
    ] = UNSET,
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
    cvss_scores_uuid_in: Union[Unset, list[UUID]] = UNSET,
    cvss_scores_vector: Union[Unset, str] = UNSET,
    cvss_scores_vector_in: Union[Unset, list[str]] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_components: Union[Unset, list[str]] = UNSET,
    flaw_components_in: Union[Unset, list[str]] = UNSET,
    flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, str] = UNSET,
    flaw_cve_id_in: Union[Unset, list[str]] = UNSET,
    flaw_cwe_id: Union[Unset, str] = UNSET,
    flaw_cwe_id_in: Union[Unset, list[str]] = UNSET,
    flaw_embargoed: Union[Unset, bool] = UNSET,
    flaw_impact: Union[Unset, OsidbApiV2AffectsListFlawImpact] = UNSET,
    flaw_impact_in: Union[Unset, list[OsidbApiV2AffectsListFlawImpactInItem]] = UNSET,
    flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, OsidbApiV2AffectsListFlawSource] = UNSET,
    flaw_source_in: Union[Unset, list[OsidbApiV2AffectsListFlawSourceInItem]] = UNSET,
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
    flaw_uuid_in: Union[Unset, list[UUID]] = UNSET,
    flaw_visibility: Union[Unset, OsidbApiV2AffectsListFlawVisibility] = UNSET,
    flaw_workflow_state: Union[
        Unset, list[OsidbApiV2AffectsListFlawWorkflowStateItem]
    ] = UNSET,
    impact: Union[Unset, OsidbApiV2AffectsListImpact] = UNSET,
    impact_in: Union[Unset, list[OsidbApiV2AffectsListImpactInItem]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV2AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, str] = UNSET,
    ps_component_in: Union[Unset, list[str]] = UNSET,
    ps_module: Union[Unset, str] = UNSET,
    ps_module_in: Union[Unset, list[str]] = UNSET,
    ps_update_stream: Union[Unset, str] = UNSET,
    ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    purl: Union[Unset, str] = UNSET,
    purl_in: Union[Unset, list[str]] = UNSET,
    resolution: Union[Unset, OsidbApiV2AffectsListResolution] = UNSET,
    resolution_in: Union[Unset, list[OsidbApiV2AffectsListResolutionInItem]] = UNSET,
    subpackage_purls: Union[Unset, str] = UNSET,
    subpackage_purls_in: Union[Unset, list[str]] = UNSET,
    subpackage_purls_isempty: Union[Unset, bool] = UNSET,
    tracker_created_dt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_date: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    tracker_embargoed: Union[Unset, bool] = UNSET,
    tracker_external_system_id: Union[Unset, str] = UNSET,
    tracker_external_system_id_in: Union[Unset, list[str]] = UNSET,
    tracker_isnull: Union[Unset, bool] = UNSET,
    tracker_ps_update_stream: Union[Unset, str] = UNSET,
    tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    tracker_resolution: Union[Unset, str] = UNSET,
    tracker_resolution_in: Union[Unset, list[str]] = UNSET,
    tracker_status: Union[Unset, str] = UNSET,
    tracker_status_in: Union[Unset, list[str]] = UNSET,
    tracker_type: Union[Unset, OsidbApiV2AffectsListTrackerType] = UNSET,
    tracker_type_in: Union[Unset, list[OsidbApiV2AffectsListTrackerTypeInItem]] = UNSET,
    tracker_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    tracker_uuid: Union[Unset, UUID] = UNSET,
    tracker_uuid_in: Union[Unset, list[UUID]] = UNSET,
    tracker_visibility: Union[Unset, OsidbApiV2AffectsListTrackerVisibility] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    visibility: Union[Unset, OsidbApiV2AffectsListVisibility] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    json_affectedness: Union[Unset, str] = UNSET
    if not isinstance(affectedness, Unset):
        json_affectedness = OsidbApiV2AffectsListAffectedness(affectedness).value

    params["affectedness"] = json_affectedness

    json_affectedness_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affectedness_in, Unset):
        json_affectedness_in = []
        for affectedness_in_item_data in affectedness_in:
            affectedness_in_item: str = UNSET
            if not isinstance(affectedness_in_item_data, Unset):
                affectedness_in_item = OsidbApiV2AffectsListAffectednessInItem(
                    affectedness_in_item_data
                ).value

            json_affectedness_in.append(affectedness_in_item)

    params["affectedness__in"] = json_affectedness_in

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

    params["cve_id"] = cve_id

    json_cve_id_in: Union[Unset, list[str]] = UNSET
    if not isinstance(cve_id_in, Unset):
        json_cve_id_in = cve_id_in

    params["cve_id__in"] = json_cve_id_in

    params["cvss_scores__comment"] = cvss_scores_comment

    json_cvss_scores_comment_in: Union[Unset, list[str]] = UNSET
    if not isinstance(cvss_scores_comment_in, Unset):
        json_cvss_scores_comment_in = cvss_scores_comment_in

    params["cvss_scores__comment__in"] = json_cvss_scores_comment_in

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
        json_cvss_scores_issuer = OsidbApiV2AffectsListCvssScoresIssuer(
            cvss_scores_issuer
        ).value

    params["cvss_scores__issuer"] = json_cvss_scores_issuer

    json_cvss_scores_issuer_in: Union[Unset, list[str]] = UNSET
    if not isinstance(cvss_scores_issuer_in, Unset):
        json_cvss_scores_issuer_in = []
        for cvss_scores_issuer_in_item_data in cvss_scores_issuer_in:
            cvss_scores_issuer_in_item: str = UNSET
            if not isinstance(cvss_scores_issuer_in_item_data, Unset):
                cvss_scores_issuer_in_item = (
                    OsidbApiV2AffectsListCvssScoresIssuerInItem(
                        cvss_scores_issuer_in_item_data
                    ).value
                )

            json_cvss_scores_issuer_in.append(cvss_scores_issuer_in_item)

    params["cvss_scores__issuer__in"] = json_cvss_scores_issuer_in

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

    json_cvss_scores_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(cvss_scores_uuid_in, Unset):
        json_cvss_scores_uuid_in = []
        for cvss_scores_uuid_in_item_data in cvss_scores_uuid_in:
            cvss_scores_uuid_in_item: str = UNSET
            if not isinstance(cvss_scores_uuid_in_item_data, Unset):
                cvss_scores_uuid_in_item = str(cvss_scores_uuid_in_item_data)

            json_cvss_scores_uuid_in.append(cvss_scores_uuid_in_item)

    params["cvss_scores__uuid__in"] = json_cvss_scores_uuid_in

    params["cvss_scores__vector"] = cvss_scores_vector

    json_cvss_scores_vector_in: Union[Unset, list[str]] = UNSET
    if not isinstance(cvss_scores_vector_in, Unset):
        json_cvss_scores_vector_in = cvss_scores_vector_in

    params["cvss_scores__vector__in"] = json_cvss_scores_vector_in

    params["embargoed"] = embargoed

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    json_flaw_components: Union[Unset, list[str]] = UNSET
    if not isinstance(flaw_components, Unset):
        json_flaw_components = flaw_components

    params["flaw__components"] = json_flaw_components

    json_flaw_components_in: Union[Unset, list[str]] = UNSET
    if not isinstance(flaw_components_in, Unset):
        json_flaw_components_in = flaw_components_in

    params["flaw__components__in"] = json_flaw_components_in

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

    json_flaw_cve_id_in: Union[Unset, list[str]] = UNSET
    if not isinstance(flaw_cve_id_in, Unset):
        json_flaw_cve_id_in = flaw_cve_id_in

    params["flaw__cve_id__in"] = json_flaw_cve_id_in

    params["flaw__cwe_id"] = flaw_cwe_id

    json_flaw_cwe_id_in: Union[Unset, list[str]] = UNSET
    if not isinstance(flaw_cwe_id_in, Unset):
        json_flaw_cwe_id_in = flaw_cwe_id_in

    params["flaw__cwe_id__in"] = json_flaw_cwe_id_in

    params["flaw__embargoed"] = flaw_embargoed

    json_flaw_impact: Union[Unset, str] = UNSET
    if not isinstance(flaw_impact, Unset):
        json_flaw_impact = OsidbApiV2AffectsListFlawImpact(flaw_impact).value

    params["flaw__impact"] = json_flaw_impact

    json_flaw_impact_in: Union[Unset, list[str]] = UNSET
    if not isinstance(flaw_impact_in, Unset):
        json_flaw_impact_in = []
        for flaw_impact_in_item_data in flaw_impact_in:
            flaw_impact_in_item: str = UNSET
            if not isinstance(flaw_impact_in_item_data, Unset):
                flaw_impact_in_item = OsidbApiV2AffectsListFlawImpactInItem(
                    flaw_impact_in_item_data
                ).value

            json_flaw_impact_in.append(flaw_impact_in_item)

    params["flaw__impact__in"] = json_flaw_impact_in

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
        json_flaw_source = OsidbApiV2AffectsListFlawSource(flaw_source).value

    params["flaw__source"] = json_flaw_source

    json_flaw_source_in: Union[Unset, list[str]] = UNSET
    if not isinstance(flaw_source_in, Unset):
        json_flaw_source_in = []
        for flaw_source_in_item_data in flaw_source_in:
            flaw_source_in_item: str = UNSET
            if not isinstance(flaw_source_in_item_data, Unset):
                flaw_source_in_item = OsidbApiV2AffectsListFlawSourceInItem(
                    flaw_source_in_item_data
                ).value

            json_flaw_source_in.append(flaw_source_in_item)

    params["flaw__source__in"] = json_flaw_source_in

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

    json_flaw_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(flaw_uuid_in, Unset):
        json_flaw_uuid_in = []
        for flaw_uuid_in_item_data in flaw_uuid_in:
            flaw_uuid_in_item: str = UNSET
            if not isinstance(flaw_uuid_in_item_data, Unset):
                flaw_uuid_in_item = str(flaw_uuid_in_item_data)

            json_flaw_uuid_in.append(flaw_uuid_in_item)

    params["flaw__uuid__in"] = json_flaw_uuid_in

    json_flaw_visibility: Union[Unset, str] = UNSET
    if not isinstance(flaw_visibility, Unset):
        json_flaw_visibility = OsidbApiV2AffectsListFlawVisibility(
            flaw_visibility
        ).value

    params["flaw__visibility"] = json_flaw_visibility

    json_flaw_workflow_state: Union[Unset, list[str]] = UNSET
    if not isinstance(flaw_workflow_state, Unset):
        json_flaw_workflow_state = []
        for flaw_workflow_state_item_data in flaw_workflow_state:
            flaw_workflow_state_item: str = UNSET
            if not isinstance(flaw_workflow_state_item_data, Unset):
                flaw_workflow_state_item = OsidbApiV2AffectsListFlawWorkflowStateItem(
                    flaw_workflow_state_item_data
                ).value

            json_flaw_workflow_state.append(flaw_workflow_state_item)

    params["flaw__workflow_state"] = json_flaw_workflow_state

    json_impact: Union[Unset, str] = UNSET
    if not isinstance(impact, Unset):
        json_impact = OsidbApiV2AffectsListImpact(impact).value

    params["impact"] = json_impact

    json_impact_in: Union[Unset, list[str]] = UNSET
    if not isinstance(impact_in, Unset):
        json_impact_in = []
        for impact_in_item_data in impact_in:
            impact_in_item: str = UNSET
            if not isinstance(impact_in_item_data, Unset):
                impact_in_item = OsidbApiV2AffectsListImpactInItem(
                    impact_in_item_data
                ).value

            json_impact_in.append(impact_in_item)

    params["impact__in"] = json_impact_in

    json_include_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(include_fields, Unset):
        json_include_fields = include_fields

    params["include_fields"] = json_include_fields

    params["include_history"] = include_history

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
                order_item = OsidbApiV2AffectsListOrderItem(order_item_data).value

            json_order.append(order_item)

    params["order"] = json_order

    params["ps_component"] = ps_component

    json_ps_component_in: Union[Unset, list[str]] = UNSET
    if not isinstance(ps_component_in, Unset):
        json_ps_component_in = ps_component_in

    params["ps_component__in"] = json_ps_component_in

    params["ps_module"] = ps_module

    json_ps_module_in: Union[Unset, list[str]] = UNSET
    if not isinstance(ps_module_in, Unset):
        json_ps_module_in = ps_module_in

    params["ps_module__in"] = json_ps_module_in

    params["ps_update_stream"] = ps_update_stream

    json_ps_update_stream_in: Union[Unset, list[str]] = UNSET
    if not isinstance(ps_update_stream_in, Unset):
        json_ps_update_stream_in = ps_update_stream_in

    params["ps_update_stream__in"] = json_ps_update_stream_in

    params["purl"] = purl

    json_purl_in: Union[Unset, list[str]] = UNSET
    if not isinstance(purl_in, Unset):
        json_purl_in = purl_in

    params["purl__in"] = json_purl_in

    json_resolution: Union[Unset, str] = UNSET
    if not isinstance(resolution, Unset):
        json_resolution = OsidbApiV2AffectsListResolution(resolution).value

    params["resolution"] = json_resolution

    json_resolution_in: Union[Unset, list[str]] = UNSET
    if not isinstance(resolution_in, Unset):
        json_resolution_in = []
        for resolution_in_item_data in resolution_in:
            resolution_in_item: str = UNSET
            if not isinstance(resolution_in_item_data, Unset):
                resolution_in_item = OsidbApiV2AffectsListResolutionInItem(
                    resolution_in_item_data
                ).value

            json_resolution_in.append(resolution_in_item)

    params["resolution__in"] = json_resolution_in

    params["subpackage_purls"] = subpackage_purls

    json_subpackage_purls_in: Union[Unset, list[str]] = UNSET
    if not isinstance(subpackage_purls_in, Unset):
        json_subpackage_purls_in = subpackage_purls_in

    params["subpackage_purls__in"] = json_subpackage_purls_in

    params["subpackage_purls__isempty"] = subpackage_purls_isempty

    json_tracker_created_dt: Union[Unset, str] = UNSET
    if not isinstance(tracker_created_dt, Unset):
        json_tracker_created_dt = tracker_created_dt.isoformat()

    params["tracker__created_dt"] = json_tracker_created_dt

    json_tracker_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(tracker_created_dt_date, Unset):
        json_tracker_created_dt_date = tracker_created_dt_date.isoformat()

    params["tracker__created_dt__date"] = json_tracker_created_dt_date

    json_tracker_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(tracker_created_dt_date_gte, Unset):
        json_tracker_created_dt_date_gte = tracker_created_dt_date_gte.isoformat()

    params["tracker__created_dt__date__gte"] = json_tracker_created_dt_date_gte

    json_tracker_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(tracker_created_dt_date_lte, Unset):
        json_tracker_created_dt_date_lte = tracker_created_dt_date_lte.isoformat()

    params["tracker__created_dt__date__lte"] = json_tracker_created_dt_date_lte

    json_tracker_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(tracker_created_dt_gt, Unset):
        json_tracker_created_dt_gt = tracker_created_dt_gt.isoformat()

    params["tracker__created_dt__gt"] = json_tracker_created_dt_gt

    json_tracker_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(tracker_created_dt_gte, Unset):
        json_tracker_created_dt_gte = tracker_created_dt_gte.isoformat()

    params["tracker__created_dt__gte"] = json_tracker_created_dt_gte

    json_tracker_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(tracker_created_dt_lt, Unset):
        json_tracker_created_dt_lt = tracker_created_dt_lt.isoformat()

    params["tracker__created_dt__lt"] = json_tracker_created_dt_lt

    json_tracker_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(tracker_created_dt_lte, Unset):
        json_tracker_created_dt_lte = tracker_created_dt_lte.isoformat()

    params["tracker__created_dt__lte"] = json_tracker_created_dt_lte

    params["tracker__embargoed"] = tracker_embargoed

    params["tracker__external_system_id"] = tracker_external_system_id

    json_tracker_external_system_id_in: Union[Unset, list[str]] = UNSET
    if not isinstance(tracker_external_system_id_in, Unset):
        json_tracker_external_system_id_in = tracker_external_system_id_in

    params["tracker__external_system_id__in"] = json_tracker_external_system_id_in

    params["tracker__isnull"] = tracker_isnull

    params["tracker__ps_update_stream"] = tracker_ps_update_stream

    json_tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET
    if not isinstance(tracker_ps_update_stream_in, Unset):
        json_tracker_ps_update_stream_in = tracker_ps_update_stream_in

    params["tracker__ps_update_stream__in"] = json_tracker_ps_update_stream_in

    params["tracker__resolution"] = tracker_resolution

    json_tracker_resolution_in: Union[Unset, list[str]] = UNSET
    if not isinstance(tracker_resolution_in, Unset):
        json_tracker_resolution_in = tracker_resolution_in

    params["tracker__resolution__in"] = json_tracker_resolution_in

    params["tracker__status"] = tracker_status

    json_tracker_status_in: Union[Unset, list[str]] = UNSET
    if not isinstance(tracker_status_in, Unset):
        json_tracker_status_in = tracker_status_in

    params["tracker__status__in"] = json_tracker_status_in

    json_tracker_type: Union[Unset, str] = UNSET
    if not isinstance(tracker_type, Unset):
        json_tracker_type = OsidbApiV2AffectsListTrackerType(tracker_type).value

    params["tracker__type"] = json_tracker_type

    json_tracker_type_in: Union[Unset, list[str]] = UNSET
    if not isinstance(tracker_type_in, Unset):
        json_tracker_type_in = []
        for tracker_type_in_item_data in tracker_type_in:
            tracker_type_in_item: str = UNSET
            if not isinstance(tracker_type_in_item_data, Unset):
                tracker_type_in_item = OsidbApiV2AffectsListTrackerTypeInItem(
                    tracker_type_in_item_data
                ).value

            json_tracker_type_in.append(tracker_type_in_item)

    params["tracker__type__in"] = json_tracker_type_in

    json_tracker_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(tracker_updated_dt, Unset):
        json_tracker_updated_dt = tracker_updated_dt.isoformat()

    params["tracker__updated_dt"] = json_tracker_updated_dt

    json_tracker_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(tracker_updated_dt_date, Unset):
        json_tracker_updated_dt_date = tracker_updated_dt_date.isoformat()

    params["tracker__updated_dt__date"] = json_tracker_updated_dt_date

    json_tracker_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(tracker_updated_dt_date_gte, Unset):
        json_tracker_updated_dt_date_gte = tracker_updated_dt_date_gte.isoformat()

    params["tracker__updated_dt__date__gte"] = json_tracker_updated_dt_date_gte

    json_tracker_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(tracker_updated_dt_date_lte, Unset):
        json_tracker_updated_dt_date_lte = tracker_updated_dt_date_lte.isoformat()

    params["tracker__updated_dt__date__lte"] = json_tracker_updated_dt_date_lte

    json_tracker_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(tracker_updated_dt_gt, Unset):
        json_tracker_updated_dt_gt = tracker_updated_dt_gt.isoformat()

    params["tracker__updated_dt__gt"] = json_tracker_updated_dt_gt

    json_tracker_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(tracker_updated_dt_gte, Unset):
        json_tracker_updated_dt_gte = tracker_updated_dt_gte.isoformat()

    params["tracker__updated_dt__gte"] = json_tracker_updated_dt_gte

    json_tracker_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(tracker_updated_dt_lt, Unset):
        json_tracker_updated_dt_lt = tracker_updated_dt_lt.isoformat()

    params["tracker__updated_dt__lt"] = json_tracker_updated_dt_lt

    json_tracker_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(tracker_updated_dt_lte, Unset):
        json_tracker_updated_dt_lte = tracker_updated_dt_lte.isoformat()

    params["tracker__updated_dt__lte"] = json_tracker_updated_dt_lte

    json_tracker_uuid: Union[Unset, str] = UNSET
    if not isinstance(tracker_uuid, Unset):
        json_tracker_uuid = str(tracker_uuid)

    params["tracker__uuid"] = json_tracker_uuid

    json_tracker_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(tracker_uuid_in, Unset):
        json_tracker_uuid_in = []
        for tracker_uuid_in_item_data in tracker_uuid_in:
            tracker_uuid_in_item: str = UNSET
            if not isinstance(tracker_uuid_in_item_data, Unset):
                tracker_uuid_in_item = str(tracker_uuid_in_item_data)

            json_tracker_uuid_in.append(tracker_uuid_in_item)

    params["tracker__uuid__in"] = json_tracker_uuid_in

    json_tracker_visibility: Union[Unset, str] = UNSET
    if not isinstance(tracker_visibility, Unset):
        json_tracker_visibility = OsidbApiV2AffectsListTrackerVisibility(
            tracker_visibility
        ).value

    params["tracker__visibility"] = json_tracker_visibility

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

    json_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(uuid_in, Unset):
        json_uuid_in = []
        for uuid_in_item_data in uuid_in:
            uuid_in_item: str = UNSET
            if not isinstance(uuid_in_item_data, Unset):
                uuid_in_item = str(uuid_in_item_data)

            json_uuid_in.append(uuid_in_item)

    params["uuid__in"] = json_uuid_in

    json_visibility: Union[Unset, str] = UNSET
    if not isinstance(visibility, Unset):
        json_visibility = OsidbApiV2AffectsListVisibility(visibility).value

    params["visibility"] = json_visibility

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v2/affects",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV2AffectsListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV2AffectsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV2AffectsListResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV2AffectsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    affectedness: Union[Unset, OsidbApiV2AffectsListAffectedness] = UNSET,
    affectedness_in: Union[
        Unset, list[OsidbApiV2AffectsListAffectednessInItem]
    ] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cve_id: Union[Unset, str] = UNSET,
    cve_id_in: Union[Unset, list[str]] = UNSET,
    cvss_scores_comment: Union[Unset, str] = UNSET,
    cvss_scores_comment_in: Union[Unset, list[str]] = UNSET,
    cvss_scores_created_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, str] = UNSET,
    cvss_scores_issuer: Union[Unset, OsidbApiV2AffectsListCvssScoresIssuer] = UNSET,
    cvss_scores_issuer_in: Union[
        Unset, list[OsidbApiV2AffectsListCvssScoresIssuerInItem]
    ] = UNSET,
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
    cvss_scores_uuid_in: Union[Unset, list[UUID]] = UNSET,
    cvss_scores_vector: Union[Unset, str] = UNSET,
    cvss_scores_vector_in: Union[Unset, list[str]] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_components: Union[Unset, list[str]] = UNSET,
    flaw_components_in: Union[Unset, list[str]] = UNSET,
    flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, str] = UNSET,
    flaw_cve_id_in: Union[Unset, list[str]] = UNSET,
    flaw_cwe_id: Union[Unset, str] = UNSET,
    flaw_cwe_id_in: Union[Unset, list[str]] = UNSET,
    flaw_embargoed: Union[Unset, bool] = UNSET,
    flaw_impact: Union[Unset, OsidbApiV2AffectsListFlawImpact] = UNSET,
    flaw_impact_in: Union[Unset, list[OsidbApiV2AffectsListFlawImpactInItem]] = UNSET,
    flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, OsidbApiV2AffectsListFlawSource] = UNSET,
    flaw_source_in: Union[Unset, list[OsidbApiV2AffectsListFlawSourceInItem]] = UNSET,
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
    flaw_uuid_in: Union[Unset, list[UUID]] = UNSET,
    flaw_visibility: Union[Unset, OsidbApiV2AffectsListFlawVisibility] = UNSET,
    flaw_workflow_state: Union[
        Unset, list[OsidbApiV2AffectsListFlawWorkflowStateItem]
    ] = UNSET,
    impact: Union[Unset, OsidbApiV2AffectsListImpact] = UNSET,
    impact_in: Union[Unset, list[OsidbApiV2AffectsListImpactInItem]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV2AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, str] = UNSET,
    ps_component_in: Union[Unset, list[str]] = UNSET,
    ps_module: Union[Unset, str] = UNSET,
    ps_module_in: Union[Unset, list[str]] = UNSET,
    ps_update_stream: Union[Unset, str] = UNSET,
    ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    purl: Union[Unset, str] = UNSET,
    purl_in: Union[Unset, list[str]] = UNSET,
    resolution: Union[Unset, OsidbApiV2AffectsListResolution] = UNSET,
    resolution_in: Union[Unset, list[OsidbApiV2AffectsListResolutionInItem]] = UNSET,
    subpackage_purls: Union[Unset, str] = UNSET,
    subpackage_purls_in: Union[Unset, list[str]] = UNSET,
    subpackage_purls_isempty: Union[Unset, bool] = UNSET,
    tracker_created_dt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_date: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    tracker_embargoed: Union[Unset, bool] = UNSET,
    tracker_external_system_id: Union[Unset, str] = UNSET,
    tracker_external_system_id_in: Union[Unset, list[str]] = UNSET,
    tracker_isnull: Union[Unset, bool] = UNSET,
    tracker_ps_update_stream: Union[Unset, str] = UNSET,
    tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    tracker_resolution: Union[Unset, str] = UNSET,
    tracker_resolution_in: Union[Unset, list[str]] = UNSET,
    tracker_status: Union[Unset, str] = UNSET,
    tracker_status_in: Union[Unset, list[str]] = UNSET,
    tracker_type: Union[Unset, OsidbApiV2AffectsListTrackerType] = UNSET,
    tracker_type_in: Union[Unset, list[OsidbApiV2AffectsListTrackerTypeInItem]] = UNSET,
    tracker_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    tracker_uuid: Union[Unset, UUID] = UNSET,
    tracker_uuid_in: Union[Unset, list[UUID]] = UNSET,
    tracker_visibility: Union[Unset, OsidbApiV2AffectsListTrackerVisibility] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    visibility: Union[Unset, OsidbApiV2AffectsListVisibility] = UNSET,
) -> Response[OsidbApiV2AffectsListResponse200]:
    """
    Args:
        affectedness (Union[Unset, OsidbApiV2AffectsListAffectedness]):
        affectedness_in (Union[Unset, list[OsidbApiV2AffectsListAffectednessInItem]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cve_id (Union[Unset, str]):
        cve_id_in (Union[Unset, list[str]]):
        cvss_scores_comment (Union[Unset, str]):
        cvss_scores_comment_in (Union[Unset, list[str]]):
        cvss_scores_created_dt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_date (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_cvss_version (Union[Unset, str]):
        cvss_scores_issuer (Union[Unset, OsidbApiV2AffectsListCvssScoresIssuer]):
        cvss_scores_issuer_in (Union[Unset, list[OsidbApiV2AffectsListCvssScoresIssuerInItem]]):
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
        cvss_scores_uuid_in (Union[Unset, list[UUID]]):
        cvss_scores_vector (Union[Unset, str]):
        cvss_scores_vector_in (Union[Unset, list[str]]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_components (Union[Unset, list[str]]):
        flaw_components_in (Union[Unset, list[str]]):
        flaw_created_dt (Union[Unset, datetime.datetime]):
        flaw_created_dt_date (Union[Unset, datetime.date]):
        flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_cve_id (Union[Unset, str]):
        flaw_cve_id_in (Union[Unset, list[str]]):
        flaw_cwe_id (Union[Unset, str]):
        flaw_cwe_id_in (Union[Unset, list[str]]):
        flaw_embargoed (Union[Unset, bool]):
        flaw_impact (Union[Unset, OsidbApiV2AffectsListFlawImpact]):
        flaw_impact_in (Union[Unset, list[OsidbApiV2AffectsListFlawImpactInItem]]):
        flaw_reported_dt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_date (Union[Unset, datetime.date]):
        flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        flaw_source (Union[Unset, OsidbApiV2AffectsListFlawSource]):
        flaw_source_in (Union[Unset, list[OsidbApiV2AffectsListFlawSourceInItem]]):
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
        flaw_uuid_in (Union[Unset, list[UUID]]):
        flaw_visibility (Union[Unset, OsidbApiV2AffectsListFlawVisibility]):
        flaw_workflow_state (Union[Unset, list[OsidbApiV2AffectsListFlawWorkflowStateItem]]):
        impact (Union[Unset, OsidbApiV2AffectsListImpact]):
        impact_in (Union[Unset, list[OsidbApiV2AffectsListImpactInItem]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV2AffectsListOrderItem]]):
        ps_component (Union[Unset, str]):
        ps_component_in (Union[Unset, list[str]]):
        ps_module (Union[Unset, str]):
        ps_module_in (Union[Unset, list[str]]):
        ps_update_stream (Union[Unset, str]):
        ps_update_stream_in (Union[Unset, list[str]]):
        purl (Union[Unset, str]):
        purl_in (Union[Unset, list[str]]):
        resolution (Union[Unset, OsidbApiV2AffectsListResolution]):
        resolution_in (Union[Unset, list[OsidbApiV2AffectsListResolutionInItem]]):
        subpackage_purls (Union[Unset, str]):
        subpackage_purls_in (Union[Unset, list[str]]):
        subpackage_purls_isempty (Union[Unset, bool]):
        tracker_created_dt (Union[Unset, datetime.datetime]):
        tracker_created_dt_date (Union[Unset, datetime.date]):
        tracker_created_dt_date_gte (Union[Unset, datetime.date]):
        tracker_created_dt_date_lte (Union[Unset, datetime.date]):
        tracker_created_dt_gt (Union[Unset, datetime.datetime]):
        tracker_created_dt_gte (Union[Unset, datetime.datetime]):
        tracker_created_dt_lt (Union[Unset, datetime.datetime]):
        tracker_created_dt_lte (Union[Unset, datetime.datetime]):
        tracker_embargoed (Union[Unset, bool]):
        tracker_external_system_id (Union[Unset, str]):
        tracker_external_system_id_in (Union[Unset, list[str]]):
        tracker_isnull (Union[Unset, bool]):
        tracker_ps_update_stream (Union[Unset, str]):
        tracker_ps_update_stream_in (Union[Unset, list[str]]):
        tracker_resolution (Union[Unset, str]):
        tracker_resolution_in (Union[Unset, list[str]]):
        tracker_status (Union[Unset, str]):
        tracker_status_in (Union[Unset, list[str]]):
        tracker_type (Union[Unset, OsidbApiV2AffectsListTrackerType]):
        tracker_type_in (Union[Unset, list[OsidbApiV2AffectsListTrackerTypeInItem]]):
        tracker_updated_dt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_date (Union[Unset, datetime.date]):
        tracker_updated_dt_date_gte (Union[Unset, datetime.date]):
        tracker_updated_dt_date_lte (Union[Unset, datetime.date]):
        tracker_updated_dt_gt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_gte (Union[Unset, datetime.datetime]):
        tracker_updated_dt_lt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_lte (Union[Unset, datetime.datetime]):
        tracker_uuid (Union[Unset, UUID]):
        tracker_uuid_in (Union[Unset, list[UUID]]):
        tracker_visibility (Union[Unset, OsidbApiV2AffectsListTrackerVisibility]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        uuid_in (Union[Unset, list[UUID]]):
        visibility (Union[Unset, OsidbApiV2AffectsListVisibility]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2AffectsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        affectedness=affectedness,
        affectedness_in=affectedness_in,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cve_id=cve_id,
        cve_id_in=cve_id_in,
        cvss_scores_comment=cvss_scores_comment,
        cvss_scores_comment_in=cvss_scores_comment_in,
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
        cvss_scores_issuer_in=cvss_scores_issuer_in,
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
        cvss_scores_uuid_in=cvss_scores_uuid_in,
        cvss_scores_vector=cvss_scores_vector,
        cvss_scores_vector_in=cvss_scores_vector_in,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        flaw_components=flaw_components,
        flaw_components_in=flaw_components_in,
        flaw_created_dt=flaw_created_dt,
        flaw_created_dt_date=flaw_created_dt_date,
        flaw_created_dt_date_gte=flaw_created_dt_date_gte,
        flaw_created_dt_date_lte=flaw_created_dt_date_lte,
        flaw_created_dt_gt=flaw_created_dt_gt,
        flaw_created_dt_gte=flaw_created_dt_gte,
        flaw_created_dt_lt=flaw_created_dt_lt,
        flaw_created_dt_lte=flaw_created_dt_lte,
        flaw_cve_id=flaw_cve_id,
        flaw_cve_id_in=flaw_cve_id_in,
        flaw_cwe_id=flaw_cwe_id,
        flaw_cwe_id_in=flaw_cwe_id_in,
        flaw_embargoed=flaw_embargoed,
        flaw_impact=flaw_impact,
        flaw_impact_in=flaw_impact_in,
        flaw_reported_dt=flaw_reported_dt,
        flaw_reported_dt_date=flaw_reported_dt_date,
        flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
        flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
        flaw_reported_dt_gt=flaw_reported_dt_gt,
        flaw_reported_dt_gte=flaw_reported_dt_gte,
        flaw_reported_dt_lt=flaw_reported_dt_lt,
        flaw_reported_dt_lte=flaw_reported_dt_lte,
        flaw_source=flaw_source,
        flaw_source_in=flaw_source_in,
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
        flaw_uuid_in=flaw_uuid_in,
        flaw_visibility=flaw_visibility,
        flaw_workflow_state=flaw_workflow_state,
        impact=impact,
        impact_in=impact_in,
        include_fields=include_fields,
        include_history=include_history,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        order=order,
        ps_component=ps_component,
        ps_component_in=ps_component_in,
        ps_module=ps_module,
        ps_module_in=ps_module_in,
        ps_update_stream=ps_update_stream,
        ps_update_stream_in=ps_update_stream_in,
        purl=purl,
        purl_in=purl_in,
        resolution=resolution,
        resolution_in=resolution_in,
        subpackage_purls=subpackage_purls,
        subpackage_purls_in=subpackage_purls_in,
        subpackage_purls_isempty=subpackage_purls_isempty,
        tracker_created_dt=tracker_created_dt,
        tracker_created_dt_date=tracker_created_dt_date,
        tracker_created_dt_date_gte=tracker_created_dt_date_gte,
        tracker_created_dt_date_lte=tracker_created_dt_date_lte,
        tracker_created_dt_gt=tracker_created_dt_gt,
        tracker_created_dt_gte=tracker_created_dt_gte,
        tracker_created_dt_lt=tracker_created_dt_lt,
        tracker_created_dt_lte=tracker_created_dt_lte,
        tracker_embargoed=tracker_embargoed,
        tracker_external_system_id=tracker_external_system_id,
        tracker_external_system_id_in=tracker_external_system_id_in,
        tracker_isnull=tracker_isnull,
        tracker_ps_update_stream=tracker_ps_update_stream,
        tracker_ps_update_stream_in=tracker_ps_update_stream_in,
        tracker_resolution=tracker_resolution,
        tracker_resolution_in=tracker_resolution_in,
        tracker_status=tracker_status,
        tracker_status_in=tracker_status_in,
        tracker_type=tracker_type,
        tracker_type_in=tracker_type_in,
        tracker_updated_dt=tracker_updated_dt,
        tracker_updated_dt_date=tracker_updated_dt_date,
        tracker_updated_dt_date_gte=tracker_updated_dt_date_gte,
        tracker_updated_dt_date_lte=tracker_updated_dt_date_lte,
        tracker_updated_dt_gt=tracker_updated_dt_gt,
        tracker_updated_dt_gte=tracker_updated_dt_gte,
        tracker_updated_dt_lt=tracker_updated_dt_lt,
        tracker_updated_dt_lte=tracker_updated_dt_lte,
        tracker_uuid=tracker_uuid,
        tracker_uuid_in=tracker_uuid_in,
        tracker_visibility=tracker_visibility,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
        uuid_in=uuid_in,
        visibility=visibility,
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
    affectedness: Union[Unset, OsidbApiV2AffectsListAffectedness] = UNSET,
    affectedness_in: Union[
        Unset, list[OsidbApiV2AffectsListAffectednessInItem]
    ] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cve_id: Union[Unset, str] = UNSET,
    cve_id_in: Union[Unset, list[str]] = UNSET,
    cvss_scores_comment: Union[Unset, str] = UNSET,
    cvss_scores_comment_in: Union[Unset, list[str]] = UNSET,
    cvss_scores_created_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, str] = UNSET,
    cvss_scores_issuer: Union[Unset, OsidbApiV2AffectsListCvssScoresIssuer] = UNSET,
    cvss_scores_issuer_in: Union[
        Unset, list[OsidbApiV2AffectsListCvssScoresIssuerInItem]
    ] = UNSET,
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
    cvss_scores_uuid_in: Union[Unset, list[UUID]] = UNSET,
    cvss_scores_vector: Union[Unset, str] = UNSET,
    cvss_scores_vector_in: Union[Unset, list[str]] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_components: Union[Unset, list[str]] = UNSET,
    flaw_components_in: Union[Unset, list[str]] = UNSET,
    flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, str] = UNSET,
    flaw_cve_id_in: Union[Unset, list[str]] = UNSET,
    flaw_cwe_id: Union[Unset, str] = UNSET,
    flaw_cwe_id_in: Union[Unset, list[str]] = UNSET,
    flaw_embargoed: Union[Unset, bool] = UNSET,
    flaw_impact: Union[Unset, OsidbApiV2AffectsListFlawImpact] = UNSET,
    flaw_impact_in: Union[Unset, list[OsidbApiV2AffectsListFlawImpactInItem]] = UNSET,
    flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, OsidbApiV2AffectsListFlawSource] = UNSET,
    flaw_source_in: Union[Unset, list[OsidbApiV2AffectsListFlawSourceInItem]] = UNSET,
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
    flaw_uuid_in: Union[Unset, list[UUID]] = UNSET,
    flaw_visibility: Union[Unset, OsidbApiV2AffectsListFlawVisibility] = UNSET,
    flaw_workflow_state: Union[
        Unset, list[OsidbApiV2AffectsListFlawWorkflowStateItem]
    ] = UNSET,
    impact: Union[Unset, OsidbApiV2AffectsListImpact] = UNSET,
    impact_in: Union[Unset, list[OsidbApiV2AffectsListImpactInItem]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV2AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, str] = UNSET,
    ps_component_in: Union[Unset, list[str]] = UNSET,
    ps_module: Union[Unset, str] = UNSET,
    ps_module_in: Union[Unset, list[str]] = UNSET,
    ps_update_stream: Union[Unset, str] = UNSET,
    ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    purl: Union[Unset, str] = UNSET,
    purl_in: Union[Unset, list[str]] = UNSET,
    resolution: Union[Unset, OsidbApiV2AffectsListResolution] = UNSET,
    resolution_in: Union[Unset, list[OsidbApiV2AffectsListResolutionInItem]] = UNSET,
    subpackage_purls: Union[Unset, str] = UNSET,
    subpackage_purls_in: Union[Unset, list[str]] = UNSET,
    subpackage_purls_isempty: Union[Unset, bool] = UNSET,
    tracker_created_dt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_date: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    tracker_embargoed: Union[Unset, bool] = UNSET,
    tracker_external_system_id: Union[Unset, str] = UNSET,
    tracker_external_system_id_in: Union[Unset, list[str]] = UNSET,
    tracker_isnull: Union[Unset, bool] = UNSET,
    tracker_ps_update_stream: Union[Unset, str] = UNSET,
    tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    tracker_resolution: Union[Unset, str] = UNSET,
    tracker_resolution_in: Union[Unset, list[str]] = UNSET,
    tracker_status: Union[Unset, str] = UNSET,
    tracker_status_in: Union[Unset, list[str]] = UNSET,
    tracker_type: Union[Unset, OsidbApiV2AffectsListTrackerType] = UNSET,
    tracker_type_in: Union[Unset, list[OsidbApiV2AffectsListTrackerTypeInItem]] = UNSET,
    tracker_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    tracker_uuid: Union[Unset, UUID] = UNSET,
    tracker_uuid_in: Union[Unset, list[UUID]] = UNSET,
    tracker_visibility: Union[Unset, OsidbApiV2AffectsListTrackerVisibility] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    visibility: Union[Unset, OsidbApiV2AffectsListVisibility] = UNSET,
) -> Optional[OsidbApiV2AffectsListResponse200]:
    """
    Args:
        affectedness (Union[Unset, OsidbApiV2AffectsListAffectedness]):
        affectedness_in (Union[Unset, list[OsidbApiV2AffectsListAffectednessInItem]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cve_id (Union[Unset, str]):
        cve_id_in (Union[Unset, list[str]]):
        cvss_scores_comment (Union[Unset, str]):
        cvss_scores_comment_in (Union[Unset, list[str]]):
        cvss_scores_created_dt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_date (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_cvss_version (Union[Unset, str]):
        cvss_scores_issuer (Union[Unset, OsidbApiV2AffectsListCvssScoresIssuer]):
        cvss_scores_issuer_in (Union[Unset, list[OsidbApiV2AffectsListCvssScoresIssuerInItem]]):
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
        cvss_scores_uuid_in (Union[Unset, list[UUID]]):
        cvss_scores_vector (Union[Unset, str]):
        cvss_scores_vector_in (Union[Unset, list[str]]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_components (Union[Unset, list[str]]):
        flaw_components_in (Union[Unset, list[str]]):
        flaw_created_dt (Union[Unset, datetime.datetime]):
        flaw_created_dt_date (Union[Unset, datetime.date]):
        flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_cve_id (Union[Unset, str]):
        flaw_cve_id_in (Union[Unset, list[str]]):
        flaw_cwe_id (Union[Unset, str]):
        flaw_cwe_id_in (Union[Unset, list[str]]):
        flaw_embargoed (Union[Unset, bool]):
        flaw_impact (Union[Unset, OsidbApiV2AffectsListFlawImpact]):
        flaw_impact_in (Union[Unset, list[OsidbApiV2AffectsListFlawImpactInItem]]):
        flaw_reported_dt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_date (Union[Unset, datetime.date]):
        flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        flaw_source (Union[Unset, OsidbApiV2AffectsListFlawSource]):
        flaw_source_in (Union[Unset, list[OsidbApiV2AffectsListFlawSourceInItem]]):
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
        flaw_uuid_in (Union[Unset, list[UUID]]):
        flaw_visibility (Union[Unset, OsidbApiV2AffectsListFlawVisibility]):
        flaw_workflow_state (Union[Unset, list[OsidbApiV2AffectsListFlawWorkflowStateItem]]):
        impact (Union[Unset, OsidbApiV2AffectsListImpact]):
        impact_in (Union[Unset, list[OsidbApiV2AffectsListImpactInItem]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV2AffectsListOrderItem]]):
        ps_component (Union[Unset, str]):
        ps_component_in (Union[Unset, list[str]]):
        ps_module (Union[Unset, str]):
        ps_module_in (Union[Unset, list[str]]):
        ps_update_stream (Union[Unset, str]):
        ps_update_stream_in (Union[Unset, list[str]]):
        purl (Union[Unset, str]):
        purl_in (Union[Unset, list[str]]):
        resolution (Union[Unset, OsidbApiV2AffectsListResolution]):
        resolution_in (Union[Unset, list[OsidbApiV2AffectsListResolutionInItem]]):
        subpackage_purls (Union[Unset, str]):
        subpackage_purls_in (Union[Unset, list[str]]):
        subpackage_purls_isempty (Union[Unset, bool]):
        tracker_created_dt (Union[Unset, datetime.datetime]):
        tracker_created_dt_date (Union[Unset, datetime.date]):
        tracker_created_dt_date_gte (Union[Unset, datetime.date]):
        tracker_created_dt_date_lte (Union[Unset, datetime.date]):
        tracker_created_dt_gt (Union[Unset, datetime.datetime]):
        tracker_created_dt_gte (Union[Unset, datetime.datetime]):
        tracker_created_dt_lt (Union[Unset, datetime.datetime]):
        tracker_created_dt_lte (Union[Unset, datetime.datetime]):
        tracker_embargoed (Union[Unset, bool]):
        tracker_external_system_id (Union[Unset, str]):
        tracker_external_system_id_in (Union[Unset, list[str]]):
        tracker_isnull (Union[Unset, bool]):
        tracker_ps_update_stream (Union[Unset, str]):
        tracker_ps_update_stream_in (Union[Unset, list[str]]):
        tracker_resolution (Union[Unset, str]):
        tracker_resolution_in (Union[Unset, list[str]]):
        tracker_status (Union[Unset, str]):
        tracker_status_in (Union[Unset, list[str]]):
        tracker_type (Union[Unset, OsidbApiV2AffectsListTrackerType]):
        tracker_type_in (Union[Unset, list[OsidbApiV2AffectsListTrackerTypeInItem]]):
        tracker_updated_dt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_date (Union[Unset, datetime.date]):
        tracker_updated_dt_date_gte (Union[Unset, datetime.date]):
        tracker_updated_dt_date_lte (Union[Unset, datetime.date]):
        tracker_updated_dt_gt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_gte (Union[Unset, datetime.datetime]):
        tracker_updated_dt_lt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_lte (Union[Unset, datetime.datetime]):
        tracker_uuid (Union[Unset, UUID]):
        tracker_uuid_in (Union[Unset, list[UUID]]):
        tracker_visibility (Union[Unset, OsidbApiV2AffectsListTrackerVisibility]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        uuid_in (Union[Unset, list[UUID]]):
        visibility (Union[Unset, OsidbApiV2AffectsListVisibility]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2AffectsListResponse200
    """

    return sync_detailed(
        client=client,
        affectedness=affectedness,
        affectedness_in=affectedness_in,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cve_id=cve_id,
        cve_id_in=cve_id_in,
        cvss_scores_comment=cvss_scores_comment,
        cvss_scores_comment_in=cvss_scores_comment_in,
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
        cvss_scores_issuer_in=cvss_scores_issuer_in,
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
        cvss_scores_uuid_in=cvss_scores_uuid_in,
        cvss_scores_vector=cvss_scores_vector,
        cvss_scores_vector_in=cvss_scores_vector_in,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        flaw_components=flaw_components,
        flaw_components_in=flaw_components_in,
        flaw_created_dt=flaw_created_dt,
        flaw_created_dt_date=flaw_created_dt_date,
        flaw_created_dt_date_gte=flaw_created_dt_date_gte,
        flaw_created_dt_date_lte=flaw_created_dt_date_lte,
        flaw_created_dt_gt=flaw_created_dt_gt,
        flaw_created_dt_gte=flaw_created_dt_gte,
        flaw_created_dt_lt=flaw_created_dt_lt,
        flaw_created_dt_lte=flaw_created_dt_lte,
        flaw_cve_id=flaw_cve_id,
        flaw_cve_id_in=flaw_cve_id_in,
        flaw_cwe_id=flaw_cwe_id,
        flaw_cwe_id_in=flaw_cwe_id_in,
        flaw_embargoed=flaw_embargoed,
        flaw_impact=flaw_impact,
        flaw_impact_in=flaw_impact_in,
        flaw_reported_dt=flaw_reported_dt,
        flaw_reported_dt_date=flaw_reported_dt_date,
        flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
        flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
        flaw_reported_dt_gt=flaw_reported_dt_gt,
        flaw_reported_dt_gte=flaw_reported_dt_gte,
        flaw_reported_dt_lt=flaw_reported_dt_lt,
        flaw_reported_dt_lte=flaw_reported_dt_lte,
        flaw_source=flaw_source,
        flaw_source_in=flaw_source_in,
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
        flaw_uuid_in=flaw_uuid_in,
        flaw_visibility=flaw_visibility,
        flaw_workflow_state=flaw_workflow_state,
        impact=impact,
        impact_in=impact_in,
        include_fields=include_fields,
        include_history=include_history,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        order=order,
        ps_component=ps_component,
        ps_component_in=ps_component_in,
        ps_module=ps_module,
        ps_module_in=ps_module_in,
        ps_update_stream=ps_update_stream,
        ps_update_stream_in=ps_update_stream_in,
        purl=purl,
        purl_in=purl_in,
        resolution=resolution,
        resolution_in=resolution_in,
        subpackage_purls=subpackage_purls,
        subpackage_purls_in=subpackage_purls_in,
        subpackage_purls_isempty=subpackage_purls_isempty,
        tracker_created_dt=tracker_created_dt,
        tracker_created_dt_date=tracker_created_dt_date,
        tracker_created_dt_date_gte=tracker_created_dt_date_gte,
        tracker_created_dt_date_lte=tracker_created_dt_date_lte,
        tracker_created_dt_gt=tracker_created_dt_gt,
        tracker_created_dt_gte=tracker_created_dt_gte,
        tracker_created_dt_lt=tracker_created_dt_lt,
        tracker_created_dt_lte=tracker_created_dt_lte,
        tracker_embargoed=tracker_embargoed,
        tracker_external_system_id=tracker_external_system_id,
        tracker_external_system_id_in=tracker_external_system_id_in,
        tracker_isnull=tracker_isnull,
        tracker_ps_update_stream=tracker_ps_update_stream,
        tracker_ps_update_stream_in=tracker_ps_update_stream_in,
        tracker_resolution=tracker_resolution,
        tracker_resolution_in=tracker_resolution_in,
        tracker_status=tracker_status,
        tracker_status_in=tracker_status_in,
        tracker_type=tracker_type,
        tracker_type_in=tracker_type_in,
        tracker_updated_dt=tracker_updated_dt,
        tracker_updated_dt_date=tracker_updated_dt_date,
        tracker_updated_dt_date_gte=tracker_updated_dt_date_gte,
        tracker_updated_dt_date_lte=tracker_updated_dt_date_lte,
        tracker_updated_dt_gt=tracker_updated_dt_gt,
        tracker_updated_dt_gte=tracker_updated_dt_gte,
        tracker_updated_dt_lt=tracker_updated_dt_lt,
        tracker_updated_dt_lte=tracker_updated_dt_lte,
        tracker_uuid=tracker_uuid,
        tracker_uuid_in=tracker_uuid_in,
        tracker_visibility=tracker_visibility,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
        uuid_in=uuid_in,
        visibility=visibility,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    affectedness: Union[Unset, OsidbApiV2AffectsListAffectedness] = UNSET,
    affectedness_in: Union[
        Unset, list[OsidbApiV2AffectsListAffectednessInItem]
    ] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cve_id: Union[Unset, str] = UNSET,
    cve_id_in: Union[Unset, list[str]] = UNSET,
    cvss_scores_comment: Union[Unset, str] = UNSET,
    cvss_scores_comment_in: Union[Unset, list[str]] = UNSET,
    cvss_scores_created_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, str] = UNSET,
    cvss_scores_issuer: Union[Unset, OsidbApiV2AffectsListCvssScoresIssuer] = UNSET,
    cvss_scores_issuer_in: Union[
        Unset, list[OsidbApiV2AffectsListCvssScoresIssuerInItem]
    ] = UNSET,
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
    cvss_scores_uuid_in: Union[Unset, list[UUID]] = UNSET,
    cvss_scores_vector: Union[Unset, str] = UNSET,
    cvss_scores_vector_in: Union[Unset, list[str]] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_components: Union[Unset, list[str]] = UNSET,
    flaw_components_in: Union[Unset, list[str]] = UNSET,
    flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, str] = UNSET,
    flaw_cve_id_in: Union[Unset, list[str]] = UNSET,
    flaw_cwe_id: Union[Unset, str] = UNSET,
    flaw_cwe_id_in: Union[Unset, list[str]] = UNSET,
    flaw_embargoed: Union[Unset, bool] = UNSET,
    flaw_impact: Union[Unset, OsidbApiV2AffectsListFlawImpact] = UNSET,
    flaw_impact_in: Union[Unset, list[OsidbApiV2AffectsListFlawImpactInItem]] = UNSET,
    flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, OsidbApiV2AffectsListFlawSource] = UNSET,
    flaw_source_in: Union[Unset, list[OsidbApiV2AffectsListFlawSourceInItem]] = UNSET,
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
    flaw_uuid_in: Union[Unset, list[UUID]] = UNSET,
    flaw_visibility: Union[Unset, OsidbApiV2AffectsListFlawVisibility] = UNSET,
    flaw_workflow_state: Union[
        Unset, list[OsidbApiV2AffectsListFlawWorkflowStateItem]
    ] = UNSET,
    impact: Union[Unset, OsidbApiV2AffectsListImpact] = UNSET,
    impact_in: Union[Unset, list[OsidbApiV2AffectsListImpactInItem]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV2AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, str] = UNSET,
    ps_component_in: Union[Unset, list[str]] = UNSET,
    ps_module: Union[Unset, str] = UNSET,
    ps_module_in: Union[Unset, list[str]] = UNSET,
    ps_update_stream: Union[Unset, str] = UNSET,
    ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    purl: Union[Unset, str] = UNSET,
    purl_in: Union[Unset, list[str]] = UNSET,
    resolution: Union[Unset, OsidbApiV2AffectsListResolution] = UNSET,
    resolution_in: Union[Unset, list[OsidbApiV2AffectsListResolutionInItem]] = UNSET,
    subpackage_purls: Union[Unset, str] = UNSET,
    subpackage_purls_in: Union[Unset, list[str]] = UNSET,
    subpackage_purls_isempty: Union[Unset, bool] = UNSET,
    tracker_created_dt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_date: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    tracker_embargoed: Union[Unset, bool] = UNSET,
    tracker_external_system_id: Union[Unset, str] = UNSET,
    tracker_external_system_id_in: Union[Unset, list[str]] = UNSET,
    tracker_isnull: Union[Unset, bool] = UNSET,
    tracker_ps_update_stream: Union[Unset, str] = UNSET,
    tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    tracker_resolution: Union[Unset, str] = UNSET,
    tracker_resolution_in: Union[Unset, list[str]] = UNSET,
    tracker_status: Union[Unset, str] = UNSET,
    tracker_status_in: Union[Unset, list[str]] = UNSET,
    tracker_type: Union[Unset, OsidbApiV2AffectsListTrackerType] = UNSET,
    tracker_type_in: Union[Unset, list[OsidbApiV2AffectsListTrackerTypeInItem]] = UNSET,
    tracker_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    tracker_uuid: Union[Unset, UUID] = UNSET,
    tracker_uuid_in: Union[Unset, list[UUID]] = UNSET,
    tracker_visibility: Union[Unset, OsidbApiV2AffectsListTrackerVisibility] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    visibility: Union[Unset, OsidbApiV2AffectsListVisibility] = UNSET,
) -> Response[OsidbApiV2AffectsListResponse200]:
    """
    Args:
        affectedness (Union[Unset, OsidbApiV2AffectsListAffectedness]):
        affectedness_in (Union[Unset, list[OsidbApiV2AffectsListAffectednessInItem]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cve_id (Union[Unset, str]):
        cve_id_in (Union[Unset, list[str]]):
        cvss_scores_comment (Union[Unset, str]):
        cvss_scores_comment_in (Union[Unset, list[str]]):
        cvss_scores_created_dt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_date (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_cvss_version (Union[Unset, str]):
        cvss_scores_issuer (Union[Unset, OsidbApiV2AffectsListCvssScoresIssuer]):
        cvss_scores_issuer_in (Union[Unset, list[OsidbApiV2AffectsListCvssScoresIssuerInItem]]):
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
        cvss_scores_uuid_in (Union[Unset, list[UUID]]):
        cvss_scores_vector (Union[Unset, str]):
        cvss_scores_vector_in (Union[Unset, list[str]]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_components (Union[Unset, list[str]]):
        flaw_components_in (Union[Unset, list[str]]):
        flaw_created_dt (Union[Unset, datetime.datetime]):
        flaw_created_dt_date (Union[Unset, datetime.date]):
        flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_cve_id (Union[Unset, str]):
        flaw_cve_id_in (Union[Unset, list[str]]):
        flaw_cwe_id (Union[Unset, str]):
        flaw_cwe_id_in (Union[Unset, list[str]]):
        flaw_embargoed (Union[Unset, bool]):
        flaw_impact (Union[Unset, OsidbApiV2AffectsListFlawImpact]):
        flaw_impact_in (Union[Unset, list[OsidbApiV2AffectsListFlawImpactInItem]]):
        flaw_reported_dt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_date (Union[Unset, datetime.date]):
        flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        flaw_source (Union[Unset, OsidbApiV2AffectsListFlawSource]):
        flaw_source_in (Union[Unset, list[OsidbApiV2AffectsListFlawSourceInItem]]):
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
        flaw_uuid_in (Union[Unset, list[UUID]]):
        flaw_visibility (Union[Unset, OsidbApiV2AffectsListFlawVisibility]):
        flaw_workflow_state (Union[Unset, list[OsidbApiV2AffectsListFlawWorkflowStateItem]]):
        impact (Union[Unset, OsidbApiV2AffectsListImpact]):
        impact_in (Union[Unset, list[OsidbApiV2AffectsListImpactInItem]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV2AffectsListOrderItem]]):
        ps_component (Union[Unset, str]):
        ps_component_in (Union[Unset, list[str]]):
        ps_module (Union[Unset, str]):
        ps_module_in (Union[Unset, list[str]]):
        ps_update_stream (Union[Unset, str]):
        ps_update_stream_in (Union[Unset, list[str]]):
        purl (Union[Unset, str]):
        purl_in (Union[Unset, list[str]]):
        resolution (Union[Unset, OsidbApiV2AffectsListResolution]):
        resolution_in (Union[Unset, list[OsidbApiV2AffectsListResolutionInItem]]):
        subpackage_purls (Union[Unset, str]):
        subpackage_purls_in (Union[Unset, list[str]]):
        subpackage_purls_isempty (Union[Unset, bool]):
        tracker_created_dt (Union[Unset, datetime.datetime]):
        tracker_created_dt_date (Union[Unset, datetime.date]):
        tracker_created_dt_date_gte (Union[Unset, datetime.date]):
        tracker_created_dt_date_lte (Union[Unset, datetime.date]):
        tracker_created_dt_gt (Union[Unset, datetime.datetime]):
        tracker_created_dt_gte (Union[Unset, datetime.datetime]):
        tracker_created_dt_lt (Union[Unset, datetime.datetime]):
        tracker_created_dt_lte (Union[Unset, datetime.datetime]):
        tracker_embargoed (Union[Unset, bool]):
        tracker_external_system_id (Union[Unset, str]):
        tracker_external_system_id_in (Union[Unset, list[str]]):
        tracker_isnull (Union[Unset, bool]):
        tracker_ps_update_stream (Union[Unset, str]):
        tracker_ps_update_stream_in (Union[Unset, list[str]]):
        tracker_resolution (Union[Unset, str]):
        tracker_resolution_in (Union[Unset, list[str]]):
        tracker_status (Union[Unset, str]):
        tracker_status_in (Union[Unset, list[str]]):
        tracker_type (Union[Unset, OsidbApiV2AffectsListTrackerType]):
        tracker_type_in (Union[Unset, list[OsidbApiV2AffectsListTrackerTypeInItem]]):
        tracker_updated_dt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_date (Union[Unset, datetime.date]):
        tracker_updated_dt_date_gte (Union[Unset, datetime.date]):
        tracker_updated_dt_date_lte (Union[Unset, datetime.date]):
        tracker_updated_dt_gt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_gte (Union[Unset, datetime.datetime]):
        tracker_updated_dt_lt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_lte (Union[Unset, datetime.datetime]):
        tracker_uuid (Union[Unset, UUID]):
        tracker_uuid_in (Union[Unset, list[UUID]]):
        tracker_visibility (Union[Unset, OsidbApiV2AffectsListTrackerVisibility]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        uuid_in (Union[Unset, list[UUID]]):
        visibility (Union[Unset, OsidbApiV2AffectsListVisibility]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2AffectsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        affectedness=affectedness,
        affectedness_in=affectedness_in,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cve_id=cve_id,
        cve_id_in=cve_id_in,
        cvss_scores_comment=cvss_scores_comment,
        cvss_scores_comment_in=cvss_scores_comment_in,
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
        cvss_scores_issuer_in=cvss_scores_issuer_in,
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
        cvss_scores_uuid_in=cvss_scores_uuid_in,
        cvss_scores_vector=cvss_scores_vector,
        cvss_scores_vector_in=cvss_scores_vector_in,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        flaw_components=flaw_components,
        flaw_components_in=flaw_components_in,
        flaw_created_dt=flaw_created_dt,
        flaw_created_dt_date=flaw_created_dt_date,
        flaw_created_dt_date_gte=flaw_created_dt_date_gte,
        flaw_created_dt_date_lte=flaw_created_dt_date_lte,
        flaw_created_dt_gt=flaw_created_dt_gt,
        flaw_created_dt_gte=flaw_created_dt_gte,
        flaw_created_dt_lt=flaw_created_dt_lt,
        flaw_created_dt_lte=flaw_created_dt_lte,
        flaw_cve_id=flaw_cve_id,
        flaw_cve_id_in=flaw_cve_id_in,
        flaw_cwe_id=flaw_cwe_id,
        flaw_cwe_id_in=flaw_cwe_id_in,
        flaw_embargoed=flaw_embargoed,
        flaw_impact=flaw_impact,
        flaw_impact_in=flaw_impact_in,
        flaw_reported_dt=flaw_reported_dt,
        flaw_reported_dt_date=flaw_reported_dt_date,
        flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
        flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
        flaw_reported_dt_gt=flaw_reported_dt_gt,
        flaw_reported_dt_gte=flaw_reported_dt_gte,
        flaw_reported_dt_lt=flaw_reported_dt_lt,
        flaw_reported_dt_lte=flaw_reported_dt_lte,
        flaw_source=flaw_source,
        flaw_source_in=flaw_source_in,
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
        flaw_uuid_in=flaw_uuid_in,
        flaw_visibility=flaw_visibility,
        flaw_workflow_state=flaw_workflow_state,
        impact=impact,
        impact_in=impact_in,
        include_fields=include_fields,
        include_history=include_history,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        order=order,
        ps_component=ps_component,
        ps_component_in=ps_component_in,
        ps_module=ps_module,
        ps_module_in=ps_module_in,
        ps_update_stream=ps_update_stream,
        ps_update_stream_in=ps_update_stream_in,
        purl=purl,
        purl_in=purl_in,
        resolution=resolution,
        resolution_in=resolution_in,
        subpackage_purls=subpackage_purls,
        subpackage_purls_in=subpackage_purls_in,
        subpackage_purls_isempty=subpackage_purls_isempty,
        tracker_created_dt=tracker_created_dt,
        tracker_created_dt_date=tracker_created_dt_date,
        tracker_created_dt_date_gte=tracker_created_dt_date_gte,
        tracker_created_dt_date_lte=tracker_created_dt_date_lte,
        tracker_created_dt_gt=tracker_created_dt_gt,
        tracker_created_dt_gte=tracker_created_dt_gte,
        tracker_created_dt_lt=tracker_created_dt_lt,
        tracker_created_dt_lte=tracker_created_dt_lte,
        tracker_embargoed=tracker_embargoed,
        tracker_external_system_id=tracker_external_system_id,
        tracker_external_system_id_in=tracker_external_system_id_in,
        tracker_isnull=tracker_isnull,
        tracker_ps_update_stream=tracker_ps_update_stream,
        tracker_ps_update_stream_in=tracker_ps_update_stream_in,
        tracker_resolution=tracker_resolution,
        tracker_resolution_in=tracker_resolution_in,
        tracker_status=tracker_status,
        tracker_status_in=tracker_status_in,
        tracker_type=tracker_type,
        tracker_type_in=tracker_type_in,
        tracker_updated_dt=tracker_updated_dt,
        tracker_updated_dt_date=tracker_updated_dt_date,
        tracker_updated_dt_date_gte=tracker_updated_dt_date_gte,
        tracker_updated_dt_date_lte=tracker_updated_dt_date_lte,
        tracker_updated_dt_gt=tracker_updated_dt_gt,
        tracker_updated_dt_gte=tracker_updated_dt_gte,
        tracker_updated_dt_lt=tracker_updated_dt_lt,
        tracker_updated_dt_lte=tracker_updated_dt_lte,
        tracker_uuid=tracker_uuid,
        tracker_uuid_in=tracker_uuid_in,
        tracker_visibility=tracker_visibility,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
        uuid_in=uuid_in,
        visibility=visibility,
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
    affectedness: Union[Unset, OsidbApiV2AffectsListAffectedness] = UNSET,
    affectedness_in: Union[
        Unset, list[OsidbApiV2AffectsListAffectednessInItem]
    ] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cve_id: Union[Unset, str] = UNSET,
    cve_id_in: Union[Unset, list[str]] = UNSET,
    cvss_scores_comment: Union[Unset, str] = UNSET,
    cvss_scores_comment_in: Union[Unset, list[str]] = UNSET,
    cvss_scores_created_dt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_date: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    cvss_scores_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cvss_scores_cvss_version: Union[Unset, str] = UNSET,
    cvss_scores_issuer: Union[Unset, OsidbApiV2AffectsListCvssScoresIssuer] = UNSET,
    cvss_scores_issuer_in: Union[
        Unset, list[OsidbApiV2AffectsListCvssScoresIssuerInItem]
    ] = UNSET,
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
    cvss_scores_uuid_in: Union[Unset, list[UUID]] = UNSET,
    cvss_scores_vector: Union[Unset, str] = UNSET,
    cvss_scores_vector_in: Union[Unset, list[str]] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_components: Union[Unset, list[str]] = UNSET,
    flaw_components_in: Union[Unset, list[str]] = UNSET,
    flaw_created_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_cve_id: Union[Unset, str] = UNSET,
    flaw_cve_id_in: Union[Unset, list[str]] = UNSET,
    flaw_cwe_id: Union[Unset, str] = UNSET,
    flaw_cwe_id_in: Union[Unset, list[str]] = UNSET,
    flaw_embargoed: Union[Unset, bool] = UNSET,
    flaw_impact: Union[Unset, OsidbApiV2AffectsListFlawImpact] = UNSET,
    flaw_impact_in: Union[Unset, list[OsidbApiV2AffectsListFlawImpactInItem]] = UNSET,
    flaw_reported_dt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_date: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    flaw_reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    flaw_reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    flaw_source: Union[Unset, OsidbApiV2AffectsListFlawSource] = UNSET,
    flaw_source_in: Union[Unset, list[OsidbApiV2AffectsListFlawSourceInItem]] = UNSET,
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
    flaw_uuid_in: Union[Unset, list[UUID]] = UNSET,
    flaw_visibility: Union[Unset, OsidbApiV2AffectsListFlawVisibility] = UNSET,
    flaw_workflow_state: Union[
        Unset, list[OsidbApiV2AffectsListFlawWorkflowStateItem]
    ] = UNSET,
    impact: Union[Unset, OsidbApiV2AffectsListImpact] = UNSET,
    impact_in: Union[Unset, list[OsidbApiV2AffectsListImpactInItem]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV2AffectsListOrderItem]] = UNSET,
    ps_component: Union[Unset, str] = UNSET,
    ps_component_in: Union[Unset, list[str]] = UNSET,
    ps_module: Union[Unset, str] = UNSET,
    ps_module_in: Union[Unset, list[str]] = UNSET,
    ps_update_stream: Union[Unset, str] = UNSET,
    ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    purl: Union[Unset, str] = UNSET,
    purl_in: Union[Unset, list[str]] = UNSET,
    resolution: Union[Unset, OsidbApiV2AffectsListResolution] = UNSET,
    resolution_in: Union[Unset, list[OsidbApiV2AffectsListResolutionInItem]] = UNSET,
    subpackage_purls: Union[Unset, str] = UNSET,
    subpackage_purls_in: Union[Unset, list[str]] = UNSET,
    subpackage_purls_isempty: Union[Unset, bool] = UNSET,
    tracker_created_dt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_date: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    tracker_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    tracker_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    tracker_embargoed: Union[Unset, bool] = UNSET,
    tracker_external_system_id: Union[Unset, str] = UNSET,
    tracker_external_system_id_in: Union[Unset, list[str]] = UNSET,
    tracker_isnull: Union[Unset, bool] = UNSET,
    tracker_ps_update_stream: Union[Unset, str] = UNSET,
    tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    tracker_resolution: Union[Unset, str] = UNSET,
    tracker_resolution_in: Union[Unset, list[str]] = UNSET,
    tracker_status: Union[Unset, str] = UNSET,
    tracker_status_in: Union[Unset, list[str]] = UNSET,
    tracker_type: Union[Unset, OsidbApiV2AffectsListTrackerType] = UNSET,
    tracker_type_in: Union[Unset, list[OsidbApiV2AffectsListTrackerTypeInItem]] = UNSET,
    tracker_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    tracker_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    tracker_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    tracker_uuid: Union[Unset, UUID] = UNSET,
    tracker_uuid_in: Union[Unset, list[UUID]] = UNSET,
    tracker_visibility: Union[Unset, OsidbApiV2AffectsListTrackerVisibility] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    visibility: Union[Unset, OsidbApiV2AffectsListVisibility] = UNSET,
) -> Optional[OsidbApiV2AffectsListResponse200]:
    """
    Args:
        affectedness (Union[Unset, OsidbApiV2AffectsListAffectedness]):
        affectedness_in (Union[Unset, list[OsidbApiV2AffectsListAffectednessInItem]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cve_id (Union[Unset, str]):
        cve_id_in (Union[Unset, list[str]]):
        cvss_scores_comment (Union[Unset, str]):
        cvss_scores_comment_in (Union[Unset, list[str]]):
        cvss_scores_created_dt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_date (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_gte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_date_lte (Union[Unset, datetime.date]):
        cvss_scores_created_dt_gt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_gte (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lt (Union[Unset, datetime.datetime]):
        cvss_scores_created_dt_lte (Union[Unset, datetime.datetime]):
        cvss_scores_cvss_version (Union[Unset, str]):
        cvss_scores_issuer (Union[Unset, OsidbApiV2AffectsListCvssScoresIssuer]):
        cvss_scores_issuer_in (Union[Unset, list[OsidbApiV2AffectsListCvssScoresIssuerInItem]]):
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
        cvss_scores_uuid_in (Union[Unset, list[UUID]]):
        cvss_scores_vector (Union[Unset, str]):
        cvss_scores_vector_in (Union[Unset, list[str]]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_components (Union[Unset, list[str]]):
        flaw_components_in (Union[Unset, list[str]]):
        flaw_created_dt (Union[Unset, datetime.datetime]):
        flaw_created_dt_date (Union[Unset, datetime.date]):
        flaw_created_dt_date_gte (Union[Unset, datetime.date]):
        flaw_created_dt_date_lte (Union[Unset, datetime.date]):
        flaw_created_dt_gt (Union[Unset, datetime.datetime]):
        flaw_created_dt_gte (Union[Unset, datetime.datetime]):
        flaw_created_dt_lt (Union[Unset, datetime.datetime]):
        flaw_created_dt_lte (Union[Unset, datetime.datetime]):
        flaw_cve_id (Union[Unset, str]):
        flaw_cve_id_in (Union[Unset, list[str]]):
        flaw_cwe_id (Union[Unset, str]):
        flaw_cwe_id_in (Union[Unset, list[str]]):
        flaw_embargoed (Union[Unset, bool]):
        flaw_impact (Union[Unset, OsidbApiV2AffectsListFlawImpact]):
        flaw_impact_in (Union[Unset, list[OsidbApiV2AffectsListFlawImpactInItem]]):
        flaw_reported_dt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_date (Union[Unset, datetime.date]):
        flaw_reported_dt_date_gte (Union[Unset, datetime.date]):
        flaw_reported_dt_date_lte (Union[Unset, datetime.date]):
        flaw_reported_dt_gt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_gte (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lt (Union[Unset, datetime.datetime]):
        flaw_reported_dt_lte (Union[Unset, datetime.datetime]):
        flaw_source (Union[Unset, OsidbApiV2AffectsListFlawSource]):
        flaw_source_in (Union[Unset, list[OsidbApiV2AffectsListFlawSourceInItem]]):
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
        flaw_uuid_in (Union[Unset, list[UUID]]):
        flaw_visibility (Union[Unset, OsidbApiV2AffectsListFlawVisibility]):
        flaw_workflow_state (Union[Unset, list[OsidbApiV2AffectsListFlawWorkflowStateItem]]):
        impact (Union[Unset, OsidbApiV2AffectsListImpact]):
        impact_in (Union[Unset, list[OsidbApiV2AffectsListImpactInItem]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV2AffectsListOrderItem]]):
        ps_component (Union[Unset, str]):
        ps_component_in (Union[Unset, list[str]]):
        ps_module (Union[Unset, str]):
        ps_module_in (Union[Unset, list[str]]):
        ps_update_stream (Union[Unset, str]):
        ps_update_stream_in (Union[Unset, list[str]]):
        purl (Union[Unset, str]):
        purl_in (Union[Unset, list[str]]):
        resolution (Union[Unset, OsidbApiV2AffectsListResolution]):
        resolution_in (Union[Unset, list[OsidbApiV2AffectsListResolutionInItem]]):
        subpackage_purls (Union[Unset, str]):
        subpackage_purls_in (Union[Unset, list[str]]):
        subpackage_purls_isempty (Union[Unset, bool]):
        tracker_created_dt (Union[Unset, datetime.datetime]):
        tracker_created_dt_date (Union[Unset, datetime.date]):
        tracker_created_dt_date_gte (Union[Unset, datetime.date]):
        tracker_created_dt_date_lte (Union[Unset, datetime.date]):
        tracker_created_dt_gt (Union[Unset, datetime.datetime]):
        tracker_created_dt_gte (Union[Unset, datetime.datetime]):
        tracker_created_dt_lt (Union[Unset, datetime.datetime]):
        tracker_created_dt_lte (Union[Unset, datetime.datetime]):
        tracker_embargoed (Union[Unset, bool]):
        tracker_external_system_id (Union[Unset, str]):
        tracker_external_system_id_in (Union[Unset, list[str]]):
        tracker_isnull (Union[Unset, bool]):
        tracker_ps_update_stream (Union[Unset, str]):
        tracker_ps_update_stream_in (Union[Unset, list[str]]):
        tracker_resolution (Union[Unset, str]):
        tracker_resolution_in (Union[Unset, list[str]]):
        tracker_status (Union[Unset, str]):
        tracker_status_in (Union[Unset, list[str]]):
        tracker_type (Union[Unset, OsidbApiV2AffectsListTrackerType]):
        tracker_type_in (Union[Unset, list[OsidbApiV2AffectsListTrackerTypeInItem]]):
        tracker_updated_dt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_date (Union[Unset, datetime.date]):
        tracker_updated_dt_date_gte (Union[Unset, datetime.date]):
        tracker_updated_dt_date_lte (Union[Unset, datetime.date]):
        tracker_updated_dt_gt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_gte (Union[Unset, datetime.datetime]):
        tracker_updated_dt_lt (Union[Unset, datetime.datetime]):
        tracker_updated_dt_lte (Union[Unset, datetime.datetime]):
        tracker_uuid (Union[Unset, UUID]):
        tracker_uuid_in (Union[Unset, list[UUID]]):
        tracker_visibility (Union[Unset, OsidbApiV2AffectsListTrackerVisibility]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        uuid_in (Union[Unset, list[UUID]]):
        visibility (Union[Unset, OsidbApiV2AffectsListVisibility]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2AffectsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            affectedness=affectedness,
            affectedness_in=affectedness_in,
            created_dt=created_dt,
            created_dt_date=created_dt_date,
            created_dt_date_gte=created_dt_date_gte,
            created_dt_date_lte=created_dt_date_lte,
            created_dt_gt=created_dt_gt,
            created_dt_gte=created_dt_gte,
            created_dt_lt=created_dt_lt,
            created_dt_lte=created_dt_lte,
            cve_id=cve_id,
            cve_id_in=cve_id_in,
            cvss_scores_comment=cvss_scores_comment,
            cvss_scores_comment_in=cvss_scores_comment_in,
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
            cvss_scores_issuer_in=cvss_scores_issuer_in,
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
            cvss_scores_uuid_in=cvss_scores_uuid_in,
            cvss_scores_vector=cvss_scores_vector,
            cvss_scores_vector_in=cvss_scores_vector_in,
            embargoed=embargoed,
            exclude_fields=exclude_fields,
            flaw_components=flaw_components,
            flaw_components_in=flaw_components_in,
            flaw_created_dt=flaw_created_dt,
            flaw_created_dt_date=flaw_created_dt_date,
            flaw_created_dt_date_gte=flaw_created_dt_date_gte,
            flaw_created_dt_date_lte=flaw_created_dt_date_lte,
            flaw_created_dt_gt=flaw_created_dt_gt,
            flaw_created_dt_gte=flaw_created_dt_gte,
            flaw_created_dt_lt=flaw_created_dt_lt,
            flaw_created_dt_lte=flaw_created_dt_lte,
            flaw_cve_id=flaw_cve_id,
            flaw_cve_id_in=flaw_cve_id_in,
            flaw_cwe_id=flaw_cwe_id,
            flaw_cwe_id_in=flaw_cwe_id_in,
            flaw_embargoed=flaw_embargoed,
            flaw_impact=flaw_impact,
            flaw_impact_in=flaw_impact_in,
            flaw_reported_dt=flaw_reported_dt,
            flaw_reported_dt_date=flaw_reported_dt_date,
            flaw_reported_dt_date_gte=flaw_reported_dt_date_gte,
            flaw_reported_dt_date_lte=flaw_reported_dt_date_lte,
            flaw_reported_dt_gt=flaw_reported_dt_gt,
            flaw_reported_dt_gte=flaw_reported_dt_gte,
            flaw_reported_dt_lt=flaw_reported_dt_lt,
            flaw_reported_dt_lte=flaw_reported_dt_lte,
            flaw_source=flaw_source,
            flaw_source_in=flaw_source_in,
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
            flaw_uuid_in=flaw_uuid_in,
            flaw_visibility=flaw_visibility,
            flaw_workflow_state=flaw_workflow_state,
            impact=impact,
            impact_in=impact_in,
            include_fields=include_fields,
            include_history=include_history,
            include_meta_attr=include_meta_attr,
            limit=limit,
            offset=offset,
            order=order,
            ps_component=ps_component,
            ps_component_in=ps_component_in,
            ps_module=ps_module,
            ps_module_in=ps_module_in,
            ps_update_stream=ps_update_stream,
            ps_update_stream_in=ps_update_stream_in,
            purl=purl,
            purl_in=purl_in,
            resolution=resolution,
            resolution_in=resolution_in,
            subpackage_purls=subpackage_purls,
            subpackage_purls_in=subpackage_purls_in,
            subpackage_purls_isempty=subpackage_purls_isempty,
            tracker_created_dt=tracker_created_dt,
            tracker_created_dt_date=tracker_created_dt_date,
            tracker_created_dt_date_gte=tracker_created_dt_date_gte,
            tracker_created_dt_date_lte=tracker_created_dt_date_lte,
            tracker_created_dt_gt=tracker_created_dt_gt,
            tracker_created_dt_gte=tracker_created_dt_gte,
            tracker_created_dt_lt=tracker_created_dt_lt,
            tracker_created_dt_lte=tracker_created_dt_lte,
            tracker_embargoed=tracker_embargoed,
            tracker_external_system_id=tracker_external_system_id,
            tracker_external_system_id_in=tracker_external_system_id_in,
            tracker_isnull=tracker_isnull,
            tracker_ps_update_stream=tracker_ps_update_stream,
            tracker_ps_update_stream_in=tracker_ps_update_stream_in,
            tracker_resolution=tracker_resolution,
            tracker_resolution_in=tracker_resolution_in,
            tracker_status=tracker_status,
            tracker_status_in=tracker_status_in,
            tracker_type=tracker_type,
            tracker_type_in=tracker_type_in,
            tracker_updated_dt=tracker_updated_dt,
            tracker_updated_dt_date=tracker_updated_dt_date,
            tracker_updated_dt_date_gte=tracker_updated_dt_date_gte,
            tracker_updated_dt_date_lte=tracker_updated_dt_date_lte,
            tracker_updated_dt_gt=tracker_updated_dt_gt,
            tracker_updated_dt_gte=tracker_updated_dt_gte,
            tracker_updated_dt_lt=tracker_updated_dt_lt,
            tracker_updated_dt_lte=tracker_updated_dt_lte,
            tracker_uuid=tracker_uuid,
            tracker_uuid_in=tracker_uuid_in,
            tracker_visibility=tracker_visibility,
            updated_dt=updated_dt,
            updated_dt_date=updated_dt_date,
            updated_dt_date_gte=updated_dt_date_gte,
            updated_dt_date_lte=updated_dt_date_lte,
            updated_dt_gt=updated_dt_gt,
            updated_dt_gte=updated_dt_gte,
            updated_dt_lt=updated_dt_lt,
            updated_dt_lte=updated_dt_lte,
            uuid=uuid,
            uuid_in=uuid_in,
            visibility=visibility,
        )
    ).parsed
