from enum import Enum


class StatsApiV1BetaFlawsRetrieveGroupByItem(str, Enum):
    AGE_BUCKET = "age_bucket"
    EMBARGO_DURATION_BUCKET = "embargo_duration_bucket"
    IMPACT = "impact"
    PS_PRODUCT = "ps_product"
    WORKFLOW_NAME = "workflow_name"
    WORKFLOW_STATE = "workflow_state"

    def __str__(self) -> str:
        return str(self.value)
