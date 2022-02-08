from dataclasses import dataclass
from models.abstractions.access_level import AccessLevel


@dataclass
class User:
    __id: int
    __username: str
    __password: str
    __access: AccessLevel

    def get_id(self) -> int:
        return self.__id

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_access_level(self) -> AccessLevel:
        return self.__access
