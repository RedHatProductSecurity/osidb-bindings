from enum import Enum


class OsidbApiV1SyncManagersListOrderItem(str, Enum):
    ID = "id"
    LAST_CONSECUTIVE_FAILURES = "last_consecutive_failures"
    LAST_CONSECUTIVE_RESCHEDULES = "last_consecutive_reschedules"
    LAST_FAILED_DT = "last_failed_dt"
    LAST_FINISHED_DT = "last_finished_dt"
    LAST_RESCHEDULED_DT = "last_rescheduled_dt"
    LAST_SCHEDULED_DT = "last_scheduled_dt"
    LAST_STARTED_DT = "last_started_dt"
    NAME = "name"
    PERMANENTLY_FAILED = "permanently_failed"
    SYNC_ID = "sync_id"
    VALUE_0 = "-id"
    VALUE_1 = "-last_consecutive_failures"
    VALUE_10 = "-sync_id"
    VALUE_2 = "-last_consecutive_reschedules"
    VALUE_3 = "-last_failed_dt"
    VALUE_4 = "-last_finished_dt"
    VALUE_5 = "-last_rescheduled_dt"
    VALUE_6 = "-last_scheduled_dt"
    VALUE_7 = "-last_started_dt"
    VALUE_8 = "-name"
    VALUE_9 = "-permanently_failed"

    def __str__(self) -> str:
        return str(self.value)
