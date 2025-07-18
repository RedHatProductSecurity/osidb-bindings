from enum import Enum


class OsidbApiV1AffectsListOrderItem(str, Enum):
    AFFECTEDNESS = "affectedness"
    CREATED_DT = "created_dt"
    CVE_ID = "cve_id"
    CVSS_SCORES_COMMENT = "cvss_scores__comment"
    CVSS_SCORES_CREATED_DT = "cvss_scores__created_dt"
    CVSS_SCORES_CVSS_VERSION = "cvss_scores__cvss_version"
    CVSS_SCORES_ISSUER = "cvss_scores__issuer"
    CVSS_SCORES_SCORE = "cvss_scores__score"
    CVSS_SCORES_UPDATED_DT = "cvss_scores__updated_dt"
    CVSS_SCORES_UUID = "cvss_scores__uuid"
    CVSS_SCORES_VECTOR = "cvss_scores__vector"
    EMBARGOED = "embargoed"
    FLAW_COMPONENTS = "flaw__components"
    FLAW_CREATED_DT = "flaw__created_dt"
    FLAW_CVE_ID = "flaw__cve_id"
    FLAW_CWE_ID = "flaw__cwe_id"
    FLAW_EMBARGOED = "flaw__embargoed"
    FLAW_IMPACT = "flaw__impact"
    FLAW_REPORTED_DT = "flaw__reported_dt"
    FLAW_SOURCE = "flaw__source"
    FLAW_UNEMBARGO_DT = "flaw__unembargo_dt"
    FLAW_UPDATED_DT = "flaw__updated_dt"
    FLAW_UUID = "flaw__uuid"
    IMPACT = "impact"
    PS_COMPONENT = "ps_component"
    PS_MODULE = "ps_module"
    RESOLUTION = "resolution"
    TRACKERS_CREATED_DT = "trackers__created_dt"
    TRACKERS_EMBARGOED = "trackers__embargoed"
    TRACKERS_EXTERNAL_SYSTEM_ID = "trackers__external_system_id"
    TRACKERS_PS_UPDATE_STREAM = "trackers__ps_update_stream"
    TRACKERS_RESOLUTION = "trackers__resolution"
    TRACKERS_STATUS = "trackers__status"
    TRACKERS_TYPE = "trackers__type"
    TRACKERS_UPDATED_DT = "trackers__updated_dt"
    TRACKERS_UUID = "trackers__uuid"
    UPDATED_DT = "updated_dt"
    UUID = "uuid"
    VALUE_0 = "-affectedness"
    VALUE_1 = "-created_dt"
    VALUE_10 = "-cvss_scores__vector"
    VALUE_11 = "-embargoed"
    VALUE_12 = "-flaw__components"
    VALUE_13 = "-flaw__created_dt"
    VALUE_14 = "-flaw__cve_id"
    VALUE_15 = "-flaw__cwe_id"
    VALUE_16 = "-flaw__embargoed"
    VALUE_17 = "-flaw__impact"
    VALUE_18 = "-flaw__reported_dt"
    VALUE_19 = "-flaw__source"
    VALUE_2 = "-cve_id"
    VALUE_20 = "-flaw__unembargo_dt"
    VALUE_21 = "-flaw__updated_dt"
    VALUE_22 = "-flaw__uuid"
    VALUE_23 = "-impact"
    VALUE_24 = "-ps_component"
    VALUE_25 = "-ps_module"
    VALUE_26 = "-resolution"
    VALUE_27 = "-trackers__created_dt"
    VALUE_28 = "-trackers__embargoed"
    VALUE_29 = "-trackers__external_system_id"
    VALUE_3 = "-cvss_scores__comment"
    VALUE_30 = "-trackers__ps_update_stream"
    VALUE_31 = "-trackers__resolution"
    VALUE_32 = "-trackers__status"
    VALUE_33 = "-trackers__type"
    VALUE_34 = "-trackers__updated_dt"
    VALUE_35 = "-trackers__uuid"
    VALUE_36 = "-updated_dt"
    VALUE_37 = "-uuid"
    VALUE_4 = "-cvss_scores__created_dt"
    VALUE_5 = "-cvss_scores__cvss_version"
    VALUE_6 = "-cvss_scores__issuer"
    VALUE_7 = "-cvss_scores__score"
    VALUE_8 = "-cvss_scores__updated_dt"
    VALUE_9 = "-cvss_scores__uuid"

    def __str__(self) -> str:
        return str(self.value)
