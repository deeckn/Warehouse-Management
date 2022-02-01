from model import Model
from data_classes.user import User


class LoginModel(Model):
    __current_user: User

    def __init__(self):
        self.__current_user = None
        self.__current_username = str()
        self.__current_password = str()
        self.valid_access = False

    def get_input(self, username: str, password: str):
        self.__current_username = username
        self.__current_password = password

    def is_valid(self) -> bool:
        if self.__current_user is None:
            return False

        if (self.__current_username == self.__current_user.get_username()
                and self.__current_password == self.__current_user.get_password()):
            return True

        return False

    def retrive_user(self, username: str) -> User:
        """Queries a user from the database"""
        pass

    def get_current_user(self) -> User:
        return self.__current_user
