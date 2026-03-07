# Epic Title: Banking Platform — Core API

from backend.models.account_opening.request_form import RequestForm

class RequestValidationService:
    @staticmethod
    def validate(request_form: RequestForm) -> bool:
        if not request_form.user_id:
            return False
        if not request_form.account_type:
            return False
        if request_form.initial_deposit < 0:
            return False
        return True