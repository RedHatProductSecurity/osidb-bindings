from enum import Enum


class NotAffectedJustificationEnum(str, Enum):
    COMPONENT_NOT_PRESENT = "Component not Present"
    INLINE_MITIGATIONS_ALREADY_EXIST = "Inline Mitigations already Exist"
    VULNERABLE_CODE_CANNOT_BE_CONTROLLED_BY_ADVERSARY = (
        "Vulnerable Code cannot be Controlled by Adversary"
    )
    VULNERABLE_CODE_NOT_IN_EXECUTE_PATH = "Vulnerable Code not in Execute Path"
    VULNERABLE_CODE_NOT_PRESENT = "Vulnerable Code not Present"

    def __str__(self) -> str:
        return str(self.value)
