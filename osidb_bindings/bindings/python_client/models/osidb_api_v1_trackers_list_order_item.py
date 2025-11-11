from enum import Enum


class OsidbApiV1TrackersListOrderItem(str, Enum):
    AFFECTS_EMBARGOED = "affects__embargoed"
    AFFECTS_FLAW_EMBARGOED = "affects__flaw__embargoed"
    CREATED_DT = "created_dt"
    CVE_ID = "cve_id"
    EMBARGOED = "embargoed"
    EXTERNAL_SYSTEM_ID = "external_system_id"
    PS_UPDATE_STREAM = "ps_update_stream"
    RESOLUTION = "resolution"
    STATUS = "status"
    TYPE = "type"
    UPDATED_DT = "updated_dt"
    UUID = "uuid"
    VALUE_0 = "-affects__embargoed"
    VALUE_1 = "-affects__flaw__embargoed"
    VALUE_10 = "-updated_dt"
    VALUE_11 = "-uuid"
    VALUE_2 = "-created_dt"
    VALUE_3 = "-cve_id"
    VALUE_4 = "-embargoed"
    VALUE_5 = "-external_system_id"
    VALUE_6 = "-ps_update_stream"
    VALUE_7 = "-resolution"
    VALUE_8 = "-status"
    VALUE_9 = "-type"

    def __str__(self) -> str:
        return str(self.value)
