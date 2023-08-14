from enum import Enum


class OsidbApiV1TrackersListOrderItem(str, Enum):
    VALUE_0 = "-affects__affectedness"
    VALUE_1 = "-affects__created_dt"
    VALUE_2 = "-affects__cvss2"
    VALUE_3 = "-affects__cvss2_score"
    VALUE_4 = "-affects__cvss3"
    VALUE_5 = "-affects__cvss3_score"
    VALUE_6 = "-affects__flaw__component"
    VALUE_7 = "-affects__flaw__created_dt"
    VALUE_8 = "-affects__flaw__cve_id"
    VALUE_9 = "-affects__flaw__cvss2"
    VALUE_10 = "-affects__flaw__cvss2_score"
    VALUE_11 = "-affects__flaw__cvss3"
    VALUE_12 = "-affects__flaw__cvss3_score"
    VALUE_13 = "-affects__flaw__cwe_id"
    VALUE_14 = "-affects__flaw__impact"
    VALUE_15 = "-affects__flaw__nvd_cvss2"
    VALUE_16 = "-affects__flaw__nvd_cvss3"
    VALUE_17 = "-affects__flaw__reported_dt"
    VALUE_18 = "-affects__flaw__source"
    VALUE_19 = "-affects__flaw__type"
    VALUE_20 = "-affects__flaw__unembargo_dt"
    VALUE_21 = "-affects__flaw__updated_dt"
    VALUE_22 = "-affects__flaw__uuid"
    VALUE_23 = "-affects__impact"
    VALUE_24 = "-affects__ps_component"
    VALUE_25 = "-affects__ps_module"
    VALUE_26 = "-affects__resolution"
    VALUE_27 = "-affects__type"
    VALUE_28 = "-affects__updated_dt"
    VALUE_29 = "-affects__uuid"
    VALUE_30 = "-created_dt"
    VALUE_31 = "-external_system_id"
    VALUE_32 = "-ps_update_stream"
    VALUE_33 = "-resolution"
    VALUE_34 = "-status"
    VALUE_35 = "-type"
    VALUE_36 = "-updated_dt"
    VALUE_37 = "-uuid"
    AFFECTS_AFFECTEDNESS = "affects__affectedness"
    AFFECTS_CREATED_DT = "affects__created_dt"
    AFFECTS_CVSS2 = "affects__cvss2"
    AFFECTS_CVSS2_SCORE = "affects__cvss2_score"
    AFFECTS_CVSS3 = "affects__cvss3"
    AFFECTS_CVSS3_SCORE = "affects__cvss3_score"
    AFFECTS_FLAW_COMPONENT = "affects__flaw__component"
    AFFECTS_FLAW_CREATED_DT = "affects__flaw__created_dt"
    AFFECTS_FLAW_CVE_ID = "affects__flaw__cve_id"
    AFFECTS_FLAW_CVSS2 = "affects__flaw__cvss2"
    AFFECTS_FLAW_CVSS2_SCORE = "affects__flaw__cvss2_score"
    AFFECTS_FLAW_CVSS3 = "affects__flaw__cvss3"
    AFFECTS_FLAW_CVSS3_SCORE = "affects__flaw__cvss3_score"
    AFFECTS_FLAW_CWE_ID = "affects__flaw__cwe_id"
    AFFECTS_FLAW_IMPACT = "affects__flaw__impact"
    AFFECTS_FLAW_NVD_CVSS2 = "affects__flaw__nvd_cvss2"
    AFFECTS_FLAW_NVD_CVSS3 = "affects__flaw__nvd_cvss3"
    AFFECTS_FLAW_REPORTED_DT = "affects__flaw__reported_dt"
    AFFECTS_FLAW_SOURCE = "affects__flaw__source"
    AFFECTS_FLAW_TYPE = "affects__flaw__type"
    AFFECTS_FLAW_UNEMBARGO_DT = "affects__flaw__unembargo_dt"
    AFFECTS_FLAW_UPDATED_DT = "affects__flaw__updated_dt"
    AFFECTS_FLAW_UUID = "affects__flaw__uuid"
    AFFECTS_IMPACT = "affects__impact"
    AFFECTS_PS_COMPONENT = "affects__ps_component"
    AFFECTS_PS_MODULE = "affects__ps_module"
    AFFECTS_RESOLUTION = "affects__resolution"
    AFFECTS_TYPE = "affects__type"
    AFFECTS_UPDATED_DT = "affects__updated_dt"
    AFFECTS_UUID = "affects__uuid"
    CREATED_DT = "created_dt"
    EXTERNAL_SYSTEM_ID = "external_system_id"
    PS_UPDATE_STREAM = "ps_update_stream"
    RESOLUTION = "resolution"
    STATUS = "status"
    TYPE = "type"
    UPDATED_DT = "updated_dt"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
