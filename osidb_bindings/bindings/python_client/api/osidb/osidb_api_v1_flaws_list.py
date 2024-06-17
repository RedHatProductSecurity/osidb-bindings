import datetime
from typing import Any, Dict, List, Optional, Union

import requests

from ...client import AuthenticatedClient
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
    "acknowledgments__uuid": str,
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
    "affects__trackers__uuid": str,
    "affects__updated_dt": datetime.datetime,
    "affects__updated_dt__date": datetime.date,
    "affects__updated_dt__date__gte": datetime.date,
    "affects__updated_dt__date__lte": datetime.date,
    "affects__updated_dt__gt": datetime.datetime,
    "affects__updated_dt__gte": datetime.datetime,
    "affects__updated_dt__lt": datetime.datetime,
    "affects__updated_dt__lte": datetime.datetime,
    "affects__uuid": str,
    "bz_id": float,
    "changed_after": datetime.datetime,
    "changed_before": datetime.datetime,
    "comment_zero": str,
    "components": List[str],
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
    "cve_id": List[str],
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
    "cvss_scores__uuid": str,
    "cvss_scores__vector": str,
    "cwe_id": str,
    "cwe_id__isempty": bool,
    "embargoed": bool,
    "exclude_fields": List[str],
    "impact": OsidbApiV1FlawsListImpact,
    "include_fields": List[str],
    "include_meta_attr": List[str],
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
    "order": List[OsidbApiV1FlawsListOrderItem],
    "owner": str,
    "owner__isempty": bool,
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
    "references__uuid": str,
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
    "tracker_ids": List[str],
    "unembargo_dt": datetime.datetime,
    "updated_dt": datetime.datetime,
    "updated_dt__date": datetime.date,
    "updated_dt__date__gte": datetime.date,
    "updated_dt__date__lte": datetime.date,
    "updated_dt__gt": datetime.datetime,
    "updated_dt__gte": datetime.datetime,
    "updated_dt__lt": datetime.datetime,
    "updated_dt__lte": datetime.datetime,
    "uuid": str,
    "workflow_state": List[OsidbApiV1FlawsListWorkflowStateItem],
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    acknowledgments_affiliation: Union[Unset, None, str] = UNSET,
    acknowledgments_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_from_upstream: Union[Unset, None, bool] = UNSET,
    acknowledgments_name: Union[Unset, None, str] = UNSET,
    acknowledgments_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, None, str] = UNSET,
    affects_affectedness: Union[
        Unset, None, OsidbApiV1FlawsListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, None, bool] = UNSET,
    affects_impact: Union[Unset, None, OsidbApiV1FlawsListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, None, str] = UNSET,
    affects_ps_module: Union[Unset, None, str] = UNSET,
    affects_resolution: Union[
        Unset, None, OsidbApiV1FlawsListAffectsResolution
    ] = UNSET,
    affects_trackers_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_embargoed: Union[Unset, None, bool] = UNSET,
    affects_trackers_errata_advisory_name: Union[Unset, None, str] = UNSET,
    affects_trackers_errata_et_id: Union[Unset, None, int] = UNSET,
    affects_trackers_errata_shipped_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_gte: Union[
        Unset, None, datetime.date
    ] = UNSET,
    affects_trackers_errata_shipped_dt_date_lte: Union[
        Unset, None, datetime.date
    ] = UNSET,
    affects_trackers_errata_shipped_dt_gt: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_gte: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_lt: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_lte: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_external_system_id: Union[Unset, None, str] = UNSET,
    affects_trackers_ps_update_stream: Union[Unset, None, str] = UNSET,
    affects_trackers_resolution: Union[Unset, None, str] = UNSET,
    affects_trackers_status: Union[Unset, None, str] = UNSET,
    affects_trackers_type: Union[
        Unset, None, OsidbApiV1FlawsListAffectsTrackersType
    ] = UNSET,
    affects_trackers_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_uuid: Union[Unset, None, str] = UNSET,
    affects_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, None, str] = UNSET,
    bz_id: Union[Unset, None, float] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, None, str] = UNSET,
    components: Union[Unset, None, List[str]] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cve_description: Union[Unset, None, str] = UNSET,
    cve_description_isempty: Union[Unset, None, bool] = UNSET,
    cve_id: Union[Unset, None, List[str]] = UNSET,
    cve_id_isempty: Union[Unset, None, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, None, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, None, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, None, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, None, OsidbApiV1FlawsListCvssScoresIssuer] = UNSET,
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
    cwe_id: Union[Unset, None, str] = UNSET,
    cwe_id_isempty: Union[Unset, None, bool] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    impact: Union[Unset, None, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    major_incident_start_dt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_date: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_state: Union[
        Unset, None, OsidbApiV1FlawsListMajorIncidentState
    ] = UNSET,
    mitigation_isempty: Union[Unset, None, bool] = UNSET,
    nist_cvss_validation: Union[
        Unset, None, OsidbApiV1FlawsListNistCvssValidation
    ] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    owner_isempty: Union[Unset, None, bool] = UNSET,
    references_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    references_description: Union[Unset, None, str] = UNSET,
    references_type: Union[Unset, None, OsidbApiV1FlawsListReferencesType] = UNSET,
    references_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    references_url: Union[Unset, None, str] = UNSET,
    references_uuid: Union[Unset, None, str] = UNSET,
    reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, None, OsidbApiV1FlawsListRequiresCveDescription
    ] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, OsidbApiV1FlawsListSource] = UNSET,
    statement: Union[Unset, None, str] = UNSET,
    statement_isempty: Union[Unset, None, bool] = UNSET,
    team_id: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
    unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
    workflow_state: Union[
        Unset, None, List[OsidbApiV1FlawsListWorkflowStateItem]
    ] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_acknowledgments_created_dt: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_created_dt, Unset):
        json_acknowledgments_created_dt = (
            acknowledgments_created_dt.isoformat()
            if acknowledgments_created_dt
            else None
        )

    json_acknowledgments_created_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_created_dt_date, Unset):
        json_acknowledgments_created_dt_date = (
            acknowledgments_created_dt_date.isoformat()
            if acknowledgments_created_dt_date
            else None
        )

    json_acknowledgments_created_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_created_dt_date_gte, Unset):
        json_acknowledgments_created_dt_date_gte = (
            acknowledgments_created_dt_date_gte.isoformat()
            if acknowledgments_created_dt_date_gte
            else None
        )

    json_acknowledgments_created_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_created_dt_date_lte, Unset):
        json_acknowledgments_created_dt_date_lte = (
            acknowledgments_created_dt_date_lte.isoformat()
            if acknowledgments_created_dt_date_lte
            else None
        )

    json_acknowledgments_created_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_created_dt_gt, Unset):
        json_acknowledgments_created_dt_gt = (
            acknowledgments_created_dt_gt.isoformat()
            if acknowledgments_created_dt_gt
            else None
        )

    json_acknowledgments_created_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_created_dt_gte, Unset):
        json_acknowledgments_created_dt_gte = (
            acknowledgments_created_dt_gte.isoformat()
            if acknowledgments_created_dt_gte
            else None
        )

    json_acknowledgments_created_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_created_dt_lt, Unset):
        json_acknowledgments_created_dt_lt = (
            acknowledgments_created_dt_lt.isoformat()
            if acknowledgments_created_dt_lt
            else None
        )

    json_acknowledgments_created_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_created_dt_lte, Unset):
        json_acknowledgments_created_dt_lte = (
            acknowledgments_created_dt_lte.isoformat()
            if acknowledgments_created_dt_lte
            else None
        )

    json_acknowledgments_updated_dt: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_updated_dt, Unset):
        json_acknowledgments_updated_dt = (
            acknowledgments_updated_dt.isoformat()
            if acknowledgments_updated_dt
            else None
        )

    json_acknowledgments_updated_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_date, Unset):
        json_acknowledgments_updated_dt_date = (
            acknowledgments_updated_dt_date.isoformat()
            if acknowledgments_updated_dt_date
            else None
        )

    json_acknowledgments_updated_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_date_gte, Unset):
        json_acknowledgments_updated_dt_date_gte = (
            acknowledgments_updated_dt_date_gte.isoformat()
            if acknowledgments_updated_dt_date_gte
            else None
        )

    json_acknowledgments_updated_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_date_lte, Unset):
        json_acknowledgments_updated_dt_date_lte = (
            acknowledgments_updated_dt_date_lte.isoformat()
            if acknowledgments_updated_dt_date_lte
            else None
        )

    json_acknowledgments_updated_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_gt, Unset):
        json_acknowledgments_updated_dt_gt = (
            acknowledgments_updated_dt_gt.isoformat()
            if acknowledgments_updated_dt_gt
            else None
        )

    json_acknowledgments_updated_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_gte, Unset):
        json_acknowledgments_updated_dt_gte = (
            acknowledgments_updated_dt_gte.isoformat()
            if acknowledgments_updated_dt_gte
            else None
        )

    json_acknowledgments_updated_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_lt, Unset):
        json_acknowledgments_updated_dt_lt = (
            acknowledgments_updated_dt_lt.isoformat()
            if acknowledgments_updated_dt_lt
            else None
        )

    json_acknowledgments_updated_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(acknowledgments_updated_dt_lte, Unset):
        json_acknowledgments_updated_dt_lte = (
            acknowledgments_updated_dt_lte.isoformat()
            if acknowledgments_updated_dt_lte
            else None
        )

    json_affects_affectedness: Union[Unset, None, str] = UNSET
    if not isinstance(affects_affectedness, Unset):

        json_affects_affectedness = (
            OsidbApiV1FlawsListAffectsAffectedness(affects_affectedness).value
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

    json_affects_impact: Union[Unset, None, str] = UNSET
    if not isinstance(affects_impact, Unset):

        json_affects_impact = (
            OsidbApiV1FlawsListAffectsImpact(affects_impact).value
            if affects_impact
            else None
        )

    json_affects_resolution: Union[Unset, None, str] = UNSET
    if not isinstance(affects_resolution, Unset):

        json_affects_resolution = (
            OsidbApiV1FlawsListAffectsResolution(affects_resolution).value
            if affects_resolution
            else None
        )

    json_affects_trackers_created_dt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_created_dt, Unset):
        json_affects_trackers_created_dt = (
            affects_trackers_created_dt.isoformat()
            if affects_trackers_created_dt
            else None
        )

    json_affects_trackers_created_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_created_dt_date, Unset):
        json_affects_trackers_created_dt_date = (
            affects_trackers_created_dt_date.isoformat()
            if affects_trackers_created_dt_date
            else None
        )

    json_affects_trackers_created_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_created_dt_date_gte, Unset):
        json_affects_trackers_created_dt_date_gte = (
            affects_trackers_created_dt_date_gte.isoformat()
            if affects_trackers_created_dt_date_gte
            else None
        )

    json_affects_trackers_created_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_created_dt_date_lte, Unset):
        json_affects_trackers_created_dt_date_lte = (
            affects_trackers_created_dt_date_lte.isoformat()
            if affects_trackers_created_dt_date_lte
            else None
        )

    json_affects_trackers_created_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_created_dt_gt, Unset):
        json_affects_trackers_created_dt_gt = (
            affects_trackers_created_dt_gt.isoformat()
            if affects_trackers_created_dt_gt
            else None
        )

    json_affects_trackers_created_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_created_dt_gte, Unset):
        json_affects_trackers_created_dt_gte = (
            affects_trackers_created_dt_gte.isoformat()
            if affects_trackers_created_dt_gte
            else None
        )

    json_affects_trackers_created_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_created_dt_lt, Unset):
        json_affects_trackers_created_dt_lt = (
            affects_trackers_created_dt_lt.isoformat()
            if affects_trackers_created_dt_lt
            else None
        )

    json_affects_trackers_created_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_created_dt_lte, Unset):
        json_affects_trackers_created_dt_lte = (
            affects_trackers_created_dt_lte.isoformat()
            if affects_trackers_created_dt_lte
            else None
        )

    json_affects_trackers_errata_shipped_dt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt, Unset):
        json_affects_trackers_errata_shipped_dt = (
            affects_trackers_errata_shipped_dt.isoformat()
            if affects_trackers_errata_shipped_dt
            else None
        )

    json_affects_trackers_errata_shipped_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_date, Unset):
        json_affects_trackers_errata_shipped_dt_date = (
            affects_trackers_errata_shipped_dt_date.isoformat()
            if affects_trackers_errata_shipped_dt_date
            else None
        )

    json_affects_trackers_errata_shipped_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_date_gte, Unset):
        json_affects_trackers_errata_shipped_dt_date_gte = (
            affects_trackers_errata_shipped_dt_date_gte.isoformat()
            if affects_trackers_errata_shipped_dt_date_gte
            else None
        )

    json_affects_trackers_errata_shipped_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_date_lte, Unset):
        json_affects_trackers_errata_shipped_dt_date_lte = (
            affects_trackers_errata_shipped_dt_date_lte.isoformat()
            if affects_trackers_errata_shipped_dt_date_lte
            else None
        )

    json_affects_trackers_errata_shipped_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_gt, Unset):
        json_affects_trackers_errata_shipped_dt_gt = (
            affects_trackers_errata_shipped_dt_gt.isoformat()
            if affects_trackers_errata_shipped_dt_gt
            else None
        )

    json_affects_trackers_errata_shipped_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_gte, Unset):
        json_affects_trackers_errata_shipped_dt_gte = (
            affects_trackers_errata_shipped_dt_gte.isoformat()
            if affects_trackers_errata_shipped_dt_gte
            else None
        )

    json_affects_trackers_errata_shipped_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_lt, Unset):
        json_affects_trackers_errata_shipped_dt_lt = (
            affects_trackers_errata_shipped_dt_lt.isoformat()
            if affects_trackers_errata_shipped_dt_lt
            else None
        )

    json_affects_trackers_errata_shipped_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_errata_shipped_dt_lte, Unset):
        json_affects_trackers_errata_shipped_dt_lte = (
            affects_trackers_errata_shipped_dt_lte.isoformat()
            if affects_trackers_errata_shipped_dt_lte
            else None
        )

    json_affects_trackers_type: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_type, Unset):

        json_affects_trackers_type = (
            OsidbApiV1FlawsListAffectsTrackersType(affects_trackers_type).value
            if affects_trackers_type
            else None
        )

    json_affects_trackers_updated_dt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_updated_dt, Unset):
        json_affects_trackers_updated_dt = (
            affects_trackers_updated_dt.isoformat()
            if affects_trackers_updated_dt
            else None
        )

    json_affects_trackers_updated_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_date, Unset):
        json_affects_trackers_updated_dt_date = (
            affects_trackers_updated_dt_date.isoformat()
            if affects_trackers_updated_dt_date
            else None
        )

    json_affects_trackers_updated_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_date_gte, Unset):
        json_affects_trackers_updated_dt_date_gte = (
            affects_trackers_updated_dt_date_gte.isoformat()
            if affects_trackers_updated_dt_date_gte
            else None
        )

    json_affects_trackers_updated_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_date_lte, Unset):
        json_affects_trackers_updated_dt_date_lte = (
            affects_trackers_updated_dt_date_lte.isoformat()
            if affects_trackers_updated_dt_date_lte
            else None
        )

    json_affects_trackers_updated_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_gt, Unset):
        json_affects_trackers_updated_dt_gt = (
            affects_trackers_updated_dt_gt.isoformat()
            if affects_trackers_updated_dt_gt
            else None
        )

    json_affects_trackers_updated_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_gte, Unset):
        json_affects_trackers_updated_dt_gte = (
            affects_trackers_updated_dt_gte.isoformat()
            if affects_trackers_updated_dt_gte
            else None
        )

    json_affects_trackers_updated_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_lt, Unset):
        json_affects_trackers_updated_dt_lt = (
            affects_trackers_updated_dt_lt.isoformat()
            if affects_trackers_updated_dt_lt
            else None
        )

    json_affects_trackers_updated_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(affects_trackers_updated_dt_lte, Unset):
        json_affects_trackers_updated_dt_lte = (
            affects_trackers_updated_dt_lte.isoformat()
            if affects_trackers_updated_dt_lte
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

    json_changed_after: Union[Unset, None, str] = UNSET
    if not isinstance(changed_after, Unset):
        json_changed_after = changed_after.isoformat() if changed_after else None

    json_changed_before: Union[Unset, None, str] = UNSET
    if not isinstance(changed_before, Unset):
        json_changed_before = changed_before.isoformat() if changed_before else None

    json_components: Union[Unset, None, List[str]] = UNSET
    if not isinstance(components, Unset):
        if components is None:
            json_components = None
        else:
            json_components = components

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

    json_cve_id: Union[Unset, None, List[str]] = UNSET
    if not isinstance(cve_id, Unset):
        if cve_id is None:
            json_cve_id = None
        else:
            json_cve_id = cve_id

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
            OsidbApiV1FlawsListCvssScoresIssuer(cvss_scores_issuer).value
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

    json_impact: Union[Unset, None, str] = UNSET
    if not isinstance(impact, Unset):

        json_impact = OsidbApiV1FlawsListImpact(impact).value if impact else None

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

    json_major_incident_start_dt: Union[Unset, None, str] = UNSET
    if not isinstance(major_incident_start_dt, Unset):
        json_major_incident_start_dt = (
            major_incident_start_dt.isoformat() if major_incident_start_dt else None
        )

    json_major_incident_start_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(major_incident_start_dt_date, Unset):
        json_major_incident_start_dt_date = (
            major_incident_start_dt_date.isoformat()
            if major_incident_start_dt_date
            else None
        )

    json_major_incident_start_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(major_incident_start_dt_date_gte, Unset):
        json_major_incident_start_dt_date_gte = (
            major_incident_start_dt_date_gte.isoformat()
            if major_incident_start_dt_date_gte
            else None
        )

    json_major_incident_start_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(major_incident_start_dt_date_lte, Unset):
        json_major_incident_start_dt_date_lte = (
            major_incident_start_dt_date_lte.isoformat()
            if major_incident_start_dt_date_lte
            else None
        )

    json_major_incident_start_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(major_incident_start_dt_gt, Unset):
        json_major_incident_start_dt_gt = (
            major_incident_start_dt_gt.isoformat()
            if major_incident_start_dt_gt
            else None
        )

    json_major_incident_start_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(major_incident_start_dt_gte, Unset):
        json_major_incident_start_dt_gte = (
            major_incident_start_dt_gte.isoformat()
            if major_incident_start_dt_gte
            else None
        )

    json_major_incident_start_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(major_incident_start_dt_lt, Unset):
        json_major_incident_start_dt_lt = (
            major_incident_start_dt_lt.isoformat()
            if major_incident_start_dt_lt
            else None
        )

    json_major_incident_start_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(major_incident_start_dt_lte, Unset):
        json_major_incident_start_dt_lte = (
            major_incident_start_dt_lte.isoformat()
            if major_incident_start_dt_lte
            else None
        )

    json_major_incident_state: Union[Unset, None, str] = UNSET
    if not isinstance(major_incident_state, Unset):

        json_major_incident_state = (
            OsidbApiV1FlawsListMajorIncidentState(major_incident_state).value
            if major_incident_state
            else None
        )

    json_nist_cvss_validation: Union[Unset, None, str] = UNSET
    if not isinstance(nist_cvss_validation, Unset):

        json_nist_cvss_validation = (
            OsidbApiV1FlawsListNistCvssValidation(nist_cvss_validation).value
            if nist_cvss_validation
            else None
        )

    json_order: Union[Unset, None, List[str]] = UNSET
    if not isinstance(order, Unset):
        if order is None:
            json_order = None
        else:
            json_order = []
            for order_item_data in order:
                order_item: str = UNSET
                if not isinstance(order_item_data, Unset):

                    order_item = OsidbApiV1FlawsListOrderItem(order_item_data).value

                json_order.append(order_item)

    json_references_created_dt: Union[Unset, None, str] = UNSET
    if not isinstance(references_created_dt, Unset):
        json_references_created_dt = (
            references_created_dt.isoformat() if references_created_dt else None
        )

    json_references_created_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(references_created_dt_date, Unset):
        json_references_created_dt_date = (
            references_created_dt_date.isoformat()
            if references_created_dt_date
            else None
        )

    json_references_created_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(references_created_dt_date_gte, Unset):
        json_references_created_dt_date_gte = (
            references_created_dt_date_gte.isoformat()
            if references_created_dt_date_gte
            else None
        )

    json_references_created_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(references_created_dt_date_lte, Unset):
        json_references_created_dt_date_lte = (
            references_created_dt_date_lte.isoformat()
            if references_created_dt_date_lte
            else None
        )

    json_references_created_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(references_created_dt_gt, Unset):
        json_references_created_dt_gt = (
            references_created_dt_gt.isoformat() if references_created_dt_gt else None
        )

    json_references_created_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(references_created_dt_gte, Unset):
        json_references_created_dt_gte = (
            references_created_dt_gte.isoformat() if references_created_dt_gte else None
        )

    json_references_created_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(references_created_dt_lt, Unset):
        json_references_created_dt_lt = (
            references_created_dt_lt.isoformat() if references_created_dt_lt else None
        )

    json_references_created_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(references_created_dt_lte, Unset):
        json_references_created_dt_lte = (
            references_created_dt_lte.isoformat() if references_created_dt_lte else None
        )

    json_references_type: Union[Unset, None, str] = UNSET
    if not isinstance(references_type, Unset):

        json_references_type = (
            OsidbApiV1FlawsListReferencesType(references_type).value
            if references_type
            else None
        )

    json_references_updated_dt: Union[Unset, None, str] = UNSET
    if not isinstance(references_updated_dt, Unset):
        json_references_updated_dt = (
            references_updated_dt.isoformat() if references_updated_dt else None
        )

    json_references_updated_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(references_updated_dt_date, Unset):
        json_references_updated_dt_date = (
            references_updated_dt_date.isoformat()
            if references_updated_dt_date
            else None
        )

    json_references_updated_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(references_updated_dt_date_gte, Unset):
        json_references_updated_dt_date_gte = (
            references_updated_dt_date_gte.isoformat()
            if references_updated_dt_date_gte
            else None
        )

    json_references_updated_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(references_updated_dt_date_lte, Unset):
        json_references_updated_dt_date_lte = (
            references_updated_dt_date_lte.isoformat()
            if references_updated_dt_date_lte
            else None
        )

    json_references_updated_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(references_updated_dt_gt, Unset):
        json_references_updated_dt_gt = (
            references_updated_dt_gt.isoformat() if references_updated_dt_gt else None
        )

    json_references_updated_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(references_updated_dt_gte, Unset):
        json_references_updated_dt_gte = (
            references_updated_dt_gte.isoformat() if references_updated_dt_gte else None
        )

    json_references_updated_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(references_updated_dt_lt, Unset):
        json_references_updated_dt_lt = (
            references_updated_dt_lt.isoformat() if references_updated_dt_lt else None
        )

    json_references_updated_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(references_updated_dt_lte, Unset):
        json_references_updated_dt_lte = (
            references_updated_dt_lte.isoformat() if references_updated_dt_lte else None
        )

    json_reported_dt: Union[Unset, None, str] = UNSET
    if not isinstance(reported_dt, Unset):
        json_reported_dt = reported_dt.isoformat() if reported_dt else None

    json_reported_dt_date: Union[Unset, None, str] = UNSET
    if not isinstance(reported_dt_date, Unset):
        json_reported_dt_date = (
            reported_dt_date.isoformat() if reported_dt_date else None
        )

    json_reported_dt_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(reported_dt_date_gte, Unset):
        json_reported_dt_date_gte = (
            reported_dt_date_gte.isoformat() if reported_dt_date_gte else None
        )

    json_reported_dt_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(reported_dt_date_lte, Unset):
        json_reported_dt_date_lte = (
            reported_dt_date_lte.isoformat() if reported_dt_date_lte else None
        )

    json_reported_dt_gt: Union[Unset, None, str] = UNSET
    if not isinstance(reported_dt_gt, Unset):
        json_reported_dt_gt = reported_dt_gt.isoformat() if reported_dt_gt else None

    json_reported_dt_gte: Union[Unset, None, str] = UNSET
    if not isinstance(reported_dt_gte, Unset):
        json_reported_dt_gte = reported_dt_gte.isoformat() if reported_dt_gte else None

    json_reported_dt_lt: Union[Unset, None, str] = UNSET
    if not isinstance(reported_dt_lt, Unset):
        json_reported_dt_lt = reported_dt_lt.isoformat() if reported_dt_lt else None

    json_reported_dt_lte: Union[Unset, None, str] = UNSET
    if not isinstance(reported_dt_lte, Unset):
        json_reported_dt_lte = reported_dt_lte.isoformat() if reported_dt_lte else None

    json_requires_cve_description: Union[Unset, None, str] = UNSET
    if not isinstance(requires_cve_description, Unset):

        json_requires_cve_description = (
            OsidbApiV1FlawsListRequiresCveDescription(requires_cve_description).value
            if requires_cve_description
            else None
        )

    json_source: Union[Unset, None, str] = UNSET
    if not isinstance(source, Unset):

        json_source = OsidbApiV1FlawsListSource(source).value if source else None

    json_tracker_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tracker_ids, Unset):
        if tracker_ids is None:
            json_tracker_ids = None
        else:
            json_tracker_ids = tracker_ids

    json_unembargo_dt: Union[Unset, None, str] = UNSET
    if not isinstance(unembargo_dt, Unset):
        json_unembargo_dt = unembargo_dt.isoformat() if unembargo_dt else None

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

    json_workflow_state: Union[Unset, None, List[str]] = UNSET
    if not isinstance(workflow_state, Unset):
        if workflow_state is None:
            json_workflow_state = None
        else:
            json_workflow_state = []
            for workflow_state_item_data in workflow_state:
                workflow_state_item: str = UNSET
                if not isinstance(workflow_state_item_data, Unset):

                    workflow_state_item = OsidbApiV1FlawsListWorkflowStateItem(
                        workflow_state_item_data
                    ).value

                json_workflow_state.append(workflow_state_item)

    params: Dict[str, Any] = {
        "acknowledgments__affiliation": acknowledgments_affiliation,
        "acknowledgments__created_dt": json_acknowledgments_created_dt,
        "acknowledgments__created_dt__date": json_acknowledgments_created_dt_date,
        "acknowledgments__created_dt__date__gte": json_acknowledgments_created_dt_date_gte,
        "acknowledgments__created_dt__date__lte": json_acknowledgments_created_dt_date_lte,
        "acknowledgments__created_dt__gt": json_acknowledgments_created_dt_gt,
        "acknowledgments__created_dt__gte": json_acknowledgments_created_dt_gte,
        "acknowledgments__created_dt__lt": json_acknowledgments_created_dt_lt,
        "acknowledgments__created_dt__lte": json_acknowledgments_created_dt_lte,
        "acknowledgments__from_upstream": acknowledgments_from_upstream,
        "acknowledgments__name": acknowledgments_name,
        "acknowledgments__updated_dt": json_acknowledgments_updated_dt,
        "acknowledgments__updated_dt__date": json_acknowledgments_updated_dt_date,
        "acknowledgments__updated_dt__date__gte": json_acknowledgments_updated_dt_date_gte,
        "acknowledgments__updated_dt__date__lte": json_acknowledgments_updated_dt_date_lte,
        "acknowledgments__updated_dt__gt": json_acknowledgments_updated_dt_gt,
        "acknowledgments__updated_dt__gte": json_acknowledgments_updated_dt_gte,
        "acknowledgments__updated_dt__lt": json_acknowledgments_updated_dt_lt,
        "acknowledgments__updated_dt__lte": json_acknowledgments_updated_dt_lte,
        "acknowledgments__uuid": acknowledgments_uuid,
        "affects__affectedness": json_affects_affectedness,
        "affects__created_dt": json_affects_created_dt,
        "affects__created_dt__date": json_affects_created_dt_date,
        "affects__created_dt__date__gte": json_affects_created_dt_date_gte,
        "affects__created_dt__date__lte": json_affects_created_dt_date_lte,
        "affects__created_dt__gt": json_affects_created_dt_gt,
        "affects__created_dt__gte": json_affects_created_dt_gte,
        "affects__created_dt__lt": json_affects_created_dt_lt,
        "affects__created_dt__lte": json_affects_created_dt_lte,
        "affects__embargoed": affects_embargoed,
        "affects__impact": json_affects_impact,
        "affects__ps_component": affects_ps_component,
        "affects__ps_module": affects_ps_module,
        "affects__resolution": json_affects_resolution,
        "affects__trackers__created_dt": json_affects_trackers_created_dt,
        "affects__trackers__created_dt__date": json_affects_trackers_created_dt_date,
        "affects__trackers__created_dt__date__gte": json_affects_trackers_created_dt_date_gte,
        "affects__trackers__created_dt__date__lte": json_affects_trackers_created_dt_date_lte,
        "affects__trackers__created_dt__gt": json_affects_trackers_created_dt_gt,
        "affects__trackers__created_dt__gte": json_affects_trackers_created_dt_gte,
        "affects__trackers__created_dt__lt": json_affects_trackers_created_dt_lt,
        "affects__trackers__created_dt__lte": json_affects_trackers_created_dt_lte,
        "affects__trackers__embargoed": affects_trackers_embargoed,
        "affects__trackers__errata__advisory_name": affects_trackers_errata_advisory_name,
        "affects__trackers__errata__et_id": affects_trackers_errata_et_id,
        "affects__trackers__errata__shipped_dt": json_affects_trackers_errata_shipped_dt,
        "affects__trackers__errata__shipped_dt__date": json_affects_trackers_errata_shipped_dt_date,
        "affects__trackers__errata__shipped_dt__date__gte": json_affects_trackers_errata_shipped_dt_date_gte,
        "affects__trackers__errata__shipped_dt__date__lte": json_affects_trackers_errata_shipped_dt_date_lte,
        "affects__trackers__errata__shipped_dt__gt": json_affects_trackers_errata_shipped_dt_gt,
        "affects__trackers__errata__shipped_dt__gte": json_affects_trackers_errata_shipped_dt_gte,
        "affects__trackers__errata__shipped_dt__lt": json_affects_trackers_errata_shipped_dt_lt,
        "affects__trackers__errata__shipped_dt__lte": json_affects_trackers_errata_shipped_dt_lte,
        "affects__trackers__external_system_id": affects_trackers_external_system_id,
        "affects__trackers__ps_update_stream": affects_trackers_ps_update_stream,
        "affects__trackers__resolution": affects_trackers_resolution,
        "affects__trackers__status": affects_trackers_status,
        "affects__trackers__type": json_affects_trackers_type,
        "affects__trackers__updated_dt": json_affects_trackers_updated_dt,
        "affects__trackers__updated_dt__date": json_affects_trackers_updated_dt_date,
        "affects__trackers__updated_dt__date__gte": json_affects_trackers_updated_dt_date_gte,
        "affects__trackers__updated_dt__date__lte": json_affects_trackers_updated_dt_date_lte,
        "affects__trackers__updated_dt__gt": json_affects_trackers_updated_dt_gt,
        "affects__trackers__updated_dt__gte": json_affects_trackers_updated_dt_gte,
        "affects__trackers__updated_dt__lt": json_affects_trackers_updated_dt_lt,
        "affects__trackers__updated_dt__lte": json_affects_trackers_updated_dt_lte,
        "affects__trackers__uuid": affects_trackers_uuid,
        "affects__updated_dt": json_affects_updated_dt,
        "affects__updated_dt__date": json_affects_updated_dt_date,
        "affects__updated_dt__date__gte": json_affects_updated_dt_date_gte,
        "affects__updated_dt__date__lte": json_affects_updated_dt_date_lte,
        "affects__updated_dt__gt": json_affects_updated_dt_gt,
        "affects__updated_dt__gte": json_affects_updated_dt_gte,
        "affects__updated_dt__lt": json_affects_updated_dt_lt,
        "affects__updated_dt__lte": json_affects_updated_dt_lte,
        "affects__uuid": affects_uuid,
        "bz_id": bz_id,
        "changed_after": json_changed_after,
        "changed_before": json_changed_before,
        "comment_zero": comment_zero,
        "components": json_components,
        "created_dt": json_created_dt,
        "created_dt__date": json_created_dt_date,
        "created_dt__date__gte": json_created_dt_date_gte,
        "created_dt__date__lte": json_created_dt_date_lte,
        "created_dt__gt": json_created_dt_gt,
        "created_dt__gte": json_created_dt_gte,
        "created_dt__lt": json_created_dt_lt,
        "created_dt__lte": json_created_dt_lte,
        "cve_description": cve_description,
        "cve_description__isempty": cve_description_isempty,
        "cve_id": json_cve_id,
        "cve_id__isempty": cve_id_isempty,
        "cvss2_nist__isempty": cvss2_nist_isempty,
        "cvss2_rh__isempty": cvss2_rh_isempty,
        "cvss3_nist__isempty": cvss3_nist_isempty,
        "cvss3_rh__isempty": cvss3_rh_isempty,
        "cvss4_nist__isempty": cvss4_nist_isempty,
        "cvss4_rh__isempty": cvss4_rh_isempty,
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
        "cwe_id": cwe_id,
        "cwe_id__isempty": cwe_id_isempty,
        "embargoed": embargoed,
        "exclude_fields": json_exclude_fields,
        "impact": json_impact,
        "include_fields": json_include_fields,
        "include_meta_attr": json_include_meta_attr,
        "limit": limit,
        "major_incident_start_dt": json_major_incident_start_dt,
        "major_incident_start_dt__date": json_major_incident_start_dt_date,
        "major_incident_start_dt__date__gte": json_major_incident_start_dt_date_gte,
        "major_incident_start_dt__date__lte": json_major_incident_start_dt_date_lte,
        "major_incident_start_dt__gt": json_major_incident_start_dt_gt,
        "major_incident_start_dt__gte": json_major_incident_start_dt_gte,
        "major_incident_start_dt__lt": json_major_incident_start_dt_lt,
        "major_incident_start_dt__lte": json_major_incident_start_dt_lte,
        "major_incident_state": json_major_incident_state,
        "mitigation__isempty": mitigation_isempty,
        "nist_cvss_validation": json_nist_cvss_validation,
        "offset": offset,
        "order": json_order,
        "owner": owner,
        "owner__isempty": owner_isempty,
        "references__created_dt": json_references_created_dt,
        "references__created_dt__date": json_references_created_dt_date,
        "references__created_dt__date__gte": json_references_created_dt_date_gte,
        "references__created_dt__date__lte": json_references_created_dt_date_lte,
        "references__created_dt__gt": json_references_created_dt_gt,
        "references__created_dt__gte": json_references_created_dt_gte,
        "references__created_dt__lt": json_references_created_dt_lt,
        "references__created_dt__lte": json_references_created_dt_lte,
        "references__description": references_description,
        "references__type": json_references_type,
        "references__updated_dt": json_references_updated_dt,
        "references__updated_dt__date": json_references_updated_dt_date,
        "references__updated_dt__date__gte": json_references_updated_dt_date_gte,
        "references__updated_dt__date__lte": json_references_updated_dt_date_lte,
        "references__updated_dt__gt": json_references_updated_dt_gt,
        "references__updated_dt__gte": json_references_updated_dt_gte,
        "references__updated_dt__lt": json_references_updated_dt_lt,
        "references__updated_dt__lte": json_references_updated_dt_lte,
        "references__url": references_url,
        "references__uuid": references_uuid,
        "reported_dt": json_reported_dt,
        "reported_dt__date": json_reported_dt_date,
        "reported_dt__date__gte": json_reported_dt_date_gte,
        "reported_dt__date__lte": json_reported_dt_date_lte,
        "reported_dt__gt": json_reported_dt_gt,
        "reported_dt__gte": json_reported_dt_gte,
        "reported_dt__lt": json_reported_dt_lt,
        "reported_dt__lte": json_reported_dt_lte,
        "requires_cve_description": json_requires_cve_description,
        "search": search,
        "source": json_source,
        "statement": statement,
        "statement__isempty": statement_isempty,
        "team_id": team_id,
        "title": title,
        "tracker_ids": json_tracker_ids,
        "unembargo_dt": json_unembargo_dt,
        "updated_dt": json_updated_dt,
        "updated_dt__date": json_updated_dt_date,
        "updated_dt__date__gte": json_updated_dt_date_gte,
        "updated_dt__date__lte": json_updated_dt_date_lte,
        "updated_dt__gt": json_updated_dt_gt,
        "updated_dt__gte": json_updated_dt_gte,
        "updated_dt__lt": json_updated_dt_lt,
        "updated_dt__lte": json_updated_dt_lte,
        "uuid": uuid,
        "workflow_state": json_workflow_state,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1FlawsListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsListResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsListResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    acknowledgments_affiliation: Union[Unset, None, str] = UNSET,
    acknowledgments_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_from_upstream: Union[Unset, None, bool] = UNSET,
    acknowledgments_name: Union[Unset, None, str] = UNSET,
    acknowledgments_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, None, str] = UNSET,
    affects_affectedness: Union[
        Unset, None, OsidbApiV1FlawsListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, None, bool] = UNSET,
    affects_impact: Union[Unset, None, OsidbApiV1FlawsListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, None, str] = UNSET,
    affects_ps_module: Union[Unset, None, str] = UNSET,
    affects_resolution: Union[
        Unset, None, OsidbApiV1FlawsListAffectsResolution
    ] = UNSET,
    affects_trackers_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_embargoed: Union[Unset, None, bool] = UNSET,
    affects_trackers_errata_advisory_name: Union[Unset, None, str] = UNSET,
    affects_trackers_errata_et_id: Union[Unset, None, int] = UNSET,
    affects_trackers_errata_shipped_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_gte: Union[
        Unset, None, datetime.date
    ] = UNSET,
    affects_trackers_errata_shipped_dt_date_lte: Union[
        Unset, None, datetime.date
    ] = UNSET,
    affects_trackers_errata_shipped_dt_gt: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_gte: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_lt: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_lte: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_external_system_id: Union[Unset, None, str] = UNSET,
    affects_trackers_ps_update_stream: Union[Unset, None, str] = UNSET,
    affects_trackers_resolution: Union[Unset, None, str] = UNSET,
    affects_trackers_status: Union[Unset, None, str] = UNSET,
    affects_trackers_type: Union[
        Unset, None, OsidbApiV1FlawsListAffectsTrackersType
    ] = UNSET,
    affects_trackers_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_uuid: Union[Unset, None, str] = UNSET,
    affects_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, None, str] = UNSET,
    bz_id: Union[Unset, None, float] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, None, str] = UNSET,
    components: Union[Unset, None, List[str]] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cve_description: Union[Unset, None, str] = UNSET,
    cve_description_isempty: Union[Unset, None, bool] = UNSET,
    cve_id: Union[Unset, None, List[str]] = UNSET,
    cve_id_isempty: Union[Unset, None, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, None, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, None, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, None, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, None, OsidbApiV1FlawsListCvssScoresIssuer] = UNSET,
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
    cwe_id: Union[Unset, None, str] = UNSET,
    cwe_id_isempty: Union[Unset, None, bool] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    impact: Union[Unset, None, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    major_incident_start_dt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_date: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_state: Union[
        Unset, None, OsidbApiV1FlawsListMajorIncidentState
    ] = UNSET,
    mitigation_isempty: Union[Unset, None, bool] = UNSET,
    nist_cvss_validation: Union[
        Unset, None, OsidbApiV1FlawsListNistCvssValidation
    ] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    owner_isempty: Union[Unset, None, bool] = UNSET,
    references_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    references_description: Union[Unset, None, str] = UNSET,
    references_type: Union[Unset, None, OsidbApiV1FlawsListReferencesType] = UNSET,
    references_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    references_url: Union[Unset, None, str] = UNSET,
    references_uuid: Union[Unset, None, str] = UNSET,
    reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, None, OsidbApiV1FlawsListRequiresCveDescription
    ] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, OsidbApiV1FlawsListSource] = UNSET,
    statement: Union[Unset, None, str] = UNSET,
    statement_isempty: Union[Unset, None, bool] = UNSET,
    team_id: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
    unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
    workflow_state: Union[
        Unset, None, List[OsidbApiV1FlawsListWorkflowStateItem]
    ] = UNSET,
) -> Response[OsidbApiV1FlawsListResponse200]:
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

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    acknowledgments_affiliation: Union[Unset, None, str] = UNSET,
    acknowledgments_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_from_upstream: Union[Unset, None, bool] = UNSET,
    acknowledgments_name: Union[Unset, None, str] = UNSET,
    acknowledgments_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, None, str] = UNSET,
    affects_affectedness: Union[
        Unset, None, OsidbApiV1FlawsListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, None, bool] = UNSET,
    affects_impact: Union[Unset, None, OsidbApiV1FlawsListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, None, str] = UNSET,
    affects_ps_module: Union[Unset, None, str] = UNSET,
    affects_resolution: Union[
        Unset, None, OsidbApiV1FlawsListAffectsResolution
    ] = UNSET,
    affects_trackers_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_embargoed: Union[Unset, None, bool] = UNSET,
    affects_trackers_errata_advisory_name: Union[Unset, None, str] = UNSET,
    affects_trackers_errata_et_id: Union[Unset, None, int] = UNSET,
    affects_trackers_errata_shipped_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_gte: Union[
        Unset, None, datetime.date
    ] = UNSET,
    affects_trackers_errata_shipped_dt_date_lte: Union[
        Unset, None, datetime.date
    ] = UNSET,
    affects_trackers_errata_shipped_dt_gt: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_gte: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_lt: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_lte: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_external_system_id: Union[Unset, None, str] = UNSET,
    affects_trackers_ps_update_stream: Union[Unset, None, str] = UNSET,
    affects_trackers_resolution: Union[Unset, None, str] = UNSET,
    affects_trackers_status: Union[Unset, None, str] = UNSET,
    affects_trackers_type: Union[
        Unset, None, OsidbApiV1FlawsListAffectsTrackersType
    ] = UNSET,
    affects_trackers_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_uuid: Union[Unset, None, str] = UNSET,
    affects_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, None, str] = UNSET,
    bz_id: Union[Unset, None, float] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, None, str] = UNSET,
    components: Union[Unset, None, List[str]] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cve_description: Union[Unset, None, str] = UNSET,
    cve_description_isempty: Union[Unset, None, bool] = UNSET,
    cve_id: Union[Unset, None, List[str]] = UNSET,
    cve_id_isempty: Union[Unset, None, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, None, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, None, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, None, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, None, OsidbApiV1FlawsListCvssScoresIssuer] = UNSET,
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
    cwe_id: Union[Unset, None, str] = UNSET,
    cwe_id_isempty: Union[Unset, None, bool] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    impact: Union[Unset, None, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    major_incident_start_dt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_date: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_state: Union[
        Unset, None, OsidbApiV1FlawsListMajorIncidentState
    ] = UNSET,
    mitigation_isempty: Union[Unset, None, bool] = UNSET,
    nist_cvss_validation: Union[
        Unset, None, OsidbApiV1FlawsListNistCvssValidation
    ] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    owner_isempty: Union[Unset, None, bool] = UNSET,
    references_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    references_description: Union[Unset, None, str] = UNSET,
    references_type: Union[Unset, None, OsidbApiV1FlawsListReferencesType] = UNSET,
    references_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    references_url: Union[Unset, None, str] = UNSET,
    references_uuid: Union[Unset, None, str] = UNSET,
    reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, None, OsidbApiV1FlawsListRequiresCveDescription
    ] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, OsidbApiV1FlawsListSource] = UNSET,
    statement: Union[Unset, None, str] = UNSET,
    statement_isempty: Union[Unset, None, bool] = UNSET,
    team_id: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
    unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
    workflow_state: Union[
        Unset, None, List[OsidbApiV1FlawsListWorkflowStateItem]
    ] = UNSET,
) -> Optional[OsidbApiV1FlawsListResponse200]:
    """ """

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


async def async_detailed(
    *,
    client: AuthenticatedClient,
    acknowledgments_affiliation: Union[Unset, None, str] = UNSET,
    acknowledgments_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_from_upstream: Union[Unset, None, bool] = UNSET,
    acknowledgments_name: Union[Unset, None, str] = UNSET,
    acknowledgments_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, None, str] = UNSET,
    affects_affectedness: Union[
        Unset, None, OsidbApiV1FlawsListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, None, bool] = UNSET,
    affects_impact: Union[Unset, None, OsidbApiV1FlawsListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, None, str] = UNSET,
    affects_ps_module: Union[Unset, None, str] = UNSET,
    affects_resolution: Union[
        Unset, None, OsidbApiV1FlawsListAffectsResolution
    ] = UNSET,
    affects_trackers_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_embargoed: Union[Unset, None, bool] = UNSET,
    affects_trackers_errata_advisory_name: Union[Unset, None, str] = UNSET,
    affects_trackers_errata_et_id: Union[Unset, None, int] = UNSET,
    affects_trackers_errata_shipped_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_gte: Union[
        Unset, None, datetime.date
    ] = UNSET,
    affects_trackers_errata_shipped_dt_date_lte: Union[
        Unset, None, datetime.date
    ] = UNSET,
    affects_trackers_errata_shipped_dt_gt: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_gte: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_lt: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_lte: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_external_system_id: Union[Unset, None, str] = UNSET,
    affects_trackers_ps_update_stream: Union[Unset, None, str] = UNSET,
    affects_trackers_resolution: Union[Unset, None, str] = UNSET,
    affects_trackers_status: Union[Unset, None, str] = UNSET,
    affects_trackers_type: Union[
        Unset, None, OsidbApiV1FlawsListAffectsTrackersType
    ] = UNSET,
    affects_trackers_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_uuid: Union[Unset, None, str] = UNSET,
    affects_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, None, str] = UNSET,
    bz_id: Union[Unset, None, float] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, None, str] = UNSET,
    components: Union[Unset, None, List[str]] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cve_description: Union[Unset, None, str] = UNSET,
    cve_description_isempty: Union[Unset, None, bool] = UNSET,
    cve_id: Union[Unset, None, List[str]] = UNSET,
    cve_id_isempty: Union[Unset, None, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, None, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, None, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, None, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, None, OsidbApiV1FlawsListCvssScoresIssuer] = UNSET,
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
    cwe_id: Union[Unset, None, str] = UNSET,
    cwe_id_isempty: Union[Unset, None, bool] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    impact: Union[Unset, None, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    major_incident_start_dt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_date: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_state: Union[
        Unset, None, OsidbApiV1FlawsListMajorIncidentState
    ] = UNSET,
    mitigation_isempty: Union[Unset, None, bool] = UNSET,
    nist_cvss_validation: Union[
        Unset, None, OsidbApiV1FlawsListNistCvssValidation
    ] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    owner_isempty: Union[Unset, None, bool] = UNSET,
    references_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    references_description: Union[Unset, None, str] = UNSET,
    references_type: Union[Unset, None, OsidbApiV1FlawsListReferencesType] = UNSET,
    references_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    references_url: Union[Unset, None, str] = UNSET,
    references_uuid: Union[Unset, None, str] = UNSET,
    reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, None, OsidbApiV1FlawsListRequiresCveDescription
    ] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, OsidbApiV1FlawsListSource] = UNSET,
    statement: Union[Unset, None, str] = UNSET,
    statement_isempty: Union[Unset, None, bool] = UNSET,
    team_id: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
    unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
    workflow_state: Union[
        Unset, None, List[OsidbApiV1FlawsListWorkflowStateItem]
    ] = UNSET,
) -> Response[OsidbApiV1FlawsListResponse200]:
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

    return _build_response(response=resp)


async def async_(
    *,
    client: AuthenticatedClient,
    acknowledgments_affiliation: Union[Unset, None, str] = UNSET,
    acknowledgments_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_from_upstream: Union[Unset, None, bool] = UNSET,
    acknowledgments_name: Union[Unset, None, str] = UNSET,
    acknowledgments_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, None, str] = UNSET,
    affects_affectedness: Union[
        Unset, None, OsidbApiV1FlawsListAffectsAffectedness
    ] = UNSET,
    affects_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_embargoed: Union[Unset, None, bool] = UNSET,
    affects_impact: Union[Unset, None, OsidbApiV1FlawsListAffectsImpact] = UNSET,
    affects_ps_component: Union[Unset, None, str] = UNSET,
    affects_ps_module: Union[Unset, None, str] = UNSET,
    affects_resolution: Union[
        Unset, None, OsidbApiV1FlawsListAffectsResolution
    ] = UNSET,
    affects_trackers_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_embargoed: Union[Unset, None, bool] = UNSET,
    affects_trackers_errata_advisory_name: Union[Unset, None, str] = UNSET,
    affects_trackers_errata_et_id: Union[Unset, None, int] = UNSET,
    affects_trackers_errata_shipped_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_errata_shipped_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_errata_shipped_dt_date_gte: Union[
        Unset, None, datetime.date
    ] = UNSET,
    affects_trackers_errata_shipped_dt_date_lte: Union[
        Unset, None, datetime.date
    ] = UNSET,
    affects_trackers_errata_shipped_dt_gt: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_gte: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_lt: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_errata_shipped_dt_lte: Union[
        Unset, None, datetime.datetime
    ] = UNSET,
    affects_trackers_external_system_id: Union[Unset, None, str] = UNSET,
    affects_trackers_ps_update_stream: Union[Unset, None, str] = UNSET,
    affects_trackers_resolution: Union[Unset, None, str] = UNSET,
    affects_trackers_status: Union[Unset, None, str] = UNSET,
    affects_trackers_type: Union[
        Unset, None, OsidbApiV1FlawsListAffectsTrackersType
    ] = UNSET,
    affects_trackers_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_trackers_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_trackers_uuid: Union[Unset, None, str] = UNSET,
    affects_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, None, str] = UNSET,
    bz_id: Union[Unset, None, float] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, None, str] = UNSET,
    components: Union[Unset, None, List[str]] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    cve_description: Union[Unset, None, str] = UNSET,
    cve_description_isempty: Union[Unset, None, bool] = UNSET,
    cve_id: Union[Unset, None, List[str]] = UNSET,
    cve_id_isempty: Union[Unset, None, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, None, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, None, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, None, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, None, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, None, OsidbApiV1FlawsListCvssScoresIssuer] = UNSET,
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
    cwe_id: Union[Unset, None, str] = UNSET,
    cwe_id_isempty: Union[Unset, None, bool] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    impact: Union[Unset, None, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    major_incident_start_dt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_date: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    major_incident_start_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_start_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    major_incident_state: Union[
        Unset, None, OsidbApiV1FlawsListMajorIncidentState
    ] = UNSET,
    mitigation_isempty: Union[Unset, None, bool] = UNSET,
    nist_cvss_validation: Union[
        Unset, None, OsidbApiV1FlawsListNistCvssValidation
    ] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, List[OsidbApiV1FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    owner_isempty: Union[Unset, None, bool] = UNSET,
    references_created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_date: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    references_created_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    references_created_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    references_description: Union[Unset, None, str] = UNSET,
    references_type: Union[Unset, None, OsidbApiV1FlawsListReferencesType] = UNSET,
    references_updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    references_url: Union[Unset, None, str] = UNSET,
    references_uuid: Union[Unset, None, str] = UNSET,
    reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, None, OsidbApiV1FlawsListRequiresCveDescription
    ] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, OsidbApiV1FlawsListSource] = UNSET,
    statement: Union[Unset, None, str] = UNSET,
    statement_isempty: Union[Unset, None, bool] = UNSET,
    team_id: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
    unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_date: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_gte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_date_lte: Union[Unset, None, datetime.date] = UNSET,
    updated_dt_gt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_gte: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt_lte: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
    workflow_state: Union[
        Unset, None, List[OsidbApiV1FlawsListWorkflowStateItem]
    ] = UNSET,
) -> Optional[OsidbApiV1FlawsListResponse200]:
    """ """

    return (
        await async_detailed(
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
