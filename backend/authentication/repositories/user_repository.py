# Epic Title: Integrate Authentication with Bank Security Infrastructure

from backend.authentication.models.user import User
from backend.database import db

class UserRepository:

    def find_by_username(self, username: str) -> User:
        return User.query.filter_by(username=username).first()

    def save_user(self, user: User) -> None:
        db.session.add(user)
        db.session.commit()