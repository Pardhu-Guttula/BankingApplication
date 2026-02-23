# Epic Title: Create User Table in PostgreSQL

from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash
from backend.authentication.repositories.user_repository import UserRepository

class RegistrationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, db: Session, name: str, email: str, password: str):
        if self.user_repository.get_user_by_email(email):
            raise ValueError("Email is already registered")
        
        password_hash = generate_password_hash(password)
        new_user = self.user_repository.create_user(name, email, password_hash)
        return new_user