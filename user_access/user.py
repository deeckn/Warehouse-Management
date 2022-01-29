from user_access.access_level import AccessLevel


class User:
    def __init__(self, username: str, password: str, access: AccessLevel) -> None:
        self.username = username
        self.__password = password
        self.access = access

    def get_username(self) -> str:
        return self.username

    def get_access_level(self) -> AccessLevel:
        return self.access
