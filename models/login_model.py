from model import Model
from user_access.user import User


class LoginModel(Model):
    current_user: User

    def __init__(self):
        self.current_user = None
        self.current_username = str()
        self.current_password = str()
        self.valid_access = False

    def get_input(self, username: str, password: str):
        self.current_username = username
        self.current_password = password

    def is_valid(self) -> bool:
        if self.current_user is None:
            return False

        if (self.current_username == self.current_user.get_username()
                and self.current_password == self.current_user.get_password()):
            return True

        return False

    def get_user(self, username: str) -> User:
        """Queries a user from the database"""
        pass
