import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import requests

from ...client import AuthenticatedClient, Client
from ...models.osidb_api_v2_flaws_list_affects_affectedness import (
    OsidbApiV2FlawsListAffectsAffectedness,
)
from ...models.osidb_api_v2_flaws_list_affects_affectedness_in_item import (
    OsidbApiV2FlawsListAffectsAffectednessInItem,
)
from ...models.osidb_api_v2_flaws_list_affects_impact import (
    OsidbApiV2FlawsListAffectsImpact,
)
from ...models.osidb_api_v2_flaws_list_affects_impact_in_item import (
    OsidbApiV2FlawsListAffectsImpactInItem,
)
from ...models.osidb_api_v2_flaws_list_affects_resolution import (
    OsidbApiV2FlawsListAffectsResolution,
)
from ...models.osidb_api_v2_flaws_list_affects_resolution_in_item import (
    OsidbApiV2FlawsListAffectsResolutionInItem,
)
from ...models.osidb_api_v2_flaws_list_affects_tracker_type import (
    OsidbApiV2FlawsListAffectsTrackerType,
)
from ...models.osidb_api_v2_flaws_list_affects_tracker_type_in_item import (
    OsidbApiV2FlawsListAffectsTrackerTypeInItem,
)
from ...models.osidb_api_v2_flaws_list_affects_tracker_visibility import (
    OsidbApiV2FlawsListAffectsTrackerVisibility,
)
from ...models.osidb_api_v2_flaws_list_affects_visibility import (
    OsidbApiV2FlawsListAffectsVisibility,
)
from ...models.osidb_api_v2_flaws_list_cvss_scores_issuer import (
    OsidbApiV2FlawsListCvssScoresIssuer,
)
from ...models.osidb_api_v2_flaws_list_cvss_scores_issuer_in_item import (
    OsidbApiV2FlawsListCvssScoresIssuerInItem,
)
from ...models.osidb_api_v2_flaws_list_impact import OsidbApiV2FlawsListImpact
from ...models.osidb_api_v2_flaws_list_impact_in_item import (
    OsidbApiV2FlawsListImpactInItem,
)
from ...models.osidb_api_v2_flaws_list_major_incident_state import (
    OsidbApiV2FlawsListMajorIncidentState,
)
from ...models.osidb_api_v2_flaws_list_major_incident_state_in_item import (
    OsidbApiV2FlawsListMajorIncidentStateInItem,
)
from ...models.osidb_api_v2_flaws_list_nist_cvss_validation import (
    OsidbApiV2FlawsListNistCvssValidation,
)
from ...models.osidb_api_v2_flaws_list_nist_cvss_validation_in_item import (
    OsidbApiV2FlawsListNistCvssValidationInItem,
)
from ...models.osidb_api_v2_flaws_list_order_item import OsidbApiV2FlawsListOrderItem
from ...models.osidb_api_v2_flaws_list_references_type import (
    OsidbApiV2FlawsListReferencesType,
)
from ...models.osidb_api_v2_flaws_list_references_type_in_item import (
    OsidbApiV2FlawsListReferencesTypeInItem,
)
from ...models.osidb_api_v2_flaws_list_requires_cve_description import (
    OsidbApiV2FlawsListRequiresCveDescription,
)
from ...models.osidb_api_v2_flaws_list_requires_cve_description_in_item import (
    OsidbApiV2FlawsListRequiresCveDescriptionInItem,
)
from ...models.osidb_api_v2_flaws_list_response_200 import (
    OsidbApiV2FlawsListResponse200,
)
from ...models.osidb_api_v2_flaws_list_source import OsidbApiV2FlawsListSource
from ...models.osidb_api_v2_flaws_list_source_in_item import (
    OsidbApiV2FlawsListSourceInItem,
)
from ...models.osidb_api_v2_flaws_list_visibility import OsidbApiV2FlawsListVisibility
from ...models.osidb_api_v2_flaws_list_workflow_state_in_item import (
    OsidbApiV2FlawsListWorkflowStateInItem,
)
from ...models.osidb_api_v2_flaws_list_workflow_state_item import (
    OsidbApiV2FlawsListWorkflowStateItem,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "acknowledgments__affiliation": str,
    "acknowledgments__affiliation__in": list[str],
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
    "acknowledgments__name__in": list[str],
    "acknowledgments__updated_dt": datetime.datetime,
    "acknowledgments__updated_dt__date": datetime.date,
    "acknowledgments__updated_dt__date__gte": datetime.date,
    "acknowledgments__updated_dt__date__lte": datetime.date,
    "acknowledgments__updated_dt__gt": datetime.datetime,
    "acknowledgments__updated_dt__gte": datetime.datetime,
    "acknowledgments__updated_dt__lt": datetime.datetime,
    "acknowledgments__updated_dt__lte": datetime.datetime,
    "acknowledgments__uuid": UUID,
    "acknowledgments__uuid__in": list[UUID],
    "affects__affectedness": OsidbApiV2FlawsListAffectsAffectedness,
    "affects__affectedness__in": list[OsidbApiV2FlawsListAffectsAffectednessInItem],
    "affects__created_dt": datetime.datetime,
    "affects__created_dt__date": datetime.date,
    "affects__created_dt__date__gte": datetime.date,
    "affects__created_dt__date__lte": datetime.date,
    "affects__created_dt__gt": datetime.datetime,
    "affects__created_dt__gte": datetime.datetime,
    "affects__created_dt__lt": datetime.datetime,
    "affects__created_dt__lte": datetime.datetime,
    "affects__embargoed": bool,
    "affects__impact": OsidbApiV2FlawsListAffectsImpact,
    "affects__impact__in": list[OsidbApiV2FlawsListAffectsImpactInItem],
    "affects__ps_component": str,
    "affects__ps_component__in": list[str],
    "affects__ps_module": str,
    "affects__ps_module__in": list[str],
    "affects__ps_update_stream": str,
    "affects__ps_update_stream__in": list[str],
    "affects__resolution": OsidbApiV2FlawsListAffectsResolution,
    "affects__resolution__in": list[OsidbApiV2FlawsListAffectsResolutionInItem],
    "affects__tracker__created_dt": datetime.datetime,
    "affects__tracker__created_dt__date": datetime.date,
    "affects__tracker__created_dt__date__gte": datetime.date,
    "affects__tracker__created_dt__date__lte": datetime.date,
    "affects__tracker__created_dt__gt": datetime.datetime,
    "affects__tracker__created_dt__gte": datetime.datetime,
    "affects__tracker__created_dt__lt": datetime.datetime,
    "affects__tracker__created_dt__lte": datetime.datetime,
    "affects__tracker__embargoed": bool,
    "affects__tracker__errata__advisory_name": str,
    "affects__tracker__errata__advisory_name__in": list[str],
    "affects__tracker__errata__et_id": int,
    "affects__tracker__errata__shipped_dt": datetime.datetime,
    "affects__tracker__errata__shipped_dt__date": datetime.date,
    "affects__tracker__errata__shipped_dt__date__gte": datetime.date,
    "affects__tracker__errata__shipped_dt__date__lte": datetime.date,
    "affects__tracker__errata__shipped_dt__gt": datetime.datetime,
    "affects__tracker__errata__shipped_dt__gte": datetime.datetime,
    "affects__tracker__errata__shipped_dt__lt": datetime.datetime,
    "affects__tracker__errata__shipped_dt__lte": datetime.datetime,
    "affects__tracker__external_system_id": str,
    "affects__tracker__external_system_id__in": list[str],
    "affects__tracker__ps_update_stream": str,
    "affects__tracker__ps_update_stream__in": list[str],
    "affects__tracker__resolution": str,
    "affects__tracker__resolution__in": list[str],
    "affects__tracker__status": str,
    "affects__tracker__status__in": list[str],
    "affects__tracker__type": OsidbApiV2FlawsListAffectsTrackerType,
    "affects__tracker__type__in": list[OsidbApiV2FlawsListAffectsTrackerTypeInItem],
    "affects__tracker__updated_dt": datetime.datetime,
    "affects__tracker__updated_dt__date": datetime.date,
    "affects__tracker__updated_dt__date__gte": datetime.date,
    "affects__tracker__updated_dt__date__lte": datetime.date,
    "affects__tracker__updated_dt__gt": datetime.datetime,
    "affects__tracker__updated_dt__gte": datetime.datetime,
    "affects__tracker__updated_dt__lt": datetime.datetime,
    "affects__tracker__updated_dt__lte": datetime.datetime,
    "affects__tracker__uuid": UUID,
    "affects__tracker__uuid__in": list[UUID],
    "affects__tracker__visibility": OsidbApiV2FlawsListAffectsTrackerVisibility,
    "affects__updated_dt": datetime.datetime,
    "affects__updated_dt__date": datetime.date,
    "affects__updated_dt__date__gte": datetime.date,
    "affects__updated_dt__date__lte": datetime.date,
    "affects__updated_dt__gt": datetime.datetime,
    "affects__updated_dt__gte": datetime.datetime,
    "affects__updated_dt__lt": datetime.datetime,
    "affects__updated_dt__lte": datetime.datetime,
    "affects__uuid": UUID,
    "affects__uuid__in": list[UUID],
    "affects__visibility": OsidbApiV2FlawsListAffectsVisibility,
    "bz_id": float,
    "changed_after": datetime.datetime,
    "changed_before": datetime.datetime,
    "comment_zero": str,
    "components": list[str],
    "components__in": list[str],
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
    "cve_id__in": list[str],
    "cve_id__isempty": bool,
    "cvss2_nist__isempty": bool,
    "cvss2_rh__isempty": bool,
    "cvss3_nist__isempty": bool,
    "cvss3_rh__isempty": bool,
    "cvss4_nist__isempty": bool,
    "cvss4_rh__isempty": bool,
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
    "cvss_scores__issuer": OsidbApiV2FlawsListCvssScoresIssuer,
    "cvss_scores__issuer__in": list[OsidbApiV2FlawsListCvssScoresIssuerInItem],
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
    "cwe_id": str,
    "cwe_id__in": list[str],
    "cwe_id__isempty": bool,
    "embargoed": bool,
    "exclude_fields": list[str],
    "flaw_has_no_non_community_affects_trackers": bool,
    "flaw_labels": list[str],
    "impact": OsidbApiV2FlawsListImpact,
    "impact__in": list[OsidbApiV2FlawsListImpactInItem],
    "include_fields": list[str],
    "include_history": bool,
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
    "major_incident_state": OsidbApiV2FlawsListMajorIncidentState,
    "major_incident_state__in": list[OsidbApiV2FlawsListMajorIncidentStateInItem],
    "mitigation__isempty": bool,
    "nist_cvss_validation": OsidbApiV2FlawsListNistCvssValidation,
    "nist_cvss_validation__in": list[OsidbApiV2FlawsListNistCvssValidationInItem],
    "offset": int,
    "order": list[OsidbApiV2FlawsListOrderItem],
    "owner": str,
    "owner__in": list[str],
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
    "references__description__in": list[str],
    "references__type": OsidbApiV2FlawsListReferencesType,
    "references__type__in": list[OsidbApiV2FlawsListReferencesTypeInItem],
    "references__updated_dt": datetime.datetime,
    "references__updated_dt__date": datetime.date,
    "references__updated_dt__date__gte": datetime.date,
    "references__updated_dt__date__lte": datetime.date,
    "references__updated_dt__gt": datetime.datetime,
    "references__updated_dt__gte": datetime.datetime,
    "references__updated_dt__lt": datetime.datetime,
    "references__updated_dt__lte": datetime.datetime,
    "references__url": str,
    "references__url__in": list[str],
    "references__uuid": UUID,
    "references__uuid__in": list[UUID],
    "reported_dt": datetime.datetime,
    "reported_dt__date": datetime.date,
    "reported_dt__date__gte": datetime.date,
    "reported_dt__date__lte": datetime.date,
    "reported_dt__gt": datetime.datetime,
    "reported_dt__gte": datetime.datetime,
    "reported_dt__lt": datetime.datetime,
    "reported_dt__lte": datetime.datetime,
    "requires_cve_description": OsidbApiV2FlawsListRequiresCveDescription,
    "requires_cve_description__in": list[
        OsidbApiV2FlawsListRequiresCveDescriptionInItem
    ],
    "search": str,
    "source": OsidbApiV2FlawsListSource,
    "source__in": list[OsidbApiV2FlawsListSourceInItem],
    "statement": str,
    "statement__isempty": bool,
    "team_id": str,
    "team_id__in": list[str],
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
    "uuid__in": list[UUID],
    "visibility": OsidbApiV2FlawsListVisibility,
    "workflow_state": list[OsidbApiV2FlawsListWorkflowStateItem],
    "workflow_state__in": list[OsidbApiV2FlawsListWorkflowStateInItem],
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    acknowledgments_affiliation: Union[Unset, str] = UNSET,
    acknowledgments_affiliation_in: Union[Unset, list[str]] = UNSET,
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
    acknowledgments_name_in: Union[Unset, list[str]] = UNSET,
    acknowledgments_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, UUID] = UNSET,
    acknowledgments_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_affectedness: Union[Unset, OsidbApiV2FlawsListAffectsAffectedness] = UNSET,
    affects_affectedness_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsAffectednessInItem]
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
    affects_impact: Union[Unset, OsidbApiV2FlawsListAffectsImpact] = UNSET,
    affects_impact_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsImpactInItem]
    ] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_component_in: Union[Unset, list[str]] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_ps_module_in: Union[Unset, list[str]] = UNSET,
    affects_ps_update_stream: Union[Unset, str] = UNSET,
    affects_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV2FlawsListAffectsResolution] = UNSET,
    affects_resolution_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsResolutionInItem]
    ] = UNSET,
    affects_tracker_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_embargoed: Union[Unset, bool] = UNSET,
    affects_tracker_errata_advisory_name: Union[Unset, str] = UNSET,
    affects_tracker_errata_advisory_name_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_errata_et_id: Union[Unset, int] = UNSET,
    affects_tracker_errata_shipped_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_external_system_id: Union[Unset, str] = UNSET,
    affects_tracker_external_system_id_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_ps_update_stream: Union[Unset, str] = UNSET,
    affects_tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_resolution: Union[Unset, str] = UNSET,
    affects_tracker_resolution_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_status: Union[Unset, str] = UNSET,
    affects_tracker_status_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_type: Union[Unset, OsidbApiV2FlawsListAffectsTrackerType] = UNSET,
    affects_tracker_type_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsTrackerTypeInItem]
    ] = UNSET,
    affects_tracker_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_uuid: Union[Unset, UUID] = UNSET,
    affects_tracker_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_tracker_visibility: Union[
        Unset, OsidbApiV2FlawsListAffectsTrackerVisibility
    ] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    affects_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_visibility: Union[Unset, OsidbApiV2FlawsListAffectsVisibility] = UNSET,
    bz_id: Union[Unset, float] = UNSET,
    changed_after: Union[Unset, datetime.datetime] = UNSET,
    changed_before: Union[Unset, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, str] = UNSET,
    components: Union[Unset, list[str]] = UNSET,
    components_in: Union[Unset, list[str]] = UNSET,
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
    cve_id_in: Union[Unset, list[str]] = UNSET,
    cve_id_isempty: Union[Unset, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, OsidbApiV2FlawsListCvssScoresIssuer] = UNSET,
    cvss_scores_issuer_in: Union[
        Unset, list[OsidbApiV2FlawsListCvssScoresIssuerInItem]
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
    cwe_id: Union[Unset, str] = UNSET,
    cwe_id_in: Union[Unset, list[str]] = UNSET,
    cwe_id_isempty: Union[Unset, bool] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_has_no_non_community_affects_trackers: Union[Unset, bool] = UNSET,
    flaw_labels: Union[Unset, list[str]] = UNSET,
    impact: Union[Unset, OsidbApiV2FlawsListImpact] = UNSET,
    impact_in: Union[Unset, list[OsidbApiV2FlawsListImpactInItem]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
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
    major_incident_state: Union[Unset, OsidbApiV2FlawsListMajorIncidentState] = UNSET,
    major_incident_state_in: Union[
        Unset, list[OsidbApiV2FlawsListMajorIncidentStateInItem]
    ] = UNSET,
    mitigation_isempty: Union[Unset, bool] = UNSET,
    nist_cvss_validation: Union[Unset, OsidbApiV2FlawsListNistCvssValidation] = UNSET,
    nist_cvss_validation_in: Union[
        Unset, list[OsidbApiV2FlawsListNistCvssValidationInItem]
    ] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV2FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, str] = UNSET,
    owner_in: Union[Unset, list[str]] = UNSET,
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
    references_description_in: Union[Unset, list[str]] = UNSET,
    references_type: Union[Unset, OsidbApiV2FlawsListReferencesType] = UNSET,
    references_type_in: Union[
        Unset, list[OsidbApiV2FlawsListReferencesTypeInItem]
    ] = UNSET,
    references_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_url: Union[Unset, str] = UNSET,
    references_url_in: Union[Unset, list[str]] = UNSET,
    references_uuid: Union[Unset, UUID] = UNSET,
    references_uuid_in: Union[Unset, list[UUID]] = UNSET,
    reported_dt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, OsidbApiV2FlawsListRequiresCveDescription
    ] = UNSET,
    requires_cve_description_in: Union[
        Unset, list[OsidbApiV2FlawsListRequiresCveDescriptionInItem]
    ] = UNSET,
    search: Union[Unset, str] = UNSET,
    source: Union[Unset, OsidbApiV2FlawsListSource] = UNSET,
    source_in: Union[Unset, list[OsidbApiV2FlawsListSourceInItem]] = UNSET,
    statement: Union[Unset, str] = UNSET,
    statement_isempty: Union[Unset, bool] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    team_id_in: Union[Unset, list[str]] = UNSET,
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
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    visibility: Union[Unset, OsidbApiV2FlawsListVisibility] = UNSET,
    workflow_state: Union[Unset, list[OsidbApiV2FlawsListWorkflowStateItem]] = UNSET,
    workflow_state_in: Union[
        Unset, list[OsidbApiV2FlawsListWorkflowStateInItem]
    ] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = client.get_headers()

    params: dict[str, Any] = {}

    params["acknowledgments__affiliation"] = acknowledgments_affiliation

    json_acknowledgments_affiliation_in: Union[Unset, list[str]] = UNSET
    if not isinstance(acknowledgments_affiliation_in, Unset):
        json_acknowledgments_affiliation_in = acknowledgments_affiliation_in

    params["acknowledgments__affiliation__in"] = json_acknowledgments_affiliation_in

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

    json_acknowledgments_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(acknowledgments_name_in, Unset):
        json_acknowledgments_name_in = acknowledgments_name_in

    params["acknowledgments__name__in"] = json_acknowledgments_name_in

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

    json_acknowledgments_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(acknowledgments_uuid_in, Unset):
        json_acknowledgments_uuid_in = []
        for acknowledgments_uuid_in_item_data in acknowledgments_uuid_in:
            acknowledgments_uuid_in_item: str = UNSET
            if not isinstance(acknowledgments_uuid_in_item_data, Unset):
                acknowledgments_uuid_in_item = str(acknowledgments_uuid_in_item_data)

            json_acknowledgments_uuid_in.append(acknowledgments_uuid_in_item)

    params["acknowledgments__uuid__in"] = json_acknowledgments_uuid_in

    json_affects_affectedness: Union[Unset, str] = UNSET
    if not isinstance(affects_affectedness, Unset):
        json_affects_affectedness = OsidbApiV2FlawsListAffectsAffectedness(
            affects_affectedness
        ).value

    params["affects__affectedness"] = json_affects_affectedness

    json_affects_affectedness_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_affectedness_in, Unset):
        json_affects_affectedness_in = []
        for affects_affectedness_in_item_data in affects_affectedness_in:
            affects_affectedness_in_item: str = UNSET
            if not isinstance(affects_affectedness_in_item_data, Unset):
                affects_affectedness_in_item = (
                    OsidbApiV2FlawsListAffectsAffectednessInItem(
                        affects_affectedness_in_item_data
                    ).value
                )

            json_affects_affectedness_in.append(affects_affectedness_in_item)

    params["affects__affectedness__in"] = json_affects_affectedness_in

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
        json_affects_impact = OsidbApiV2FlawsListAffectsImpact(affects_impact).value

    params["affects__impact"] = json_affects_impact

    json_affects_impact_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_impact_in, Unset):
        json_affects_impact_in = []
        for affects_impact_in_item_data in affects_impact_in:
            affects_impact_in_item: str = UNSET
            if not isinstance(affects_impact_in_item_data, Unset):
                affects_impact_in_item = OsidbApiV2FlawsListAffectsImpactInItem(
                    affects_impact_in_item_data
                ).value

            json_affects_impact_in.append(affects_impact_in_item)

    params["affects__impact__in"] = json_affects_impact_in

    params["affects__ps_component"] = affects_ps_component

    json_affects_ps_component_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_ps_component_in, Unset):
        json_affects_ps_component_in = affects_ps_component_in

    params["affects__ps_component__in"] = json_affects_ps_component_in

    params["affects__ps_module"] = affects_ps_module

    json_affects_ps_module_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_ps_module_in, Unset):
        json_affects_ps_module_in = affects_ps_module_in

    params["affects__ps_module__in"] = json_affects_ps_module_in

    params["affects__ps_update_stream"] = affects_ps_update_stream

    json_affects_ps_update_stream_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_ps_update_stream_in, Unset):
        json_affects_ps_update_stream_in = affects_ps_update_stream_in

    params["affects__ps_update_stream__in"] = json_affects_ps_update_stream_in

    json_affects_resolution: Union[Unset, str] = UNSET
    if not isinstance(affects_resolution, Unset):
        json_affects_resolution = OsidbApiV2FlawsListAffectsResolution(
            affects_resolution
        ).value

    params["affects__resolution"] = json_affects_resolution

    json_affects_resolution_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_resolution_in, Unset):
        json_affects_resolution_in = []
        for affects_resolution_in_item_data in affects_resolution_in:
            affects_resolution_in_item: str = UNSET
            if not isinstance(affects_resolution_in_item_data, Unset):
                affects_resolution_in_item = OsidbApiV2FlawsListAffectsResolutionInItem(
                    affects_resolution_in_item_data
                ).value

            json_affects_resolution_in.append(affects_resolution_in_item)

    params["affects__resolution__in"] = json_affects_resolution_in

    json_affects_tracker_created_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_created_dt, Unset):
        json_affects_tracker_created_dt = affects_tracker_created_dt.isoformat()

    params["affects__tracker__created_dt"] = json_affects_tracker_created_dt

    json_affects_tracker_created_dt_date: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_created_dt_date, Unset):
        json_affects_tracker_created_dt_date = (
            affects_tracker_created_dt_date.isoformat()
        )

    params["affects__tracker__created_dt__date"] = json_affects_tracker_created_dt_date

    json_affects_tracker_created_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_created_dt_date_gte, Unset):
        json_affects_tracker_created_dt_date_gte = (
            affects_tracker_created_dt_date_gte.isoformat()
        )

    params["affects__tracker__created_dt__date__gte"] = (
        json_affects_tracker_created_dt_date_gte
    )

    json_affects_tracker_created_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_created_dt_date_lte, Unset):
        json_affects_tracker_created_dt_date_lte = (
            affects_tracker_created_dt_date_lte.isoformat()
        )

    params["affects__tracker__created_dt__date__lte"] = (
        json_affects_tracker_created_dt_date_lte
    )

    json_affects_tracker_created_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_created_dt_gt, Unset):
        json_affects_tracker_created_dt_gt = affects_tracker_created_dt_gt.isoformat()

    params["affects__tracker__created_dt__gt"] = json_affects_tracker_created_dt_gt

    json_affects_tracker_created_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_created_dt_gte, Unset):
        json_affects_tracker_created_dt_gte = affects_tracker_created_dt_gte.isoformat()

    params["affects__tracker__created_dt__gte"] = json_affects_tracker_created_dt_gte

    json_affects_tracker_created_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_created_dt_lt, Unset):
        json_affects_tracker_created_dt_lt = affects_tracker_created_dt_lt.isoformat()

    params["affects__tracker__created_dt__lt"] = json_affects_tracker_created_dt_lt

    json_affects_tracker_created_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_created_dt_lte, Unset):
        json_affects_tracker_created_dt_lte = affects_tracker_created_dt_lte.isoformat()

    params["affects__tracker__created_dt__lte"] = json_affects_tracker_created_dt_lte

    params["affects__tracker__embargoed"] = affects_tracker_embargoed

    params["affects__tracker__errata__advisory_name"] = (
        affects_tracker_errata_advisory_name
    )

    json_affects_tracker_errata_advisory_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_tracker_errata_advisory_name_in, Unset):
        json_affects_tracker_errata_advisory_name_in = (
            affects_tracker_errata_advisory_name_in
        )

    params["affects__tracker__errata__advisory_name__in"] = (
        json_affects_tracker_errata_advisory_name_in
    )

    params["affects__tracker__errata__et_id"] = affects_tracker_errata_et_id

    json_affects_tracker_errata_shipped_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_errata_shipped_dt, Unset):
        json_affects_tracker_errata_shipped_dt = (
            affects_tracker_errata_shipped_dt.isoformat()
        )

    params["affects__tracker__errata__shipped_dt"] = (
        json_affects_tracker_errata_shipped_dt
    )

    json_affects_tracker_errata_shipped_dt_date: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_errata_shipped_dt_date, Unset):
        json_affects_tracker_errata_shipped_dt_date = (
            affects_tracker_errata_shipped_dt_date.isoformat()
        )

    params["affects__tracker__errata__shipped_dt__date"] = (
        json_affects_tracker_errata_shipped_dt_date
    )

    json_affects_tracker_errata_shipped_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_errata_shipped_dt_date_gte, Unset):
        json_affects_tracker_errata_shipped_dt_date_gte = (
            affects_tracker_errata_shipped_dt_date_gte.isoformat()
        )

    params["affects__tracker__errata__shipped_dt__date__gte"] = (
        json_affects_tracker_errata_shipped_dt_date_gte
    )

    json_affects_tracker_errata_shipped_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_errata_shipped_dt_date_lte, Unset):
        json_affects_tracker_errata_shipped_dt_date_lte = (
            affects_tracker_errata_shipped_dt_date_lte.isoformat()
        )

    params["affects__tracker__errata__shipped_dt__date__lte"] = (
        json_affects_tracker_errata_shipped_dt_date_lte
    )

    json_affects_tracker_errata_shipped_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_errata_shipped_dt_gt, Unset):
        json_affects_tracker_errata_shipped_dt_gt = (
            affects_tracker_errata_shipped_dt_gt.isoformat()
        )

    params["affects__tracker__errata__shipped_dt__gt"] = (
        json_affects_tracker_errata_shipped_dt_gt
    )

    json_affects_tracker_errata_shipped_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_errata_shipped_dt_gte, Unset):
        json_affects_tracker_errata_shipped_dt_gte = (
            affects_tracker_errata_shipped_dt_gte.isoformat()
        )

    params["affects__tracker__errata__shipped_dt__gte"] = (
        json_affects_tracker_errata_shipped_dt_gte
    )

    json_affects_tracker_errata_shipped_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_errata_shipped_dt_lt, Unset):
        json_affects_tracker_errata_shipped_dt_lt = (
            affects_tracker_errata_shipped_dt_lt.isoformat()
        )

    params["affects__tracker__errata__shipped_dt__lt"] = (
        json_affects_tracker_errata_shipped_dt_lt
    )

    json_affects_tracker_errata_shipped_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_errata_shipped_dt_lte, Unset):
        json_affects_tracker_errata_shipped_dt_lte = (
            affects_tracker_errata_shipped_dt_lte.isoformat()
        )

    params["affects__tracker__errata__shipped_dt__lte"] = (
        json_affects_tracker_errata_shipped_dt_lte
    )

    params["affects__tracker__external_system_id"] = affects_tracker_external_system_id

    json_affects_tracker_external_system_id_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_tracker_external_system_id_in, Unset):
        json_affects_tracker_external_system_id_in = (
            affects_tracker_external_system_id_in
        )

    params["affects__tracker__external_system_id__in"] = (
        json_affects_tracker_external_system_id_in
    )

    params["affects__tracker__ps_update_stream"] = affects_tracker_ps_update_stream

    json_affects_tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_tracker_ps_update_stream_in, Unset):
        json_affects_tracker_ps_update_stream_in = affects_tracker_ps_update_stream_in

    params["affects__tracker__ps_update_stream__in"] = (
        json_affects_tracker_ps_update_stream_in
    )

    params["affects__tracker__resolution"] = affects_tracker_resolution

    json_affects_tracker_resolution_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_tracker_resolution_in, Unset):
        json_affects_tracker_resolution_in = affects_tracker_resolution_in

    params["affects__tracker__resolution__in"] = json_affects_tracker_resolution_in

    params["affects__tracker__status"] = affects_tracker_status

    json_affects_tracker_status_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_tracker_status_in, Unset):
        json_affects_tracker_status_in = affects_tracker_status_in

    params["affects__tracker__status__in"] = json_affects_tracker_status_in

    json_affects_tracker_type: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_type, Unset):
        json_affects_tracker_type = OsidbApiV2FlawsListAffectsTrackerType(
            affects_tracker_type
        ).value

    params["affects__tracker__type"] = json_affects_tracker_type

    json_affects_tracker_type_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_tracker_type_in, Unset):
        json_affects_tracker_type_in = []
        for affects_tracker_type_in_item_data in affects_tracker_type_in:
            affects_tracker_type_in_item: str = UNSET
            if not isinstance(affects_tracker_type_in_item_data, Unset):
                affects_tracker_type_in_item = (
                    OsidbApiV2FlawsListAffectsTrackerTypeInItem(
                        affects_tracker_type_in_item_data
                    ).value
                )

            json_affects_tracker_type_in.append(affects_tracker_type_in_item)

    params["affects__tracker__type__in"] = json_affects_tracker_type_in

    json_affects_tracker_updated_dt: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_updated_dt, Unset):
        json_affects_tracker_updated_dt = affects_tracker_updated_dt.isoformat()

    params["affects__tracker__updated_dt"] = json_affects_tracker_updated_dt

    json_affects_tracker_updated_dt_date: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_updated_dt_date, Unset):
        json_affects_tracker_updated_dt_date = (
            affects_tracker_updated_dt_date.isoformat()
        )

    params["affects__tracker__updated_dt__date"] = json_affects_tracker_updated_dt_date

    json_affects_tracker_updated_dt_date_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_updated_dt_date_gte, Unset):
        json_affects_tracker_updated_dt_date_gte = (
            affects_tracker_updated_dt_date_gte.isoformat()
        )

    params["affects__tracker__updated_dt__date__gte"] = (
        json_affects_tracker_updated_dt_date_gte
    )

    json_affects_tracker_updated_dt_date_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_updated_dt_date_lte, Unset):
        json_affects_tracker_updated_dt_date_lte = (
            affects_tracker_updated_dt_date_lte.isoformat()
        )

    params["affects__tracker__updated_dt__date__lte"] = (
        json_affects_tracker_updated_dt_date_lte
    )

    json_affects_tracker_updated_dt_gt: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_updated_dt_gt, Unset):
        json_affects_tracker_updated_dt_gt = affects_tracker_updated_dt_gt.isoformat()

    params["affects__tracker__updated_dt__gt"] = json_affects_tracker_updated_dt_gt

    json_affects_tracker_updated_dt_gte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_updated_dt_gte, Unset):
        json_affects_tracker_updated_dt_gte = affects_tracker_updated_dt_gte.isoformat()

    params["affects__tracker__updated_dt__gte"] = json_affects_tracker_updated_dt_gte

    json_affects_tracker_updated_dt_lt: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_updated_dt_lt, Unset):
        json_affects_tracker_updated_dt_lt = affects_tracker_updated_dt_lt.isoformat()

    params["affects__tracker__updated_dt__lt"] = json_affects_tracker_updated_dt_lt

    json_affects_tracker_updated_dt_lte: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_updated_dt_lte, Unset):
        json_affects_tracker_updated_dt_lte = affects_tracker_updated_dt_lte.isoformat()

    params["affects__tracker__updated_dt__lte"] = json_affects_tracker_updated_dt_lte

    json_affects_tracker_uuid: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_uuid, Unset):
        json_affects_tracker_uuid = str(affects_tracker_uuid)

    params["affects__tracker__uuid"] = json_affects_tracker_uuid

    json_affects_tracker_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_tracker_uuid_in, Unset):
        json_affects_tracker_uuid_in = []
        for affects_tracker_uuid_in_item_data in affects_tracker_uuid_in:
            affects_tracker_uuid_in_item: str = UNSET
            if not isinstance(affects_tracker_uuid_in_item_data, Unset):
                affects_tracker_uuid_in_item = str(affects_tracker_uuid_in_item_data)

            json_affects_tracker_uuid_in.append(affects_tracker_uuid_in_item)

    params["affects__tracker__uuid__in"] = json_affects_tracker_uuid_in

    json_affects_tracker_visibility: Union[Unset, str] = UNSET
    if not isinstance(affects_tracker_visibility, Unset):
        json_affects_tracker_visibility = OsidbApiV2FlawsListAffectsTrackerVisibility(
            affects_tracker_visibility
        ).value

    params["affects__tracker__visibility"] = json_affects_tracker_visibility

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

    json_affects_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(affects_uuid_in, Unset):
        json_affects_uuid_in = []
        for affects_uuid_in_item_data in affects_uuid_in:
            affects_uuid_in_item: str = UNSET
            if not isinstance(affects_uuid_in_item_data, Unset):
                affects_uuid_in_item = str(affects_uuid_in_item_data)

            json_affects_uuid_in.append(affects_uuid_in_item)

    params["affects__uuid__in"] = json_affects_uuid_in

    json_affects_visibility: Union[Unset, str] = UNSET
    if not isinstance(affects_visibility, Unset):
        json_affects_visibility = OsidbApiV2FlawsListAffectsVisibility(
            affects_visibility
        ).value

    params["affects__visibility"] = json_affects_visibility

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

    json_components_in: Union[Unset, list[str]] = UNSET
    if not isinstance(components_in, Unset):
        json_components_in = components_in

    params["components__in"] = json_components_in

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

    json_cve_id_in: Union[Unset, list[str]] = UNSET
    if not isinstance(cve_id_in, Unset):
        json_cve_id_in = cve_id_in

    params["cve_id__in"] = json_cve_id_in

    params["cve_id__isempty"] = cve_id_isempty

    params["cvss2_nist__isempty"] = cvss2_nist_isempty

    params["cvss2_rh__isempty"] = cvss2_rh_isempty

    params["cvss3_nist__isempty"] = cvss3_nist_isempty

    params["cvss3_rh__isempty"] = cvss3_rh_isempty

    params["cvss4_nist__isempty"] = cvss4_nist_isempty

    params["cvss4_rh__isempty"] = cvss4_rh_isempty

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
        json_cvss_scores_issuer = OsidbApiV2FlawsListCvssScoresIssuer(
            cvss_scores_issuer
        ).value

    params["cvss_scores__issuer"] = json_cvss_scores_issuer

    json_cvss_scores_issuer_in: Union[Unset, list[str]] = UNSET
    if not isinstance(cvss_scores_issuer_in, Unset):
        json_cvss_scores_issuer_in = []
        for cvss_scores_issuer_in_item_data in cvss_scores_issuer_in:
            cvss_scores_issuer_in_item: str = UNSET
            if not isinstance(cvss_scores_issuer_in_item_data, Unset):
                cvss_scores_issuer_in_item = OsidbApiV2FlawsListCvssScoresIssuerInItem(
                    cvss_scores_issuer_in_item_data
                ).value

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

    params["cwe_id"] = cwe_id

    json_cwe_id_in: Union[Unset, list[str]] = UNSET
    if not isinstance(cwe_id_in, Unset):
        json_cwe_id_in = cwe_id_in

    params["cwe_id__in"] = json_cwe_id_in

    params["cwe_id__isempty"] = cwe_id_isempty

    params["embargoed"] = embargoed

    json_exclude_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        json_exclude_fields = exclude_fields

    params["exclude_fields"] = json_exclude_fields

    params["flaw_has_no_non_community_affects_trackers"] = (
        flaw_has_no_non_community_affects_trackers
    )

    json_flaw_labels: Union[Unset, list[str]] = UNSET
    if not isinstance(flaw_labels, Unset):
        json_flaw_labels = flaw_labels

    params["flaw_labels"] = json_flaw_labels

    json_impact: Union[Unset, str] = UNSET
    if not isinstance(impact, Unset):
        json_impact = OsidbApiV2FlawsListImpact(impact).value

    params["impact"] = json_impact

    json_impact_in: Union[Unset, list[str]] = UNSET
    if not isinstance(impact_in, Unset):
        json_impact_in = []
        for impact_in_item_data in impact_in:
            impact_in_item: str = UNSET
            if not isinstance(impact_in_item_data, Unset):
                impact_in_item = OsidbApiV2FlawsListImpactInItem(
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
        json_major_incident_state = OsidbApiV2FlawsListMajorIncidentState(
            major_incident_state
        ).value

    params["major_incident_state"] = json_major_incident_state

    json_major_incident_state_in: Union[Unset, list[str]] = UNSET
    if not isinstance(major_incident_state_in, Unset):
        json_major_incident_state_in = []
        for major_incident_state_in_item_data in major_incident_state_in:
            major_incident_state_in_item: str = UNSET
            if not isinstance(major_incident_state_in_item_data, Unset):
                major_incident_state_in_item = (
                    OsidbApiV2FlawsListMajorIncidentStateInItem(
                        major_incident_state_in_item_data
                    ).value
                )

            json_major_incident_state_in.append(major_incident_state_in_item)

    params["major_incident_state__in"] = json_major_incident_state_in

    params["mitigation__isempty"] = mitigation_isempty

    json_nist_cvss_validation: Union[Unset, str] = UNSET
    if not isinstance(nist_cvss_validation, Unset):
        json_nist_cvss_validation = OsidbApiV2FlawsListNistCvssValidation(
            nist_cvss_validation
        ).value

    params["nist_cvss_validation"] = json_nist_cvss_validation

    json_nist_cvss_validation_in: Union[Unset, list[str]] = UNSET
    if not isinstance(nist_cvss_validation_in, Unset):
        json_nist_cvss_validation_in = []
        for nist_cvss_validation_in_item_data in nist_cvss_validation_in:
            nist_cvss_validation_in_item: str = UNSET
            if not isinstance(nist_cvss_validation_in_item_data, Unset):
                nist_cvss_validation_in_item = (
                    OsidbApiV2FlawsListNistCvssValidationInItem(
                        nist_cvss_validation_in_item_data
                    ).value
                )

            json_nist_cvss_validation_in.append(nist_cvss_validation_in_item)

    params["nist_cvss_validation__in"] = json_nist_cvss_validation_in

    params["offset"] = offset

    json_order: Union[Unset, list[str]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item: str = UNSET
            if not isinstance(order_item_data, Unset):
                order_item = OsidbApiV2FlawsListOrderItem(order_item_data).value

            json_order.append(order_item)

    params["order"] = json_order

    params["owner"] = owner

    json_owner_in: Union[Unset, list[str]] = UNSET
    if not isinstance(owner_in, Unset):
        json_owner_in = owner_in

    params["owner__in"] = json_owner_in

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

    json_references_description_in: Union[Unset, list[str]] = UNSET
    if not isinstance(references_description_in, Unset):
        json_references_description_in = references_description_in

    params["references__description__in"] = json_references_description_in

    json_references_type: Union[Unset, str] = UNSET
    if not isinstance(references_type, Unset):
        json_references_type = OsidbApiV2FlawsListReferencesType(references_type).value

    params["references__type"] = json_references_type

    json_references_type_in: Union[Unset, list[str]] = UNSET
    if not isinstance(references_type_in, Unset):
        json_references_type_in = []
        for references_type_in_item_data in references_type_in:
            references_type_in_item: str = UNSET
            if not isinstance(references_type_in_item_data, Unset):
                references_type_in_item = OsidbApiV2FlawsListReferencesTypeInItem(
                    references_type_in_item_data
                ).value

            json_references_type_in.append(references_type_in_item)

    params["references__type__in"] = json_references_type_in

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

    json_references_url_in: Union[Unset, list[str]] = UNSET
    if not isinstance(references_url_in, Unset):
        json_references_url_in = references_url_in

    params["references__url__in"] = json_references_url_in

    json_references_uuid: Union[Unset, str] = UNSET
    if not isinstance(references_uuid, Unset):
        json_references_uuid = str(references_uuid)

    params["references__uuid"] = json_references_uuid

    json_references_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(references_uuid_in, Unset):
        json_references_uuid_in = []
        for references_uuid_in_item_data in references_uuid_in:
            references_uuid_in_item: str = UNSET
            if not isinstance(references_uuid_in_item_data, Unset):
                references_uuid_in_item = str(references_uuid_in_item_data)

            json_references_uuid_in.append(references_uuid_in_item)

    params["references__uuid__in"] = json_references_uuid_in

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
        json_requires_cve_description = OsidbApiV2FlawsListRequiresCveDescription(
            requires_cve_description
        ).value

    params["requires_cve_description"] = json_requires_cve_description

    json_requires_cve_description_in: Union[Unset, list[str]] = UNSET
    if not isinstance(requires_cve_description_in, Unset):
        json_requires_cve_description_in = []
        for requires_cve_description_in_item_data in requires_cve_description_in:
            requires_cve_description_in_item: str = UNSET
            if not isinstance(requires_cve_description_in_item_data, Unset):
                requires_cve_description_in_item = (
                    OsidbApiV2FlawsListRequiresCveDescriptionInItem(
                        requires_cve_description_in_item_data
                    ).value
                )

            json_requires_cve_description_in.append(requires_cve_description_in_item)

    params["requires_cve_description__in"] = json_requires_cve_description_in

    params["search"] = search

    json_source: Union[Unset, str] = UNSET
    if not isinstance(source, Unset):
        json_source = OsidbApiV2FlawsListSource(source).value

    params["source"] = json_source

    json_source_in: Union[Unset, list[str]] = UNSET
    if not isinstance(source_in, Unset):
        json_source_in = []
        for source_in_item_data in source_in:
            source_in_item: str = UNSET
            if not isinstance(source_in_item_data, Unset):
                source_in_item = OsidbApiV2FlawsListSourceInItem(
                    source_in_item_data
                ).value

            json_source_in.append(source_in_item)

    params["source__in"] = json_source_in

    params["statement"] = statement

    params["statement__isempty"] = statement_isempty

    params["team_id"] = team_id

    json_team_id_in: Union[Unset, list[str]] = UNSET
    if not isinstance(team_id_in, Unset):
        json_team_id_in = team_id_in

    params["team_id__in"] = json_team_id_in

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
        json_visibility = OsidbApiV2FlawsListVisibility(visibility).value

    params["visibility"] = json_visibility

    json_workflow_state: Union[Unset, list[str]] = UNSET
    if not isinstance(workflow_state, Unset):
        json_workflow_state = []
        for workflow_state_item_data in workflow_state:
            workflow_state_item: str = UNSET
            if not isinstance(workflow_state_item_data, Unset):
                workflow_state_item = OsidbApiV2FlawsListWorkflowStateItem(
                    workflow_state_item_data
                ).value

            json_workflow_state.append(workflow_state_item)

    params["workflow_state"] = json_workflow_state

    json_workflow_state_in: Union[Unset, list[str]] = UNSET
    if not isinstance(workflow_state_in, Unset):
        json_workflow_state_in = []
        for workflow_state_in_item_data in workflow_state_in:
            workflow_state_in_item: str = UNSET
            if not isinstance(workflow_state_in_item_data, Unset):
                workflow_state_in_item = OsidbApiV2FlawsListWorkflowStateInItem(
                    workflow_state_in_item_data
                ).value

            json_workflow_state_in.append(workflow_state_in_item)

    params["workflow_state__in"] = json_workflow_state_in

    params = {
        k: (",".join(v) if isinstance(v, list) else v)
        for k, v in params.items()
        if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "url": f"{client.base_url}/osidb/api/v2/flaws",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Optional[OsidbApiV2FlawsListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV2FlawsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV2FlawsListResponse200.from_dict(_response_200)

        return response_200


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: requests.Response
) -> Response[OsidbApiV2FlawsListResponse200]:
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
    acknowledgments_affiliation_in: Union[Unset, list[str]] = UNSET,
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
    acknowledgments_name_in: Union[Unset, list[str]] = UNSET,
    acknowledgments_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, UUID] = UNSET,
    acknowledgments_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_affectedness: Union[Unset, OsidbApiV2FlawsListAffectsAffectedness] = UNSET,
    affects_affectedness_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsAffectednessInItem]
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
    affects_impact: Union[Unset, OsidbApiV2FlawsListAffectsImpact] = UNSET,
    affects_impact_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsImpactInItem]
    ] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_component_in: Union[Unset, list[str]] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_ps_module_in: Union[Unset, list[str]] = UNSET,
    affects_ps_update_stream: Union[Unset, str] = UNSET,
    affects_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV2FlawsListAffectsResolution] = UNSET,
    affects_resolution_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsResolutionInItem]
    ] = UNSET,
    affects_tracker_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_embargoed: Union[Unset, bool] = UNSET,
    affects_tracker_errata_advisory_name: Union[Unset, str] = UNSET,
    affects_tracker_errata_advisory_name_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_errata_et_id: Union[Unset, int] = UNSET,
    affects_tracker_errata_shipped_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_external_system_id: Union[Unset, str] = UNSET,
    affects_tracker_external_system_id_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_ps_update_stream: Union[Unset, str] = UNSET,
    affects_tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_resolution: Union[Unset, str] = UNSET,
    affects_tracker_resolution_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_status: Union[Unset, str] = UNSET,
    affects_tracker_status_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_type: Union[Unset, OsidbApiV2FlawsListAffectsTrackerType] = UNSET,
    affects_tracker_type_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsTrackerTypeInItem]
    ] = UNSET,
    affects_tracker_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_uuid: Union[Unset, UUID] = UNSET,
    affects_tracker_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_tracker_visibility: Union[
        Unset, OsidbApiV2FlawsListAffectsTrackerVisibility
    ] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    affects_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_visibility: Union[Unset, OsidbApiV2FlawsListAffectsVisibility] = UNSET,
    bz_id: Union[Unset, float] = UNSET,
    changed_after: Union[Unset, datetime.datetime] = UNSET,
    changed_before: Union[Unset, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, str] = UNSET,
    components: Union[Unset, list[str]] = UNSET,
    components_in: Union[Unset, list[str]] = UNSET,
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
    cve_id_in: Union[Unset, list[str]] = UNSET,
    cve_id_isempty: Union[Unset, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, OsidbApiV2FlawsListCvssScoresIssuer] = UNSET,
    cvss_scores_issuer_in: Union[
        Unset, list[OsidbApiV2FlawsListCvssScoresIssuerInItem]
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
    cwe_id: Union[Unset, str] = UNSET,
    cwe_id_in: Union[Unset, list[str]] = UNSET,
    cwe_id_isempty: Union[Unset, bool] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_has_no_non_community_affects_trackers: Union[Unset, bool] = UNSET,
    flaw_labels: Union[Unset, list[str]] = UNSET,
    impact: Union[Unset, OsidbApiV2FlawsListImpact] = UNSET,
    impact_in: Union[Unset, list[OsidbApiV2FlawsListImpactInItem]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
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
    major_incident_state: Union[Unset, OsidbApiV2FlawsListMajorIncidentState] = UNSET,
    major_incident_state_in: Union[
        Unset, list[OsidbApiV2FlawsListMajorIncidentStateInItem]
    ] = UNSET,
    mitigation_isempty: Union[Unset, bool] = UNSET,
    nist_cvss_validation: Union[Unset, OsidbApiV2FlawsListNistCvssValidation] = UNSET,
    nist_cvss_validation_in: Union[
        Unset, list[OsidbApiV2FlawsListNistCvssValidationInItem]
    ] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV2FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, str] = UNSET,
    owner_in: Union[Unset, list[str]] = UNSET,
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
    references_description_in: Union[Unset, list[str]] = UNSET,
    references_type: Union[Unset, OsidbApiV2FlawsListReferencesType] = UNSET,
    references_type_in: Union[
        Unset, list[OsidbApiV2FlawsListReferencesTypeInItem]
    ] = UNSET,
    references_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_url: Union[Unset, str] = UNSET,
    references_url_in: Union[Unset, list[str]] = UNSET,
    references_uuid: Union[Unset, UUID] = UNSET,
    references_uuid_in: Union[Unset, list[UUID]] = UNSET,
    reported_dt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, OsidbApiV2FlawsListRequiresCveDescription
    ] = UNSET,
    requires_cve_description_in: Union[
        Unset, list[OsidbApiV2FlawsListRequiresCveDescriptionInItem]
    ] = UNSET,
    search: Union[Unset, str] = UNSET,
    source: Union[Unset, OsidbApiV2FlawsListSource] = UNSET,
    source_in: Union[Unset, list[OsidbApiV2FlawsListSourceInItem]] = UNSET,
    statement: Union[Unset, str] = UNSET,
    statement_isempty: Union[Unset, bool] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    team_id_in: Union[Unset, list[str]] = UNSET,
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
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    visibility: Union[Unset, OsidbApiV2FlawsListVisibility] = UNSET,
    workflow_state: Union[Unset, list[OsidbApiV2FlawsListWorkflowStateItem]] = UNSET,
    workflow_state_in: Union[
        Unset, list[OsidbApiV2FlawsListWorkflowStateInItem]
    ] = UNSET,
) -> Response[OsidbApiV2FlawsListResponse200]:
    """
    Args:
        acknowledgments_affiliation (Union[Unset, str]):
        acknowledgments_affiliation_in (Union[Unset, list[str]]):
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
        acknowledgments_name_in (Union[Unset, list[str]]):
        acknowledgments_updated_dt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_date (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_uuid (Union[Unset, UUID]):
        acknowledgments_uuid_in (Union[Unset, list[UUID]]):
        affects_affectedness (Union[Unset, OsidbApiV2FlawsListAffectsAffectedness]):
        affects_affectedness_in (Union[Unset,
            list[OsidbApiV2FlawsListAffectsAffectednessInItem]]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_impact (Union[Unset, OsidbApiV2FlawsListAffectsImpact]):
        affects_impact_in (Union[Unset, list[OsidbApiV2FlawsListAffectsImpactInItem]]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_component_in (Union[Unset, list[str]]):
        affects_ps_module (Union[Unset, str]):
        affects_ps_module_in (Union[Unset, list[str]]):
        affects_ps_update_stream (Union[Unset, str]):
        affects_ps_update_stream_in (Union[Unset, list[str]]):
        affects_resolution (Union[Unset, OsidbApiV2FlawsListAffectsResolution]):
        affects_resolution_in (Union[Unset, list[OsidbApiV2FlawsListAffectsResolutionInItem]]):
        affects_tracker_created_dt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_date (Union[Unset, datetime.date]):
        affects_tracker_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_embargoed (Union[Unset, bool]):
        affects_tracker_errata_advisory_name (Union[Unset, str]):
        affects_tracker_errata_advisory_name_in (Union[Unset, list[str]]):
        affects_tracker_errata_et_id (Union[Unset, int]):
        affects_tracker_errata_shipped_dt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_date (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_external_system_id (Union[Unset, str]):
        affects_tracker_external_system_id_in (Union[Unset, list[str]]):
        affects_tracker_ps_update_stream (Union[Unset, str]):
        affects_tracker_ps_update_stream_in (Union[Unset, list[str]]):
        affects_tracker_resolution (Union[Unset, str]):
        affects_tracker_resolution_in (Union[Unset, list[str]]):
        affects_tracker_status (Union[Unset, str]):
        affects_tracker_status_in (Union[Unset, list[str]]):
        affects_tracker_type (Union[Unset, OsidbApiV2FlawsListAffectsTrackerType]):
        affects_tracker_type_in (Union[Unset, list[OsidbApiV2FlawsListAffectsTrackerTypeInItem]]):
        affects_tracker_updated_dt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_date (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_uuid (Union[Unset, UUID]):
        affects_tracker_uuid_in (Union[Unset, list[UUID]]):
        affects_tracker_visibility (Union[Unset, OsidbApiV2FlawsListAffectsTrackerVisibility]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        affects_uuid_in (Union[Unset, list[UUID]]):
        affects_visibility (Union[Unset, OsidbApiV2FlawsListAffectsVisibility]):
        bz_id (Union[Unset, float]):
        changed_after (Union[Unset, datetime.datetime]):
        changed_before (Union[Unset, datetime.datetime]):
        comment_zero (Union[Unset, str]):
        components (Union[Unset, list[str]]):
        components_in (Union[Unset, list[str]]):
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
        cve_id_in (Union[Unset, list[str]]):
        cve_id_isempty (Union[Unset, bool]):
        cvss2_nist_isempty (Union[Unset, bool]):
        cvss2_rh_isempty (Union[Unset, bool]):
        cvss3_nist_isempty (Union[Unset, bool]):
        cvss3_rh_isempty (Union[Unset, bool]):
        cvss4_nist_isempty (Union[Unset, bool]):
        cvss4_rh_isempty (Union[Unset, bool]):
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
        cvss_scores_issuer (Union[Unset, OsidbApiV2FlawsListCvssScoresIssuer]):
        cvss_scores_issuer_in (Union[Unset, list[OsidbApiV2FlawsListCvssScoresIssuerInItem]]):
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
        cwe_id (Union[Unset, str]):
        cwe_id_in (Union[Unset, list[str]]):
        cwe_id_isempty (Union[Unset, bool]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_has_no_non_community_affects_trackers (Union[Unset, bool]):
        flaw_labels (Union[Unset, list[str]]):
        impact (Union[Unset, OsidbApiV2FlawsListImpact]):
        impact_in (Union[Unset, list[OsidbApiV2FlawsListImpactInItem]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
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
        major_incident_state (Union[Unset, OsidbApiV2FlawsListMajorIncidentState]):
        major_incident_state_in (Union[Unset, list[OsidbApiV2FlawsListMajorIncidentStateInItem]]):
        mitigation_isempty (Union[Unset, bool]):
        nist_cvss_validation (Union[Unset, OsidbApiV2FlawsListNistCvssValidation]):
        nist_cvss_validation_in (Union[Unset, list[OsidbApiV2FlawsListNistCvssValidationInItem]]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV2FlawsListOrderItem]]):
        owner (Union[Unset, str]):
        owner_in (Union[Unset, list[str]]):
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
        references_description_in (Union[Unset, list[str]]):
        references_type (Union[Unset, OsidbApiV2FlawsListReferencesType]):
        references_type_in (Union[Unset, list[OsidbApiV2FlawsListReferencesTypeInItem]]):
        references_updated_dt (Union[Unset, datetime.datetime]):
        references_updated_dt_date (Union[Unset, datetime.date]):
        references_updated_dt_date_gte (Union[Unset, datetime.date]):
        references_updated_dt_date_lte (Union[Unset, datetime.date]):
        references_updated_dt_gt (Union[Unset, datetime.datetime]):
        references_updated_dt_gte (Union[Unset, datetime.datetime]):
        references_updated_dt_lt (Union[Unset, datetime.datetime]):
        references_updated_dt_lte (Union[Unset, datetime.datetime]):
        references_url (Union[Unset, str]):
        references_url_in (Union[Unset, list[str]]):
        references_uuid (Union[Unset, UUID]):
        references_uuid_in (Union[Unset, list[UUID]]):
        reported_dt (Union[Unset, datetime.datetime]):
        reported_dt_date (Union[Unset, datetime.date]):
        reported_dt_date_gte (Union[Unset, datetime.date]):
        reported_dt_date_lte (Union[Unset, datetime.date]):
        reported_dt_gt (Union[Unset, datetime.datetime]):
        reported_dt_gte (Union[Unset, datetime.datetime]):
        reported_dt_lt (Union[Unset, datetime.datetime]):
        reported_dt_lte (Union[Unset, datetime.datetime]):
        requires_cve_description (Union[Unset, OsidbApiV2FlawsListRequiresCveDescription]):
        requires_cve_description_in (Union[Unset,
            list[OsidbApiV2FlawsListRequiresCveDescriptionInItem]]):
        search (Union[Unset, str]):
        source (Union[Unset, OsidbApiV2FlawsListSource]):
        source_in (Union[Unset, list[OsidbApiV2FlawsListSourceInItem]]):
        statement (Union[Unset, str]):
        statement_isempty (Union[Unset, bool]):
        team_id (Union[Unset, str]):
        team_id_in (Union[Unset, list[str]]):
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
        uuid_in (Union[Unset, list[UUID]]):
        visibility (Union[Unset, OsidbApiV2FlawsListVisibility]):
        workflow_state (Union[Unset, list[OsidbApiV2FlawsListWorkflowStateItem]]):
        workflow_state_in (Union[Unset, list[OsidbApiV2FlawsListWorkflowStateInItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2FlawsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        acknowledgments_affiliation=acknowledgments_affiliation,
        acknowledgments_affiliation_in=acknowledgments_affiliation_in,
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
        acknowledgments_name_in=acknowledgments_name_in,
        acknowledgments_updated_dt=acknowledgments_updated_dt,
        acknowledgments_updated_dt_date=acknowledgments_updated_dt_date,
        acknowledgments_updated_dt_date_gte=acknowledgments_updated_dt_date_gte,
        acknowledgments_updated_dt_date_lte=acknowledgments_updated_dt_date_lte,
        acknowledgments_updated_dt_gt=acknowledgments_updated_dt_gt,
        acknowledgments_updated_dt_gte=acknowledgments_updated_dt_gte,
        acknowledgments_updated_dt_lt=acknowledgments_updated_dt_lt,
        acknowledgments_updated_dt_lte=acknowledgments_updated_dt_lte,
        acknowledgments_uuid=acknowledgments_uuid,
        acknowledgments_uuid_in=acknowledgments_uuid_in,
        affects_affectedness=affects_affectedness,
        affects_affectedness_in=affects_affectedness_in,
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
        affects_impact_in=affects_impact_in,
        affects_ps_component=affects_ps_component,
        affects_ps_component_in=affects_ps_component_in,
        affects_ps_module=affects_ps_module,
        affects_ps_module_in=affects_ps_module_in,
        affects_ps_update_stream=affects_ps_update_stream,
        affects_ps_update_stream_in=affects_ps_update_stream_in,
        affects_resolution=affects_resolution,
        affects_resolution_in=affects_resolution_in,
        affects_tracker_created_dt=affects_tracker_created_dt,
        affects_tracker_created_dt_date=affects_tracker_created_dt_date,
        affects_tracker_created_dt_date_gte=affects_tracker_created_dt_date_gte,
        affects_tracker_created_dt_date_lte=affects_tracker_created_dt_date_lte,
        affects_tracker_created_dt_gt=affects_tracker_created_dt_gt,
        affects_tracker_created_dt_gte=affects_tracker_created_dt_gte,
        affects_tracker_created_dt_lt=affects_tracker_created_dt_lt,
        affects_tracker_created_dt_lte=affects_tracker_created_dt_lte,
        affects_tracker_embargoed=affects_tracker_embargoed,
        affects_tracker_errata_advisory_name=affects_tracker_errata_advisory_name,
        affects_tracker_errata_advisory_name_in=affects_tracker_errata_advisory_name_in,
        affects_tracker_errata_et_id=affects_tracker_errata_et_id,
        affects_tracker_errata_shipped_dt=affects_tracker_errata_shipped_dt,
        affects_tracker_errata_shipped_dt_date=affects_tracker_errata_shipped_dt_date,
        affects_tracker_errata_shipped_dt_date_gte=affects_tracker_errata_shipped_dt_date_gte,
        affects_tracker_errata_shipped_dt_date_lte=affects_tracker_errata_shipped_dt_date_lte,
        affects_tracker_errata_shipped_dt_gt=affects_tracker_errata_shipped_dt_gt,
        affects_tracker_errata_shipped_dt_gte=affects_tracker_errata_shipped_dt_gte,
        affects_tracker_errata_shipped_dt_lt=affects_tracker_errata_shipped_dt_lt,
        affects_tracker_errata_shipped_dt_lte=affects_tracker_errata_shipped_dt_lte,
        affects_tracker_external_system_id=affects_tracker_external_system_id,
        affects_tracker_external_system_id_in=affects_tracker_external_system_id_in,
        affects_tracker_ps_update_stream=affects_tracker_ps_update_stream,
        affects_tracker_ps_update_stream_in=affects_tracker_ps_update_stream_in,
        affects_tracker_resolution=affects_tracker_resolution,
        affects_tracker_resolution_in=affects_tracker_resolution_in,
        affects_tracker_status=affects_tracker_status,
        affects_tracker_status_in=affects_tracker_status_in,
        affects_tracker_type=affects_tracker_type,
        affects_tracker_type_in=affects_tracker_type_in,
        affects_tracker_updated_dt=affects_tracker_updated_dt,
        affects_tracker_updated_dt_date=affects_tracker_updated_dt_date,
        affects_tracker_updated_dt_date_gte=affects_tracker_updated_dt_date_gte,
        affects_tracker_updated_dt_date_lte=affects_tracker_updated_dt_date_lte,
        affects_tracker_updated_dt_gt=affects_tracker_updated_dt_gt,
        affects_tracker_updated_dt_gte=affects_tracker_updated_dt_gte,
        affects_tracker_updated_dt_lt=affects_tracker_updated_dt_lt,
        affects_tracker_updated_dt_lte=affects_tracker_updated_dt_lte,
        affects_tracker_uuid=affects_tracker_uuid,
        affects_tracker_uuid_in=affects_tracker_uuid_in,
        affects_tracker_visibility=affects_tracker_visibility,
        affects_updated_dt=affects_updated_dt,
        affects_updated_dt_date=affects_updated_dt_date,
        affects_updated_dt_date_gte=affects_updated_dt_date_gte,
        affects_updated_dt_date_lte=affects_updated_dt_date_lte,
        affects_updated_dt_gt=affects_updated_dt_gt,
        affects_updated_dt_gte=affects_updated_dt_gte,
        affects_updated_dt_lt=affects_updated_dt_lt,
        affects_updated_dt_lte=affects_updated_dt_lte,
        affects_uuid=affects_uuid,
        affects_uuid_in=affects_uuid_in,
        affects_visibility=affects_visibility,
        bz_id=bz_id,
        changed_after=changed_after,
        changed_before=changed_before,
        comment_zero=comment_zero,
        components=components,
        components_in=components_in,
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
        cve_id_in=cve_id_in,
        cve_id_isempty=cve_id_isempty,
        cvss2_nist_isempty=cvss2_nist_isempty,
        cvss2_rh_isempty=cvss2_rh_isempty,
        cvss3_nist_isempty=cvss3_nist_isempty,
        cvss3_rh_isempty=cvss3_rh_isempty,
        cvss4_nist_isempty=cvss4_nist_isempty,
        cvss4_rh_isempty=cvss4_rh_isempty,
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
        cwe_id=cwe_id,
        cwe_id_in=cwe_id_in,
        cwe_id_isempty=cwe_id_isempty,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        flaw_has_no_non_community_affects_trackers=flaw_has_no_non_community_affects_trackers,
        flaw_labels=flaw_labels,
        impact=impact,
        impact_in=impact_in,
        include_fields=include_fields,
        include_history=include_history,
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
        major_incident_state_in=major_incident_state_in,
        mitigation_isempty=mitigation_isempty,
        nist_cvss_validation=nist_cvss_validation,
        nist_cvss_validation_in=nist_cvss_validation_in,
        offset=offset,
        order=order,
        owner=owner,
        owner_in=owner_in,
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
        references_description_in=references_description_in,
        references_type=references_type,
        references_type_in=references_type_in,
        references_updated_dt=references_updated_dt,
        references_updated_dt_date=references_updated_dt_date,
        references_updated_dt_date_gte=references_updated_dt_date_gte,
        references_updated_dt_date_lte=references_updated_dt_date_lte,
        references_updated_dt_gt=references_updated_dt_gt,
        references_updated_dt_gte=references_updated_dt_gte,
        references_updated_dt_lt=references_updated_dt_lt,
        references_updated_dt_lte=references_updated_dt_lte,
        references_url=references_url,
        references_url_in=references_url_in,
        references_uuid=references_uuid,
        references_uuid_in=references_uuid_in,
        reported_dt=reported_dt,
        reported_dt_date=reported_dt_date,
        reported_dt_date_gte=reported_dt_date_gte,
        reported_dt_date_lte=reported_dt_date_lte,
        reported_dt_gt=reported_dt_gt,
        reported_dt_gte=reported_dt_gte,
        reported_dt_lt=reported_dt_lt,
        reported_dt_lte=reported_dt_lte,
        requires_cve_description=requires_cve_description,
        requires_cve_description_in=requires_cve_description_in,
        search=search,
        source=source,
        source_in=source_in,
        statement=statement,
        statement_isempty=statement_isempty,
        team_id=team_id,
        team_id_in=team_id_in,
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
        uuid_in=uuid_in,
        visibility=visibility,
        workflow_state=workflow_state,
        workflow_state_in=workflow_state_in,
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
    acknowledgments_affiliation_in: Union[Unset, list[str]] = UNSET,
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
    acknowledgments_name_in: Union[Unset, list[str]] = UNSET,
    acknowledgments_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, UUID] = UNSET,
    acknowledgments_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_affectedness: Union[Unset, OsidbApiV2FlawsListAffectsAffectedness] = UNSET,
    affects_affectedness_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsAffectednessInItem]
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
    affects_impact: Union[Unset, OsidbApiV2FlawsListAffectsImpact] = UNSET,
    affects_impact_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsImpactInItem]
    ] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_component_in: Union[Unset, list[str]] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_ps_module_in: Union[Unset, list[str]] = UNSET,
    affects_ps_update_stream: Union[Unset, str] = UNSET,
    affects_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV2FlawsListAffectsResolution] = UNSET,
    affects_resolution_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsResolutionInItem]
    ] = UNSET,
    affects_tracker_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_embargoed: Union[Unset, bool] = UNSET,
    affects_tracker_errata_advisory_name: Union[Unset, str] = UNSET,
    affects_tracker_errata_advisory_name_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_errata_et_id: Union[Unset, int] = UNSET,
    affects_tracker_errata_shipped_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_external_system_id: Union[Unset, str] = UNSET,
    affects_tracker_external_system_id_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_ps_update_stream: Union[Unset, str] = UNSET,
    affects_tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_resolution: Union[Unset, str] = UNSET,
    affects_tracker_resolution_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_status: Union[Unset, str] = UNSET,
    affects_tracker_status_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_type: Union[Unset, OsidbApiV2FlawsListAffectsTrackerType] = UNSET,
    affects_tracker_type_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsTrackerTypeInItem]
    ] = UNSET,
    affects_tracker_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_uuid: Union[Unset, UUID] = UNSET,
    affects_tracker_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_tracker_visibility: Union[
        Unset, OsidbApiV2FlawsListAffectsTrackerVisibility
    ] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    affects_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_visibility: Union[Unset, OsidbApiV2FlawsListAffectsVisibility] = UNSET,
    bz_id: Union[Unset, float] = UNSET,
    changed_after: Union[Unset, datetime.datetime] = UNSET,
    changed_before: Union[Unset, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, str] = UNSET,
    components: Union[Unset, list[str]] = UNSET,
    components_in: Union[Unset, list[str]] = UNSET,
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
    cve_id_in: Union[Unset, list[str]] = UNSET,
    cve_id_isempty: Union[Unset, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, OsidbApiV2FlawsListCvssScoresIssuer] = UNSET,
    cvss_scores_issuer_in: Union[
        Unset, list[OsidbApiV2FlawsListCvssScoresIssuerInItem]
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
    cwe_id: Union[Unset, str] = UNSET,
    cwe_id_in: Union[Unset, list[str]] = UNSET,
    cwe_id_isempty: Union[Unset, bool] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_has_no_non_community_affects_trackers: Union[Unset, bool] = UNSET,
    flaw_labels: Union[Unset, list[str]] = UNSET,
    impact: Union[Unset, OsidbApiV2FlawsListImpact] = UNSET,
    impact_in: Union[Unset, list[OsidbApiV2FlawsListImpactInItem]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
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
    major_incident_state: Union[Unset, OsidbApiV2FlawsListMajorIncidentState] = UNSET,
    major_incident_state_in: Union[
        Unset, list[OsidbApiV2FlawsListMajorIncidentStateInItem]
    ] = UNSET,
    mitigation_isempty: Union[Unset, bool] = UNSET,
    nist_cvss_validation: Union[Unset, OsidbApiV2FlawsListNistCvssValidation] = UNSET,
    nist_cvss_validation_in: Union[
        Unset, list[OsidbApiV2FlawsListNistCvssValidationInItem]
    ] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV2FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, str] = UNSET,
    owner_in: Union[Unset, list[str]] = UNSET,
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
    references_description_in: Union[Unset, list[str]] = UNSET,
    references_type: Union[Unset, OsidbApiV2FlawsListReferencesType] = UNSET,
    references_type_in: Union[
        Unset, list[OsidbApiV2FlawsListReferencesTypeInItem]
    ] = UNSET,
    references_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_url: Union[Unset, str] = UNSET,
    references_url_in: Union[Unset, list[str]] = UNSET,
    references_uuid: Union[Unset, UUID] = UNSET,
    references_uuid_in: Union[Unset, list[UUID]] = UNSET,
    reported_dt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, OsidbApiV2FlawsListRequiresCveDescription
    ] = UNSET,
    requires_cve_description_in: Union[
        Unset, list[OsidbApiV2FlawsListRequiresCveDescriptionInItem]
    ] = UNSET,
    search: Union[Unset, str] = UNSET,
    source: Union[Unset, OsidbApiV2FlawsListSource] = UNSET,
    source_in: Union[Unset, list[OsidbApiV2FlawsListSourceInItem]] = UNSET,
    statement: Union[Unset, str] = UNSET,
    statement_isempty: Union[Unset, bool] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    team_id_in: Union[Unset, list[str]] = UNSET,
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
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    visibility: Union[Unset, OsidbApiV2FlawsListVisibility] = UNSET,
    workflow_state: Union[Unset, list[OsidbApiV2FlawsListWorkflowStateItem]] = UNSET,
    workflow_state_in: Union[
        Unset, list[OsidbApiV2FlawsListWorkflowStateInItem]
    ] = UNSET,
) -> Optional[OsidbApiV2FlawsListResponse200]:
    """
    Args:
        acknowledgments_affiliation (Union[Unset, str]):
        acknowledgments_affiliation_in (Union[Unset, list[str]]):
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
        acknowledgments_name_in (Union[Unset, list[str]]):
        acknowledgments_updated_dt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_date (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_uuid (Union[Unset, UUID]):
        acknowledgments_uuid_in (Union[Unset, list[UUID]]):
        affects_affectedness (Union[Unset, OsidbApiV2FlawsListAffectsAffectedness]):
        affects_affectedness_in (Union[Unset,
            list[OsidbApiV2FlawsListAffectsAffectednessInItem]]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_impact (Union[Unset, OsidbApiV2FlawsListAffectsImpact]):
        affects_impact_in (Union[Unset, list[OsidbApiV2FlawsListAffectsImpactInItem]]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_component_in (Union[Unset, list[str]]):
        affects_ps_module (Union[Unset, str]):
        affects_ps_module_in (Union[Unset, list[str]]):
        affects_ps_update_stream (Union[Unset, str]):
        affects_ps_update_stream_in (Union[Unset, list[str]]):
        affects_resolution (Union[Unset, OsidbApiV2FlawsListAffectsResolution]):
        affects_resolution_in (Union[Unset, list[OsidbApiV2FlawsListAffectsResolutionInItem]]):
        affects_tracker_created_dt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_date (Union[Unset, datetime.date]):
        affects_tracker_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_embargoed (Union[Unset, bool]):
        affects_tracker_errata_advisory_name (Union[Unset, str]):
        affects_tracker_errata_advisory_name_in (Union[Unset, list[str]]):
        affects_tracker_errata_et_id (Union[Unset, int]):
        affects_tracker_errata_shipped_dt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_date (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_external_system_id (Union[Unset, str]):
        affects_tracker_external_system_id_in (Union[Unset, list[str]]):
        affects_tracker_ps_update_stream (Union[Unset, str]):
        affects_tracker_ps_update_stream_in (Union[Unset, list[str]]):
        affects_tracker_resolution (Union[Unset, str]):
        affects_tracker_resolution_in (Union[Unset, list[str]]):
        affects_tracker_status (Union[Unset, str]):
        affects_tracker_status_in (Union[Unset, list[str]]):
        affects_tracker_type (Union[Unset, OsidbApiV2FlawsListAffectsTrackerType]):
        affects_tracker_type_in (Union[Unset, list[OsidbApiV2FlawsListAffectsTrackerTypeInItem]]):
        affects_tracker_updated_dt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_date (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_uuid (Union[Unset, UUID]):
        affects_tracker_uuid_in (Union[Unset, list[UUID]]):
        affects_tracker_visibility (Union[Unset, OsidbApiV2FlawsListAffectsTrackerVisibility]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        affects_uuid_in (Union[Unset, list[UUID]]):
        affects_visibility (Union[Unset, OsidbApiV2FlawsListAffectsVisibility]):
        bz_id (Union[Unset, float]):
        changed_after (Union[Unset, datetime.datetime]):
        changed_before (Union[Unset, datetime.datetime]):
        comment_zero (Union[Unset, str]):
        components (Union[Unset, list[str]]):
        components_in (Union[Unset, list[str]]):
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
        cve_id_in (Union[Unset, list[str]]):
        cve_id_isempty (Union[Unset, bool]):
        cvss2_nist_isempty (Union[Unset, bool]):
        cvss2_rh_isempty (Union[Unset, bool]):
        cvss3_nist_isempty (Union[Unset, bool]):
        cvss3_rh_isempty (Union[Unset, bool]):
        cvss4_nist_isempty (Union[Unset, bool]):
        cvss4_rh_isempty (Union[Unset, bool]):
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
        cvss_scores_issuer (Union[Unset, OsidbApiV2FlawsListCvssScoresIssuer]):
        cvss_scores_issuer_in (Union[Unset, list[OsidbApiV2FlawsListCvssScoresIssuerInItem]]):
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
        cwe_id (Union[Unset, str]):
        cwe_id_in (Union[Unset, list[str]]):
        cwe_id_isempty (Union[Unset, bool]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_has_no_non_community_affects_trackers (Union[Unset, bool]):
        flaw_labels (Union[Unset, list[str]]):
        impact (Union[Unset, OsidbApiV2FlawsListImpact]):
        impact_in (Union[Unset, list[OsidbApiV2FlawsListImpactInItem]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
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
        major_incident_state (Union[Unset, OsidbApiV2FlawsListMajorIncidentState]):
        major_incident_state_in (Union[Unset, list[OsidbApiV2FlawsListMajorIncidentStateInItem]]):
        mitigation_isempty (Union[Unset, bool]):
        nist_cvss_validation (Union[Unset, OsidbApiV2FlawsListNistCvssValidation]):
        nist_cvss_validation_in (Union[Unset, list[OsidbApiV2FlawsListNistCvssValidationInItem]]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV2FlawsListOrderItem]]):
        owner (Union[Unset, str]):
        owner_in (Union[Unset, list[str]]):
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
        references_description_in (Union[Unset, list[str]]):
        references_type (Union[Unset, OsidbApiV2FlawsListReferencesType]):
        references_type_in (Union[Unset, list[OsidbApiV2FlawsListReferencesTypeInItem]]):
        references_updated_dt (Union[Unset, datetime.datetime]):
        references_updated_dt_date (Union[Unset, datetime.date]):
        references_updated_dt_date_gte (Union[Unset, datetime.date]):
        references_updated_dt_date_lte (Union[Unset, datetime.date]):
        references_updated_dt_gt (Union[Unset, datetime.datetime]):
        references_updated_dt_gte (Union[Unset, datetime.datetime]):
        references_updated_dt_lt (Union[Unset, datetime.datetime]):
        references_updated_dt_lte (Union[Unset, datetime.datetime]):
        references_url (Union[Unset, str]):
        references_url_in (Union[Unset, list[str]]):
        references_uuid (Union[Unset, UUID]):
        references_uuid_in (Union[Unset, list[UUID]]):
        reported_dt (Union[Unset, datetime.datetime]):
        reported_dt_date (Union[Unset, datetime.date]):
        reported_dt_date_gte (Union[Unset, datetime.date]):
        reported_dt_date_lte (Union[Unset, datetime.date]):
        reported_dt_gt (Union[Unset, datetime.datetime]):
        reported_dt_gte (Union[Unset, datetime.datetime]):
        reported_dt_lt (Union[Unset, datetime.datetime]):
        reported_dt_lte (Union[Unset, datetime.datetime]):
        requires_cve_description (Union[Unset, OsidbApiV2FlawsListRequiresCveDescription]):
        requires_cve_description_in (Union[Unset,
            list[OsidbApiV2FlawsListRequiresCveDescriptionInItem]]):
        search (Union[Unset, str]):
        source (Union[Unset, OsidbApiV2FlawsListSource]):
        source_in (Union[Unset, list[OsidbApiV2FlawsListSourceInItem]]):
        statement (Union[Unset, str]):
        statement_isempty (Union[Unset, bool]):
        team_id (Union[Unset, str]):
        team_id_in (Union[Unset, list[str]]):
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
        uuid_in (Union[Unset, list[UUID]]):
        visibility (Union[Unset, OsidbApiV2FlawsListVisibility]):
        workflow_state (Union[Unset, list[OsidbApiV2FlawsListWorkflowStateItem]]):
        workflow_state_in (Union[Unset, list[OsidbApiV2FlawsListWorkflowStateInItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2FlawsListResponse200
    """

    return sync_detailed(
        client=client,
        acknowledgments_affiliation=acknowledgments_affiliation,
        acknowledgments_affiliation_in=acknowledgments_affiliation_in,
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
        acknowledgments_name_in=acknowledgments_name_in,
        acknowledgments_updated_dt=acknowledgments_updated_dt,
        acknowledgments_updated_dt_date=acknowledgments_updated_dt_date,
        acknowledgments_updated_dt_date_gte=acknowledgments_updated_dt_date_gte,
        acknowledgments_updated_dt_date_lte=acknowledgments_updated_dt_date_lte,
        acknowledgments_updated_dt_gt=acknowledgments_updated_dt_gt,
        acknowledgments_updated_dt_gte=acknowledgments_updated_dt_gte,
        acknowledgments_updated_dt_lt=acknowledgments_updated_dt_lt,
        acknowledgments_updated_dt_lte=acknowledgments_updated_dt_lte,
        acknowledgments_uuid=acknowledgments_uuid,
        acknowledgments_uuid_in=acknowledgments_uuid_in,
        affects_affectedness=affects_affectedness,
        affects_affectedness_in=affects_affectedness_in,
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
        affects_impact_in=affects_impact_in,
        affects_ps_component=affects_ps_component,
        affects_ps_component_in=affects_ps_component_in,
        affects_ps_module=affects_ps_module,
        affects_ps_module_in=affects_ps_module_in,
        affects_ps_update_stream=affects_ps_update_stream,
        affects_ps_update_stream_in=affects_ps_update_stream_in,
        affects_resolution=affects_resolution,
        affects_resolution_in=affects_resolution_in,
        affects_tracker_created_dt=affects_tracker_created_dt,
        affects_tracker_created_dt_date=affects_tracker_created_dt_date,
        affects_tracker_created_dt_date_gte=affects_tracker_created_dt_date_gte,
        affects_tracker_created_dt_date_lte=affects_tracker_created_dt_date_lte,
        affects_tracker_created_dt_gt=affects_tracker_created_dt_gt,
        affects_tracker_created_dt_gte=affects_tracker_created_dt_gte,
        affects_tracker_created_dt_lt=affects_tracker_created_dt_lt,
        affects_tracker_created_dt_lte=affects_tracker_created_dt_lte,
        affects_tracker_embargoed=affects_tracker_embargoed,
        affects_tracker_errata_advisory_name=affects_tracker_errata_advisory_name,
        affects_tracker_errata_advisory_name_in=affects_tracker_errata_advisory_name_in,
        affects_tracker_errata_et_id=affects_tracker_errata_et_id,
        affects_tracker_errata_shipped_dt=affects_tracker_errata_shipped_dt,
        affects_tracker_errata_shipped_dt_date=affects_tracker_errata_shipped_dt_date,
        affects_tracker_errata_shipped_dt_date_gte=affects_tracker_errata_shipped_dt_date_gte,
        affects_tracker_errata_shipped_dt_date_lte=affects_tracker_errata_shipped_dt_date_lte,
        affects_tracker_errata_shipped_dt_gt=affects_tracker_errata_shipped_dt_gt,
        affects_tracker_errata_shipped_dt_gte=affects_tracker_errata_shipped_dt_gte,
        affects_tracker_errata_shipped_dt_lt=affects_tracker_errata_shipped_dt_lt,
        affects_tracker_errata_shipped_dt_lte=affects_tracker_errata_shipped_dt_lte,
        affects_tracker_external_system_id=affects_tracker_external_system_id,
        affects_tracker_external_system_id_in=affects_tracker_external_system_id_in,
        affects_tracker_ps_update_stream=affects_tracker_ps_update_stream,
        affects_tracker_ps_update_stream_in=affects_tracker_ps_update_stream_in,
        affects_tracker_resolution=affects_tracker_resolution,
        affects_tracker_resolution_in=affects_tracker_resolution_in,
        affects_tracker_status=affects_tracker_status,
        affects_tracker_status_in=affects_tracker_status_in,
        affects_tracker_type=affects_tracker_type,
        affects_tracker_type_in=affects_tracker_type_in,
        affects_tracker_updated_dt=affects_tracker_updated_dt,
        affects_tracker_updated_dt_date=affects_tracker_updated_dt_date,
        affects_tracker_updated_dt_date_gte=affects_tracker_updated_dt_date_gte,
        affects_tracker_updated_dt_date_lte=affects_tracker_updated_dt_date_lte,
        affects_tracker_updated_dt_gt=affects_tracker_updated_dt_gt,
        affects_tracker_updated_dt_gte=affects_tracker_updated_dt_gte,
        affects_tracker_updated_dt_lt=affects_tracker_updated_dt_lt,
        affects_tracker_updated_dt_lte=affects_tracker_updated_dt_lte,
        affects_tracker_uuid=affects_tracker_uuid,
        affects_tracker_uuid_in=affects_tracker_uuid_in,
        affects_tracker_visibility=affects_tracker_visibility,
        affects_updated_dt=affects_updated_dt,
        affects_updated_dt_date=affects_updated_dt_date,
        affects_updated_dt_date_gte=affects_updated_dt_date_gte,
        affects_updated_dt_date_lte=affects_updated_dt_date_lte,
        affects_updated_dt_gt=affects_updated_dt_gt,
        affects_updated_dt_gte=affects_updated_dt_gte,
        affects_updated_dt_lt=affects_updated_dt_lt,
        affects_updated_dt_lte=affects_updated_dt_lte,
        affects_uuid=affects_uuid,
        affects_uuid_in=affects_uuid_in,
        affects_visibility=affects_visibility,
        bz_id=bz_id,
        changed_after=changed_after,
        changed_before=changed_before,
        comment_zero=comment_zero,
        components=components,
        components_in=components_in,
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
        cve_id_in=cve_id_in,
        cve_id_isempty=cve_id_isempty,
        cvss2_nist_isempty=cvss2_nist_isempty,
        cvss2_rh_isempty=cvss2_rh_isempty,
        cvss3_nist_isempty=cvss3_nist_isempty,
        cvss3_rh_isempty=cvss3_rh_isempty,
        cvss4_nist_isempty=cvss4_nist_isempty,
        cvss4_rh_isempty=cvss4_rh_isempty,
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
        cwe_id=cwe_id,
        cwe_id_in=cwe_id_in,
        cwe_id_isempty=cwe_id_isempty,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        flaw_has_no_non_community_affects_trackers=flaw_has_no_non_community_affects_trackers,
        flaw_labels=flaw_labels,
        impact=impact,
        impact_in=impact_in,
        include_fields=include_fields,
        include_history=include_history,
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
        major_incident_state_in=major_incident_state_in,
        mitigation_isempty=mitigation_isempty,
        nist_cvss_validation=nist_cvss_validation,
        nist_cvss_validation_in=nist_cvss_validation_in,
        offset=offset,
        order=order,
        owner=owner,
        owner_in=owner_in,
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
        references_description_in=references_description_in,
        references_type=references_type,
        references_type_in=references_type_in,
        references_updated_dt=references_updated_dt,
        references_updated_dt_date=references_updated_dt_date,
        references_updated_dt_date_gte=references_updated_dt_date_gte,
        references_updated_dt_date_lte=references_updated_dt_date_lte,
        references_updated_dt_gt=references_updated_dt_gt,
        references_updated_dt_gte=references_updated_dt_gte,
        references_updated_dt_lt=references_updated_dt_lt,
        references_updated_dt_lte=references_updated_dt_lte,
        references_url=references_url,
        references_url_in=references_url_in,
        references_uuid=references_uuid,
        references_uuid_in=references_uuid_in,
        reported_dt=reported_dt,
        reported_dt_date=reported_dt_date,
        reported_dt_date_gte=reported_dt_date_gte,
        reported_dt_date_lte=reported_dt_date_lte,
        reported_dt_gt=reported_dt_gt,
        reported_dt_gte=reported_dt_gte,
        reported_dt_lt=reported_dt_lt,
        reported_dt_lte=reported_dt_lte,
        requires_cve_description=requires_cve_description,
        requires_cve_description_in=requires_cve_description_in,
        search=search,
        source=source,
        source_in=source_in,
        statement=statement,
        statement_isempty=statement_isempty,
        team_id=team_id,
        team_id_in=team_id_in,
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
        uuid_in=uuid_in,
        visibility=visibility,
        workflow_state=workflow_state,
        workflow_state_in=workflow_state_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    acknowledgments_affiliation: Union[Unset, str] = UNSET,
    acknowledgments_affiliation_in: Union[Unset, list[str]] = UNSET,
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
    acknowledgments_name_in: Union[Unset, list[str]] = UNSET,
    acknowledgments_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, UUID] = UNSET,
    acknowledgments_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_affectedness: Union[Unset, OsidbApiV2FlawsListAffectsAffectedness] = UNSET,
    affects_affectedness_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsAffectednessInItem]
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
    affects_impact: Union[Unset, OsidbApiV2FlawsListAffectsImpact] = UNSET,
    affects_impact_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsImpactInItem]
    ] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_component_in: Union[Unset, list[str]] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_ps_module_in: Union[Unset, list[str]] = UNSET,
    affects_ps_update_stream: Union[Unset, str] = UNSET,
    affects_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV2FlawsListAffectsResolution] = UNSET,
    affects_resolution_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsResolutionInItem]
    ] = UNSET,
    affects_tracker_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_embargoed: Union[Unset, bool] = UNSET,
    affects_tracker_errata_advisory_name: Union[Unset, str] = UNSET,
    affects_tracker_errata_advisory_name_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_errata_et_id: Union[Unset, int] = UNSET,
    affects_tracker_errata_shipped_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_external_system_id: Union[Unset, str] = UNSET,
    affects_tracker_external_system_id_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_ps_update_stream: Union[Unset, str] = UNSET,
    affects_tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_resolution: Union[Unset, str] = UNSET,
    affects_tracker_resolution_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_status: Union[Unset, str] = UNSET,
    affects_tracker_status_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_type: Union[Unset, OsidbApiV2FlawsListAffectsTrackerType] = UNSET,
    affects_tracker_type_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsTrackerTypeInItem]
    ] = UNSET,
    affects_tracker_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_uuid: Union[Unset, UUID] = UNSET,
    affects_tracker_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_tracker_visibility: Union[
        Unset, OsidbApiV2FlawsListAffectsTrackerVisibility
    ] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    affects_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_visibility: Union[Unset, OsidbApiV2FlawsListAffectsVisibility] = UNSET,
    bz_id: Union[Unset, float] = UNSET,
    changed_after: Union[Unset, datetime.datetime] = UNSET,
    changed_before: Union[Unset, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, str] = UNSET,
    components: Union[Unset, list[str]] = UNSET,
    components_in: Union[Unset, list[str]] = UNSET,
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
    cve_id_in: Union[Unset, list[str]] = UNSET,
    cve_id_isempty: Union[Unset, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, OsidbApiV2FlawsListCvssScoresIssuer] = UNSET,
    cvss_scores_issuer_in: Union[
        Unset, list[OsidbApiV2FlawsListCvssScoresIssuerInItem]
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
    cwe_id: Union[Unset, str] = UNSET,
    cwe_id_in: Union[Unset, list[str]] = UNSET,
    cwe_id_isempty: Union[Unset, bool] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_has_no_non_community_affects_trackers: Union[Unset, bool] = UNSET,
    flaw_labels: Union[Unset, list[str]] = UNSET,
    impact: Union[Unset, OsidbApiV2FlawsListImpact] = UNSET,
    impact_in: Union[Unset, list[OsidbApiV2FlawsListImpactInItem]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
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
    major_incident_state: Union[Unset, OsidbApiV2FlawsListMajorIncidentState] = UNSET,
    major_incident_state_in: Union[
        Unset, list[OsidbApiV2FlawsListMajorIncidentStateInItem]
    ] = UNSET,
    mitigation_isempty: Union[Unset, bool] = UNSET,
    nist_cvss_validation: Union[Unset, OsidbApiV2FlawsListNistCvssValidation] = UNSET,
    nist_cvss_validation_in: Union[
        Unset, list[OsidbApiV2FlawsListNistCvssValidationInItem]
    ] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV2FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, str] = UNSET,
    owner_in: Union[Unset, list[str]] = UNSET,
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
    references_description_in: Union[Unset, list[str]] = UNSET,
    references_type: Union[Unset, OsidbApiV2FlawsListReferencesType] = UNSET,
    references_type_in: Union[
        Unset, list[OsidbApiV2FlawsListReferencesTypeInItem]
    ] = UNSET,
    references_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_url: Union[Unset, str] = UNSET,
    references_url_in: Union[Unset, list[str]] = UNSET,
    references_uuid: Union[Unset, UUID] = UNSET,
    references_uuid_in: Union[Unset, list[UUID]] = UNSET,
    reported_dt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, OsidbApiV2FlawsListRequiresCveDescription
    ] = UNSET,
    requires_cve_description_in: Union[
        Unset, list[OsidbApiV2FlawsListRequiresCveDescriptionInItem]
    ] = UNSET,
    search: Union[Unset, str] = UNSET,
    source: Union[Unset, OsidbApiV2FlawsListSource] = UNSET,
    source_in: Union[Unset, list[OsidbApiV2FlawsListSourceInItem]] = UNSET,
    statement: Union[Unset, str] = UNSET,
    statement_isempty: Union[Unset, bool] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    team_id_in: Union[Unset, list[str]] = UNSET,
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
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    visibility: Union[Unset, OsidbApiV2FlawsListVisibility] = UNSET,
    workflow_state: Union[Unset, list[OsidbApiV2FlawsListWorkflowStateItem]] = UNSET,
    workflow_state_in: Union[
        Unset, list[OsidbApiV2FlawsListWorkflowStateInItem]
    ] = UNSET,
) -> Response[OsidbApiV2FlawsListResponse200]:
    """
    Args:
        acknowledgments_affiliation (Union[Unset, str]):
        acknowledgments_affiliation_in (Union[Unset, list[str]]):
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
        acknowledgments_name_in (Union[Unset, list[str]]):
        acknowledgments_updated_dt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_date (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_uuid (Union[Unset, UUID]):
        acknowledgments_uuid_in (Union[Unset, list[UUID]]):
        affects_affectedness (Union[Unset, OsidbApiV2FlawsListAffectsAffectedness]):
        affects_affectedness_in (Union[Unset,
            list[OsidbApiV2FlawsListAffectsAffectednessInItem]]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_impact (Union[Unset, OsidbApiV2FlawsListAffectsImpact]):
        affects_impact_in (Union[Unset, list[OsidbApiV2FlawsListAffectsImpactInItem]]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_component_in (Union[Unset, list[str]]):
        affects_ps_module (Union[Unset, str]):
        affects_ps_module_in (Union[Unset, list[str]]):
        affects_ps_update_stream (Union[Unset, str]):
        affects_ps_update_stream_in (Union[Unset, list[str]]):
        affects_resolution (Union[Unset, OsidbApiV2FlawsListAffectsResolution]):
        affects_resolution_in (Union[Unset, list[OsidbApiV2FlawsListAffectsResolutionInItem]]):
        affects_tracker_created_dt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_date (Union[Unset, datetime.date]):
        affects_tracker_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_embargoed (Union[Unset, bool]):
        affects_tracker_errata_advisory_name (Union[Unset, str]):
        affects_tracker_errata_advisory_name_in (Union[Unset, list[str]]):
        affects_tracker_errata_et_id (Union[Unset, int]):
        affects_tracker_errata_shipped_dt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_date (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_external_system_id (Union[Unset, str]):
        affects_tracker_external_system_id_in (Union[Unset, list[str]]):
        affects_tracker_ps_update_stream (Union[Unset, str]):
        affects_tracker_ps_update_stream_in (Union[Unset, list[str]]):
        affects_tracker_resolution (Union[Unset, str]):
        affects_tracker_resolution_in (Union[Unset, list[str]]):
        affects_tracker_status (Union[Unset, str]):
        affects_tracker_status_in (Union[Unset, list[str]]):
        affects_tracker_type (Union[Unset, OsidbApiV2FlawsListAffectsTrackerType]):
        affects_tracker_type_in (Union[Unset, list[OsidbApiV2FlawsListAffectsTrackerTypeInItem]]):
        affects_tracker_updated_dt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_date (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_uuid (Union[Unset, UUID]):
        affects_tracker_uuid_in (Union[Unset, list[UUID]]):
        affects_tracker_visibility (Union[Unset, OsidbApiV2FlawsListAffectsTrackerVisibility]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        affects_uuid_in (Union[Unset, list[UUID]]):
        affects_visibility (Union[Unset, OsidbApiV2FlawsListAffectsVisibility]):
        bz_id (Union[Unset, float]):
        changed_after (Union[Unset, datetime.datetime]):
        changed_before (Union[Unset, datetime.datetime]):
        comment_zero (Union[Unset, str]):
        components (Union[Unset, list[str]]):
        components_in (Union[Unset, list[str]]):
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
        cve_id_in (Union[Unset, list[str]]):
        cve_id_isempty (Union[Unset, bool]):
        cvss2_nist_isempty (Union[Unset, bool]):
        cvss2_rh_isempty (Union[Unset, bool]):
        cvss3_nist_isempty (Union[Unset, bool]):
        cvss3_rh_isempty (Union[Unset, bool]):
        cvss4_nist_isempty (Union[Unset, bool]):
        cvss4_rh_isempty (Union[Unset, bool]):
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
        cvss_scores_issuer (Union[Unset, OsidbApiV2FlawsListCvssScoresIssuer]):
        cvss_scores_issuer_in (Union[Unset, list[OsidbApiV2FlawsListCvssScoresIssuerInItem]]):
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
        cwe_id (Union[Unset, str]):
        cwe_id_in (Union[Unset, list[str]]):
        cwe_id_isempty (Union[Unset, bool]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_has_no_non_community_affects_trackers (Union[Unset, bool]):
        flaw_labels (Union[Unset, list[str]]):
        impact (Union[Unset, OsidbApiV2FlawsListImpact]):
        impact_in (Union[Unset, list[OsidbApiV2FlawsListImpactInItem]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
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
        major_incident_state (Union[Unset, OsidbApiV2FlawsListMajorIncidentState]):
        major_incident_state_in (Union[Unset, list[OsidbApiV2FlawsListMajorIncidentStateInItem]]):
        mitigation_isempty (Union[Unset, bool]):
        nist_cvss_validation (Union[Unset, OsidbApiV2FlawsListNistCvssValidation]):
        nist_cvss_validation_in (Union[Unset, list[OsidbApiV2FlawsListNistCvssValidationInItem]]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV2FlawsListOrderItem]]):
        owner (Union[Unset, str]):
        owner_in (Union[Unset, list[str]]):
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
        references_description_in (Union[Unset, list[str]]):
        references_type (Union[Unset, OsidbApiV2FlawsListReferencesType]):
        references_type_in (Union[Unset, list[OsidbApiV2FlawsListReferencesTypeInItem]]):
        references_updated_dt (Union[Unset, datetime.datetime]):
        references_updated_dt_date (Union[Unset, datetime.date]):
        references_updated_dt_date_gte (Union[Unset, datetime.date]):
        references_updated_dt_date_lte (Union[Unset, datetime.date]):
        references_updated_dt_gt (Union[Unset, datetime.datetime]):
        references_updated_dt_gte (Union[Unset, datetime.datetime]):
        references_updated_dt_lt (Union[Unset, datetime.datetime]):
        references_updated_dt_lte (Union[Unset, datetime.datetime]):
        references_url (Union[Unset, str]):
        references_url_in (Union[Unset, list[str]]):
        references_uuid (Union[Unset, UUID]):
        references_uuid_in (Union[Unset, list[UUID]]):
        reported_dt (Union[Unset, datetime.datetime]):
        reported_dt_date (Union[Unset, datetime.date]):
        reported_dt_date_gte (Union[Unset, datetime.date]):
        reported_dt_date_lte (Union[Unset, datetime.date]):
        reported_dt_gt (Union[Unset, datetime.datetime]):
        reported_dt_gte (Union[Unset, datetime.datetime]):
        reported_dt_lt (Union[Unset, datetime.datetime]):
        reported_dt_lte (Union[Unset, datetime.datetime]):
        requires_cve_description (Union[Unset, OsidbApiV2FlawsListRequiresCveDescription]):
        requires_cve_description_in (Union[Unset,
            list[OsidbApiV2FlawsListRequiresCveDescriptionInItem]]):
        search (Union[Unset, str]):
        source (Union[Unset, OsidbApiV2FlawsListSource]):
        source_in (Union[Unset, list[OsidbApiV2FlawsListSourceInItem]]):
        statement (Union[Unset, str]):
        statement_isempty (Union[Unset, bool]):
        team_id (Union[Unset, str]):
        team_id_in (Union[Unset, list[str]]):
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
        uuid_in (Union[Unset, list[UUID]]):
        visibility (Union[Unset, OsidbApiV2FlawsListVisibility]):
        workflow_state (Union[Unset, list[OsidbApiV2FlawsListWorkflowStateItem]]):
        workflow_state_in (Union[Unset, list[OsidbApiV2FlawsListWorkflowStateInItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OsidbApiV2FlawsListResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        acknowledgments_affiliation=acknowledgments_affiliation,
        acknowledgments_affiliation_in=acknowledgments_affiliation_in,
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
        acknowledgments_name_in=acknowledgments_name_in,
        acknowledgments_updated_dt=acknowledgments_updated_dt,
        acknowledgments_updated_dt_date=acknowledgments_updated_dt_date,
        acknowledgments_updated_dt_date_gte=acknowledgments_updated_dt_date_gte,
        acknowledgments_updated_dt_date_lte=acknowledgments_updated_dt_date_lte,
        acknowledgments_updated_dt_gt=acknowledgments_updated_dt_gt,
        acknowledgments_updated_dt_gte=acknowledgments_updated_dt_gte,
        acknowledgments_updated_dt_lt=acknowledgments_updated_dt_lt,
        acknowledgments_updated_dt_lte=acknowledgments_updated_dt_lte,
        acknowledgments_uuid=acknowledgments_uuid,
        acknowledgments_uuid_in=acknowledgments_uuid_in,
        affects_affectedness=affects_affectedness,
        affects_affectedness_in=affects_affectedness_in,
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
        affects_impact_in=affects_impact_in,
        affects_ps_component=affects_ps_component,
        affects_ps_component_in=affects_ps_component_in,
        affects_ps_module=affects_ps_module,
        affects_ps_module_in=affects_ps_module_in,
        affects_ps_update_stream=affects_ps_update_stream,
        affects_ps_update_stream_in=affects_ps_update_stream_in,
        affects_resolution=affects_resolution,
        affects_resolution_in=affects_resolution_in,
        affects_tracker_created_dt=affects_tracker_created_dt,
        affects_tracker_created_dt_date=affects_tracker_created_dt_date,
        affects_tracker_created_dt_date_gte=affects_tracker_created_dt_date_gte,
        affects_tracker_created_dt_date_lte=affects_tracker_created_dt_date_lte,
        affects_tracker_created_dt_gt=affects_tracker_created_dt_gt,
        affects_tracker_created_dt_gte=affects_tracker_created_dt_gte,
        affects_tracker_created_dt_lt=affects_tracker_created_dt_lt,
        affects_tracker_created_dt_lte=affects_tracker_created_dt_lte,
        affects_tracker_embargoed=affects_tracker_embargoed,
        affects_tracker_errata_advisory_name=affects_tracker_errata_advisory_name,
        affects_tracker_errata_advisory_name_in=affects_tracker_errata_advisory_name_in,
        affects_tracker_errata_et_id=affects_tracker_errata_et_id,
        affects_tracker_errata_shipped_dt=affects_tracker_errata_shipped_dt,
        affects_tracker_errata_shipped_dt_date=affects_tracker_errata_shipped_dt_date,
        affects_tracker_errata_shipped_dt_date_gte=affects_tracker_errata_shipped_dt_date_gte,
        affects_tracker_errata_shipped_dt_date_lte=affects_tracker_errata_shipped_dt_date_lte,
        affects_tracker_errata_shipped_dt_gt=affects_tracker_errata_shipped_dt_gt,
        affects_tracker_errata_shipped_dt_gte=affects_tracker_errata_shipped_dt_gte,
        affects_tracker_errata_shipped_dt_lt=affects_tracker_errata_shipped_dt_lt,
        affects_tracker_errata_shipped_dt_lte=affects_tracker_errata_shipped_dt_lte,
        affects_tracker_external_system_id=affects_tracker_external_system_id,
        affects_tracker_external_system_id_in=affects_tracker_external_system_id_in,
        affects_tracker_ps_update_stream=affects_tracker_ps_update_stream,
        affects_tracker_ps_update_stream_in=affects_tracker_ps_update_stream_in,
        affects_tracker_resolution=affects_tracker_resolution,
        affects_tracker_resolution_in=affects_tracker_resolution_in,
        affects_tracker_status=affects_tracker_status,
        affects_tracker_status_in=affects_tracker_status_in,
        affects_tracker_type=affects_tracker_type,
        affects_tracker_type_in=affects_tracker_type_in,
        affects_tracker_updated_dt=affects_tracker_updated_dt,
        affects_tracker_updated_dt_date=affects_tracker_updated_dt_date,
        affects_tracker_updated_dt_date_gte=affects_tracker_updated_dt_date_gte,
        affects_tracker_updated_dt_date_lte=affects_tracker_updated_dt_date_lte,
        affects_tracker_updated_dt_gt=affects_tracker_updated_dt_gt,
        affects_tracker_updated_dt_gte=affects_tracker_updated_dt_gte,
        affects_tracker_updated_dt_lt=affects_tracker_updated_dt_lt,
        affects_tracker_updated_dt_lte=affects_tracker_updated_dt_lte,
        affects_tracker_uuid=affects_tracker_uuid,
        affects_tracker_uuid_in=affects_tracker_uuid_in,
        affects_tracker_visibility=affects_tracker_visibility,
        affects_updated_dt=affects_updated_dt,
        affects_updated_dt_date=affects_updated_dt_date,
        affects_updated_dt_date_gte=affects_updated_dt_date_gte,
        affects_updated_dt_date_lte=affects_updated_dt_date_lte,
        affects_updated_dt_gt=affects_updated_dt_gt,
        affects_updated_dt_gte=affects_updated_dt_gte,
        affects_updated_dt_lt=affects_updated_dt_lt,
        affects_updated_dt_lte=affects_updated_dt_lte,
        affects_uuid=affects_uuid,
        affects_uuid_in=affects_uuid_in,
        affects_visibility=affects_visibility,
        bz_id=bz_id,
        changed_after=changed_after,
        changed_before=changed_before,
        comment_zero=comment_zero,
        components=components,
        components_in=components_in,
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
        cve_id_in=cve_id_in,
        cve_id_isempty=cve_id_isempty,
        cvss2_nist_isempty=cvss2_nist_isempty,
        cvss2_rh_isempty=cvss2_rh_isempty,
        cvss3_nist_isempty=cvss3_nist_isempty,
        cvss3_rh_isempty=cvss3_rh_isempty,
        cvss4_nist_isempty=cvss4_nist_isempty,
        cvss4_rh_isempty=cvss4_rh_isempty,
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
        cwe_id=cwe_id,
        cwe_id_in=cwe_id_in,
        cwe_id_isempty=cwe_id_isempty,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        flaw_has_no_non_community_affects_trackers=flaw_has_no_non_community_affects_trackers,
        flaw_labels=flaw_labels,
        impact=impact,
        impact_in=impact_in,
        include_fields=include_fields,
        include_history=include_history,
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
        major_incident_state_in=major_incident_state_in,
        mitigation_isempty=mitigation_isempty,
        nist_cvss_validation=nist_cvss_validation,
        nist_cvss_validation_in=nist_cvss_validation_in,
        offset=offset,
        order=order,
        owner=owner,
        owner_in=owner_in,
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
        references_description_in=references_description_in,
        references_type=references_type,
        references_type_in=references_type_in,
        references_updated_dt=references_updated_dt,
        references_updated_dt_date=references_updated_dt_date,
        references_updated_dt_date_gte=references_updated_dt_date_gte,
        references_updated_dt_date_lte=references_updated_dt_date_lte,
        references_updated_dt_gt=references_updated_dt_gt,
        references_updated_dt_gte=references_updated_dt_gte,
        references_updated_dt_lt=references_updated_dt_lt,
        references_updated_dt_lte=references_updated_dt_lte,
        references_url=references_url,
        references_url_in=references_url_in,
        references_uuid=references_uuid,
        references_uuid_in=references_uuid_in,
        reported_dt=reported_dt,
        reported_dt_date=reported_dt_date,
        reported_dt_date_gte=reported_dt_date_gte,
        reported_dt_date_lte=reported_dt_date_lte,
        reported_dt_gt=reported_dt_gt,
        reported_dt_gte=reported_dt_gte,
        reported_dt_lt=reported_dt_lt,
        reported_dt_lte=reported_dt_lte,
        requires_cve_description=requires_cve_description,
        requires_cve_description_in=requires_cve_description_in,
        search=search,
        source=source,
        source_in=source_in,
        statement=statement,
        statement_isempty=statement_isempty,
        team_id=team_id,
        team_id_in=team_id_in,
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
        uuid_in=uuid_in,
        visibility=visibility,
        workflow_state=workflow_state,
        workflow_state_in=workflow_state_in,
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
    acknowledgments_affiliation_in: Union[Unset, list[str]] = UNSET,
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
    acknowledgments_name_in: Union[Unset, list[str]] = UNSET,
    acknowledgments_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    acknowledgments_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    acknowledgments_uuid: Union[Unset, UUID] = UNSET,
    acknowledgments_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_affectedness: Union[Unset, OsidbApiV2FlawsListAffectsAffectedness] = UNSET,
    affects_affectedness_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsAffectednessInItem]
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
    affects_impact: Union[Unset, OsidbApiV2FlawsListAffectsImpact] = UNSET,
    affects_impact_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsImpactInItem]
    ] = UNSET,
    affects_ps_component: Union[Unset, str] = UNSET,
    affects_ps_component_in: Union[Unset, list[str]] = UNSET,
    affects_ps_module: Union[Unset, str] = UNSET,
    affects_ps_module_in: Union[Unset, list[str]] = UNSET,
    affects_ps_update_stream: Union[Unset, str] = UNSET,
    affects_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    affects_resolution: Union[Unset, OsidbApiV2FlawsListAffectsResolution] = UNSET,
    affects_resolution_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsResolutionInItem]
    ] = UNSET,
    affects_tracker_created_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_created_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_created_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_embargoed: Union[Unset, bool] = UNSET,
    affects_tracker_errata_advisory_name: Union[Unset, str] = UNSET,
    affects_tracker_errata_advisory_name_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_errata_et_id: Union[Unset, int] = UNSET,
    affects_tracker_errata_shipped_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_errata_shipped_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_errata_shipped_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_external_system_id: Union[Unset, str] = UNSET,
    affects_tracker_external_system_id_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_ps_update_stream: Union[Unset, str] = UNSET,
    affects_tracker_ps_update_stream_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_resolution: Union[Unset, str] = UNSET,
    affects_tracker_resolution_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_status: Union[Unset, str] = UNSET,
    affects_tracker_status_in: Union[Unset, list[str]] = UNSET,
    affects_tracker_type: Union[Unset, OsidbApiV2FlawsListAffectsTrackerType] = UNSET,
    affects_tracker_type_in: Union[
        Unset, list[OsidbApiV2FlawsListAffectsTrackerTypeInItem]
    ] = UNSET,
    affects_tracker_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_tracker_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_tracker_uuid: Union[Unset, UUID] = UNSET,
    affects_tracker_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_tracker_visibility: Union[
        Unset, OsidbApiV2FlawsListAffectsTrackerVisibility
    ] = UNSET,
    affects_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    affects_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    affects_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    affects_uuid: Union[Unset, UUID] = UNSET,
    affects_uuid_in: Union[Unset, list[UUID]] = UNSET,
    affects_visibility: Union[Unset, OsidbApiV2FlawsListAffectsVisibility] = UNSET,
    bz_id: Union[Unset, float] = UNSET,
    changed_after: Union[Unset, datetime.datetime] = UNSET,
    changed_before: Union[Unset, datetime.datetime] = UNSET,
    comment_zero: Union[Unset, str] = UNSET,
    components: Union[Unset, list[str]] = UNSET,
    components_in: Union[Unset, list[str]] = UNSET,
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
    cve_id_in: Union[Unset, list[str]] = UNSET,
    cve_id_isempty: Union[Unset, bool] = UNSET,
    cvss2_nist_isempty: Union[Unset, bool] = UNSET,
    cvss2_rh_isempty: Union[Unset, bool] = UNSET,
    cvss3_nist_isempty: Union[Unset, bool] = UNSET,
    cvss3_rh_isempty: Union[Unset, bool] = UNSET,
    cvss4_nist_isempty: Union[Unset, bool] = UNSET,
    cvss4_rh_isempty: Union[Unset, bool] = UNSET,
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
    cvss_scores_issuer: Union[Unset, OsidbApiV2FlawsListCvssScoresIssuer] = UNSET,
    cvss_scores_issuer_in: Union[
        Unset, list[OsidbApiV2FlawsListCvssScoresIssuerInItem]
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
    cwe_id: Union[Unset, str] = UNSET,
    cwe_id_in: Union[Unset, list[str]] = UNSET,
    cwe_id_isempty: Union[Unset, bool] = UNSET,
    embargoed: Union[Unset, bool] = UNSET,
    exclude_fields: Union[Unset, list[str]] = UNSET,
    flaw_has_no_non_community_affects_trackers: Union[Unset, bool] = UNSET,
    flaw_labels: Union[Unset, list[str]] = UNSET,
    impact: Union[Unset, OsidbApiV2FlawsListImpact] = UNSET,
    impact_in: Union[Unset, list[OsidbApiV2FlawsListImpactInItem]] = UNSET,
    include_fields: Union[Unset, list[str]] = UNSET,
    include_history: Union[Unset, bool] = UNSET,
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
    major_incident_state: Union[Unset, OsidbApiV2FlawsListMajorIncidentState] = UNSET,
    major_incident_state_in: Union[
        Unset, list[OsidbApiV2FlawsListMajorIncidentStateInItem]
    ] = UNSET,
    mitigation_isempty: Union[Unset, bool] = UNSET,
    nist_cvss_validation: Union[Unset, OsidbApiV2FlawsListNistCvssValidation] = UNSET,
    nist_cvss_validation_in: Union[
        Unset, list[OsidbApiV2FlawsListNistCvssValidationInItem]
    ] = UNSET,
    offset: Union[Unset, int] = UNSET,
    order: Union[Unset, list[OsidbApiV2FlawsListOrderItem]] = UNSET,
    owner: Union[Unset, str] = UNSET,
    owner_in: Union[Unset, list[str]] = UNSET,
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
    references_description_in: Union[Unset, list[str]] = UNSET,
    references_type: Union[Unset, OsidbApiV2FlawsListReferencesType] = UNSET,
    references_type_in: Union[
        Unset, list[OsidbApiV2FlawsListReferencesTypeInItem]
    ] = UNSET,
    references_updated_dt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_date: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    references_updated_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    references_updated_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    references_url: Union[Unset, str] = UNSET,
    references_url_in: Union[Unset, list[str]] = UNSET,
    references_uuid: Union[Unset, UUID] = UNSET,
    references_uuid_in: Union[Unset, list[UUID]] = UNSET,
    reported_dt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_date: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_gte: Union[Unset, datetime.date] = UNSET,
    reported_dt_date_lte: Union[Unset, datetime.date] = UNSET,
    reported_dt_gt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_gte: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lt: Union[Unset, datetime.datetime] = UNSET,
    reported_dt_lte: Union[Unset, datetime.datetime] = UNSET,
    requires_cve_description: Union[
        Unset, OsidbApiV2FlawsListRequiresCveDescription
    ] = UNSET,
    requires_cve_description_in: Union[
        Unset, list[OsidbApiV2FlawsListRequiresCveDescriptionInItem]
    ] = UNSET,
    search: Union[Unset, str] = UNSET,
    source: Union[Unset, OsidbApiV2FlawsListSource] = UNSET,
    source_in: Union[Unset, list[OsidbApiV2FlawsListSourceInItem]] = UNSET,
    statement: Union[Unset, str] = UNSET,
    statement_isempty: Union[Unset, bool] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    team_id_in: Union[Unset, list[str]] = UNSET,
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
    uuid_in: Union[Unset, list[UUID]] = UNSET,
    visibility: Union[Unset, OsidbApiV2FlawsListVisibility] = UNSET,
    workflow_state: Union[Unset, list[OsidbApiV2FlawsListWorkflowStateItem]] = UNSET,
    workflow_state_in: Union[
        Unset, list[OsidbApiV2FlawsListWorkflowStateInItem]
    ] = UNSET,
) -> Optional[OsidbApiV2FlawsListResponse200]:
    """
    Args:
        acknowledgments_affiliation (Union[Unset, str]):
        acknowledgments_affiliation_in (Union[Unset, list[str]]):
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
        acknowledgments_name_in (Union[Unset, list[str]]):
        acknowledgments_updated_dt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_date (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_gte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_date_lte (Union[Unset, datetime.date]):
        acknowledgments_updated_dt_gt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_gte (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lt (Union[Unset, datetime.datetime]):
        acknowledgments_updated_dt_lte (Union[Unset, datetime.datetime]):
        acknowledgments_uuid (Union[Unset, UUID]):
        acknowledgments_uuid_in (Union[Unset, list[UUID]]):
        affects_affectedness (Union[Unset, OsidbApiV2FlawsListAffectsAffectedness]):
        affects_affectedness_in (Union[Unset,
            list[OsidbApiV2FlawsListAffectsAffectednessInItem]]):
        affects_created_dt (Union[Unset, datetime.datetime]):
        affects_created_dt_date (Union[Unset, datetime.date]):
        affects_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_embargoed (Union[Unset, bool]):
        affects_impact (Union[Unset, OsidbApiV2FlawsListAffectsImpact]):
        affects_impact_in (Union[Unset, list[OsidbApiV2FlawsListAffectsImpactInItem]]):
        affects_ps_component (Union[Unset, str]):
        affects_ps_component_in (Union[Unset, list[str]]):
        affects_ps_module (Union[Unset, str]):
        affects_ps_module_in (Union[Unset, list[str]]):
        affects_ps_update_stream (Union[Unset, str]):
        affects_ps_update_stream_in (Union[Unset, list[str]]):
        affects_resolution (Union[Unset, OsidbApiV2FlawsListAffectsResolution]):
        affects_resolution_in (Union[Unset, list[OsidbApiV2FlawsListAffectsResolutionInItem]]):
        affects_tracker_created_dt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_date (Union[Unset, datetime.date]):
        affects_tracker_created_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_created_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_created_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_created_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_embargoed (Union[Unset, bool]):
        affects_tracker_errata_advisory_name (Union[Unset, str]):
        affects_tracker_errata_advisory_name_in (Union[Unset, list[str]]):
        affects_tracker_errata_et_id (Union[Unset, int]):
        affects_tracker_errata_shipped_dt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_date (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_errata_shipped_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_errata_shipped_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_external_system_id (Union[Unset, str]):
        affects_tracker_external_system_id_in (Union[Unset, list[str]]):
        affects_tracker_ps_update_stream (Union[Unset, str]):
        affects_tracker_ps_update_stream_in (Union[Unset, list[str]]):
        affects_tracker_resolution (Union[Unset, str]):
        affects_tracker_resolution_in (Union[Unset, list[str]]):
        affects_tracker_status (Union[Unset, str]):
        affects_tracker_status_in (Union[Unset, list[str]]):
        affects_tracker_type (Union[Unset, OsidbApiV2FlawsListAffectsTrackerType]):
        affects_tracker_type_in (Union[Unset, list[OsidbApiV2FlawsListAffectsTrackerTypeInItem]]):
        affects_tracker_updated_dt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_date (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_tracker_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_tracker_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_tracker_uuid (Union[Unset, UUID]):
        affects_tracker_uuid_in (Union[Unset, list[UUID]]):
        affects_tracker_visibility (Union[Unset, OsidbApiV2FlawsListAffectsTrackerVisibility]):
        affects_updated_dt (Union[Unset, datetime.datetime]):
        affects_updated_dt_date (Union[Unset, datetime.date]):
        affects_updated_dt_date_gte (Union[Unset, datetime.date]):
        affects_updated_dt_date_lte (Union[Unset, datetime.date]):
        affects_updated_dt_gt (Union[Unset, datetime.datetime]):
        affects_updated_dt_gte (Union[Unset, datetime.datetime]):
        affects_updated_dt_lt (Union[Unset, datetime.datetime]):
        affects_updated_dt_lte (Union[Unset, datetime.datetime]):
        affects_uuid (Union[Unset, UUID]):
        affects_uuid_in (Union[Unset, list[UUID]]):
        affects_visibility (Union[Unset, OsidbApiV2FlawsListAffectsVisibility]):
        bz_id (Union[Unset, float]):
        changed_after (Union[Unset, datetime.datetime]):
        changed_before (Union[Unset, datetime.datetime]):
        comment_zero (Union[Unset, str]):
        components (Union[Unset, list[str]]):
        components_in (Union[Unset, list[str]]):
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
        cve_id_in (Union[Unset, list[str]]):
        cve_id_isempty (Union[Unset, bool]):
        cvss2_nist_isempty (Union[Unset, bool]):
        cvss2_rh_isempty (Union[Unset, bool]):
        cvss3_nist_isempty (Union[Unset, bool]):
        cvss3_rh_isempty (Union[Unset, bool]):
        cvss4_nist_isempty (Union[Unset, bool]):
        cvss4_rh_isempty (Union[Unset, bool]):
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
        cvss_scores_issuer (Union[Unset, OsidbApiV2FlawsListCvssScoresIssuer]):
        cvss_scores_issuer_in (Union[Unset, list[OsidbApiV2FlawsListCvssScoresIssuerInItem]]):
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
        cwe_id (Union[Unset, str]):
        cwe_id_in (Union[Unset, list[str]]):
        cwe_id_isempty (Union[Unset, bool]):
        embargoed (Union[Unset, bool]):
        exclude_fields (Union[Unset, list[str]]):
        flaw_has_no_non_community_affects_trackers (Union[Unset, bool]):
        flaw_labels (Union[Unset, list[str]]):
        impact (Union[Unset, OsidbApiV2FlawsListImpact]):
        impact_in (Union[Unset, list[OsidbApiV2FlawsListImpactInItem]]):
        include_fields (Union[Unset, list[str]]):
        include_history (Union[Unset, bool]):
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
        major_incident_state (Union[Unset, OsidbApiV2FlawsListMajorIncidentState]):
        major_incident_state_in (Union[Unset, list[OsidbApiV2FlawsListMajorIncidentStateInItem]]):
        mitigation_isempty (Union[Unset, bool]):
        nist_cvss_validation (Union[Unset, OsidbApiV2FlawsListNistCvssValidation]):
        nist_cvss_validation_in (Union[Unset, list[OsidbApiV2FlawsListNistCvssValidationInItem]]):
        offset (Union[Unset, int]):
        order (Union[Unset, list[OsidbApiV2FlawsListOrderItem]]):
        owner (Union[Unset, str]):
        owner_in (Union[Unset, list[str]]):
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
        references_description_in (Union[Unset, list[str]]):
        references_type (Union[Unset, OsidbApiV2FlawsListReferencesType]):
        references_type_in (Union[Unset, list[OsidbApiV2FlawsListReferencesTypeInItem]]):
        references_updated_dt (Union[Unset, datetime.datetime]):
        references_updated_dt_date (Union[Unset, datetime.date]):
        references_updated_dt_date_gte (Union[Unset, datetime.date]):
        references_updated_dt_date_lte (Union[Unset, datetime.date]):
        references_updated_dt_gt (Union[Unset, datetime.datetime]):
        references_updated_dt_gte (Union[Unset, datetime.datetime]):
        references_updated_dt_lt (Union[Unset, datetime.datetime]):
        references_updated_dt_lte (Union[Unset, datetime.datetime]):
        references_url (Union[Unset, str]):
        references_url_in (Union[Unset, list[str]]):
        references_uuid (Union[Unset, UUID]):
        references_uuid_in (Union[Unset, list[UUID]]):
        reported_dt (Union[Unset, datetime.datetime]):
        reported_dt_date (Union[Unset, datetime.date]):
        reported_dt_date_gte (Union[Unset, datetime.date]):
        reported_dt_date_lte (Union[Unset, datetime.date]):
        reported_dt_gt (Union[Unset, datetime.datetime]):
        reported_dt_gte (Union[Unset, datetime.datetime]):
        reported_dt_lt (Union[Unset, datetime.datetime]):
        reported_dt_lte (Union[Unset, datetime.datetime]):
        requires_cve_description (Union[Unset, OsidbApiV2FlawsListRequiresCveDescription]):
        requires_cve_description_in (Union[Unset,
            list[OsidbApiV2FlawsListRequiresCveDescriptionInItem]]):
        search (Union[Unset, str]):
        source (Union[Unset, OsidbApiV2FlawsListSource]):
        source_in (Union[Unset, list[OsidbApiV2FlawsListSourceInItem]]):
        statement (Union[Unset, str]):
        statement_isempty (Union[Unset, bool]):
        team_id (Union[Unset, str]):
        team_id_in (Union[Unset, list[str]]):
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
        uuid_in (Union[Unset, list[UUID]]):
        visibility (Union[Unset, OsidbApiV2FlawsListVisibility]):
        workflow_state (Union[Unset, list[OsidbApiV2FlawsListWorkflowStateItem]]):
        workflow_state_in (Union[Unset, list[OsidbApiV2FlawsListWorkflowStateInItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OsidbApiV2FlawsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            acknowledgments_affiliation=acknowledgments_affiliation,
            acknowledgments_affiliation_in=acknowledgments_affiliation_in,
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
            acknowledgments_name_in=acknowledgments_name_in,
            acknowledgments_updated_dt=acknowledgments_updated_dt,
            acknowledgments_updated_dt_date=acknowledgments_updated_dt_date,
            acknowledgments_updated_dt_date_gte=acknowledgments_updated_dt_date_gte,
            acknowledgments_updated_dt_date_lte=acknowledgments_updated_dt_date_lte,
            acknowledgments_updated_dt_gt=acknowledgments_updated_dt_gt,
            acknowledgments_updated_dt_gte=acknowledgments_updated_dt_gte,
            acknowledgments_updated_dt_lt=acknowledgments_updated_dt_lt,
            acknowledgments_updated_dt_lte=acknowledgments_updated_dt_lte,
            acknowledgments_uuid=acknowledgments_uuid,
            acknowledgments_uuid_in=acknowledgments_uuid_in,
            affects_affectedness=affects_affectedness,
            affects_affectedness_in=affects_affectedness_in,
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
            affects_impact_in=affects_impact_in,
            affects_ps_component=affects_ps_component,
            affects_ps_component_in=affects_ps_component_in,
            affects_ps_module=affects_ps_module,
            affects_ps_module_in=affects_ps_module_in,
            affects_ps_update_stream=affects_ps_update_stream,
            affects_ps_update_stream_in=affects_ps_update_stream_in,
            affects_resolution=affects_resolution,
            affects_resolution_in=affects_resolution_in,
            affects_tracker_created_dt=affects_tracker_created_dt,
            affects_tracker_created_dt_date=affects_tracker_created_dt_date,
            affects_tracker_created_dt_date_gte=affects_tracker_created_dt_date_gte,
            affects_tracker_created_dt_date_lte=affects_tracker_created_dt_date_lte,
            affects_tracker_created_dt_gt=affects_tracker_created_dt_gt,
            affects_tracker_created_dt_gte=affects_tracker_created_dt_gte,
            affects_tracker_created_dt_lt=affects_tracker_created_dt_lt,
            affects_tracker_created_dt_lte=affects_tracker_created_dt_lte,
            affects_tracker_embargoed=affects_tracker_embargoed,
            affects_tracker_errata_advisory_name=affects_tracker_errata_advisory_name,
            affects_tracker_errata_advisory_name_in=affects_tracker_errata_advisory_name_in,
            affects_tracker_errata_et_id=affects_tracker_errata_et_id,
            affects_tracker_errata_shipped_dt=affects_tracker_errata_shipped_dt,
            affects_tracker_errata_shipped_dt_date=affects_tracker_errata_shipped_dt_date,
            affects_tracker_errata_shipped_dt_date_gte=affects_tracker_errata_shipped_dt_date_gte,
            affects_tracker_errata_shipped_dt_date_lte=affects_tracker_errata_shipped_dt_date_lte,
            affects_tracker_errata_shipped_dt_gt=affects_tracker_errata_shipped_dt_gt,
            affects_tracker_errata_shipped_dt_gte=affects_tracker_errata_shipped_dt_gte,
            affects_tracker_errata_shipped_dt_lt=affects_tracker_errata_shipped_dt_lt,
            affects_tracker_errata_shipped_dt_lte=affects_tracker_errata_shipped_dt_lte,
            affects_tracker_external_system_id=affects_tracker_external_system_id,
            affects_tracker_external_system_id_in=affects_tracker_external_system_id_in,
            affects_tracker_ps_update_stream=affects_tracker_ps_update_stream,
            affects_tracker_ps_update_stream_in=affects_tracker_ps_update_stream_in,
            affects_tracker_resolution=affects_tracker_resolution,
            affects_tracker_resolution_in=affects_tracker_resolution_in,
            affects_tracker_status=affects_tracker_status,
            affects_tracker_status_in=affects_tracker_status_in,
            affects_tracker_type=affects_tracker_type,
            affects_tracker_type_in=affects_tracker_type_in,
            affects_tracker_updated_dt=affects_tracker_updated_dt,
            affects_tracker_updated_dt_date=affects_tracker_updated_dt_date,
            affects_tracker_updated_dt_date_gte=affects_tracker_updated_dt_date_gte,
            affects_tracker_updated_dt_date_lte=affects_tracker_updated_dt_date_lte,
            affects_tracker_updated_dt_gt=affects_tracker_updated_dt_gt,
            affects_tracker_updated_dt_gte=affects_tracker_updated_dt_gte,
            affects_tracker_updated_dt_lt=affects_tracker_updated_dt_lt,
            affects_tracker_updated_dt_lte=affects_tracker_updated_dt_lte,
            affects_tracker_uuid=affects_tracker_uuid,
            affects_tracker_uuid_in=affects_tracker_uuid_in,
            affects_tracker_visibility=affects_tracker_visibility,
            affects_updated_dt=affects_updated_dt,
            affects_updated_dt_date=affects_updated_dt_date,
            affects_updated_dt_date_gte=affects_updated_dt_date_gte,
            affects_updated_dt_date_lte=affects_updated_dt_date_lte,
            affects_updated_dt_gt=affects_updated_dt_gt,
            affects_updated_dt_gte=affects_updated_dt_gte,
            affects_updated_dt_lt=affects_updated_dt_lt,
            affects_updated_dt_lte=affects_updated_dt_lte,
            affects_uuid=affects_uuid,
            affects_uuid_in=affects_uuid_in,
            affects_visibility=affects_visibility,
            bz_id=bz_id,
            changed_after=changed_after,
            changed_before=changed_before,
            comment_zero=comment_zero,
            components=components,
            components_in=components_in,
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
            cve_id_in=cve_id_in,
            cve_id_isempty=cve_id_isempty,
            cvss2_nist_isempty=cvss2_nist_isempty,
            cvss2_rh_isempty=cvss2_rh_isempty,
            cvss3_nist_isempty=cvss3_nist_isempty,
            cvss3_rh_isempty=cvss3_rh_isempty,
            cvss4_nist_isempty=cvss4_nist_isempty,
            cvss4_rh_isempty=cvss4_rh_isempty,
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
            cwe_id=cwe_id,
            cwe_id_in=cwe_id_in,
            cwe_id_isempty=cwe_id_isempty,
            embargoed=embargoed,
            exclude_fields=exclude_fields,
            flaw_has_no_non_community_affects_trackers=flaw_has_no_non_community_affects_trackers,
            flaw_labels=flaw_labels,
            impact=impact,
            impact_in=impact_in,
            include_fields=include_fields,
            include_history=include_history,
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
            major_incident_state_in=major_incident_state_in,
            mitigation_isempty=mitigation_isempty,
            nist_cvss_validation=nist_cvss_validation,
            nist_cvss_validation_in=nist_cvss_validation_in,
            offset=offset,
            order=order,
            owner=owner,
            owner_in=owner_in,
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
            references_description_in=references_description_in,
            references_type=references_type,
            references_type_in=references_type_in,
            references_updated_dt=references_updated_dt,
            references_updated_dt_date=references_updated_dt_date,
            references_updated_dt_date_gte=references_updated_dt_date_gte,
            references_updated_dt_date_lte=references_updated_dt_date_lte,
            references_updated_dt_gt=references_updated_dt_gt,
            references_updated_dt_gte=references_updated_dt_gte,
            references_updated_dt_lt=references_updated_dt_lt,
            references_updated_dt_lte=references_updated_dt_lte,
            references_url=references_url,
            references_url_in=references_url_in,
            references_uuid=references_uuid,
            references_uuid_in=references_uuid_in,
            reported_dt=reported_dt,
            reported_dt_date=reported_dt_date,
            reported_dt_date_gte=reported_dt_date_gte,
            reported_dt_date_lte=reported_dt_date_lte,
            reported_dt_gt=reported_dt_gt,
            reported_dt_gte=reported_dt_gte,
            reported_dt_lt=reported_dt_lt,
            reported_dt_lte=reported_dt_lte,
            requires_cve_description=requires_cve_description,
            requires_cve_description_in=requires_cve_description_in,
            search=search,
            source=source,
            source_in=source_in,
            statement=statement,
            statement_isempty=statement_isempty,
            team_id=team_id,
            team_id_in=team_id_in,
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
            uuid_in=uuid_in,
            visibility=visibility,
            workflow_state=workflow_state,
            workflow_state_in=workflow_state_in,
        )
    ).parsed
