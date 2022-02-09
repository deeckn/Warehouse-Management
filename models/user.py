from dataclasses import dataclass
from access_level import AccessLevel


@dataclass
class User:
    __id: int
    __first_name: str
    __last_name: str
    __username: str
    __password: str
    __access: AccessLevel

    def get_id(self) -> int:
        return self.__id

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_access_level(self) -> AccessLevel:
        return self.__access
