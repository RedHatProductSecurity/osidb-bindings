from .osidb_api_v1_affects_cvss_scores_list import *
from .osidb_api_v1_affects_cvss_scores_retrieve import *
from .osidb_api_v1_affects_list import *
from .osidb_api_v1_affects_retrieve import *
from .osidb_api_v1_alerts_list import *
from .osidb_api_v1_alerts_retrieve import *
from .osidb_api_v1_audit_list import *
from .osidb_api_v1_audit_retrieve import *
from .osidb_api_v1_audit_update import *
from .osidb_api_v1_available_flaws_retrieve import *
from .osidb_api_v1_flaws_acknowledgments_create import *
from .osidb_api_v1_flaws_acknowledgments_destroy import *
from .osidb_api_v1_flaws_acknowledgments_list import *
from .osidb_api_v1_flaws_acknowledgments_retrieve import *
from .osidb_api_v1_flaws_acknowledgments_update import *
from .osidb_api_v1_flaws_comments_create import *
from .osidb_api_v1_flaws_comments_list import *
from .osidb_api_v1_flaws_comments_retrieve import *
from .osidb_api_v1_flaws_create import *
from .osidb_api_v1_flaws_cvss_scores_create import *
from .osidb_api_v1_flaws_cvss_scores_destroy import *
from .osidb_api_v1_flaws_cvss_scores_list import *
from .osidb_api_v1_flaws_cvss_scores_retrieve import *
from .osidb_api_v1_flaws_cvss_scores_update import *
from .osidb_api_v1_flaws_labels_create import *
from .osidb_api_v1_flaws_labels_destroy import *
from .osidb_api_v1_flaws_labels_list import *
from .osidb_api_v1_flaws_labels_retrieve import *
from .osidb_api_v1_flaws_labels_update import *
from .osidb_api_v1_flaws_list import *
from .osidb_api_v1_flaws_package_versions_create import *
from .osidb_api_v1_flaws_package_versions_destroy import *
from .osidb_api_v1_flaws_package_versions_list import *
from .osidb_api_v1_flaws_package_versions_retrieve import *
from .osidb_api_v1_flaws_package_versions_update import *
from .osidb_api_v1_flaws_promote_create import *
from .osidb_api_v1_flaws_references_create import *
from .osidb_api_v1_flaws_references_destroy import *
from .osidb_api_v1_flaws_references_list import *
from .osidb_api_v1_flaws_references_retrieve import *
from .osidb_api_v1_flaws_references_update import *
from .osidb_api_v1_flaws_reject_create import *
from .osidb_api_v1_flaws_retrieve import *
from .osidb_api_v1_flaws_update import *
from .osidb_api_v1_labels_list import *
from .osidb_api_v1_labels_retrieve import *
from .osidb_api_v1_manifest_retrieve import *
from .osidb_api_v1_schema_retrieve import *
from .osidb_api_v1_status_retrieve import *
from .osidb_api_v1_trackers_create import *
from .osidb_api_v1_trackers_list import *
from .osidb_api_v1_trackers_retrieve import *
from .osidb_api_v1_trackers_update import *
from .osidb_api_v2_affects_bulk_create import *
from .osidb_api_v2_affects_bulk_destroy import *
from .osidb_api_v2_affects_bulk_update import *
from .osidb_api_v2_affects_create import *
from .osidb_api_v2_affects_cvss_scores_create import *
from .osidb_api_v2_affects_cvss_scores_destroy import *
from .osidb_api_v2_affects_cvss_scores_list import *
from .osidb_api_v2_affects_cvss_scores_retrieve import *
from .osidb_api_v2_affects_cvss_scores_update import *
from .osidb_api_v2_affects_destroy import *
from .osidb_api_v2_affects_list import *
from .osidb_api_v2_affects_retrieve import *
from .osidb_api_v2_affects_update import *
from .osidb_api_v2_flaws_create import *
from .osidb_api_v2_flaws_cvss_scores_create import *
from .osidb_api_v2_flaws_cvss_scores_destroy import *
from .osidb_api_v2_flaws_cvss_scores_list import *
from .osidb_api_v2_flaws_cvss_scores_retrieve import *
from .osidb_api_v2_flaws_cvss_scores_update import *
from .osidb_api_v2_flaws_list import *
from .osidb_api_v2_flaws_retrieve import *
from .osidb_api_v2_flaws_update import *
from .osidb_api_v2_trackers_create import *
from .osidb_api_v2_trackers_list import *
from .osidb_api_v2_trackers_retrieve import *
from .osidb_api_v2_trackers_update import *
from .osidb_healthy_retrieve import *
from .osidb_integrations_partial_update import *
from .osidb_integrations_retrieve import *
from .osidb_whoami_retrieve import *

ENDPOINT_NAMES = [
    "osidb_api_v1_affects_list",
    "osidb_api_v1_affects_cvss_scores_list",
    "osidb_api_v1_affects_cvss_scores_retrieve",
    "osidb_api_v1_affects_retrieve",
    "osidb_api_v1_alerts_list",
    "osidb_api_v1_alerts_retrieve",
    "osidb_api_v1_audit_list",
    "osidb_api_v1_audit_retrieve",
    "osidb_api_v1_audit_update",
    "osidb_api_v1_available_flaws_retrieve",
    "osidb_api_v1_flaws_list",
    "osidb_api_v1_flaws_create",
    "osidb_api_v1_flaws_acknowledgments_list",
    "osidb_api_v1_flaws_acknowledgments_create",
    "osidb_api_v1_flaws_acknowledgments_retrieve",
    "osidb_api_v1_flaws_acknowledgments_update",
    "osidb_api_v1_flaws_acknowledgments_destroy",
    "osidb_api_v1_flaws_comments_list",
    "osidb_api_v1_flaws_comments_create",
    "osidb_api_v1_flaws_comments_retrieve",
    "osidb_api_v1_flaws_cvss_scores_list",
    "osidb_api_v1_flaws_cvss_scores_create",
    "osidb_api_v1_flaws_cvss_scores_retrieve",
    "osidb_api_v1_flaws_cvss_scores_update",
    "osidb_api_v1_flaws_cvss_scores_destroy",
    "osidb_api_v1_flaws_labels_list",
    "osidb_api_v1_flaws_labels_create",
    "osidb_api_v1_flaws_labels_retrieve",
    "osidb_api_v1_flaws_labels_update",
    "osidb_api_v1_flaws_labels_destroy",
    "osidb_api_v1_flaws_package_versions_list",
    "osidb_api_v1_flaws_package_versions_create",
    "osidb_api_v1_flaws_package_versions_retrieve",
    "osidb_api_v1_flaws_package_versions_update",
    "osidb_api_v1_flaws_package_versions_destroy",
    "osidb_api_v1_flaws_promote_create",
    "osidb_api_v1_flaws_references_list",
    "osidb_api_v1_flaws_references_create",
    "osidb_api_v1_flaws_references_retrieve",
    "osidb_api_v1_flaws_references_update",
    "osidb_api_v1_flaws_references_destroy",
    "osidb_api_v1_flaws_reject_create",
    "osidb_api_v1_flaws_retrieve",
    "osidb_api_v1_flaws_update",
    "osidb_api_v1_labels_list",
    "osidb_api_v1_labels_retrieve",
    "osidb_api_v1_manifest_retrieve",
    "osidb_api_v1_schema_retrieve",
    "osidb_api_v1_status_retrieve",
    "osidb_api_v1_trackers_list",
    "osidb_api_v1_trackers_create",
    "osidb_api_v1_trackers_retrieve",
    "osidb_api_v1_trackers_update",
    "osidb_api_v2_affects_list",
    "osidb_api_v2_affects_create",
    "osidb_api_v2_affects_cvss_scores_list",
    "osidb_api_v2_affects_cvss_scores_create",
    "osidb_api_v2_affects_cvss_scores_retrieve",
    "osidb_api_v2_affects_cvss_scores_update",
    "osidb_api_v2_affects_cvss_scores_destroy",
    "osidb_api_v2_affects_retrieve",
    "osidb_api_v2_affects_update",
    "osidb_api_v2_affects_destroy",
    "osidb_api_v2_affects_bulk_update",
    "osidb_api_v2_affects_bulk_create",
    "osidb_api_v2_affects_bulk_destroy",
    "osidb_api_v2_flaws_list",
    "osidb_api_v2_flaws_create",
    "osidb_api_v2_flaws_cvss_scores_list",
    "osidb_api_v2_flaws_cvss_scores_create",
    "osidb_api_v2_flaws_cvss_scores_retrieve",
    "osidb_api_v2_flaws_cvss_scores_update",
    "osidb_api_v2_flaws_cvss_scores_destroy",
    "osidb_api_v2_flaws_retrieve",
    "osidb_api_v2_flaws_update",
    "osidb_api_v2_trackers_list",
    "osidb_api_v2_trackers_create",
    "osidb_api_v2_trackers_retrieve",
    "osidb_api_v2_trackers_update",
    "osidb_healthy_retrieve",
    "osidb_integrations_retrieve",
    "osidb_integrations_partial_update",
    "osidb_whoami_retrieve",
]
