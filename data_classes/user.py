from dataclasses import dataclass
from abstractions.access_level import AccessLevel


@dataclass
class User:
    username: str
    password: str
    access: AccessLevel

    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password

    def get_access_level(self) -> AccessLevel:
        return self.access
