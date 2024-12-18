"""Contains all the data models used in inputs/outputs"""

from .affect import Affect
from .affect_bulk_post_put_response import AffectBulkPostPutResponse
from .affect_bulk_put import AffectBulkPut
from .affect_cvss import AffectCVSS
from .affect_cvss_post import AffectCVSSPost
from .affect_cvss_put import AffectCVSSPut
from .affect_post import AffectPost
from .affect_report_data import AffectReportData
from .affectedness_enum import AffectednessEnum
from .alert import Alert
from .alert_type_enum import AlertTypeEnum
from .audit import Audit
from .auth_token_create_response_200 import AuthTokenCreateResponse200
from .auth_token_refresh_create_response_200 import AuthTokenRefreshCreateResponse200
from .auth_token_retrieve_response_200 import AuthTokenRetrieveResponse200
from .auth_token_verify_create_response_200 import AuthTokenVerifyCreateResponse200
from .blank_enum import BlankEnum
from .collectors_api_v1_status_retrieve_response_200 import (
    CollectorsApiV1StatusRetrieveResponse200,
)
from .collectors_api_v1_status_retrieve_response_200_collectors_item import (
    CollectorsApiV1StatusRetrieveResponse200CollectorsItem,
)
from .collectors_api_v1_status_retrieve_response_200_collectors_item_data import (
    CollectorsApiV1StatusRetrieveResponse200CollectorsItemData,
)
from .collectors_api_v1_status_retrieve_response_200_collectors_item_error_type_0 import (
    CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0,
)
from .collectors_api_v1_status_retrieve_response_200_collectors_item_state import (
    CollectorsApiV1StatusRetrieveResponse200CollectorsItemState,
)
from .collectors_healthy_retrieve_response_200 import (
    CollectorsHealthyRetrieveResponse200,
)
from .collectors_retrieve_response_200 import CollectorsRetrieveResponse200
from .comment import Comment
from .cvss_version_enum import CvssVersionEnum
from .epss import EPSS
from .erratum import Erratum
from .exploit_only_report_data import ExploitOnlyReportData
from .exploit_only_report_data_source_enum import ExploitOnlyReportDataSourceEnum
from .exploits_api_v1_collect_update_response_200 import (
    ExploitsApiV1CollectUpdateResponse200,
)
from .exploits_api_v1_cve_map_retrieve_response_200 import (
    ExploitsApiV1CveMapRetrieveResponse200,
)
from .exploits_api_v1_cve_map_retrieve_response_200_cves import (
    ExploitsApiV1CveMapRetrieveResponse200Cves,
)
from .exploits_api_v1_epss_list_response_200 import ExploitsApiV1EpssListResponse200
from .exploits_api_v1_flaw_data_list_response_200 import (
    ExploitsApiV1FlawDataListResponse200,
)
from .exploits_api_v1_report_data_list_response_200 import (
    ExploitsApiV1ReportDataListResponse200,
)
from .exploits_api_v1_report_date_retrieve_response_200 import (
    ExploitsApiV1ReportDateRetrieveResponse200,
)
from .exploits_api_v1_report_date_retrieve_response_200_action_required_item import (
    ExploitsApiV1ReportDateRetrieveResponse200ActionRequiredItem,
)
from .exploits_api_v1_report_date_retrieve_response_200_no_action_item import (
    ExploitsApiV1ReportDateRetrieveResponse200NoActionItem,
)
from .exploits_api_v1_report_date_retrieve_response_200_not_relevant_item import (
    ExploitsApiV1ReportDateRetrieveResponse200NotRelevantItem,
)
from .exploits_api_v1_report_explanations_retrieve_response_200 import (
    ExploitsApiV1ReportExplanationsRetrieveResponse200,
)
from .exploits_api_v1_report_explanations_retrieve_response_200_explanations_item import (
    ExploitsApiV1ReportExplanationsRetrieveResponse200ExplanationsItem,
)
from .exploits_api_v1_report_pending_retrieve_response_200 import (
    ExploitsApiV1ReportPendingRetrieveResponse200,
)
from .exploits_api_v1_report_pending_retrieve_response_200_pending_actions_item import (
    ExploitsApiV1ReportPendingRetrieveResponse200PendingActionsItem,
)
from .exploits_api_v1_status_retrieve_response_200 import (
    ExploitsApiV1StatusRetrieveResponse200,
)
from .exploits_api_v1_supported_products_list_response_200 import (
    ExploitsApiV1SupportedProductsListResponse200,
)
from .flaw import Flaw
from .flaw_acknowledgment import FlawAcknowledgment
from .flaw_acknowledgment_post import FlawAcknowledgmentPost
from .flaw_acknowledgment_put import FlawAcknowledgmentPut
from .flaw_classification import FlawClassification
from .flaw_classification_state import FlawClassificationState
from .flaw_comment import FlawComment
from .flaw_comment_post import FlawCommentPost
from .flaw_cvss import FlawCVSS
from .flaw_cvss_post import FlawCVSSPost
from .flaw_cvss_put import FlawCVSSPut
from .flaw_package_version import FlawPackageVersion
from .flaw_package_version_post import FlawPackageVersionPost
from .flaw_package_version_put import FlawPackageVersionPut
from .flaw_post import FlawPost
from .flaw_post_classification import FlawPostClassification
from .flaw_post_classification_state import FlawPostClassificationState
from .flaw_reference import FlawReference
from .flaw_reference_post import FlawReferencePost
from .flaw_reference_put import FlawReferencePut
from .flaw_reference_type import FlawReferenceType
from .flaw_report_data import FlawReportData
from .flaw_uuid_list import FlawUUIDList
from .flaw_version import FlawVersion
from .impact_enum import ImpactEnum
from .issuer_enum import IssuerEnum
from .major_incident_state_enum import MajorIncidentStateEnum
from .maturity_preliminary_enum import MaturityPreliminaryEnum
from .module_component import ModuleComponent
from .nist_cvss_validation_enum import NistCvssValidationEnum
from .osidb_api_v1_affects_bulk_create_response_200 import (
    OsidbApiV1AffectsBulkCreateResponse200,
)
from .osidb_api_v1_affects_bulk_destroy_response_200 import (
    OsidbApiV1AffectsBulkDestroyResponse200,
)
from .osidb_api_v1_affects_bulk_update_response_200 import (
    OsidbApiV1AffectsBulkUpdateResponse200,
)
from .osidb_api_v1_affects_create_response_201 import OsidbApiV1AffectsCreateResponse201
from .osidb_api_v1_affects_cvss_scores_create_response_201 import (
    OsidbApiV1AffectsCvssScoresCreateResponse201,
)
from .osidb_api_v1_affects_cvss_scores_destroy_response_200 import (
    OsidbApiV1AffectsCvssScoresDestroyResponse200,
)
from .osidb_api_v1_affects_cvss_scores_list_issuer import (
    OsidbApiV1AffectsCvssScoresListIssuer,
)
from .osidb_api_v1_affects_cvss_scores_list_response_200 import (
    OsidbApiV1AffectsCvssScoresListResponse200,
)
from .osidb_api_v1_affects_cvss_scores_retrieve_response_200 import (
    OsidbApiV1AffectsCvssScoresRetrieveResponse200,
)
from .osidb_api_v1_affects_cvss_scores_update_response_200 import (
    OsidbApiV1AffectsCvssScoresUpdateResponse200,
)
from .osidb_api_v1_affects_destroy_response_200 import (
    OsidbApiV1AffectsDestroyResponse200,
)
from .osidb_api_v1_affects_list_affectedness import OsidbApiV1AffectsListAffectedness
from .osidb_api_v1_affects_list_cvss_scores_issuer import (
    OsidbApiV1AffectsListCvssScoresIssuer,
)
from .osidb_api_v1_affects_list_flaw_impact import OsidbApiV1AffectsListFlawImpact
from .osidb_api_v1_affects_list_flaw_source import OsidbApiV1AffectsListFlawSource
from .osidb_api_v1_affects_list_impact import OsidbApiV1AffectsListImpact
from .osidb_api_v1_affects_list_order_item import OsidbApiV1AffectsListOrderItem
from .osidb_api_v1_affects_list_resolution import OsidbApiV1AffectsListResolution
from .osidb_api_v1_affects_list_response_200 import OsidbApiV1AffectsListResponse200
from .osidb_api_v1_affects_list_trackers_type import OsidbApiV1AffectsListTrackersType
from .osidb_api_v1_affects_retrieve_response_200 import (
    OsidbApiV1AffectsRetrieveResponse200,
)
from .osidb_api_v1_affects_update_response_200 import OsidbApiV1AffectsUpdateResponse200
from .osidb_api_v1_alerts_list_alert_type import OsidbApiV1AlertsListAlertType
from .osidb_api_v1_alerts_list_parent_model import OsidbApiV1AlertsListParentModel
from .osidb_api_v1_alerts_list_response_200 import OsidbApiV1AlertsListResponse200
from .osidb_api_v1_alerts_retrieve_response_200 import (
    OsidbApiV1AlertsRetrieveResponse200,
)
from .osidb_api_v1_audit_list_response_200 import OsidbApiV1AuditListResponse200
from .osidb_api_v1_audit_retrieve_response_200 import OsidbApiV1AuditRetrieveResponse200
from .osidb_api_v1_audit_update_response_200 import OsidbApiV1AuditUpdateResponse200
from .osidb_api_v1_flaws_acknowledgments_create_response_201 import (
    OsidbApiV1FlawsAcknowledgmentsCreateResponse201,
)
from .osidb_api_v1_flaws_acknowledgments_destroy_response_200 import (
    OsidbApiV1FlawsAcknowledgmentsDestroyResponse200,
)
from .osidb_api_v1_flaws_acknowledgments_list_response_200 import (
    OsidbApiV1FlawsAcknowledgmentsListResponse200,
)
from .osidb_api_v1_flaws_acknowledgments_retrieve_response_200 import (
    OsidbApiV1FlawsAcknowledgmentsRetrieveResponse200,
)
from .osidb_api_v1_flaws_acknowledgments_update_response_200 import (
    OsidbApiV1FlawsAcknowledgmentsUpdateResponse200,
)
from .osidb_api_v1_flaws_comments_create_response_201 import (
    OsidbApiV1FlawsCommentsCreateResponse201,
)
from .osidb_api_v1_flaws_comments_list_response_200 import (
    OsidbApiV1FlawsCommentsListResponse200,
)
from .osidb_api_v1_flaws_comments_retrieve_response_200 import (
    OsidbApiV1FlawsCommentsRetrieveResponse200,
)
from .osidb_api_v1_flaws_create_response_201 import OsidbApiV1FlawsCreateResponse201
from .osidb_api_v1_flaws_cvss_scores_create_response_201 import (
    OsidbApiV1FlawsCvssScoresCreateResponse201,
)
from .osidb_api_v1_flaws_cvss_scores_destroy_response_200 import (
    OsidbApiV1FlawsCvssScoresDestroyResponse200,
)
from .osidb_api_v1_flaws_cvss_scores_list_issuer import (
    OsidbApiV1FlawsCvssScoresListIssuer,
)
from .osidb_api_v1_flaws_cvss_scores_list_response_200 import (
    OsidbApiV1FlawsCvssScoresListResponse200,
)
from .osidb_api_v1_flaws_cvss_scores_retrieve_response_200 import (
    OsidbApiV1FlawsCvssScoresRetrieveResponse200,
)
from .osidb_api_v1_flaws_cvss_scores_update_response_200 import (
    OsidbApiV1FlawsCvssScoresUpdateResponse200,
)
from .osidb_api_v1_flaws_list_affects_affectedness import (
    OsidbApiV1FlawsListAffectsAffectedness,
)
from .osidb_api_v1_flaws_list_affects_impact import OsidbApiV1FlawsListAffectsImpact
from .osidb_api_v1_flaws_list_affects_resolution import (
    OsidbApiV1FlawsListAffectsResolution,
)
from .osidb_api_v1_flaws_list_affects_trackers_type import (
    OsidbApiV1FlawsListAffectsTrackersType,
)
from .osidb_api_v1_flaws_list_cvss_scores_issuer import (
    OsidbApiV1FlawsListCvssScoresIssuer,
)
from .osidb_api_v1_flaws_list_impact import OsidbApiV1FlawsListImpact
from .osidb_api_v1_flaws_list_major_incident_state import (
    OsidbApiV1FlawsListMajorIncidentState,
)
from .osidb_api_v1_flaws_list_nist_cvss_validation import (
    OsidbApiV1FlawsListNistCvssValidation,
)
from .osidb_api_v1_flaws_list_order_item import OsidbApiV1FlawsListOrderItem
from .osidb_api_v1_flaws_list_references_type import OsidbApiV1FlawsListReferencesType
from .osidb_api_v1_flaws_list_requires_cve_description import (
    OsidbApiV1FlawsListRequiresCveDescription,
)
from .osidb_api_v1_flaws_list_response_200 import OsidbApiV1FlawsListResponse200
from .osidb_api_v1_flaws_list_source import OsidbApiV1FlawsListSource
from .osidb_api_v1_flaws_list_workflow_state_item import (
    OsidbApiV1FlawsListWorkflowStateItem,
)
from .osidb_api_v1_flaws_package_versions_create_response_201 import (
    OsidbApiV1FlawsPackageVersionsCreateResponse201,
)
from .osidb_api_v1_flaws_package_versions_destroy_response_200 import (
    OsidbApiV1FlawsPackageVersionsDestroyResponse200,
)
from .osidb_api_v1_flaws_package_versions_list_response_200 import (
    OsidbApiV1FlawsPackageVersionsListResponse200,
)
from .osidb_api_v1_flaws_package_versions_retrieve_response_200 import (
    OsidbApiV1FlawsPackageVersionsRetrieveResponse200,
)
from .osidb_api_v1_flaws_package_versions_update_response_200 import (
    OsidbApiV1FlawsPackageVersionsUpdateResponse200,
)
from .osidb_api_v1_flaws_promote_create_response_200 import (
    OsidbApiV1FlawsPromoteCreateResponse200,
)
from .osidb_api_v1_flaws_references_create_response_201 import (
    OsidbApiV1FlawsReferencesCreateResponse201,
)
from .osidb_api_v1_flaws_references_destroy_response_200 import (
    OsidbApiV1FlawsReferencesDestroyResponse200,
)
from .osidb_api_v1_flaws_references_list_response_200 import (
    OsidbApiV1FlawsReferencesListResponse200,
)
from .osidb_api_v1_flaws_references_list_type import OsidbApiV1FlawsReferencesListType
from .osidb_api_v1_flaws_references_retrieve_response_200 import (
    OsidbApiV1FlawsReferencesRetrieveResponse200,
)
from .osidb_api_v1_flaws_references_update_response_200 import (
    OsidbApiV1FlawsReferencesUpdateResponse200,
)
from .osidb_api_v1_flaws_reject_create_response_200 import (
    OsidbApiV1FlawsRejectCreateResponse200,
)
from .osidb_api_v1_flaws_retrieve_response_200 import OsidbApiV1FlawsRetrieveResponse200
from .osidb_api_v1_flaws_update_response_200 import OsidbApiV1FlawsUpdateResponse200
from .osidb_api_v1_manifest_retrieve_response_200 import (
    OsidbApiV1ManifestRetrieveResponse200,
)
from .osidb_api_v1_schema_retrieve_format import OsidbApiV1SchemaRetrieveFormat
from .osidb_api_v1_schema_retrieve_lang import OsidbApiV1SchemaRetrieveLang
from .osidb_api_v1_schema_retrieve_response_200 import (
    OsidbApiV1SchemaRetrieveResponse200,
)
from .osidb_api_v1_status_retrieve_response_200 import (
    OsidbApiV1StatusRetrieveResponse200,
)
from .osidb_api_v1_status_retrieve_response_200_osidb_data import (
    OsidbApiV1StatusRetrieveResponse200OsidbData,
)
from .osidb_api_v1_status_retrieve_response_200_osidb_service import (
    OsidbApiV1StatusRetrieveResponse200OsidbService,
)
from .osidb_api_v1_trackers_create_response_201 import (
    OsidbApiV1TrackersCreateResponse201,
)
from .osidb_api_v1_trackers_list_affects_affectedness import (
    OsidbApiV1TrackersListAffectsAffectedness,
)
from .osidb_api_v1_trackers_list_affects_flaw_impact import (
    OsidbApiV1TrackersListAffectsFlawImpact,
)
from .osidb_api_v1_trackers_list_affects_flaw_source import (
    OsidbApiV1TrackersListAffectsFlawSource,
)
from .osidb_api_v1_trackers_list_affects_impact import (
    OsidbApiV1TrackersListAffectsImpact,
)
from .osidb_api_v1_trackers_list_affects_resolution import (
    OsidbApiV1TrackersListAffectsResolution,
)
from .osidb_api_v1_trackers_list_order_item import OsidbApiV1TrackersListOrderItem
from .osidb_api_v1_trackers_list_response_200 import OsidbApiV1TrackersListResponse200
from .osidb_api_v1_trackers_list_type import OsidbApiV1TrackersListType
from .osidb_api_v1_trackers_retrieve_response_200 import (
    OsidbApiV1TrackersRetrieveResponse200,
)
from .osidb_api_v1_trackers_update_response_200 import (
    OsidbApiV1TrackersUpdateResponse200,
)
from .osidb_healthy_retrieve_response_200 import OsidbHealthyRetrieveResponse200
from .osidb_whoami_retrieve_response_200 import OsidbWhoamiRetrieveResponse200
from .osidb_whoami_retrieve_response_200_profile import (
    OsidbWhoamiRetrieveResponse200Profile,
)
from .package import Package
from .package_ver import PackageVer
from .paginated_affect_cvss_list import PaginatedAffectCVSSList
from .paginated_affect_list import PaginatedAffectList
from .paginated_alert_list import PaginatedAlertList
from .paginated_audit_list import PaginatedAuditList
from .paginated_epss_list import PaginatedEPSSList
from .paginated_exploit_only_report_data_list import PaginatedExploitOnlyReportDataList
from .paginated_flaw_acknowledgment_list import PaginatedFlawAcknowledgmentList
from .paginated_flaw_comment_list import PaginatedFlawCommentList
from .paginated_flaw_cvss_list import PaginatedFlawCVSSList
from .paginated_flaw_list import PaginatedFlawList
from .paginated_flaw_package_version_list import PaginatedFlawPackageVersionList
from .paginated_flaw_reference_list import PaginatedFlawReferenceList
from .paginated_flaw_report_data_list import PaginatedFlawReportDataList
from .paginated_supported_products_list import PaginatedSupportedProductsList
from .paginated_tracker_list import PaginatedTrackerList
from .ps_stream_selection import PsStreamSelection
from .reject import Reject
from .requires_cve_description_enum import RequiresCveDescriptionEnum
from .resolution_enum import ResolutionEnum
from .source_be_0_enum import SourceBe0Enum
from .supported_products import SupportedProducts
from .token_obtain_pair import TokenObtainPair
from .token_refresh import TokenRefresh
from .token_verify import TokenVerify
from .tracker import Tracker
from .tracker_post import TrackerPost
from .tracker_report_data import TrackerReportData
from .tracker_suggestion import TrackerSuggestion
from .tracker_type import TrackerType
from .trackers_api_v1_file_create_response_200 import TrackersApiV1FileCreateResponse200
from .workflows_api_v1_workflows_adjust_create_response_200 import (
    WorkflowsApiV1WorkflowsAdjustCreateResponse200,
)
from .workflows_api_v1_workflows_retrieve_2_response_200 import (
    WorkflowsApiV1WorkflowsRetrieve2Response200,
)
from .workflows_api_v1_workflows_retrieve_response_200 import (
    WorkflowsApiV1WorkflowsRetrieveResponse200,
)
from .workflows_healthy_retrieve_response_200 import WorkflowsHealthyRetrieveResponse200
from .workflows_retrieve_response_200 import WorkflowsRetrieveResponse200

__all__ = (
    "Affect",
    "AffectBulkPostPutResponse",
    "AffectBulkPut",
    "AffectCVSS",
    "AffectCVSSPost",
    "AffectCVSSPut",
    "AffectednessEnum",
    "AffectPost",
    "AffectReportData",
    "Alert",
    "AlertTypeEnum",
    "Audit",
    "AuthTokenCreateResponse200",
    "AuthTokenRefreshCreateResponse200",
    "AuthTokenRetrieveResponse200",
    "AuthTokenVerifyCreateResponse200",
    "BlankEnum",
    "CollectorsApiV1StatusRetrieveResponse200",
    "CollectorsApiV1StatusRetrieveResponse200CollectorsItem",
    "CollectorsApiV1StatusRetrieveResponse200CollectorsItemData",
    "CollectorsApiV1StatusRetrieveResponse200CollectorsItemErrorType0",
    "CollectorsApiV1StatusRetrieveResponse200CollectorsItemState",
    "CollectorsHealthyRetrieveResponse200",
    "CollectorsRetrieveResponse200",
    "Comment",
    "CvssVersionEnum",
    "EPSS",
    "Erratum",
    "ExploitOnlyReportData",
    "ExploitOnlyReportDataSourceEnum",
    "ExploitsApiV1CollectUpdateResponse200",
    "ExploitsApiV1CveMapRetrieveResponse200",
    "ExploitsApiV1CveMapRetrieveResponse200Cves",
    "ExploitsApiV1EpssListResponse200",
    "ExploitsApiV1FlawDataListResponse200",
    "ExploitsApiV1ReportDataListResponse200",
    "ExploitsApiV1ReportDateRetrieveResponse200",
    "ExploitsApiV1ReportDateRetrieveResponse200ActionRequiredItem",
    "ExploitsApiV1ReportDateRetrieveResponse200NoActionItem",
    "ExploitsApiV1ReportDateRetrieveResponse200NotRelevantItem",
    "ExploitsApiV1ReportExplanationsRetrieveResponse200",
    "ExploitsApiV1ReportExplanationsRetrieveResponse200ExplanationsItem",
    "ExploitsApiV1ReportPendingRetrieveResponse200",
    "ExploitsApiV1ReportPendingRetrieveResponse200PendingActionsItem",
    "ExploitsApiV1StatusRetrieveResponse200",
    "ExploitsApiV1SupportedProductsListResponse200",
    "Flaw",
    "FlawAcknowledgment",
    "FlawAcknowledgmentPost",
    "FlawAcknowledgmentPut",
    "FlawClassification",
    "FlawClassificationState",
    "FlawComment",
    "FlawCommentPost",
    "FlawCVSS",
    "FlawCVSSPost",
    "FlawCVSSPut",
    "FlawPackageVersion",
    "FlawPackageVersionPost",
    "FlawPackageVersionPut",
    "FlawPost",
    "FlawPostClassification",
    "FlawPostClassificationState",
    "FlawReference",
    "FlawReferencePost",
    "FlawReferencePut",
    "FlawReferenceType",
    "FlawReportData",
    "FlawUUIDList",
    "FlawVersion",
    "ImpactEnum",
    "IssuerEnum",
    "MajorIncidentStateEnum",
    "MaturityPreliminaryEnum",
    "ModuleComponent",
    "NistCvssValidationEnum",
    "OsidbApiV1AffectsBulkCreateResponse200",
    "OsidbApiV1AffectsBulkDestroyResponse200",
    "OsidbApiV1AffectsBulkUpdateResponse200",
    "OsidbApiV1AffectsCreateResponse201",
    "OsidbApiV1AffectsCvssScoresCreateResponse201",
    "OsidbApiV1AffectsCvssScoresDestroyResponse200",
    "OsidbApiV1AffectsCvssScoresListIssuer",
    "OsidbApiV1AffectsCvssScoresListResponse200",
    "OsidbApiV1AffectsCvssScoresRetrieveResponse200",
    "OsidbApiV1AffectsCvssScoresUpdateResponse200",
    "OsidbApiV1AffectsDestroyResponse200",
    "OsidbApiV1AffectsListAffectedness",
    "OsidbApiV1AffectsListCvssScoresIssuer",
    "OsidbApiV1AffectsListFlawImpact",
    "OsidbApiV1AffectsListFlawSource",
    "OsidbApiV1AffectsListImpact",
    "OsidbApiV1AffectsListOrderItem",
    "OsidbApiV1AffectsListResolution",
    "OsidbApiV1AffectsListResponse200",
    "OsidbApiV1AffectsListTrackersType",
    "OsidbApiV1AffectsRetrieveResponse200",
    "OsidbApiV1AffectsUpdateResponse200",
    "OsidbApiV1AlertsListAlertType",
    "OsidbApiV1AlertsListParentModel",
    "OsidbApiV1AlertsListResponse200",
    "OsidbApiV1AlertsRetrieveResponse200",
    "OsidbApiV1AuditListResponse200",
    "OsidbApiV1AuditRetrieveResponse200",
    "OsidbApiV1AuditUpdateResponse200",
    "OsidbApiV1FlawsAcknowledgmentsCreateResponse201",
    "OsidbApiV1FlawsAcknowledgmentsDestroyResponse200",
    "OsidbApiV1FlawsAcknowledgmentsListResponse200",
    "OsidbApiV1FlawsAcknowledgmentsRetrieveResponse200",
    "OsidbApiV1FlawsAcknowledgmentsUpdateResponse200",
    "OsidbApiV1FlawsCommentsCreateResponse201",
    "OsidbApiV1FlawsCommentsListResponse200",
    "OsidbApiV1FlawsCommentsRetrieveResponse200",
    "OsidbApiV1FlawsCreateResponse201",
    "OsidbApiV1FlawsCvssScoresCreateResponse201",
    "OsidbApiV1FlawsCvssScoresDestroyResponse200",
    "OsidbApiV1FlawsCvssScoresListIssuer",
    "OsidbApiV1FlawsCvssScoresListResponse200",
    "OsidbApiV1FlawsCvssScoresRetrieveResponse200",
    "OsidbApiV1FlawsCvssScoresUpdateResponse200",
    "OsidbApiV1FlawsListAffectsAffectedness",
    "OsidbApiV1FlawsListAffectsImpact",
    "OsidbApiV1FlawsListAffectsResolution",
    "OsidbApiV1FlawsListAffectsTrackersType",
    "OsidbApiV1FlawsListCvssScoresIssuer",
    "OsidbApiV1FlawsListImpact",
    "OsidbApiV1FlawsListMajorIncidentState",
    "OsidbApiV1FlawsListNistCvssValidation",
    "OsidbApiV1FlawsListOrderItem",
    "OsidbApiV1FlawsListReferencesType",
    "OsidbApiV1FlawsListRequiresCveDescription",
    "OsidbApiV1FlawsListResponse200",
    "OsidbApiV1FlawsListSource",
    "OsidbApiV1FlawsListWorkflowStateItem",
    "OsidbApiV1FlawsPackageVersionsCreateResponse201",
    "OsidbApiV1FlawsPackageVersionsDestroyResponse200",
    "OsidbApiV1FlawsPackageVersionsListResponse200",
    "OsidbApiV1FlawsPackageVersionsRetrieveResponse200",
    "OsidbApiV1FlawsPackageVersionsUpdateResponse200",
    "OsidbApiV1FlawsPromoteCreateResponse200",
    "OsidbApiV1FlawsReferencesCreateResponse201",
    "OsidbApiV1FlawsReferencesDestroyResponse200",
    "OsidbApiV1FlawsReferencesListResponse200",
    "OsidbApiV1FlawsReferencesListType",
    "OsidbApiV1FlawsReferencesRetrieveResponse200",
    "OsidbApiV1FlawsReferencesUpdateResponse200",
    "OsidbApiV1FlawsRejectCreateResponse200",
    "OsidbApiV1FlawsRetrieveResponse200",
    "OsidbApiV1FlawsUpdateResponse200",
    "OsidbApiV1ManifestRetrieveResponse200",
    "OsidbApiV1SchemaRetrieveFormat",
    "OsidbApiV1SchemaRetrieveLang",
    "OsidbApiV1SchemaRetrieveResponse200",
    "OsidbApiV1StatusRetrieveResponse200",
    "OsidbApiV1StatusRetrieveResponse200OsidbData",
    "OsidbApiV1StatusRetrieveResponse200OsidbService",
    "OsidbApiV1TrackersCreateResponse201",
    "OsidbApiV1TrackersListAffectsAffectedness",
    "OsidbApiV1TrackersListAffectsFlawImpact",
    "OsidbApiV1TrackersListAffectsFlawSource",
    "OsidbApiV1TrackersListAffectsImpact",
    "OsidbApiV1TrackersListAffectsResolution",
    "OsidbApiV1TrackersListOrderItem",
    "OsidbApiV1TrackersListResponse200",
    "OsidbApiV1TrackersListType",
    "OsidbApiV1TrackersRetrieveResponse200",
    "OsidbApiV1TrackersUpdateResponse200",
    "OsidbHealthyRetrieveResponse200",
    "OsidbWhoamiRetrieveResponse200",
    "OsidbWhoamiRetrieveResponse200Profile",
    "Package",
    "PackageVer",
    "PaginatedAffectCVSSList",
    "PaginatedAffectList",
    "PaginatedAlertList",
    "PaginatedAuditList",
    "PaginatedEPSSList",
    "PaginatedExploitOnlyReportDataList",
    "PaginatedFlawAcknowledgmentList",
    "PaginatedFlawCommentList",
    "PaginatedFlawCVSSList",
    "PaginatedFlawList",
    "PaginatedFlawPackageVersionList",
    "PaginatedFlawReferenceList",
    "PaginatedFlawReportDataList",
    "PaginatedSupportedProductsList",
    "PaginatedTrackerList",
    "PsStreamSelection",
    "Reject",
    "RequiresCveDescriptionEnum",
    "ResolutionEnum",
    "SourceBe0Enum",
    "SupportedProducts",
    "TokenObtainPair",
    "TokenRefresh",
    "TokenVerify",
    "Tracker",
    "TrackerPost",
    "TrackerReportData",
    "TrackersApiV1FileCreateResponse200",
    "TrackerSuggestion",
    "TrackerType",
    "WorkflowsApiV1WorkflowsAdjustCreateResponse200",
    "WorkflowsApiV1WorkflowsRetrieve2Response200",
    "WorkflowsApiV1WorkflowsRetrieveResponse200",
    "WorkflowsHealthyRetrieveResponse200",
    "WorkflowsRetrieveResponse200",
)
