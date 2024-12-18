from enum import Enum


class OsidbApiV1TrackersListOrderItem(str, Enum):
    AFFECTS_AFFECTEDNESS = "affects__affectedness"
    AFFECTS_CREATED_DT = "affects__created_dt"
    AFFECTS_EMBARGOED = "affects__embargoed"
    AFFECTS_FLAW_COMPONENTS = "affects__flaw__components"
    AFFECTS_FLAW_CREATED_DT = "affects__flaw__created_dt"
    AFFECTS_FLAW_CVE_ID = "affects__flaw__cve_id"
    AFFECTS_FLAW_CWE_ID = "affects__flaw__cwe_id"
    AFFECTS_FLAW_EMBARGOED = "affects__flaw__embargoed"
    AFFECTS_FLAW_IMPACT = "affects__flaw__impact"
    AFFECTS_FLAW_REPORTED_DT = "affects__flaw__reported_dt"
    AFFECTS_FLAW_SOURCE = "affects__flaw__source"
    AFFECTS_FLAW_UNEMBARGO_DT = "affects__flaw__unembargo_dt"
    AFFECTS_FLAW_UPDATED_DT = "affects__flaw__updated_dt"
    AFFECTS_FLAW_UUID = "affects__flaw__uuid"
    AFFECTS_IMPACT = "affects__impact"
    AFFECTS_PS_COMPONENT = "affects__ps_component"
    AFFECTS_PS_MODULE = "affects__ps_module"
    AFFECTS_RESOLUTION = "affects__resolution"
    AFFECTS_UPDATED_DT = "affects__updated_dt"
    AFFECTS_UUID = "affects__uuid"
    CREATED_DT = "created_dt"
    EMBARGOED = "embargoed"
    EXTERNAL_SYSTEM_ID = "external_system_id"
    PS_UPDATE_STREAM = "ps_update_stream"
    RESOLUTION = "resolution"
    STATUS = "status"
    TYPE = "type"
    UPDATED_DT = "updated_dt"
    UUID = "uuid"
    VALUE_0 = "-affects__affectedness"
    VALUE_1 = "-affects__created_dt"
    VALUE_10 = "-affects__flaw__source"
    VALUE_11 = "-affects__flaw__unembargo_dt"
    VALUE_12 = "-affects__flaw__updated_dt"
    VALUE_13 = "-affects__flaw__uuid"
    VALUE_14 = "-affects__impact"
    VALUE_15 = "-affects__ps_component"
    VALUE_16 = "-affects__ps_module"
    VALUE_17 = "-affects__resolution"
    VALUE_18 = "-affects__updated_dt"
    VALUE_19 = "-affects__uuid"
    VALUE_2 = "-affects__embargoed"
    VALUE_20 = "-created_dt"
    VALUE_21 = "-embargoed"
    VALUE_22 = "-external_system_id"
    VALUE_23 = "-ps_update_stream"
    VALUE_24 = "-resolution"
    VALUE_25 = "-status"
    VALUE_26 = "-type"
    VALUE_27 = "-updated_dt"
    VALUE_28 = "-uuid"
    VALUE_3 = "-affects__flaw__components"
    VALUE_4 = "-affects__flaw__created_dt"
    VALUE_5 = "-affects__flaw__cve_id"
    VALUE_6 = "-affects__flaw__cwe_id"
    VALUE_7 = "-affects__flaw__embargoed"
    VALUE_8 = "-affects__flaw__impact"
    VALUE_9 = "-affects__flaw__reported_dt"

    def __str__(self) -> str:
        return str(self.value)
