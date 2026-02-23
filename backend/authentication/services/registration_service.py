# Epic Title: Develop User Registration Capability

from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash
from backend.authentication.repositories.user_repository import UserRepository
from backend.authentication.models.user import User
from backend.authentication.utils.email_utils import send_confirmation_email
import re

class RegistrationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, db: Session, name: str, email: str, password: str) -> Optional[User]:
        if not self.is_email_valid(email):
            raise ValueError("Invalid email format")
        if not self.is_password_secure(password):
            raise ValueError("Password does not meet security criteria")
        
        if self.user_repository.get_user_by_email(email):
            raise ValueError("Email is already registered")

        password_hash = generate_password_hash(password)
        new_user = self.user_repository.create_user(name, email, password_hash)
        send_confirmation_email(new_user.email)
        return new_user
    
    def is_email_valid(self, email: str) -> bool:
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(email_regex, email) is not None

    def is_password_secure(self, password: str) -> bool:
        return len(password) >= 8