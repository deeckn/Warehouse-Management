import sqlite3
from access_level import AdminAccess, EmployeeAccess
from user import User


class UserDAO:

    __table_name = "USERS"
    __query_list = list()

    def __init__(self, connection: sqlite3.Connection):
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    def get_all_users(self) -> list[User]:
        self.__cursor.execute(f"SELECT * FROM {UserDAO.__table_name}")
        users = self.__cursor.fetchall()
        self.__query_list = users
        self.__convert_to_object()
        return self.__query_list

    def __convert_to_object(self):
        temp = list()
        for data in self.__query_list:
            if data[3] == "admin":
                access = AdminAccess()
            else:
                access = EmployeeAccess()

            user = User(data[0], data[1], data[2], access)
            temp.append(user)
        self.__query_list = temp

    def get_user_by_id(self, id: int) -> User:
        self.__cursor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE id={id}")
        data = self.__cursor.fetchone()
        if data is None:
            return None
        else:
            if data[3] == "admin":
                access = AdminAccess()
            else:
                access = EmployeeAccess()

            return User(data[0], data[1], data[2], access)

    def get_user_by_username(self, username: str) -> User:
        self.__cursor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE username='{username}'")
        data = self.__cursor.fetchone()
        if data is None:
            return None
        else:
            if data[3] == "admin":
                access = AdminAccess()
            else:
                access = EmployeeAccess()

            return User(data[0], data[1], data[2], access)
