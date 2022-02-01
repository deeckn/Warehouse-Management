from dataclasses import dataclass
from abstractions.access_level import AccessLevel


@dataclass
class User:
    __username: str
    __password: str
    __access: AccessLevel

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_access_level(self) -> AccessLevel:
        return self.__access
