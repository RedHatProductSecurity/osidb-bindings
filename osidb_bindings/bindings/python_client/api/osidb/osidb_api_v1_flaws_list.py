import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v1_flaws_list_affects_affectedness import (
    OsidbApiV1FlawsListAffectsAffectedness,
)
from ...models.osidb_api_v1_flaws_list_affects_impact import (
    OsidbApiV1FlawsListAffectsImpact,
)
from ...models.osidb_api_v1_flaws_list_affects_resolution import (
    OsidbApiV1FlawsListAffectsResolution,
)
from ...models.osidb_api_v1_flaws_list_affects_trackers_type import (
    OsidbApiV1FlawsListAffectsTrackersType,
)
from ...models.osidb_api_v1_flaws_list_cvss_scores_issuer import (
    OsidbApiV1FlawsListCvssScoresIssuer,
)
from ...models.osidb_api_v1_flaws_list_impact import OsidbApiV1FlawsListImpact
from ...models.osidb_api_v1_flaws_list_major_incident_state import (
    OsidbApiV1FlawsListMajorIncidentState,
)
from ...models.osidb_api_v1_flaws_list_nist_cvss_validation import (
    OsidbApiV1FlawsListNistCvssValidation,
)
from ...models.osidb_api_v1_flaws_list_order_item import OsidbApiV1FlawsListOrderItem
from ...models.osidb_api_v1_flaws_list_references_type import (
    OsidbApiV1FlawsListReferencesType,
)
from ...models.osidb_api_v1_flaws_list_requires_cve_description import (
    OsidbApiV1FlawsListRequiresCveDescription,
)
from ...models.osidb_api_v1_flaws_list_response_200 import (
    OsidbApiV1FlawsListResponse200,
)
from ...models.osidb_api_v1_flaws_list_source import OsidbApiV1FlawsListSource
from ...models.osidb_api_v1_flaws_list_workflow_state_item import (
    OsidbApiV1FlawsListWorkflowStateItem,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "acknowledgments__affiliation": str,
    "acknowledgments__created_dt": datetime.datetime,
    "acknowledgments__created_dt__date": datetime.date,
    "acknowledgments__created_dt__date__gte": datetime.date,
    "acknowledgments__created_dt__date__lte": datetime.date,
    "acknowledgments__created_dt__gt": datetime.datetime,
    "acknowledgments__created_dt__gte": datetime.datetime,
    "acknowledgments__created_dt__lt": datetime.datetime,
    "acknowledgments__created_dt__lte": datetime.datetime,
    "acknowledgments__from_upstream": bool,
    "acknowledgments__name": str,
    "acknowledgments__updated_dt": datetime.datetime,
    "acknowledgments__updated_dt__date": datetime.date,
    "acknowledgments__updated_dt__date__gte": datetime.date,
    "acknowledgments__updated_dt__date__lte": datetime.date,
    "acknowledgments__updated_dt__gt": datetime.datetime,
    "acknowledgments__updated_dt__gte": datetime.datetime,
    "acknowledgments__updated_dt__lt": datetime.datetime,
    "acknowledgments__updated_dt__lte": datetime.datetime,
    "acknowledgments__uuid": UUID,
    "affects__affectedness": OsidbApiV1FlawsListAffectsAffectedness,
    "affects__created_dt": datetime.datetime,
    "affects__created_dt__date": datetime.date,
    "affects__created_dt__date__gte": datetime.date,
    "affects__created_dt__date__lte": datetime.date,
    "affects__created_dt__gt": datetime.datetime,
    "affects__created_dt__gte": datetime.datetime,
    "affects__created_dt__lt": datetime.datetime,
    "affects__created_dt__lte": datetime.datetime,
    "affects__embargoed": bool,
    "affects__impact": OsidbApiV1FlawsListAffectsImpact,
    "affects__ps_component": str,
    "affects__ps_module": str,
    "affects__resolution": OsidbApiV1FlawsListAffectsResolution,
    "affects__trackers__created_dt": datetime.datetime,
    "affects__trackers__created_dt__date": datetime.date,
    "affects__trackers__created_dt__date__gte": datetime.date,
    "affects__trackers__created_dt__date__lte": datetime.date,
    "affects__trackers__created_dt__gt": datetime.datetime,
    "affects__trackers__created_dt__gte": datetime.datetime,
    "affects__trackers__created_dt__lt": datetime.datetime,
    "affects__trackers__created_dt__lte": datetime.datetime,
    "affects__trackers__embargoed": bool,
    "affects__trackers__errata__advisory_name": str,
    "affects__trackers__errata__et_id": int,
    "affects__trackers__errata__shipped_dt": datetime.datetime,
    "affects__trackers__errata__shipped_dt__date": datetime.date,
    "affects__trackers__errata__shipped_dt__date__gte": datetime.date,
    "affects__trackers__errata__shipped_dt__date__lte": datetime.date,
    "affects__trackers__errata__shipped_dt__gt": datetime.datetime,
    "affects__trackers__errata__shipped_dt__gte": datetime.datetime,
    "affects__trackers__errata__shipped_dt__lt": datetime.datetime,
    "affects__trackers__errata__shipped_dt__lte": datetime.datetime,
    "affects__trackers__external_system_id": str,
    "affects__trackers__ps_update_stream": str,
    "affects__trackers__resolution": str,
    "affects__trackers__status": str,
    "affects__trackers__type": OsidbApiV1FlawsListAffectsTrackersType,
    "affects__trackers__updated_dt": datetime.datetime,
    "affects__trackers__updated_dt__date": datetime.date,
    "affects__trackers__updated_dt__date__gte": datetime.date,
    "affects__trackers__updated_dt__date__lte": datetime.date,
    "affects__trackers__updated_dt__gt": datetime.datetime,
    "affects__trackers__updated_dt__gte": datetime.datetime,
    "affects__trackers__updated_dt__lt": datetime.datetime,
    "affects__trackers__updated_dt__lte": datetime.datetime,
    "affects__trackers__uuid": UUID,
    "affects__updated_dt": datetime.datetime,
    "affects__updated_dt__date": datetime.date,
    "affects__updated_dt__date__gte": datetime.date,
    "affects__updated_dt__date__lte": datetime.date,
    "affects__updated_dt__gt": datetime.datetime,
    "affects__updated_dt__gte": datetime.datetime,
    "affects__updated_dt__lt": datetime.datetime,
    "affects__updated_dt__lte": datetime.datetime,
    "affects__uuid": UUID,
    "bz_id": float,
    "changed_after": datetime.datetime,
    "changed_before": datetime.datetime,
    "comment_zero": str,
    "components": list[str],
    "created_dt": datetime.datetime,
    "created_dt__date": datetime.date,
    "created_dt__date__gte": datetime.date,
    "created_dt__date__lte": datetime.date,
    "created_dt__gt": datetime.datetime,
    "created_dt__gte": datetime.datetime,
    "created_dt__lt": datetime.datetime,
    "created_dt__lte": datetime.datetime,
    "cve_description": str,
    "cve_description__isempty": bool,
    "cve_id": list[str],
    "cve_id__isempty": bool,
    "cvss2_nist__isempty": bool,
    "cvss2_rh__isempty": bool,
    "cvss3_nist__isempty": bool,
    "cvss3_rh__isempty": bool,
    "cvss4_nist__isempty": bool,
    "cvss4_rh__isempty": bool,
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
    "cvss_scores__issuer": OsidbApiV1FlawsListCvssScoresIssuer,
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
    "cwe_id": str,
    "cwe_id__isempty": bool,
    "embargoed": bool,
    "exclude_fields": list[str],
    "impact": OsidbApiV1FlawsListImpact,
    "include_fields": list[str],
    "include_meta_attr": list[str],
    "limit": int,
    "major_incident_start_dt": datetime.datetime,
    "major_incident_start_dt__date": datetime.date,
    "major_incident_start_dt__date__gte": datetime.date,
    "major_incident_start_dt__date__lte": datetime.date,
    "major_incident_start_dt__gt": datetime.datetime,
    "major_incident_start_dt__gte": datetime.datetime,
    "major_incident_start_dt__lt": datetime.datetime,
    "major_incident_start_dt__lte": datetime.datetime,
    "major_incident_state": OsidbApiV1FlawsListMajorIncidentState,
    "mitigation__isempty": bool,
    "nist_cvss_validation": OsidbApiV1FlawsListNistCvssValidation,
    "offset": int,
    "order": list[OsidbApiV1FlawsListOrderItem],
    "owner": str,
    "owner__isempty": bool,
    "query": str,
    "references__created_dt": datetime.datetime,
    "references__created_dt__date": datetime.date,
    "references__created_dt__date__gte": datetime.date,
    "references__created_dt__date__lte": datetime.date,
    "references__created_dt__gt": datetime.datetime,
    "references__created_dt__gte": datetime.datetime,
    "references__created_dt__lt": datetime.datetime,
    "references__created_dt__lte": datetime.datetime,
    "references__description": str,
    "references__type": OsidbApiV1FlawsListReferencesType,
    "references__updated_dt": datetime.datetime,
    "references__updated_dt__date": datetime.date,
    "references__updated_dt__date__gte": datetime.date,
    "references__updated_dt__date__lte": datetime.date,
    "references__updated_dt__gt": datetime.datetime,
    "references__updated_dt__gte": datetime.datetime,
    "references__updated_dt__lt": datetime.datetime,
    "references__updated_dt__lte": datetime.datetime,
    "references__url": str,
    "references__uuid": UUID,
    "reported_dt": datetime.datetime,
    "reported_dt__date": datetime.date,
    "reported_dt__date__gte": datetime.date,
    "reported_dt__date__lte": datetime.date,
    "reported_dt__gt": datetime.datetime,
    "reported_dt__gte": datetime.datetime,
    "reported_dt__lt": datetime.datetime,
    "reported_dt__lte": datetime.datetime,
    "requires_cve_description": OsidbApiV1FlawsListRequiresCveDescription,
    "search": str,
    "source": OsidbApiV1FlawsListSource,
    "statement": str,
    "statement__isempty": bool,
    "team_id": str,
    "title": str,
    "tracker_ids": list[str],
    "unembargo_dt": datetime.datetime,
    "updated_dt": datetime.datetime,
    "updated_dt__date": datetime.date,
    "updated_dt__date__gte": datetime.date,
    "updated_dt__date__lte": datetime.date,
    "updated_dt__gt": datetime.datetime,
    "updated_dt__gte": datetime.datetime,
    "updated_dt__lt": datetime.datetime,
    "updated_dt__lte": datetime.datetime,
    "uuid": UUID,
    "workflow_state": list[OsidbApiV1FlawsListWorkflowStateItem],
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    acknowledgments_affiliation: Union[Unset, str] = UNSET,
    acknowledgments_created_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_from_upstream: Union[Unset, bool] = UNSET,
    acknowledgments_name: Union[Unset, str] = UNSET,
    acknowledgments_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, UUID] = UNSET,
    affects_affectedness: Union[Unset, OsidbApiV1FlawsListAffectsAffectedness] = UNSET,
    affects_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, bool] = UNSET,
    affects_impact: Union[Unset, OsidbApiV1FlawsListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV1FlawsListAffectsResolution] = UNSET,
    affects_trackers_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_embargoed: Union[Unset, bool] = UNSET,
    affects_trackers_errata_advisory_name: Union[Unset, str] = UNSET,
    affects_trackers_errata_et_id: Union[Unset, int] = UNSET,
    affects_trackers_errata_shipped_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_external_system_id: Union[Unset, str] = UNSET,
    affects_trackers_ps_update_stream: Union[Unset, str] = UNSET,
    affects_trackers_resolution: Union[Unset, str] = UNSET,
    affects_trackers_status: Union[Unset, str] = UNSET,
    affects_trackers_type: Union[Unset, OsidbApiV1FlawsListAffectsTrackersType] = UNSET,
    affects_trackers_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_uuid: Union[Unset, UUID] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    bz_id: Union[Unset, float] = UNSET,
    changed_after: Union[Unset, datetime.datetime] = UNSET,
    changed_before: Union[Unset, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, str] = UNSET,
    components: Union[Unset, list[str]] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cve_description: Union[Unset, str] = UNSET,
    cve_description_isempty: Union[Unset, bool] = UNSET,
    cve_id: Union[Unset, list[str]] = UNSET,
    cve_id_isempty: Union[Unset, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, OsidbApiV1FlawsListCvssScoresIssuer] = UNSET,
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
    cwe_id: Union[Unset, str] = UNSET,
    cwe_id_isempty: Union[Unset, bool] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    impact: Union[Unset, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    major_incident_start_dt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_date: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    major_incident_state: Union[Unset, OsidbApiV1FlawsListMajorIncidentState] = UNSET,
    mitigation_isempty: Union[Unset, bool] = UNSET,
    nist_cvss_validation: Union[Unset, OsidbApiV1FlawsListNistCvssValidation] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, str] = UNSET,
    owner_isempty: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    references_created_dt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_date: Union[Unset, datetime.date] = UNSET,
    references_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_description: Union[Unset, str] = UNSET,
    references_type: Union[Unset, OsidbApiV1FlawsListReferencesType] = UNSET,
    references_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_url: Union[Unset, str] = UNSET,
    references_uuid: Union[Unset, UUID] = UNSET,
    reported_dt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, OsidbApiV1FlawsListRequiresCveDescription
    ] = UNSET,
    search: Union[Unset, str] = UNSET,
    source: Union[Unset, OsidbApiV1FlawsListSource] = UNSET,
    statement: Union[Unset, str] = UNSET,
    statement_isempty: Union[Unset, bool] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    tracker_ids: Union[Unset, list[str]] = UNSET,
    unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    workflow_state: Union[Unset, list[OsidbApiV1FlawsListWorkflowStateItem]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["acknowledgments__affiliation"] = acknowledgments_affiliation

    json_acknowledgments_created_dt: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_created_dt, Unset):
        json_acknowledgments_created_dt = acknowledgments_created_dt.isoformat()

    params["acknowledgments__created_dt"] = json_acknowledgments_created_dt

    json_acknowledgments_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_created_dt_date, Unset):
        json_acknowledgments_created_dt_date = (
            acknowledgments_created_dt_date.isoformat()
        )

    params["acknowledgments__created_dt__date"] = json_acknowledgments_created_dt_date

    json_acknowledgments_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_created_dt_date_gte, Unset):
        json_acknowledgments_created_dt_date_gte = (
            acknowledgments_created_dt_date_gte.isoformat()
        )

    params["acknowledgments__created_dt__date__gte"] = (
        json_acknowledgments_created_dt_date_gte
    )

    json_acknowledgments_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_created_dt_date_lte, Unset):
        json_acknowledgments_created_dt_date_lte = (
            acknowledgments_created_dt_date_lte.isoformat()
        )

    params["acknowledgments__created_dt__date__lte"] = (
        json_acknowledgments_created_dt_date_lte
    )

    json_acknowledgments_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_created_dt_gt, Unset):
        json_acknowledgments_created_dt_gt = acknowledgments_created_dt_gt.isoformat()

    params["acknowledgments__created_dt__gt"] = json_acknowledgments_created_dt_gt

    json_acknowledgments_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_created_dt_gte, Unset):
        json_acknowledgments_created_dt_gte = acknowledgments_created_dt_gte.isoformat()

    params["acknowledgments__created_dt__gte"] = json_acknowledgments_created_dt_gte

    json_acknowledgments_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_created_dt_lt, Unset):
        json_acknowledgments_created_dt_lt = acknowledgments_created_dt_lt.isoformat()

    params["acknowledgments__created_dt__lt"] = json_acknowledgments_created_dt_lt

    json_acknowledgments_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_created_dt_lte, Unset):
        json_acknowledgments_created_dt_lte = acknowledgments_created_dt_lte.isoformat()

    params["acknowledgments__created_dt__lte"] = json_acknowledgments_created_dt_lte

    params["acknowledgments__from_upstream"] = acknowledgments_from_upstream

    params["acknowledgments__name"] = acknowledgments_name

    json_acknowledgments_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_updated_dt, Unset):
        json_acknowledgments_updated_dt = acknowledgments_updated_dt.isoformat()

    params["acknowledgments__updated_dt"] = json_acknowledgments_updated_dt

    json_acknowledgments_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_date, Unset):
        json_acknowledgments_updated_dt_date = (
            acknowledgments_updated_dt_date.isoformat()
        )

    params["acknowledgments__updated_dt__date"] = json_acknowledgments_updated_dt_date

    json_acknowledgments_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_date_gte, Unset):
        json_acknowledgments_updated_dt_date_gte = (
            acknowledgments_updated_dt_date_gte.isoformat()
        )

    params["acknowledgments__updated_dt__date__gte"] = (
        json_acknowledgments_updated_dt_date_gte
    )

    json_acknowledgments_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_date_lte, Unset):
        json_acknowledgments_updated_dt_date_lte = (
            acknowledgments_updated_dt_date_lte.isoformat()
        )

    params["acknowledgments__updated_dt__date__lte"] = (
        json_acknowledgments_updated_dt_date_lte
    )

    json_acknowledgments_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_gt, Unset):
        json_acknowledgments_updated_dt_gt = acknowledgments_updated_dt_gt.isoformat()

    params["acknowledgments__updated_dt__gt"] = json_acknowledgments_updated_dt_gt

    json_acknowledgments_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_gte, Unset):
        json_acknowledgments_updated_dt_gte = acknowledgments_updated_dt_gte.isoformat()

    params["acknowledgments__updated_dt__gte"] = json_acknowledgments_updated_dt_gte

    json_acknowledgments_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_lt, Unset):
        json_acknowledgments_updated_dt_lt = acknowledgments_updated_dt_lt.isoformat()

    params["acknowledgments__updated_dt__lt"] = json_acknowledgments_updated_dt_lt

    json_acknowledgments_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_lte, Unset):
        json_acknowledgments_updated_dt_lte = acknowledgments_updated_dt_lte.isoformat()

    params["acknowledgments__updated_dt__lte"] = json_acknowledgments_updated_dt_lte

    json_acknowledgments_uuid: Union[Unset, str] = UNSET
    if not isinstance(acknowledgments_uuid, Unset):
        json_acknowledgments_uuid = str(acknowledgments_uuid)

    params["acknowledgments__uuid"] = json_acknowledgments_uuid

    json_affects_affectedness: Union[Unset, str] = UNSET
    if not isinstance(affects_affectedness, Unset):
        json_affects_affectedness = OsidbApiV1FlawsListAffectsAffectedness(
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

    json_affects_impact: Union[Unset, str] = UNSET
    if not isinstance(affects_impact, Unset):
        json_affects_impact = OsidbApiV1FlawsListAffectsImpact(affects_impact).value

    params["affects__impact"] = json_affects_impact

    params["affects__ps_component"] = affects_ps_component

    params["affects__ps_module"] = affects_ps_module

    json_affects_resolution: Union[Unset, str] = UNSET
    if not isinstance(affects_resolution, Unset):
        json_affects_resolution = OsidbApiV1FlawsListAffectsResolution(
            affects_resolution
        ).value

    params["affects__resolution"] = json_affects_resolution

    json_affects_trackers_created_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_created_dt, Unset):
        json_affects_trackers_created_dt = affects_trackers_created_dt.isoformat()

    params["affects__trackers__created_dt"] = json_affects_trackers_created_dt

    json_affects_trackers_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_created_dt_date, Unset):
        json_affects_trackers_created_dt_date = (
            affects_trackers_created_dt_date.isoformat()
        )

    params["affects__trackers__created_dt__date"] = (
        json_affects_trackers_created_dt_date
    )

    json_affects_trackers_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_created_dt_date_gte, Unset):
        json_affects_trackers_created_dt_date_gte = (
            affects_trackers_created_dt_date_gte.isoformat()
        )

    params["affects__trackers__created_dt__date__gte"] = (
        json_affects_trackers_created_dt_date_gte
    )

    json_affects_trackers_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_created_dt_date_lte, Unset):
        json_affects_trackers_created_dt_date_lte = (
            affects_trackers_created_dt_date_lte.isoformat()
        )

    params["affects__trackers__created_dt__date__lte"] = (
        json_affects_trackers_created_dt_date_lte
    )

    json_affects_trackers_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_created_dt_gt, Unset):
        json_affects_trackers_created_dt_gt = affects_trackers_created_dt_gt.isoformat()

    params["affects__trackers__created_dt__gt"] = json_affects_trackers_created_dt_gt

    json_affects_trackers_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_created_dt_gte, Unset):
        json_affects_trackers_created_dt_gte = (
            affects_trackers_created_dt_gte.isoformat()
        )

    params["affects__trackers__created_dt__gte"] = json_affects_trackers_created_dt_gte

    json_affects_trackers_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_created_dt_lt, Unset):
        json_affects_trackers_created_dt_lt = affects_trackers_created_dt_lt.isoformat()

    params["affects__trackers__created_dt__lt"] = json_affects_trackers_created_dt_lt

    json_affects_trackers_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_created_dt_lte, Unset):
        json_affects_trackers_created_dt_lte = (
            affects_trackers_created_dt_lte.isoformat()
        )

    params["affects__trackers__created_dt__lte"] = json_affects_trackers_created_dt_lte

    params["affects__trackers__embargoed"] = affects_trackers_embargoed

    params["affects__trackers__errata__advisory_name"] = (
        affects_trackers_errata_advisory_name
    )

    params["affects__trackers__errata__et_id"] = affects_trackers_errata_et_id

    json_affects_trackers_errata_shipped_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt, Unset):
        json_affects_trackers_errata_shipped_dt = (
            affects_trackers_errata_shipped_dt.isoformat()
        )

    params["affects__trackers__errata__shipped_dt"] = (
        json_affects_trackers_errata_shipped_dt
    )

    json_affects_trackers_errata_shipped_dt_date: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_date, Unset):
        json_affects_trackers_errata_shipped_dt_date = (
            affects_trackers_errata_shipped_dt_date.isoformat()
        )

    params["affects__trackers__errata__shipped_dt__date"] = (
        json_affects_trackers_errata_shipped_dt_date
    )

    json_affects_trackers_errata_shipped_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_date_gte, Unset):
        json_affects_trackers_errata_shipped_dt_date_gte = (
            affects_trackers_errata_shipped_dt_date_gte.isoformat()
        )

    params["affects__trackers__errata__shipped_dt__date__gte"] = (
        json_affects_trackers_errata_shipped_dt_date_gte
    )

    json_affects_trackers_errata_shipped_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_date_lte, Unset):
        json_affects_trackers_errata_shipped_dt_date_lte = (
            affects_trackers_errata_shipped_dt_date_lte.isoformat()
        )

    params["affects__trackers__errata__shipped_dt__date__lte"] = (
        json_affects_trackers_errata_shipped_dt_date_lte
    )

    json_affects_trackers_errata_shipped_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_gt, Unset):
        json_affects_trackers_errata_shipped_dt_gt = (
            affects_trackers_errata_shipped_dt_gt.isoformat()
        )

    params["affects__trackers__errata__shipped_dt__gt"] = (
        json_affects_trackers_errata_shipped_dt_gt
    )

    json_affects_trackers_errata_shipped_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_gte, Unset):
        json_affects_trackers_errata_shipped_dt_gte = (
            affects_trackers_errata_shipped_dt_gte.isoformat()
        )

    params["affects__trackers__errata__shipped_dt__gte"] = (
        json_affects_trackers_errata_shipped_dt_gte
    )

    json_affects_trackers_errata_shipped_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_lt, Unset):
        json_affects_trackers_errata_shipped_dt_lt = (
            affects_trackers_errata_shipped_dt_lt.isoformat()
        )

    params["affects__trackers__errata__shipped_dt__lt"] = (
        json_affects_trackers_errata_shipped_dt_lt
    )

    json_affects_trackers_errata_shipped_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_lte, Unset):
        json_affects_trackers_errata_shipped_dt_lte = (
            affects_trackers_errata_shipped_dt_lte.isoformat()
        )

    params["affects__trackers__errata__shipped_dt__lte"] = (
        json_affects_trackers_errata_shipped_dt_lte
    )

    params["affects__trackers__external_system_id"] = (
        affects_trackers_external_system_id
    )

    params["affects__trackers__ps_update_stream"] = affects_trackers_ps_update_stream

    params["affects__trackers__resolution"] = affects_trackers_resolution

    params["affects__trackers__status"] = affects_trackers_status

    json_affects_trackers_type: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_type, Unset):
        json_affects_trackers_type = OsidbApiV1FlawsListAffectsTrackersType(
            affects_trackers_type
        ).value

    params["affects__trackers__type"] = json_affects_trackers_type

    json_affects_trackers_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_updated_dt, Unset):
        json_affects_trackers_updated_dt = affects_trackers_updated_dt.isoformat()

    params["affects__trackers__updated_dt"] = json_affects_trackers_updated_dt

    json_affects_trackers_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_date, Unset):
        json_affects_trackers_updated_dt_date = (
            affects_trackers_updated_dt_date.isoformat()
        )

    params["affects__trackers__updated_dt__date"] = (
        json_affects_trackers_updated_dt_date
    )

    json_affects_trackers_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_date_gte, Unset):
        json_affects_trackers_updated_dt_date_gte = (
            affects_trackers_updated_dt_date_gte.isoformat()
        )

    params["affects__trackers__updated_dt__date__gte"] = (
        json_affects_trackers_updated_dt_date_gte
    )

    json_affects_trackers_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_date_lte, Unset):
        json_affects_trackers_updated_dt_date_lte = (
            affects_trackers_updated_dt_date_lte.isoformat()
        )

    params["affects__trackers__updated_dt__date__lte"] = (
        json_affects_trackers_updated_dt_date_lte
    )

    json_affects_trackers_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_gt, Unset):
        json_affects_trackers_updated_dt_gt = affects_trackers_updated_dt_gt.isoformat()

    params["affects__trackers__updated_dt__gt"] = json_affects_trackers_updated_dt_gt

    json_affects_trackers_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_gte, Unset):
        json_affects_trackers_updated_dt_gte = (
            affects_trackers_updated_dt_gte.isoformat()
        )

    params["affects__trackers__updated_dt__gte"] = json_affects_trackers_updated_dt_gte

    json_affects_trackers_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_lt, Unset):
        json_affects_trackers_updated_dt_lt = affects_trackers_updated_dt_lt.isoformat()

    params["affects__trackers__updated_dt__lt"] = json_affects_trackers_updated_dt_lt

    json_affects_trackers_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_lte, Unset):
        json_affects_trackers_updated_dt_lte = (
            affects_trackers_updated_dt_lte.isoformat()
        )

    params["affects__trackers__updated_dt__lte"] = json_affects_trackers_updated_dt_lte

    json_affects_trackers_uuid: Union[Unset, str] = UNSET
    if not isinstance(affects_trackers_uuid, Unset):
        json_affects_trackers_uuid = str(affects_trackers_uuid)

    params["affects__trackers__uuid"] = json_affects_trackers_uuid

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

    params["bz_id"] = bz_id

    json_changed_after: Union[Unset, str] = UNSET
    if not isinstance(changed_after, Unset):
        json_changed_after = changed_after.isoformat()

    params["changed_after"] = json_changed_after

    json_changed_before: Union[Unset, str] = UNSET
    if not isinstance(changed_before, Unset):
        json_changed_before = changed_before.isoformat()

    params["changed_before"] = json_changed_before

    params["comment_zero"] = comment_zero

    json_components: Union[Unset, list[str]] = UNSET
    if not isinstance(components, Unset):
        json_components = components

    params["components"] = json_components

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

    params["cve_description"] = cve_description

    params["cve_description__isempty"] = cve_description_isempty

    json_cve_id: Union[Unset, list[str]] = UNSET
    if not isinstance(cve_id, Unset):
        json_cve_id = cve_id

    params["cve_id"] = json_cve_id

    params["cve_id__isempty"] = cve_id_isempty

    params["cvss2_nist__isempty"] = cvss2_nist_isempty

    params["cvss2_rh__isempty"] = cvss2_rh_isempty

    params["cvss3_nist__isempty"] = cvss3_nist_isempty

    params["cvss3_rh__isempty"] = cvss3_rh_isempty

    params["cvss4_nist__isempty"] = cvss4_nist_isempty

    params["cvss4_rh__isempty"] = cvss4_rh_isempty

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
        json_cvss_scores_issuer = OsidbApiV1FlawsListCvssScoresIssuer(
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

    params["cwe_id"] = cwe_id

    params["cwe_id__isempty"] = cwe_id_isempty

    params["embargoed"] = embargoed

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    json_impact: Union[Unset, str] = UNSET
    if not isinstance(impact, Unset):
        json_impact = OsidbApiV1FlawsListImpact(impact).value

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

    json_major_incident_start_dt: Union[Unset, str] = UNSET
    if not isinstance(major_incident_start_dt, Unset):
        json_major_incident_start_dt = major_incident_start_dt.isoformat()

    params["major_incident_start_dt"] = json_major_incident_start_dt

    json_major_incident_start_dt_date: Union[Unset, str] = UNSET
    if not isinstance(major_incident_start_dt_date, Unset):
        json_major_incident_start_dt_date = major_incident_start_dt_date.isoformat()

    params["major_incident_start_dt__date"] = json_major_incident_start_dt_date

    json_major_incident_start_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(major_incident_start_dt_date_gte, Unset):
        json_major_incident_start_dt_date_gte = (
            major_incident_start_dt_date_gte.isoformat()
        )

    params["major_incident_start_dt__date__gte"] = json_major_incident_start_dt_date_gte

    json_major_incident_start_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(major_incident_start_dt_date_lte, Unset):
        json_major_incident_start_dt_date_lte = (
            major_incident_start_dt_date_lte.isoformat()
        )

    params["major_incident_start_dt__date__lte"] = json_major_incident_start_dt_date_lte

    json_major_incident_start_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(major_incident_start_dt_gt, Unset):
        json_major_incident_start_dt_gt = major_incident_start_dt_gt.isoformat()

    params["major_incident_start_dt__gt"] = json_major_incident_start_dt_gt

    json_major_incident_start_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(major_incident_start_dt_gte, Unset):
        json_major_incident_start_dt_gte = major_incident_start_dt_gte.isoformat()

    params["major_incident_start_dt__gte"] = json_major_incident_start_dt_gte

    json_major_incident_start_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(major_incident_start_dt_lt, Unset):
        json_major_incident_start_dt_lt = major_incident_start_dt_lt.isoformat()

    params["major_incident_start_dt__lt"] = json_major_incident_start_dt_lt

    json_major_incident_start_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(major_incident_start_dt_lte, Unset):
        json_major_incident_start_dt_lte = major_incident_start_dt_lte.isoformat()

    params["major_incident_start_dt__lte"] = json_major_incident_start_dt_lte

    json_major_incident_state: Union[Unset, str] = UNSET
    if not isinstance(major_incident_state, Unset):
        json_major_incident_state = OsidbApiV1FlawsListMajorIncidentState(
            major_incident_state
        ).value

    params["major_incident_state"] = json_major_incident_state

    params["mitigation__isempty"] = mitigation_isempty

    json_nist_cvss_validation: Union[Unset, str] = UNSET
    if not isinstance(nist_cvss_validation, Unset):
        json_nist_cvss_validation = OsidbApiV1FlawsListNistCvssValidation(
            nist_cvss_validation
        ).value

    params["nist_cvss_validation"] = json_nist_cvss_validation

    params["offset"] = offset

    json_order: Union[Unset, list[str]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item: str = UNSET
            if not isinstance(order_item_data, Unset):
                order_item = OsidbApiV1FlawsListOrderItem(order_item_data).value

            json_order.append(order_item)

    params["order"] = json_order

    params["owner"] = owner

    params["owner__isempty"] = owner_isempty

    params["query"] = query

    json_references_created_dt: Union[Unset, str] = UNSET
    if not isinstance(references_created_dt, Unset):
        json_references_created_dt = references_created_dt.isoformat()

    params["references__created_dt"] = json_references_created_dt

    json_references_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(references_created_dt_date, Unset):
        json_references_created_dt_date = references_created_dt_date.isoformat()

    params["references__created_dt__date"] = json_references_created_dt_date

    json_references_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(references_created_dt_date_gte, Unset):
        json_references_created_dt_date_gte = references_created_dt_date_gte.isoformat()

    params["references__created_dt__date__gte"] = json_references_created_dt_date_gte

    json_references_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(references_created_dt_date_lte, Unset):
        json_references_created_dt_date_lte = references_created_dt_date_lte.isoformat()

    params["references__created_dt__date__lte"] = json_references_created_dt_date_lte

    json_references_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(references_created_dt_gt, Unset):
        json_references_created_dt_gt = references_created_dt_gt.isoformat()

    params["references__created_dt__gt"] = json_references_created_dt_gt

    json_references_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(references_created_dt_gte, Unset):
        json_references_created_dt_gte = references_created_dt_gte.isoformat()

    params["references__created_dt__gte"] = json_references_created_dt_gte

    json_references_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(references_created_dt_lt, Unset):
        json_references_created_dt_lt = references_created_dt_lt.isoformat()

    params["references__created_dt__lt"] = json_references_created_dt_lt

    json_references_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(references_created_dt_lte, Unset):
        json_references_created_dt_lte = references_created_dt_lte.isoformat()

    params["references__created_dt__lte"] = json_references_created_dt_lte

    params["references__description"] = references_description

    json_references_type: Union[Unset, str] = UNSET
    if not isinstance(references_type, Unset):
        json_references_type = OsidbApiV1FlawsListReferencesType(references_type).value

    params["references__type"] = json_references_type

    json_references_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(references_updated_dt, Unset):
        json_references_updated_dt = references_updated_dt.isoformat()

    params["references__updated_dt"] = json_references_updated_dt

    json_references_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(references_updated_dt_date, Unset):
        json_references_updated_dt_date = references_updated_dt_date.isoformat()

    params["references__updated_dt__date"] = json_references_updated_dt_date

    json_references_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(references_updated_dt_date_gte, Unset):
        json_references_updated_dt_date_gte = references_updated_dt_date_gte.isoformat()

    params["references__updated_dt__date__gte"] = json_references_updated_dt_date_gte

    json_references_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(references_updated_dt_date_lte, Unset):
        json_references_updated_dt_date_lte = references_updated_dt_date_lte.isoformat()

    params["references__updated_dt__date__lte"] = json_references_updated_dt_date_lte

    json_references_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(references_updated_dt_gt, Unset):
        json_references_updated_dt_gt = references_updated_dt_gt.isoformat()

    params["references__updated_dt__gt"] = json_references_updated_dt_gt

    json_references_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(references_updated_dt_gte, Unset):
        json_references_updated_dt_gte = references_updated_dt_gte.isoformat()

    params["references__updated_dt__gte"] = json_references_updated_dt_gte

    json_references_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(references_updated_dt_lt, Unset):
        json_references_updated_dt_lt = references_updated_dt_lt.isoformat()

    params["references__updated_dt__lt"] = json_references_updated_dt_lt

    json_references_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(references_updated_dt_lte, Unset):
        json_references_updated_dt_lte = references_updated_dt_lte.isoformat()

    params["references__updated_dt__lte"] = json_references_updated_dt_lte

    params["references__url"] = references_url

    json_references_uuid: Union[Unset, str] = UNSET
    if not isinstance(references_uuid, Unset):
        json_references_uuid = str(references_uuid)

    params["references__uuid"] = json_references_uuid

    json_reported_dt: Union[Unset, str] = UNSET
    if not isinstance(reported_dt, Unset):
        json_reported_dt = reported_dt.isoformat()

    params["reported_dt"] = json_reported_dt

    json_reported_dt_date: Union[Unset, str] = UNSET
    if not isinstance(reported_dt_date, Unset):
        json_reported_dt_date = reported_dt_date.isoformat()

    params["reported_dt__date"] = json_reported_dt_date

    json_reported_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(reported_dt_date_gte, Unset):
        json_reported_dt_date_gte = reported_dt_date_gte.isoformat()

    params["reported_dt__date__gte"] = json_reported_dt_date_gte

    json_reported_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(reported_dt_date_lte, Unset):
        json_reported_dt_date_lte = reported_dt_date_lte.isoformat()

    params["reported_dt__date__lte"] = json_reported_dt_date_lte

    json_reported_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(reported_dt_gt, Unset):
        json_reported_dt_gt = reported_dt_gt.isoformat()

    params["reported_dt__gt"] = json_reported_dt_gt

    json_reported_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(reported_dt_gte, Unset):
        json_reported_dt_gte = reported_dt_gte.isoformat()

    params["reported_dt__gte"] = json_reported_dt_gte

    json_reported_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(reported_dt_lt, Unset):
        json_reported_dt_lt = reported_dt_lt.isoformat()

    params["reported_dt__lt"] = json_reported_dt_lt

    json_reported_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(reported_dt_lte, Unset):
        json_reported_dt_lte = reported_dt_lte.isoformat()

    params["reported_dt__lte"] = json_reported_dt_lte

    json_requires_cve_description: Union[Unset, str] = UNSET
    if not isinstance(requires_cve_description, Unset):
        json_requires_cve_description = OsidbApiV1FlawsListRequiresCveDescription(
            requires_cve_description
        ).value

    params["requires_cve_description"] = json_requires_cve_description

    params["search"] = search

    json_source: Union[Unset, str] = UNSET
    if not isinstance(source, Unset):
        json_source = OsidbApiV1FlawsListSource(source).value

    params["source"] = json_source

    params["statement"] = statement

    params["statement__isempty"] = statement_isempty

    params["team_id"] = team_id

    params["title"] = title

    json_tracker_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(tracker_ids, Unset):
        json_tracker_ids = tracker_ids

    params["tracker_ids"] = json_tracker_ids

    json_unembargo_dt: Union[Unset, str] = UNSET
    if not isinstance(unembargo_dt, Unset):
        json_unembargo_dt = unembargo_dt.isoformat()

    params["unembargo_dt"] = json_unembargo_dt

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

    json_workflow_state: Union[Unset, list[str]] = UNSET
    if not isinstance(workflow_state, Unset):
        json_workflow_state = []
        for workflow_state_item_data in workflow_state:
            workflow_state_item: str = UNSET
            if not isinstance(workflow_state_item_data, Unset):
                workflow_state_item = OsidbApiV1FlawsListWorkflowStateItem(
                    workflow_state_item_data
                ).value

            json_workflow_state.append(workflow_state_item)

    params["workflow_state"] = json_workflow_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v1/flaws",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV1FlawsListResponse200]:
    if response.status_code == 200:
        # }
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsListResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV1FlawsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    acknowledgments_affiliation: Union[Unset, str] = UNSET,
    acknowledgments_created_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_from_upstream: Union[Unset, bool] = UNSET,
    acknowledgments_name: Union[Unset, str] = UNSET,
    acknowledgments_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, UUID] = UNSET,
    affects_affectedness: Union[Unset, OsidbApiV1FlawsListAffectsAffectedness] = UNSET,
    affects_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, bool] = UNSET,
    affects_impact: Union[Unset, OsidbApiV1FlawsListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV1FlawsListAffectsResolution] = UNSET,
    affects_trackers_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_embargoed: Union[Unset, bool] = UNSET,
    affects_trackers_errata_advisory_name: Union[Unset, str] = UNSET,
    affects_trackers_errata_et_id: Union[Unset, int] = UNSET,
    affects_trackers_errata_shipped_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_external_system_id: Union[Unset, str] = UNSET,
    affects_trackers_ps_update_stream: Union[Unset, str] = UNSET,
    affects_trackers_resolution: Union[Unset, str] = UNSET,
    affects_trackers_status: Union[Unset, str] = UNSET,
    affects_trackers_type: Union[Unset, OsidbApiV1FlawsListAffectsTrackersType] = UNSET,
    affects_trackers_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_uuid: Union[Unset, UUID] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    bz_id: Union[Unset, float] = UNSET,
    changed_after: Union[Unset, datetime.datetime] = UNSET,
    changed_before: Union[Unset, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, str] = UNSET,
    components: Union[Unset, list[str]] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cve_description: Union[Unset, str] = UNSET,
    cve_description_isempty: Union[Unset, bool] = UNSET,
    cve_id: Union[Unset, list[str]] = UNSET,
    cve_id_isempty: Union[Unset, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, OsidbApiV1FlawsListCvssScoresIssuer] = UNSET,
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
    cwe_id: Union[Unset, str] = UNSET,
    cwe_id_isempty: Union[Unset, bool] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    impact: Union[Unset, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    major_incident_start_dt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_date: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    major_incident_state: Union[Unset, OsidbApiV1FlawsListMajorIncidentState] = UNSET,
    mitigation_isempty: Union[Unset, bool] = UNSET,
    nist_cvss_validation: Union[Unset, OsidbApiV1FlawsListNistCvssValidation] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, str] = UNSET,
    owner_isempty: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    references_created_dt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_date: Union[Unset, datetime.date] = UNSET,
    references_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_description: Union[Unset, str] = UNSET,
    references_type: Union[Unset, OsidbApiV1FlawsListReferencesType] = UNSET,
    references_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_url: Union[Unset, str] = UNSET,
    references_uuid: Union[Unset, UUID] = UNSET,
    reported_dt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, OsidbApiV1FlawsListRequiresCveDescription
    ] = UNSET,
    search: Union[Unset, str] = UNSET,
    source: Union[Unset, OsidbApiV1FlawsListSource] = UNSET,
    statement: Union[Unset, str] = UNSET,
    statement_isempty: Union[Unset, bool] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    tracker_ids: Union[Unset, list[str]] = UNSET,
    unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    workflow_state: Union[Unset, list[OsidbApiV1FlawsListWorkflowStateItem]] = UNSET,
) -> Response[OsidbApiV1FlawsListResponse200]:
    """
    Args:
        acknowledgments_affiliation (Union[Unset, str]):
        acknowledgments_created_dt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_date (Union[Unset, datetime.date]):
        acknowledgments_created_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_created_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_created_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_from_upstream (Union[Unset, bool]):
        acknowledgments_name (Union[Unset, str]):
        acknowledgments_updated_dt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_date (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_uuid (Union[Unset, UUID]):
        affects_affectedness (Union[Unset, OsidbApiV1FlawsListAffectsAffectedness]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_impact (Union[Unset, OsidbApiV1FlawsListAffectsImpact]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_module (Union[Unset, str]):
        affects_resolution (Union[Unset, OsidbApiV1FlawsListAffectsResolution]):
        affects_trackers_created_dt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_date (Union[Unset, datetime.date]):
        affects_trackers_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_embargoed (Union[Unset, bool]):
        affects_trackers_errata_advisory_name (Union[Unset, str]):
        affects_trackers_errata_et_id (Union[Unset, int]):
        affects_trackers_errata_shipped_dt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_date (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_external_system_id (Union[Unset, str]):
        affects_trackers_ps_update_stream (Union[Unset, str]):
        affects_trackers_resolution (Union[Unset, str]):
        affects_trackers_status (Union[Unset, str]):
        affects_trackers_type (Union[Unset, OsidbApiV1FlawsListAffectsTrackersType]):
        affects_trackers_updated_dt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_date (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_uuid (Union[Unset, UUID]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        bz_id (Union[Unset, float]):
        changed_after (Union[Unset, datetime.datetime]):
        changed_before (Union[Unset, datetime.datetime]):
        comment_zero (Union[Unset, str]):
        components (Union[Unset, list[str]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cve_description (Union[Unset, str]):
        cve_description_isempty (Union[Unset, bool]):
        cve_id (Union[Unset, list[str]]):
        cve_id_isempty (Union[Unset, bool]):
        cvss2_nist_isempty (Union[Unset, bool]):
        cvss2_rh_isempty (Union[Unset, bool]):
        cvss3_nist_isempty (Union[Unset, bool]):
        cvss3_rh_isempty (Union[Unset, bool]):
        cvss4_nist_isempty (Union[Unset, bool]):
        cvss4_rh_isempty (Union[Unset, bool]):
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
        cvss_scores_issuer (Union[Unset, OsidbApiV1FlawsListCvssScoresIssuer]):
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
        cwe_id (Union[Unset, str]):
        cwe_id_isempty (Union[Unset, bool]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        impact (Union[Unset, OsidbApiV1FlawsListImpact]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        major_incident_start_dt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_date (Union[Unset, datetime.date]):
        major_incident_start_dt_date_gte (Union[Unset, datetime.date]):
        major_incident_start_dt_date_lte (Union[Unset, datetime.date]):
        major_incident_start_dt_gt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_gte (Union[Unset, datetime.datetime]):
        major_incident_start_dt_lt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_lte (Union[Unset, datetime.datetime]):
        major_incident_state (Union[Unset, OsidbApiV1FlawsListMajorIncidentState]):
        mitigation_isempty (Union[Unset, bool]):
        nist_cvss_validation (Union[Unset, OsidbApiV1FlawsListNistCvssValidation]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1FlawsListOrderItem]]):
        owner (Union[Unset, str]):
        owner_isempty (Union[Unset, bool]):
        query (Union[Unset, str]):
        references_created_dt (Union[Unset, datetime.datetime]):
        references_created_dt_date (Union[Unset, datetime.date]):
        references_created_dt_date_gte (Union[Unset, datetime.date]):
        references_created_dt_date_lte (Union[Unset, datetime.date]):
        references_created_dt_gt (Union[Unset, datetime.datetime]):
        references_created_dt_gte (Union[Unset, datetime.datetime]):
        references_created_dt_lt (Union[Unset, datetime.datetime]):
        references_created_dt_lte (Union[Unset, datetime.datetime]):
        references_description (Union[Unset, str]):
        references_type (Union[Unset, OsidbApiV1FlawsListReferencesType]):
        references_updated_dt (Union[Unset, datetime.datetime]):
        references_updated_dt_date (Union[Unset, datetime.date]):
        references_updated_dt_date_gte (Union[Unset, datetime.date]):
        references_updated_dt_date_lte (Union[Unset, datetime.date]):
        references_updated_dt_gt (Union[Unset, datetime.datetime]):
        references_updated_dt_gte (Union[Unset, datetime.datetime]):
        references_updated_dt_lt (Union[Unset, datetime.datetime]):
        references_updated_dt_lte (Union[Unset, datetime.datetime]):
        references_url (Union[Unset, str]):
        references_uuid (Union[Unset, UUID]):
        reported_dt (Union[Unset, datetime.datetime]):
        reported_dt_date (Union[Unset, datetime.date]):
        reported_dt_date_gte (Union[Unset, datetime.date]):
        reported_dt_date_lte (Union[Unset, datetime.date]):
        reported_dt_gt (Union[Unset, datetime.datetime]):
        reported_dt_gte (Union[Unset, datetime.datetime]):
        reported_dt_lt (Union[Unset, datetime.datetime]):
        reported_dt_lte (Union[Unset, datetime.datetime]):
        requires_cve_description (Union[Unset, OsidbApiV1FlawsListRequiresCveDescription]):
        search (Union[Unset, str]):
        source (Union[Unset, OsidbApiV1FlawsListSource]):
        statement (Union[Unset, str]):
        statement_isempty (Union[Unset, bool]):
        team_id (Union[Unset, str]):
        title (Union[Unset, str]):
        tracker_ids (Union[Unset, list[str]]):
        unembargo_dt (Union[Unset, datetime.datetime]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        workflow_state (Union[Unset, list[OsidbApiV1FlawsListWorkflowStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        acknowledgments_affiliation=acknowledgments_affiliation,
        acknowledgments_created_dt=acknowledgments_created_dt,
        acknowledgments_created_dt_date=acknowledgments_created_dt_date,
        acknowledgments_created_dt_date_gte=acknowledgments_created_dt_date_gte,
        acknowledgments_created_dt_date_lte=acknowledgments_created_dt_date_lte,
        acknowledgments_created_dt_gt=acknowledgments_created_dt_gt,
        acknowledgments_created_dt_gte=acknowledgments_created_dt_gte,
        acknowledgments_created_dt_lt=acknowledgments_created_dt_lt,
        acknowledgments_created_dt_lte=acknowledgments_created_dt_lte,
        acknowledgments_from_upstream=acknowledgments_from_upstream,
        acknowledgments_name=acknowledgments_name,
        acknowledgments_updated_dt=acknowledgments_updated_dt,
        acknowledgments_updated_dt_date=acknowledgments_updated_dt_date,
        acknowledgments_updated_dt_date_gte=acknowledgments_updated_dt_date_gte,
        acknowledgments_updated_dt_date_lte=acknowledgments_updated_dt_date_lte,
        acknowledgments_updated_dt_gt=acknowledgments_updated_dt_gt,
        acknowledgments_updated_dt_gte=acknowledgments_updated_dt_gte,
        acknowledgments_updated_dt_lt=acknowledgments_updated_dt_lt,
        acknowledgments_updated_dt_lte=acknowledgments_updated_dt_lte,
        acknowledgments_uuid=acknowledgments_uuid,
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
        affects_impact=affects_impact,
        affects_ps_component=affects_ps_component,
        affects_ps_module=affects_ps_module,
        affects_resolution=affects_resolution,
        affects_trackers_created_dt=affects_trackers_created_dt,
        affects_trackers_created_dt_date=affects_trackers_created_dt_date,
        affects_trackers_created_dt_date_gte=affects_trackers_created_dt_date_gte,
        affects_trackers_created_dt_date_lte=affects_trackers_created_dt_date_lte,
        affects_trackers_created_dt_gt=affects_trackers_created_dt_gt,
        affects_trackers_created_dt_gte=affects_trackers_created_dt_gte,
        affects_trackers_created_dt_lt=affects_trackers_created_dt_lt,
        affects_trackers_created_dt_lte=affects_trackers_created_dt_lte,
        affects_trackers_embargoed=affects_trackers_embargoed,
        affects_trackers_errata_advisory_name=affects_trackers_errata_advisory_name,
        affects_trackers_errata_et_id=affects_trackers_errata_et_id,
        affects_trackers_errata_shipped_dt=affects_trackers_errata_shipped_dt,
        affects_trackers_errata_shipped_dt_date=affects_trackers_errata_shipped_dt_date,
        affects_trackers_errata_shipped_dt_date_gte=affects_trackers_errata_shipped_dt_date_gte,
        affects_trackers_errata_shipped_dt_date_lte=affects_trackers_errata_shipped_dt_date_lte,
        affects_trackers_errata_shipped_dt_gt=affects_trackers_errata_shipped_dt_gt,
        affects_trackers_errata_shipped_dt_gte=affects_trackers_errata_shipped_dt_gte,
        affects_trackers_errata_shipped_dt_lt=affects_trackers_errata_shipped_dt_lt,
        affects_trackers_errata_shipped_dt_lte=affects_trackers_errata_shipped_dt_lte,
        affects_trackers_external_system_id=affects_trackers_external_system_id,
        affects_trackers_ps_update_stream=affects_trackers_ps_update_stream,
        affects_trackers_resolution=affects_trackers_resolution,
        affects_trackers_status=affects_trackers_status,
        affects_trackers_type=affects_trackers_type,
        affects_trackers_updated_dt=affects_trackers_updated_dt,
        affects_trackers_updated_dt_date=affects_trackers_updated_dt_date,
        affects_trackers_updated_dt_date_gte=affects_trackers_updated_dt_date_gte,
        affects_trackers_updated_dt_date_lte=affects_trackers_updated_dt_date_lte,
        affects_trackers_updated_dt_gt=affects_trackers_updated_dt_gt,
        affects_trackers_updated_dt_gte=affects_trackers_updated_dt_gte,
        affects_trackers_updated_dt_lt=affects_trackers_updated_dt_lt,
        affects_trackers_updated_dt_lte=affects_trackers_updated_dt_lte,
        affects_trackers_uuid=affects_trackers_uuid,
        affects_updated_dt=affects_updated_dt,
        affects_updated_dt_date=affects_updated_dt_date,
        affects_updated_dt_date_gte=affects_updated_dt_date_gte,
        affects_updated_dt_date_lte=affects_updated_dt_date_lte,
        affects_updated_dt_gt=affects_updated_dt_gt,
        affects_updated_dt_gte=affects_updated_dt_gte,
        affects_updated_dt_lt=affects_updated_dt_lt,
        affects_updated_dt_lte=affects_updated_dt_lte,
        affects_uuid=affects_uuid,
        bz_id=bz_id,
        changed_after=changed_after,
        changed_before=changed_before,
        comment_zero=comment_zero,
        components=components,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cve_description=cve_description,
        cve_description_isempty=cve_description_isempty,
        cve_id=cve_id,
        cve_id_isempty=cve_id_isempty,
        cvss2_nist_isempty=cvss2_nist_isempty,
        cvss2_rh_isempty=cvss2_rh_isempty,
        cvss3_nist_isempty=cvss3_nist_isempty,
        cvss3_rh_isempty=cvss3_rh_isempty,
        cvss4_nist_isempty=cvss4_nist_isempty,
        cvss4_rh_isempty=cvss4_rh_isempty,
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
        cwe_id=cwe_id,
        cwe_id_isempty=cwe_id_isempty,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        impact=impact,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        major_incident_start_dt=major_incident_start_dt,
        major_incident_start_dt_date=major_incident_start_dt_date,
        major_incident_start_dt_date_gte=major_incident_start_dt_date_gte,
        major_incident_start_dt_date_lte=major_incident_start_dt_date_lte,
        major_incident_start_dt_gt=major_incident_start_dt_gt,
        major_incident_start_dt_gte=major_incident_start_dt_gte,
        major_incident_start_dt_lt=major_incident_start_dt_lt,
        major_incident_start_dt_lte=major_incident_start_dt_lte,
        major_incident_state=major_incident_state,
        mitigation_isempty=mitigation_isempty,
        nist_cvss_validation=nist_cvss_validation,
        offset=offset,
        order=order,
        owner=owner,
        owner_isempty=owner_isempty,
        query=query,
        references_created_dt=references_created_dt,
        references_created_dt_date=references_created_dt_date,
        references_created_dt_date_gte=references_created_dt_date_gte,
        references_created_dt_date_lte=references_created_dt_date_lte,
        references_created_dt_gt=references_created_dt_gt,
        references_created_dt_gte=references_created_dt_gte,
        references_created_dt_lt=references_created_dt_lt,
        references_created_dt_lte=references_created_dt_lte,
        references_description=references_description,
        references_type=references_type,
        references_updated_dt=references_updated_dt,
        references_updated_dt_date=references_updated_dt_date,
        references_updated_dt_date_gte=references_updated_dt_date_gte,
        references_updated_dt_date_lte=references_updated_dt_date_lte,
        references_updated_dt_gt=references_updated_dt_gt,
        references_updated_dt_gte=references_updated_dt_gte,
        references_updated_dt_lt=references_updated_dt_lt,
        references_updated_dt_lte=references_updated_dt_lte,
        references_url=references_url,
        references_uuid=references_uuid,
        reported_dt=reported_dt,
        reported_dt_date=reported_dt_date,
        reported_dt_date_gte=reported_dt_date_gte,
        reported_dt_date_lte=reported_dt_date_lte,
        reported_dt_gt=reported_dt_gt,
        reported_dt_gte=reported_dt_gte,
        reported_dt_lt=reported_dt_lt,
        reported_dt_lte=reported_dt_lte,
        requires_cve_description=requires_cve_description,
        search=search,
        source=source,
        statement=statement,
        statement_isempty=statement_isempty,
        team_id=team_id,
        title=title,
        tracker_ids=tracker_ids,
        unembargo_dt=unembargo_dt,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
        workflow_state=workflow_state,
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
    acknowledgments_affiliation: Union[Unset, str] = UNSET,
    acknowledgments_created_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_from_upstream: Union[Unset, bool] = UNSET,
    acknowledgments_name: Union[Unset, str] = UNSET,
    acknowledgments_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, UUID] = UNSET,
    affects_affectedness: Union[Unset, OsidbApiV1FlawsListAffectsAffectedness] = UNSET,
    affects_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, bool] = UNSET,
    affects_impact: Union[Unset, OsidbApiV1FlawsListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV1FlawsListAffectsResolution] = UNSET,
    affects_trackers_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_embargoed: Union[Unset, bool] = UNSET,
    affects_trackers_errata_advisory_name: Union[Unset, str] = UNSET,
    affects_trackers_errata_et_id: Union[Unset, int] = UNSET,
    affects_trackers_errata_shipped_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_external_system_id: Union[Unset, str] = UNSET,
    affects_trackers_ps_update_stream: Union[Unset, str] = UNSET,
    affects_trackers_resolution: Union[Unset, str] = UNSET,
    affects_trackers_status: Union[Unset, str] = UNSET,
    affects_trackers_type: Union[Unset, OsidbApiV1FlawsListAffectsTrackersType] = UNSET,
    affects_trackers_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_uuid: Union[Unset, UUID] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    bz_id: Union[Unset, float] = UNSET,
    changed_after: Union[Unset, datetime.datetime] = UNSET,
    changed_before: Union[Unset, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, str] = UNSET,
    components: Union[Unset, list[str]] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cve_description: Union[Unset, str] = UNSET,
    cve_description_isempty: Union[Unset, bool] = UNSET,
    cve_id: Union[Unset, list[str]] = UNSET,
    cve_id_isempty: Union[Unset, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, OsidbApiV1FlawsListCvssScoresIssuer] = UNSET,
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
    cwe_id: Union[Unset, str] = UNSET,
    cwe_id_isempty: Union[Unset, bool] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    impact: Union[Unset, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    major_incident_start_dt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_date: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    major_incident_state: Union[Unset, OsidbApiV1FlawsListMajorIncidentState] = UNSET,
    mitigation_isempty: Union[Unset, bool] = UNSET,
    nist_cvss_validation: Union[Unset, OsidbApiV1FlawsListNistCvssValidation] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, str] = UNSET,
    owner_isempty: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    references_created_dt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_date: Union[Unset, datetime.date] = UNSET,
    references_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_description: Union[Unset, str] = UNSET,
    references_type: Union[Unset, OsidbApiV1FlawsListReferencesType] = UNSET,
    references_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_url: Union[Unset, str] = UNSET,
    references_uuid: Union[Unset, UUID] = UNSET,
    reported_dt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, OsidbApiV1FlawsListRequiresCveDescription
    ] = UNSET,
    search: Union[Unset, str] = UNSET,
    source: Union[Unset, OsidbApiV1FlawsListSource] = UNSET,
    statement: Union[Unset, str] = UNSET,
    statement_isempty: Union[Unset, bool] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    tracker_ids: Union[Unset, list[str]] = UNSET,
    unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    workflow_state: Union[Unset, list[OsidbApiV1FlawsListWorkflowStateItem]] = UNSET,
) -> Optional[OsidbApiV1FlawsListResponse200]:
    """
    Args:
        acknowledgments_affiliation (Union[Unset, str]):
        acknowledgments_created_dt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_date (Union[Unset, datetime.date]):
        acknowledgments_created_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_created_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_created_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_from_upstream (Union[Unset, bool]):
        acknowledgments_name (Union[Unset, str]):
        acknowledgments_updated_dt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_date (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_uuid (Union[Unset, UUID]):
        affects_affectedness (Union[Unset, OsidbApiV1FlawsListAffectsAffectedness]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_impact (Union[Unset, OsidbApiV1FlawsListAffectsImpact]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_module (Union[Unset, str]):
        affects_resolution (Union[Unset, OsidbApiV1FlawsListAffectsResolution]):
        affects_trackers_created_dt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_date (Union[Unset, datetime.date]):
        affects_trackers_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_embargoed (Union[Unset, bool]):
        affects_trackers_errata_advisory_name (Union[Unset, str]):
        affects_trackers_errata_et_id (Union[Unset, int]):
        affects_trackers_errata_shipped_dt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_date (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_external_system_id (Union[Unset, str]):
        affects_trackers_ps_update_stream (Union[Unset, str]):
        affects_trackers_resolution (Union[Unset, str]):
        affects_trackers_status (Union[Unset, str]):
        affects_trackers_type (Union[Unset, OsidbApiV1FlawsListAffectsTrackersType]):
        affects_trackers_updated_dt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_date (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_uuid (Union[Unset, UUID]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        bz_id (Union[Unset, float]):
        changed_after (Union[Unset, datetime.datetime]):
        changed_before (Union[Unset, datetime.datetime]):
        comment_zero (Union[Unset, str]):
        components (Union[Unset, list[str]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cve_description (Union[Unset, str]):
        cve_description_isempty (Union[Unset, bool]):
        cve_id (Union[Unset, list[str]]):
        cve_id_isempty (Union[Unset, bool]):
        cvss2_nist_isempty (Union[Unset, bool]):
        cvss2_rh_isempty (Union[Unset, bool]):
        cvss3_nist_isempty (Union[Unset, bool]):
        cvss3_rh_isempty (Union[Unset, bool]):
        cvss4_nist_isempty (Union[Unset, bool]):
        cvss4_rh_isempty (Union[Unset, bool]):
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
        cvss_scores_issuer (Union[Unset, OsidbApiV1FlawsListCvssScoresIssuer]):
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
        cwe_id (Union[Unset, str]):
        cwe_id_isempty (Union[Unset, bool]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        impact (Union[Unset, OsidbApiV1FlawsListImpact]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        major_incident_start_dt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_date (Union[Unset, datetime.date]):
        major_incident_start_dt_date_gte (Union[Unset, datetime.date]):
        major_incident_start_dt_date_lte (Union[Unset, datetime.date]):
        major_incident_start_dt_gt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_gte (Union[Unset, datetime.datetime]):
        major_incident_start_dt_lt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_lte (Union[Unset, datetime.datetime]):
        major_incident_state (Union[Unset, OsidbApiV1FlawsListMajorIncidentState]):
        mitigation_isempty (Union[Unset, bool]):
        nist_cvss_validation (Union[Unset, OsidbApiV1FlawsListNistCvssValidation]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1FlawsListOrderItem]]):
        owner (Union[Unset, str]):
        owner_isempty (Union[Unset, bool]):
        query (Union[Unset, str]):
        references_created_dt (Union[Unset, datetime.datetime]):
        references_created_dt_date (Union[Unset, datetime.date]):
        references_created_dt_date_gte (Union[Unset, datetime.date]):
        references_created_dt_date_lte (Union[Unset, datetime.date]):
        references_created_dt_gt (Union[Unset, datetime.datetime]):
        references_created_dt_gte (Union[Unset, datetime.datetime]):
        references_created_dt_lt (Union[Unset, datetime.datetime]):
        references_created_dt_lte (Union[Unset, datetime.datetime]):
        references_description (Union[Unset, str]):
        references_type (Union[Unset, OsidbApiV1FlawsListReferencesType]):
        references_updated_dt (Union[Unset, datetime.datetime]):
        references_updated_dt_date (Union[Unset, datetime.date]):
        references_updated_dt_date_gte (Union[Unset, datetime.date]):
        references_updated_dt_date_lte (Union[Unset, datetime.date]):
        references_updated_dt_gt (Union[Unset, datetime.datetime]):
        references_updated_dt_gte (Union[Unset, datetime.datetime]):
        references_updated_dt_lt (Union[Unset, datetime.datetime]):
        references_updated_dt_lte (Union[Unset, datetime.datetime]):
        references_url (Union[Unset, str]):
        references_uuid (Union[Unset, UUID]):
        reported_dt (Union[Unset, datetime.datetime]):
        reported_dt_date (Union[Unset, datetime.date]):
        reported_dt_date_gte (Union[Unset, datetime.date]):
        reported_dt_date_lte (Union[Unset, datetime.date]):
        reported_dt_gt (Union[Unset, datetime.datetime]):
        reported_dt_gte (Union[Unset, datetime.datetime]):
        reported_dt_lt (Union[Unset, datetime.datetime]):
        reported_dt_lte (Union[Unset, datetime.datetime]):
        requires_cve_description (Union[Unset, OsidbApiV1FlawsListRequiresCveDescription]):
        search (Union[Unset, str]):
        source (Union[Unset, OsidbApiV1FlawsListSource]):
        statement (Union[Unset, str]):
        statement_isempty (Union[Unset, bool]):
        team_id (Union[Unset, str]):
        title (Union[Unset, str]):
        tracker_ids (Union[Unset, list[str]]):
        unembargo_dt (Union[Unset, datetime.datetime]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        workflow_state (Union[Unset, list[OsidbApiV1FlawsListWorkflowStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsListResponse200
    """

    return sync_detailed(
        client=client,
        acknowledgments_affiliation=acknowledgments_affiliation,
        acknowledgments_created_dt=acknowledgments_created_dt,
        acknowledgments_created_dt_date=acknowledgments_created_dt_date,
        acknowledgments_created_dt_date_gte=acknowledgments_created_dt_date_gte,
        acknowledgments_created_dt_date_lte=acknowledgments_created_dt_date_lte,
        acknowledgments_created_dt_gt=acknowledgments_created_dt_gt,
        acknowledgments_created_dt_gte=acknowledgments_created_dt_gte,
        acknowledgments_created_dt_lt=acknowledgments_created_dt_lt,
        acknowledgments_created_dt_lte=acknowledgments_created_dt_lte,
        acknowledgments_from_upstream=acknowledgments_from_upstream,
        acknowledgments_name=acknowledgments_name,
        acknowledgments_updated_dt=acknowledgments_updated_dt,
        acknowledgments_updated_dt_date=acknowledgments_updated_dt_date,
        acknowledgments_updated_dt_date_gte=acknowledgments_updated_dt_date_gte,
        acknowledgments_updated_dt_date_lte=acknowledgments_updated_dt_date_lte,
        acknowledgments_updated_dt_gt=acknowledgments_updated_dt_gt,
        acknowledgments_updated_dt_gte=acknowledgments_updated_dt_gte,
        acknowledgments_updated_dt_lt=acknowledgments_updated_dt_lt,
        acknowledgments_updated_dt_lte=acknowledgments_updated_dt_lte,
        acknowledgments_uuid=acknowledgments_uuid,
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
        affects_impact=affects_impact,
        affects_ps_component=affects_ps_component,
        affects_ps_module=affects_ps_module,
        affects_resolution=affects_resolution,
        affects_trackers_created_dt=affects_trackers_created_dt,
        affects_trackers_created_dt_date=affects_trackers_created_dt_date,
        affects_trackers_created_dt_date_gte=affects_trackers_created_dt_date_gte,
        affects_trackers_created_dt_date_lte=affects_trackers_created_dt_date_lte,
        affects_trackers_created_dt_gt=affects_trackers_created_dt_gt,
        affects_trackers_created_dt_gte=affects_trackers_created_dt_gte,
        affects_trackers_created_dt_lt=affects_trackers_created_dt_lt,
        affects_trackers_created_dt_lte=affects_trackers_created_dt_lte,
        affects_trackers_embargoed=affects_trackers_embargoed,
        affects_trackers_errata_advisory_name=affects_trackers_errata_advisory_name,
        affects_trackers_errata_et_id=affects_trackers_errata_et_id,
        affects_trackers_errata_shipped_dt=affects_trackers_errata_shipped_dt,
        affects_trackers_errata_shipped_dt_date=affects_trackers_errata_shipped_dt_date,
        affects_trackers_errata_shipped_dt_date_gte=affects_trackers_errata_shipped_dt_date_gte,
        affects_trackers_errata_shipped_dt_date_lte=affects_trackers_errata_shipped_dt_date_lte,
        affects_trackers_errata_shipped_dt_gt=affects_trackers_errata_shipped_dt_gt,
        affects_trackers_errata_shipped_dt_gte=affects_trackers_errata_shipped_dt_gte,
        affects_trackers_errata_shipped_dt_lt=affects_trackers_errata_shipped_dt_lt,
        affects_trackers_errata_shipped_dt_lte=affects_trackers_errata_shipped_dt_lte,
        affects_trackers_external_system_id=affects_trackers_external_system_id,
        affects_trackers_ps_update_stream=affects_trackers_ps_update_stream,
        affects_trackers_resolution=affects_trackers_resolution,
        affects_trackers_status=affects_trackers_status,
        affects_trackers_type=affects_trackers_type,
        affects_trackers_updated_dt=affects_trackers_updated_dt,
        affects_trackers_updated_dt_date=affects_trackers_updated_dt_date,
        affects_trackers_updated_dt_date_gte=affects_trackers_updated_dt_date_gte,
        affects_trackers_updated_dt_date_lte=affects_trackers_updated_dt_date_lte,
        affects_trackers_updated_dt_gt=affects_trackers_updated_dt_gt,
        affects_trackers_updated_dt_gte=affects_trackers_updated_dt_gte,
        affects_trackers_updated_dt_lt=affects_trackers_updated_dt_lt,
        affects_trackers_updated_dt_lte=affects_trackers_updated_dt_lte,
        affects_trackers_uuid=affects_trackers_uuid,
        affects_updated_dt=affects_updated_dt,
        affects_updated_dt_date=affects_updated_dt_date,
        affects_updated_dt_date_gte=affects_updated_dt_date_gte,
        affects_updated_dt_date_lte=affects_updated_dt_date_lte,
        affects_updated_dt_gt=affects_updated_dt_gt,
        affects_updated_dt_gte=affects_updated_dt_gte,
        affects_updated_dt_lt=affects_updated_dt_lt,
        affects_updated_dt_lte=affects_updated_dt_lte,
        affects_uuid=affects_uuid,
        bz_id=bz_id,
        changed_after=changed_after,
        changed_before=changed_before,
        comment_zero=comment_zero,
        components=components,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cve_description=cve_description,
        cve_description_isempty=cve_description_isempty,
        cve_id=cve_id,
        cve_id_isempty=cve_id_isempty,
        cvss2_nist_isempty=cvss2_nist_isempty,
        cvss2_rh_isempty=cvss2_rh_isempty,
        cvss3_nist_isempty=cvss3_nist_isempty,
        cvss3_rh_isempty=cvss3_rh_isempty,
        cvss4_nist_isempty=cvss4_nist_isempty,
        cvss4_rh_isempty=cvss4_rh_isempty,
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
        cwe_id=cwe_id,
        cwe_id_isempty=cwe_id_isempty,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        impact=impact,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        major_incident_start_dt=major_incident_start_dt,
        major_incident_start_dt_date=major_incident_start_dt_date,
        major_incident_start_dt_date_gte=major_incident_start_dt_date_gte,
        major_incident_start_dt_date_lte=major_incident_start_dt_date_lte,
        major_incident_start_dt_gt=major_incident_start_dt_gt,
        major_incident_start_dt_gte=major_incident_start_dt_gte,
        major_incident_start_dt_lt=major_incident_start_dt_lt,
        major_incident_start_dt_lte=major_incident_start_dt_lte,
        major_incident_state=major_incident_state,
        mitigation_isempty=mitigation_isempty,
        nist_cvss_validation=nist_cvss_validation,
        offset=offset,
        order=order,
        owner=owner,
        owner_isempty=owner_isempty,
        query=query,
        references_created_dt=references_created_dt,
        references_created_dt_date=references_created_dt_date,
        references_created_dt_date_gte=references_created_dt_date_gte,
        references_created_dt_date_lte=references_created_dt_date_lte,
        references_created_dt_gt=references_created_dt_gt,
        references_created_dt_gte=references_created_dt_gte,
        references_created_dt_lt=references_created_dt_lt,
        references_created_dt_lte=references_created_dt_lte,
        references_description=references_description,
        references_type=references_type,
        references_updated_dt=references_updated_dt,
        references_updated_dt_date=references_updated_dt_date,
        references_updated_dt_date_gte=references_updated_dt_date_gte,
        references_updated_dt_date_lte=references_updated_dt_date_lte,
        references_updated_dt_gt=references_updated_dt_gt,
        references_updated_dt_gte=references_updated_dt_gte,
        references_updated_dt_lt=references_updated_dt_lt,
        references_updated_dt_lte=references_updated_dt_lte,
        references_url=references_url,
        references_uuid=references_uuid,
        reported_dt=reported_dt,
        reported_dt_date=reported_dt_date,
        reported_dt_date_gte=reported_dt_date_gte,
        reported_dt_date_lte=reported_dt_date_lte,
        reported_dt_gt=reported_dt_gt,
        reported_dt_gte=reported_dt_gte,
        reported_dt_lt=reported_dt_lt,
        reported_dt_lte=reported_dt_lte,
        requires_cve_description=requires_cve_description,
        search=search,
        source=source,
        statement=statement,
        statement_isempty=statement_isempty,
        team_id=team_id,
        title=title,
        tracker_ids=tracker_ids,
        unembargo_dt=unembargo_dt,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
        workflow_state=workflow_state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    acknowledgments_affiliation: Union[Unset, str] = UNSET,
    acknowledgments_created_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_from_upstream: Union[Unset, bool] = UNSET,
    acknowledgments_name: Union[Unset, str] = UNSET,
    acknowledgments_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, UUID] = UNSET,
    affects_affectedness: Union[Unset, OsidbApiV1FlawsListAffectsAffectedness] = UNSET,
    affects_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, bool] = UNSET,
    affects_impact: Union[Unset, OsidbApiV1FlawsListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV1FlawsListAffectsResolution] = UNSET,
    affects_trackers_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_embargoed: Union[Unset, bool] = UNSET,
    affects_trackers_errata_advisory_name: Union[Unset, str] = UNSET,
    affects_trackers_errata_et_id: Union[Unset, int] = UNSET,
    affects_trackers_errata_shipped_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_external_system_id: Union[Unset, str] = UNSET,
    affects_trackers_ps_update_stream: Union[Unset, str] = UNSET,
    affects_trackers_resolution: Union[Unset, str] = UNSET,
    affects_trackers_status: Union[Unset, str] = UNSET,
    affects_trackers_type: Union[Unset, OsidbApiV1FlawsListAffectsTrackersType] = UNSET,
    affects_trackers_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_uuid: Union[Unset, UUID] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    bz_id: Union[Unset, float] = UNSET,
    changed_after: Union[Unset, datetime.datetime] = UNSET,
    changed_before: Union[Unset, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, str] = UNSET,
    components: Union[Unset, list[str]] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cve_description: Union[Unset, str] = UNSET,
    cve_description_isempty: Union[Unset, bool] = UNSET,
    cve_id: Union[Unset, list[str]] = UNSET,
    cve_id_isempty: Union[Unset, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, OsidbApiV1FlawsListCvssScoresIssuer] = UNSET,
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
    cwe_id: Union[Unset, str] = UNSET,
    cwe_id_isempty: Union[Unset, bool] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    impact: Union[Unset, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    major_incident_start_dt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_date: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    major_incident_state: Union[Unset, OsidbApiV1FlawsListMajorIncidentState] = UNSET,
    mitigation_isempty: Union[Unset, bool] = UNSET,
    nist_cvss_validation: Union[Unset, OsidbApiV1FlawsListNistCvssValidation] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, str] = UNSET,
    owner_isempty: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    references_created_dt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_date: Union[Unset, datetime.date] = UNSET,
    references_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_description: Union[Unset, str] = UNSET,
    references_type: Union[Unset, OsidbApiV1FlawsListReferencesType] = UNSET,
    references_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_url: Union[Unset, str] = UNSET,
    references_uuid: Union[Unset, UUID] = UNSET,
    reported_dt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, OsidbApiV1FlawsListRequiresCveDescription
    ] = UNSET,
    search: Union[Unset, str] = UNSET,
    source: Union[Unset, OsidbApiV1FlawsListSource] = UNSET,
    statement: Union[Unset, str] = UNSET,
    statement_isempty: Union[Unset, bool] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    tracker_ids: Union[Unset, list[str]] = UNSET,
    unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    workflow_state: Union[Unset, list[OsidbApiV1FlawsListWorkflowStateItem]] = UNSET,
) -> Response[OsidbApiV1FlawsListResponse200]:
    """
    Args:
        acknowledgments_affiliation (Union[Unset, str]):
        acknowledgments_created_dt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_date (Union[Unset, datetime.date]):
        acknowledgments_created_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_created_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_created_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_from_upstream (Union[Unset, bool]):
        acknowledgments_name (Union[Unset, str]):
        acknowledgments_updated_dt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_date (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_uuid (Union[Unset, UUID]):
        affects_affectedness (Union[Unset, OsidbApiV1FlawsListAffectsAffectedness]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_impact (Union[Unset, OsidbApiV1FlawsListAffectsImpact]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_module (Union[Unset, str]):
        affects_resolution (Union[Unset, OsidbApiV1FlawsListAffectsResolution]):
        affects_trackers_created_dt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_date (Union[Unset, datetime.date]):
        affects_trackers_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_embargoed (Union[Unset, bool]):
        affects_trackers_errata_advisory_name (Union[Unset, str]):
        affects_trackers_errata_et_id (Union[Unset, int]):
        affects_trackers_errata_shipped_dt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_date (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_external_system_id (Union[Unset, str]):
        affects_trackers_ps_update_stream (Union[Unset, str]):
        affects_trackers_resolution (Union[Unset, str]):
        affects_trackers_status (Union[Unset, str]):
        affects_trackers_type (Union[Unset, OsidbApiV1FlawsListAffectsTrackersType]):
        affects_trackers_updated_dt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_date (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_uuid (Union[Unset, UUID]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        bz_id (Union[Unset, float]):
        changed_after (Union[Unset, datetime.datetime]):
        changed_before (Union[Unset, datetime.datetime]):
        comment_zero (Union[Unset, str]):
        components (Union[Unset, list[str]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cve_description (Union[Unset, str]):
        cve_description_isempty (Union[Unset, bool]):
        cve_id (Union[Unset, list[str]]):
        cve_id_isempty (Union[Unset, bool]):
        cvss2_nist_isempty (Union[Unset, bool]):
        cvss2_rh_isempty (Union[Unset, bool]):
        cvss3_nist_isempty (Union[Unset, bool]):
        cvss3_rh_isempty (Union[Unset, bool]):
        cvss4_nist_isempty (Union[Unset, bool]):
        cvss4_rh_isempty (Union[Unset, bool]):
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
        cvss_scores_issuer (Union[Unset, OsidbApiV1FlawsListCvssScoresIssuer]):
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
        cwe_id (Union[Unset, str]):
        cwe_id_isempty (Union[Unset, bool]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        impact (Union[Unset, OsidbApiV1FlawsListImpact]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        major_incident_start_dt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_date (Union[Unset, datetime.date]):
        major_incident_start_dt_date_gte (Union[Unset, datetime.date]):
        major_incident_start_dt_date_lte (Union[Unset, datetime.date]):
        major_incident_start_dt_gt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_gte (Union[Unset, datetime.datetime]):
        major_incident_start_dt_lt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_lte (Union[Unset, datetime.datetime]):
        major_incident_state (Union[Unset, OsidbApiV1FlawsListMajorIncidentState]):
        mitigation_isempty (Union[Unset, bool]):
        nist_cvss_validation (Union[Unset, OsidbApiV1FlawsListNistCvssValidation]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1FlawsListOrderItem]]):
        owner (Union[Unset, str]):
        owner_isempty (Union[Unset, bool]):
        query (Union[Unset, str]):
        references_created_dt (Union[Unset, datetime.datetime]):
        references_created_dt_date (Union[Unset, datetime.date]):
        references_created_dt_date_gte (Union[Unset, datetime.date]):
        references_created_dt_date_lte (Union[Unset, datetime.date]):
        references_created_dt_gt (Union[Unset, datetime.datetime]):
        references_created_dt_gte (Union[Unset, datetime.datetime]):
        references_created_dt_lt (Union[Unset, datetime.datetime]):
        references_created_dt_lte (Union[Unset, datetime.datetime]):
        references_description (Union[Unset, str]):
        references_type (Union[Unset, OsidbApiV1FlawsListReferencesType]):
        references_updated_dt (Union[Unset, datetime.datetime]):
        references_updated_dt_date (Union[Unset, datetime.date]):
        references_updated_dt_date_gte (Union[Unset, datetime.date]):
        references_updated_dt_date_lte (Union[Unset, datetime.date]):
        references_updated_dt_gt (Union[Unset, datetime.datetime]):
        references_updated_dt_gte (Union[Unset, datetime.datetime]):
        references_updated_dt_lt (Union[Unset, datetime.datetime]):
        references_updated_dt_lte (Union[Unset, datetime.datetime]):
        references_url (Union[Unset, str]):
        references_uuid (Union[Unset, UUID]):
        reported_dt (Union[Unset, datetime.datetime]):
        reported_dt_date (Union[Unset, datetime.date]):
        reported_dt_date_gte (Union[Unset, datetime.date]):
        reported_dt_date_lte (Union[Unset, datetime.date]):
        reported_dt_gt (Union[Unset, datetime.datetime]):
        reported_dt_gte (Union[Unset, datetime.datetime]):
        reported_dt_lt (Union[Unset, datetime.datetime]):
        reported_dt_lte (Union[Unset, datetime.datetime]):
        requires_cve_description (Union[Unset, OsidbApiV1FlawsListRequiresCveDescription]):
        search (Union[Unset, str]):
        source (Union[Unset, OsidbApiV1FlawsListSource]):
        statement (Union[Unset, str]):
        statement_isempty (Union[Unset, bool]):
        team_id (Union[Unset, str]):
        title (Union[Unset, str]):
        tracker_ids (Union[Unset, list[str]]):
        unembargo_dt (Union[Unset, datetime.datetime]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        workflow_state (Union[Unset, list[OsidbApiV1FlawsListWorkflowStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV1FlawsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        acknowledgments_affiliation=acknowledgments_affiliation,
        acknowledgments_created_dt=acknowledgments_created_dt,
        acknowledgments_created_dt_date=acknowledgments_created_dt_date,
        acknowledgments_created_dt_date_gte=acknowledgments_created_dt_date_gte,
        acknowledgments_created_dt_date_lte=acknowledgments_created_dt_date_lte,
        acknowledgments_created_dt_gt=acknowledgments_created_dt_gt,
        acknowledgments_created_dt_gte=acknowledgments_created_dt_gte,
        acknowledgments_created_dt_lt=acknowledgments_created_dt_lt,
        acknowledgments_created_dt_lte=acknowledgments_created_dt_lte,
        acknowledgments_from_upstream=acknowledgments_from_upstream,
        acknowledgments_name=acknowledgments_name,
        acknowledgments_updated_dt=acknowledgments_updated_dt,
        acknowledgments_updated_dt_date=acknowledgments_updated_dt_date,
        acknowledgments_updated_dt_date_gte=acknowledgments_updated_dt_date_gte,
        acknowledgments_updated_dt_date_lte=acknowledgments_updated_dt_date_lte,
        acknowledgments_updated_dt_gt=acknowledgments_updated_dt_gt,
        acknowledgments_updated_dt_gte=acknowledgments_updated_dt_gte,
        acknowledgments_updated_dt_lt=acknowledgments_updated_dt_lt,
        acknowledgments_updated_dt_lte=acknowledgments_updated_dt_lte,
        acknowledgments_uuid=acknowledgments_uuid,
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
        affects_impact=affects_impact,
        affects_ps_component=affects_ps_component,
        affects_ps_module=affects_ps_module,
        affects_resolution=affects_resolution,
        affects_trackers_created_dt=affects_trackers_created_dt,
        affects_trackers_created_dt_date=affects_trackers_created_dt_date,
        affects_trackers_created_dt_date_gte=affects_trackers_created_dt_date_gte,
        affects_trackers_created_dt_date_lte=affects_trackers_created_dt_date_lte,
        affects_trackers_created_dt_gt=affects_trackers_created_dt_gt,
        affects_trackers_created_dt_gte=affects_trackers_created_dt_gte,
        affects_trackers_created_dt_lt=affects_trackers_created_dt_lt,
        affects_trackers_created_dt_lte=affects_trackers_created_dt_lte,
        affects_trackers_embargoed=affects_trackers_embargoed,
        affects_trackers_errata_advisory_name=affects_trackers_errata_advisory_name,
        affects_trackers_errata_et_id=affects_trackers_errata_et_id,
        affects_trackers_errata_shipped_dt=affects_trackers_errata_shipped_dt,
        affects_trackers_errata_shipped_dt_date=affects_trackers_errata_shipped_dt_date,
        affects_trackers_errata_shipped_dt_date_gte=affects_trackers_errata_shipped_dt_date_gte,
        affects_trackers_errata_shipped_dt_date_lte=affects_trackers_errata_shipped_dt_date_lte,
        affects_trackers_errata_shipped_dt_gt=affects_trackers_errata_shipped_dt_gt,
        affects_trackers_errata_shipped_dt_gte=affects_trackers_errata_shipped_dt_gte,
        affects_trackers_errata_shipped_dt_lt=affects_trackers_errata_shipped_dt_lt,
        affects_trackers_errata_shipped_dt_lte=affects_trackers_errata_shipped_dt_lte,
        affects_trackers_external_system_id=affects_trackers_external_system_id,
        affects_trackers_ps_update_stream=affects_trackers_ps_update_stream,
        affects_trackers_resolution=affects_trackers_resolution,
        affects_trackers_status=affects_trackers_status,
        affects_trackers_type=affects_trackers_type,
        affects_trackers_updated_dt=affects_trackers_updated_dt,
        affects_trackers_updated_dt_date=affects_trackers_updated_dt_date,
        affects_trackers_updated_dt_date_gte=affects_trackers_updated_dt_date_gte,
        affects_trackers_updated_dt_date_lte=affects_trackers_updated_dt_date_lte,
        affects_trackers_updated_dt_gt=affects_trackers_updated_dt_gt,
        affects_trackers_updated_dt_gte=affects_trackers_updated_dt_gte,
        affects_trackers_updated_dt_lt=affects_trackers_updated_dt_lt,
        affects_trackers_updated_dt_lte=affects_trackers_updated_dt_lte,
        affects_trackers_uuid=affects_trackers_uuid,
        affects_updated_dt=affects_updated_dt,
        affects_updated_dt_date=affects_updated_dt_date,
        affects_updated_dt_date_gte=affects_updated_dt_date_gte,
        affects_updated_dt_date_lte=affects_updated_dt_date_lte,
        affects_updated_dt_gt=affects_updated_dt_gt,
        affects_updated_dt_gte=affects_updated_dt_gte,
        affects_updated_dt_lt=affects_updated_dt_lt,
        affects_updated_dt_lte=affects_updated_dt_lte,
        affects_uuid=affects_uuid,
        bz_id=bz_id,
        changed_after=changed_after,
        changed_before=changed_before,
        comment_zero=comment_zero,
        components=components,
        created_dt=created_dt,
        created_dt_date=created_dt_date,
        created_dt_date_gte=created_dt_date_gte,
        created_dt_date_lte=created_dt_date_lte,
        created_dt_gt=created_dt_gt,
        created_dt_gte=created_dt_gte,
        created_dt_lt=created_dt_lt,
        created_dt_lte=created_dt_lte,
        cve_description=cve_description,
        cve_description_isempty=cve_description_isempty,
        cve_id=cve_id,
        cve_id_isempty=cve_id_isempty,
        cvss2_nist_isempty=cvss2_nist_isempty,
        cvss2_rh_isempty=cvss2_rh_isempty,
        cvss3_nist_isempty=cvss3_nist_isempty,
        cvss3_rh_isempty=cvss3_rh_isempty,
        cvss4_nist_isempty=cvss4_nist_isempty,
        cvss4_rh_isempty=cvss4_rh_isempty,
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
        cwe_id=cwe_id,
        cwe_id_isempty=cwe_id_isempty,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        impact=impact,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        major_incident_start_dt=major_incident_start_dt,
        major_incident_start_dt_date=major_incident_start_dt_date,
        major_incident_start_dt_date_gte=major_incident_start_dt_date_gte,
        major_incident_start_dt_date_lte=major_incident_start_dt_date_lte,
        major_incident_start_dt_gt=major_incident_start_dt_gt,
        major_incident_start_dt_gte=major_incident_start_dt_gte,
        major_incident_start_dt_lt=major_incident_start_dt_lt,
        major_incident_start_dt_lte=major_incident_start_dt_lte,
        major_incident_state=major_incident_state,
        mitigation_isempty=mitigation_isempty,
        nist_cvss_validation=nist_cvss_validation,
        offset=offset,
        order=order,
        owner=owner,
        owner_isempty=owner_isempty,
        query=query,
        references_created_dt=references_created_dt,
        references_created_dt_date=references_created_dt_date,
        references_created_dt_date_gte=references_created_dt_date_gte,
        references_created_dt_date_lte=references_created_dt_date_lte,
        references_created_dt_gt=references_created_dt_gt,
        references_created_dt_gte=references_created_dt_gte,
        references_created_dt_lt=references_created_dt_lt,
        references_created_dt_lte=references_created_dt_lte,
        references_description=references_description,
        references_type=references_type,
        references_updated_dt=references_updated_dt,
        references_updated_dt_date=references_updated_dt_date,
        references_updated_dt_date_gte=references_updated_dt_date_gte,
        references_updated_dt_date_lte=references_updated_dt_date_lte,
        references_updated_dt_gt=references_updated_dt_gt,
        references_updated_dt_gte=references_updated_dt_gte,
        references_updated_dt_lt=references_updated_dt_lt,
        references_updated_dt_lte=references_updated_dt_lte,
        references_url=references_url,
        references_uuid=references_uuid,
        reported_dt=reported_dt,
        reported_dt_date=reported_dt_date,
        reported_dt_date_gte=reported_dt_date_gte,
        reported_dt_date_lte=reported_dt_date_lte,
        reported_dt_gt=reported_dt_gt,
        reported_dt_gte=reported_dt_gte,
        reported_dt_lt=reported_dt_lt,
        reported_dt_lte=reported_dt_lte,
        requires_cve_description=requires_cve_description,
        search=search,
        source=source,
        statement=statement,
        statement_isempty=statement_isempty,
        team_id=team_id,
        title=title,
        tracker_ids=tracker_ids,
        unembargo_dt=unembargo_dt,
        updated_dt=updated_dt,
        updated_dt_date=updated_dt_date,
        updated_dt_date_gte=updated_dt_date_gte,
        updated_dt_date_lte=updated_dt_date_lte,
        updated_dt_gt=updated_dt_gt,
        updated_dt_gte=updated_dt_gte,
        updated_dt_lt=updated_dt_lt,
        updated_dt_lte=updated_dt_lte,
        uuid=uuid,
        workflow_state=workflow_state,
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
    acknowledgments_affiliation: Union[Unset, str] = UNSET,
    acknowledgments_created_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_from_upstream: Union[Unset, bool] = UNSET,
    acknowledgments_name: Union[Unset, str] = UNSET,
    acknowledgments_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, UUID] = UNSET,
    affects_affectedness: Union[Unset, OsidbApiV1FlawsListAffectsAffectedness] = UNSET,
    affects_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, bool] = UNSET,
    affects_impact: Union[Unset, OsidbApiV1FlawsListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV1FlawsListAffectsResolution] = UNSET,
    affects_trackers_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_embargoed: Union[Unset, bool] = UNSET,
    affects_trackers_errata_advisory_name: Union[Unset, str] = UNSET,
    affects_trackers_errata_et_id: Union[Unset, int] = UNSET,
    affects_trackers_errata_shipped_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_external_system_id: Union[Unset, str] = UNSET,
    affects_trackers_ps_update_stream: Union[Unset, str] = UNSET,
    affects_trackers_resolution: Union[Unset, str] = UNSET,
    affects_trackers_status: Union[Unset, str] = UNSET,
    affects_trackers_type: Union[Unset, OsidbApiV1FlawsListAffectsTrackersType] = UNSET,
    affects_trackers_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_trackers_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_trackers_uuid: Union[Unset, UUID] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    bz_id: Union[Unset, float] = UNSET,
    changed_after: Union[Unset, datetime.datetime] = UNSET,
    changed_before: Union[Unset, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, str] = UNSET,
    components: Union[Unset, list[str]] = UNSET,
    created_dt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    cve_description: Union[Unset, str] = UNSET,
    cve_description_isempty: Union[Unset, bool] = UNSET,
    cve_id: Union[Unset, list[str]] = UNSET,
    cve_id_isempty: Union[Unset, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, OsidbApiV1FlawsListCvssScoresIssuer] = UNSET,
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
    cwe_id: Union[Unset, str] = UNSET,
    cwe_id_isempty: Union[Unset, bool] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    impact: Union[Unset, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_meta_attr: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    major_incident_start_dt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_date: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    major_incident_start_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    major_incident_start_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    major_incident_state: Union[Unset, OsidbApiV1FlawsListMajorIncidentState] = UNSET,
    mitigation_isempty: Union[Unset, bool] = UNSET,
    nist_cvss_validation: Union[Unset, OsidbApiV1FlawsListNistCvssValidation] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV1FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, str] = UNSET,
    owner_isempty: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    references_created_dt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_date: Union[Unset, datetime.date] = UNSET,
    references_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_description: Union[Unset, str] = UNSET,
    references_type: Union[Unset, OsidbApiV1FlawsListReferencesType] = UNSET,
    references_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_url: Union[Unset, str] = UNSET,
    references_uuid: Union[Unset, UUID] = UNSET,
    reported_dt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, OsidbApiV1FlawsListRequiresCveDescription
    ] = UNSET,
    search: Union[Unset, str] = UNSET,
    source: Union[Unset, OsidbApiV1FlawsListSource] = UNSET,
    statement: Union[Unset, str] = UNSET,
    statement_isempty: Union[Unset, bool] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    tracker_ids: Union[Unset, list[str]] = UNSET,
    unembargo_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    uuid: Union[Unset, UUID] = UNSET,
    workflow_state: Union[Unset, list[OsidbApiV1FlawsListWorkflowStateItem]] = UNSET,
) -> Optional[OsidbApiV1FlawsListResponse200]:
    """
    Args:
        acknowledgments_affiliation (Union[Unset, str]):
        acknowledgments_created_dt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_date (Union[Unset, datetime.date]):
        acknowledgments_created_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_created_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_created_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_created_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_from_upstream (Union[Unset, bool]):
        acknowledgments_name (Union[Unset, str]):
        acknowledgments_updated_dt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_date (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_uuid (Union[Unset, UUID]):
        affects_affectedness (Union[Unset, OsidbApiV1FlawsListAffectsAffectedness]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_impact (Union[Unset, OsidbApiV1FlawsListAffectsImpact]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_module (Union[Unset, str]):
        affects_resolution (Union[Unset, OsidbApiV1FlawsListAffectsResolution]):
        affects_trackers_created_dt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_date (Union[Unset, datetime.date]):
        affects_trackers_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_embargoed (Union[Unset, bool]):
        affects_trackers_errata_advisory_name (Union[Unset, str]):
        affects_trackers_errata_et_id (Union[Unset, int]):
        affects_trackers_errata_shipped_dt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_date (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_errata_shipped_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_errata_shipped_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_external_system_id (Union[Unset, str]):
        affects_trackers_ps_update_stream (Union[Unset, str]):
        affects_trackers_resolution (Union[Unset, str]):
        affects_trackers_status (Union[Unset, str]):
        affects_trackers_type (Union[Unset, OsidbApiV1FlawsListAffectsTrackersType]):
        affects_trackers_updated_dt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_date (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_trackers_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_trackers_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_trackers_uuid (Union[Unset, UUID]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        bz_id (Union[Unset, float]):
        changed_after (Union[Unset, datetime.datetime]):
        changed_before (Union[Unset, datetime.datetime]):
        comment_zero (Union[Unset, str]):
        components (Union[Unset, list[str]]):
        created_dt (Union[Unset, datetime.datetime]):
        created_dt_date (Union[Unset, datetime.date]):
        created_dt_date_gte (Union[Unset, datetime.date]):
        created_dt_date_lte (Union[Unset, datetime.date]):
        created_dt_gt (Union[Unset, datetime.datetime]):
        created_dt_gte (Union[Unset, datetime.datetime]):
        created_dt_lt (Union[Unset, datetime.datetime]):
        created_dt_lte (Union[Unset, datetime.datetime]):
        cve_description (Union[Unset, str]):
        cve_description_isempty (Union[Unset, bool]):
        cve_id (Union[Unset, list[str]]):
        cve_id_isempty (Union[Unset, bool]):
        cvss2_nist_isempty (Union[Unset, bool]):
        cvss2_rh_isempty (Union[Unset, bool]):
        cvss3_nist_isempty (Union[Unset, bool]):
        cvss3_rh_isempty (Union[Unset, bool]):
        cvss4_nist_isempty (Union[Unset, bool]):
        cvss4_rh_isempty (Union[Unset, bool]):
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
        cvss_scores_issuer (Union[Unset, OsidbApiV1FlawsListCvssScoresIssuer]):
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
        cwe_id (Union[Unset, str]):
        cwe_id_isempty (Union[Unset, bool]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        impact (Union[Unset, OsidbApiV1FlawsListImpact]):
        include_fields (Union[Unset, list[str]]):
        include_meta_attr (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        major_incident_start_dt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_date (Union[Unset, datetime.date]):
        major_incident_start_dt_date_gte (Union[Unset, datetime.date]):
        major_incident_start_dt_date_lte (Union[Unset, datetime.date]):
        major_incident_start_dt_gt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_gte (Union[Unset, datetime.datetime]):
        major_incident_start_dt_lt (Union[Unset, datetime.datetime]):
        major_incident_start_dt_lte (Union[Unset, datetime.datetime]):
        major_incident_state (Union[Unset, OsidbApiV1FlawsListMajorIncidentState]):
        mitigation_isempty (Union[Unset, bool]):
        nist_cvss_validation (Union[Unset, OsidbApiV1FlawsListNistCvssValidation]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV1FlawsListOrderItem]]):
        owner (Union[Unset, str]):
        owner_isempty (Union[Unset, bool]):
        query (Union[Unset, str]):
        references_created_dt (Union[Unset, datetime.datetime]):
        references_created_dt_date (Union[Unset, datetime.date]):
        references_created_dt_date_gte (Union[Unset, datetime.date]):
        references_created_dt_date_lte (Union[Unset, datetime.date]):
        references_created_dt_gt (Union[Unset, datetime.datetime]):
        references_created_dt_gte (Union[Unset, datetime.datetime]):
        references_created_dt_lt (Union[Unset, datetime.datetime]):
        references_created_dt_lte (Union[Unset, datetime.datetime]):
        references_description (Union[Unset, str]):
        references_type (Union[Unset, OsidbApiV1FlawsListReferencesType]):
        references_updated_dt (Union[Unset, datetime.datetime]):
        references_updated_dt_date (Union[Unset, datetime.date]):
        references_updated_dt_date_gte (Union[Unset, datetime.date]):
        references_updated_dt_date_lte (Union[Unset, datetime.date]):
        references_updated_dt_gt (Union[Unset, datetime.datetime]):
        references_updated_dt_gte (Union[Unset, datetime.datetime]):
        references_updated_dt_lt (Union[Unset, datetime.datetime]):
        references_updated_dt_lte (Union[Unset, datetime.datetime]):
        references_url (Union[Unset, str]):
        references_uuid (Union[Unset, UUID]):
        reported_dt (Union[Unset, datetime.datetime]):
        reported_dt_date (Union[Unset, datetime.date]):
        reported_dt_date_gte (Union[Unset, datetime.date]):
        reported_dt_date_lte (Union[Unset, datetime.date]):
        reported_dt_gt (Union[Unset, datetime.datetime]):
        reported_dt_gte (Union[Unset, datetime.datetime]):
        reported_dt_lt (Union[Unset, datetime.datetime]):
        reported_dt_lte (Union[Unset, datetime.datetime]):
        requires_cve_description (Union[Unset, OsidbApiV1FlawsListRequiresCveDescription]):
        search (Union[Unset, str]):
        source (Union[Unset, OsidbApiV1FlawsListSource]):
        statement (Union[Unset, str]):
        statement_isempty (Union[Unset, bool]):
        team_id (Union[Unset, str]):
        title (Union[Unset, str]):
        tracker_ids (Union[Unset, list[str]]):
        unembargo_dt (Union[Unset, datetime.datetime]):
        updated_dt (Union[Unset, datetime.datetime]):
        updated_dt_date (Union[Unset, datetime.date]):
        updated_dt_date_gte (Union[Unset, datetime.date]):
        updated_dt_date_lte (Union[Unset, datetime.date]):
        updated_dt_gt (Union[Unset, datetime.datetime]):
        updated_dt_gte (Union[Unset, datetime.datetime]):
        updated_dt_lt (Union[Unset, datetime.datetime]):
        updated_dt_lte (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, UUID]):
        workflow_state (Union[Unset, list[OsidbApiV1FlawsListWorkflowStateItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV1FlawsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            acknowledgments_affiliation=acknowledgments_affiliation,
            acknowledgments_created_dt=acknowledgments_created_dt,
            acknowledgments_created_dt_date=acknowledgments_created_dt_date,
            acknowledgments_created_dt_date_gte=acknowledgments_created_dt_date_gte,
            acknowledgments_created_dt_date_lte=acknowledgments_created_dt_date_lte,
            acknowledgments_created_dt_gt=acknowledgments_created_dt_gt,
            acknowledgments_created_dt_gte=acknowledgments_created_dt_gte,
            acknowledgments_created_dt_lt=acknowledgments_created_dt_lt,
            acknowledgments_created_dt_lte=acknowledgments_created_dt_lte,
            acknowledgments_from_upstream=acknowledgments_from_upstream,
            acknowledgments_name=acknowledgments_name,
            acknowledgments_updated_dt=acknowledgments_updated_dt,
            acknowledgments_updated_dt_date=acknowledgments_updated_dt_date,
            acknowledgments_updated_dt_date_gte=acknowledgments_updated_dt_date_gte,
            acknowledgments_updated_dt_date_lte=acknowledgments_updated_dt_date_lte,
            acknowledgments_updated_dt_gt=acknowledgments_updated_dt_gt,
            acknowledgments_updated_dt_gte=acknowledgments_updated_dt_gte,
            acknowledgments_updated_dt_lt=acknowledgments_updated_dt_lt,
            acknowledgments_updated_dt_lte=acknowledgments_updated_dt_lte,
            acknowledgments_uuid=acknowledgments_uuid,
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
            affects_impact=affects_impact,
            affects_ps_component=affects_ps_component,
            affects_ps_module=affects_ps_module,
            affects_resolution=affects_resolution,
            affects_trackers_created_dt=affects_trackers_created_dt,
            affects_trackers_created_dt_date=affects_trackers_created_dt_date,
            affects_trackers_created_dt_date_gte=affects_trackers_created_dt_date_gte,
            affects_trackers_created_dt_date_lte=affects_trackers_created_dt_date_lte,
            affects_trackers_created_dt_gt=affects_trackers_created_dt_gt,
            affects_trackers_created_dt_gte=affects_trackers_created_dt_gte,
            affects_trackers_created_dt_lt=affects_trackers_created_dt_lt,
            affects_trackers_created_dt_lte=affects_trackers_created_dt_lte,
            affects_trackers_embargoed=affects_trackers_embargoed,
            affects_trackers_errata_advisory_name=affects_trackers_errata_advisory_name,
            affects_trackers_errata_et_id=affects_trackers_errata_et_id,
            affects_trackers_errata_shipped_dt=affects_trackers_errata_shipped_dt,
            affects_trackers_errata_shipped_dt_date=affects_trackers_errata_shipped_dt_date,
            affects_trackers_errata_shipped_dt_date_gte=affects_trackers_errata_shipped_dt_date_gte,
            affects_trackers_errata_shipped_dt_date_lte=affects_trackers_errata_shipped_dt_date_lte,
            affects_trackers_errata_shipped_dt_gt=affects_trackers_errata_shipped_dt_gt,
            affects_trackers_errata_shipped_dt_gte=affects_trackers_errata_shipped_dt_gte,
            affects_trackers_errata_shipped_dt_lt=affects_trackers_errata_shipped_dt_lt,
            affects_trackers_errata_shipped_dt_lte=affects_trackers_errata_shipped_dt_lte,
            affects_trackers_external_system_id=affects_trackers_external_system_id,
            affects_trackers_ps_update_stream=affects_trackers_ps_update_stream,
            affects_trackers_resolution=affects_trackers_resolution,
            affects_trackers_status=affects_trackers_status,
            affects_trackers_type=affects_trackers_type,
            affects_trackers_updated_dt=affects_trackers_updated_dt,
            affects_trackers_updated_dt_date=affects_trackers_updated_dt_date,
            affects_trackers_updated_dt_date_gte=affects_trackers_updated_dt_date_gte,
            affects_trackers_updated_dt_date_lte=affects_trackers_updated_dt_date_lte,
            affects_trackers_updated_dt_gt=affects_trackers_updated_dt_gt,
            affects_trackers_updated_dt_gte=affects_trackers_updated_dt_gte,
            affects_trackers_updated_dt_lt=affects_trackers_updated_dt_lt,
            affects_trackers_updated_dt_lte=affects_trackers_updated_dt_lte,
            affects_trackers_uuid=affects_trackers_uuid,
            affects_updated_dt=affects_updated_dt,
            affects_updated_dt_date=affects_updated_dt_date,
            affects_updated_dt_date_gte=affects_updated_dt_date_gte,
            affects_updated_dt_date_lte=affects_updated_dt_date_lte,
            affects_updated_dt_gt=affects_updated_dt_gt,
            affects_updated_dt_gte=affects_updated_dt_gte,
            affects_updated_dt_lt=affects_updated_dt_lt,
            affects_updated_dt_lte=affects_updated_dt_lte,
            affects_uuid=affects_uuid,
            bz_id=bz_id,
            changed_after=changed_after,
            changed_before=changed_before,
            comment_zero=comment_zero,
            components=components,
            created_dt=created_dt,
            created_dt_date=created_dt_date,
            created_dt_date_gte=created_dt_date_gte,
            created_dt_date_lte=created_dt_date_lte,
            created_dt_gt=created_dt_gt,
            created_dt_gte=created_dt_gte,
            created_dt_lt=created_dt_lt,
            created_dt_lte=created_dt_lte,
            cve_description=cve_description,
            cve_description_isempty=cve_description_isempty,
            cve_id=cve_id,
            cve_id_isempty=cve_id_isempty,
            cvss2_nist_isempty=cvss2_nist_isempty,
            cvss2_rh_isempty=cvss2_rh_isempty,
            cvss3_nist_isempty=cvss3_nist_isempty,
            cvss3_rh_isempty=cvss3_rh_isempty,
            cvss4_nist_isempty=cvss4_nist_isempty,
            cvss4_rh_isempty=cvss4_rh_isempty,
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
            cwe_id=cwe_id,
            cwe_id_isempty=cwe_id_isempty,
            embargoed=embargoed,
            exclude_fields=exclude_fields,
            impact=impact,
            include_fields=include_fields,
            include_meta_attr=include_meta_attr,
            limit=limit,
            major_incident_start_dt=major_incident_start_dt,
            major_incident_start_dt_date=major_incident_start_dt_date,
            major_incident_start_dt_date_gte=major_incident_start_dt_date_gte,
            major_incident_start_dt_date_lte=major_incident_start_dt_date_lte,
            major_incident_start_dt_gt=major_incident_start_dt_gt,
            major_incident_start_dt_gte=major_incident_start_dt_gte,
            major_incident_start_dt_lt=major_incident_start_dt_lt,
            major_incident_start_dt_lte=major_incident_start_dt_lte,
            major_incident_state=major_incident_state,
            mitigation_isempty=mitigation_isempty,
            nist_cvss_validation=nist_cvss_validation,
            offset=offset,
            order=order,
            owner=owner,
            owner_isempty=owner_isempty,
            query=query,
            references_created_dt=references_created_dt,
            references_created_dt_date=references_created_dt_date,
            references_created_dt_date_gte=references_created_dt_date_gte,
            references_created_dt_date_lte=references_created_dt_date_lte,
            references_created_dt_gt=references_created_dt_gt,
            references_created_dt_gte=references_created_dt_gte,
            references_created_dt_lt=references_created_dt_lt,
            references_created_dt_lte=references_created_dt_lte,
            references_description=references_description,
            references_type=references_type,
            references_updated_dt=references_updated_dt,
            references_updated_dt_date=references_updated_dt_date,
            references_updated_dt_date_gte=references_updated_dt_date_gte,
            references_updated_dt_date_lte=references_updated_dt_date_lte,
            references_updated_dt_gt=references_updated_dt_gt,
            references_updated_dt_gte=references_updated_dt_gte,
            references_updated_dt_lt=references_updated_dt_lt,
            references_updated_dt_lte=references_updated_dt_lte,
            references_url=references_url,
            references_uuid=references_uuid,
            reported_dt=reported_dt,
            reported_dt_date=reported_dt_date,
            reported_dt_date_gte=reported_dt_date_gte,
            reported_dt_date_lte=reported_dt_date_lte,
            reported_dt_gt=reported_dt_gt,
            reported_dt_gte=reported_dt_gte,
            reported_dt_lt=reported_dt_lt,
            reported_dt_lte=reported_dt_lte,
            requires_cve_description=requires_cve_description,
            search=search,
            source=source,
            statement=statement,
            statement_isempty=statement_isempty,
            team_id=team_id,
            title=title,
            tracker_ids=tracker_ids,
            unembargo_dt=unembargo_dt,
            updated_dt=updated_dt,
            updated_dt_date=updated_dt_date,
            updated_dt_date_gte=updated_dt_date_gte,
            updated_dt_date_lte=updated_dt_date_lte,
            updated_dt_gt=updated_dt_gt,
            updated_dt_gte=updated_dt_gte,
            updated_dt_lt=updated_dt_lt,
            updated_dt_lte=updated_dt_lte,
            uuid=uuid,
            workflow_state=workflow_state,
        )
    ).parsed
