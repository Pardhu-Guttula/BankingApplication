# Epic Title: Integrate Authentication with Bank Security Infrastructure

import logging
from backend.authentication.repositories.user_repository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()

    def authenticate(self, username: str, password: str) -> bool:
        user = self.user_repository.find_by_username(username)
        if user and user.check_password(password):
            logging.info(f'User {username} authenticated successfully.')
            return True
        logging.warning(f'Failed authentication attempt for user {username}.')
        return False