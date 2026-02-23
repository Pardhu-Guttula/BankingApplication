# Epic Title: Create User Table in PostgreSQL

from sqlalchemy.orm import Session
from backend.authentication.models.user import User
from typing import Optional

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, name: str, email: str, password_hash: str) -> User:
        db_user = User(name=name, email=email, password_hash=password_hash)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()