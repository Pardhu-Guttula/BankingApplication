# Epic Title: Banking Platform — Core API

from backend.models.service_modifications.modification_request import ModificationRequest
from backend.models.service_modifications.validation_result import ValidationResult

class ValidationService:
    @staticmethod
    def validate(request: ModificationRequest) -> ValidationResult:
        if not request.user_id:
            return ValidationResult(False, "Missing user ID")
        if not request.modification_type:
            return ValidationResult(False, "Missing modification type")
        if not request.data:
            return ValidationResult(False, "Missing data")

        # Example business rule validation
        if request.modification_type == "account_upgrade" and "account_level" not in request.data:
            return ValidationResult(False, "Missing account level for modification type 'account_upgrade'")

        return ValidationResult(True)