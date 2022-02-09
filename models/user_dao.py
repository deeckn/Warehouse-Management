import sqlite3
from access_level import AdminAccess, EmployeeAccess
from user import User


class UserDAO:

    __table_name = "USERS"
    __COLUMN_ID = "id"
    __COLUMN_FIRST_NAME = "first_name"
    __COLUMN_LAST_NAME = "last_name"
    __COLUMN_USERNAME = "username"
    __COLUMN_PASSWORD = "password"
    __COLUMN_ACCESS = "access_level"

    def __init__(self, connection: sqlite3.Connection):
        self.__connection = connection
        self.__cursor = self.__connection.cursor()
        self.__query_list = list()

    def get_all_users(self) -> list[User]:
        """Retrieves all users from the USERS table"""
        self.__cursor.execute(f"SELECT * FROM {UserDAO.__table_name}")
        users = self.__cursor.fetchall()
        self.__query_list = users
        self.__convert_to_object()
        return self.__query_list

    def __convert_to_object(self) -> None:
        """Converts raw data to User objects"""
        temp = list()
        for data in self.__query_list:
            access = AdminAccess() if data[5] == "admin" else EmployeeAccess()
            user = User(data[0], data[1], data[2], data[3], data[4], access)
            temp.append(user)
        self.__query_list = temp

    def get_user_by_id(self, id: int) -> User:
        """Retreives a User object from an id"""
        self.__cursor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_ID}={id}")
        data = self.__cursor.fetchone()
        if data is None:
            return None

        access = AdminAccess() if data[5] == "admin" else EmployeeAccess()
        return User(data[0], data[1], data[2], data[3], data[4], access)

    def get_user_by_username(self, username: str) -> User:
        """Retreives a User object from a username"""
        self.__cursor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_USERNAME}='{username}'")
        data = self.__cursor.fetchone()
        if data is None:
            return None

        access = AdminAccess() if data[5] == "admin" else EmployeeAccess()
        return User(data[0], data[1], data[2], data[3], data[4], access)

    def update_user(self, user: User) -> None:
        """Updates the data of the given user"""
        pass

    def delete_user_by_username(self, username: str) -> None:
        pass
