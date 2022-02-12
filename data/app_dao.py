import sqlite3
import os.path
from data.access_level import *
from data.data_classes import *


class AppDAO:

    __BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    __DB_PATH = os.path.join(__BASE_DIR, "geb_arai_dee.db")

    def __init__(self):
        self.connection = sqlite3.connect(AppDAO.__DB_PATH)
        self.user_dao = UserDAO(self.connection)
        self.customer_dao = CustomerDAO(self.connection)
        self.product_dao = ProductDAO()
        self.shelf_dao = ShelfDAO()
        self.log_dao = LogDAO(self.connection)

    """User Data Access CRUD Methods"""

    def get_all_users(self) -> list[User]:
        """Returns a list of User objects from the database"""
        return self.user_dao.get_all_users()

    def get_user_by_id(self, id: int) -> User:
        """Returns a User object given by an id"""
        return self.user_dao.get_user_by_id(id)

    def get_user_by_username(self, username: str) -> User:
        """Returns a User object given by a username"""
        return self.user_dao.get_user_by_username(username)

    def insert_user(self, user: User):
        """Inserts a user into the database"""
        self.user_dao.add_user(user)

    """Log Data Access CRUD Methods"""

    def insert_log_entry(self, log_entry: LogEntry):
        """Inserts a log entry to the database"""
        self.log_dao.add_log_entry(log_entry)

    def get_all_log_entries(self) -> list[LogEntry]:
        """Returns a list of log entries from the database"""
        return self.log_dao.get_all_log_entries()

    def close_db(self):
        """Disconnects the connection to the database"""
        self.connection.close()


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

    def add_user(self, user: User) -> None:
        access = "admin" if isinstance(
            user.get_access_level(), AdminAccess) else "employee"
        self.__cursor.execute(f"""
            INSERT INTO {UserDAO.__table_name}
            ({UserDAO.__COLUMN_FIRST_NAME},
            {UserDAO.__COLUMN_LAST_NAME},
            {UserDAO.__COLUMN_USERNAME},
            {UserDAO.__COLUMN_PASSWORD},
            {UserDAO.__COLUMN_ACCESS})
            VALUES 
            ('{user.get_first_name()}',
            '{user.get_last_name()}',
            '{user.get_username()}',
            '{user.get_password()}',
            '{access}')
        """)
        self.__connection.commit()

    def update_user(self, user_id: int) -> None:
        """Updates the data of a user given by the id"""
        pass

    def delete_user_by_username(self, username: str) -> None:
        pass


class LogDAO:

    __table_name = "LOG_ENTRIES"
    __COLUMN_ID = "id"
    __COLUMN_DATE = "date"
    __COLUMN_TIME = "time"
    __COLUMN_DESCRIPTION = "description"

    def __init__(self, connection: sqlite3.Connection):
        self.__connection = connection
        self.__cursor = self.__connection.cursor()
        self.__query_list = list()

    def get_all_log_entries(self) -> list[LogEntry]:
        """Retreives all log entries"""
        self.__cursor.execute(f"SELECT * FROM {LogDAO.__table_name}")
        users = self.__cursor.fetchall()
        self.__query_list = users
        self.__convert_to_object()
        return self.__query_list

    def __convert_to_object(self):
        """Converts raw data to User objects"""
        temp = list()
        for data in self.__query_list:
            log_entry = LogEntry(data[0], data[1], data[2], data[3])
            temp.append(log_entry)
        self.__query_list = temp

    def add_log_entry(self, log_entry: LogEntry):
        """Appends a log entry to the LOG_ENTRIES table"""
        self.__cursor.execute(f"""
            INSERT INTO {LogDAO.__table_name}
            ({LogDAO.__COLUMN_DATE}, {LogDAO.__COLUMN_TIME}, {LogDAO.__COLUMN_DESCRIPTION})
            VALUES ('{log_entry.get_date()}', '{log_entry.get_time()}', '{log_entry.get_description()}')
        """)
        self.__connection.commit()


class CustomerDAO:

    __table_name = "CUSTOMERS"
    __COLUMN_ID = "id"
    __COLUMN_NAME = "name"
    __COLUMN_PHONE = "phone"
    __COLUMN_EMAIL = "email"
    __COLUMN_PACKING_SERVICE = "packing_service"
    __COLUMN_RENTAL_DURATION = "rental_duration"
    __COLUMN_DATE_JOINED = "date_joined"
    __COLUMN_EXPIRY_DATE = "expiry_date"
    __COLUMN_TOTAL_PAYMENT = "total_payment"

    def __init__(self, connection: sqlite3.Connection):
        self.__connection = connection
        self.__cursor = self.__connection.cursor()
        self.__query_list = list()

    def get_all_customers(self) -> list[Customer]:
        """Retreives all log entries"""
        self.__cursor.execute(f"SELECT * FROM {CustomerDAO.__table_name}")
        users = self.__cursor.fetchall()
        self.__query_list = users
        self.__convert_to_object()
        return self.__query_list

    def __convert_to_object(self):
        """Converts raw data to User objects"""
        temp = list()
        for data in self.__query_list:
            packing_service = True if data[4] == "1" else False
            customer = Customer(
                int(data[0]),
                data[1],
                data[2],
                data[3],
                packing_service,
                data[5],
                data[6],
                data[7],
                float(data[8])
            )
            temp.append(customer)
        self.__query_list = temp

    def add_customer(self, customer: Customer):
        pass

    def update_customer(self, customer: Customer):
        pass

    def get_customer_by_name(self, name: str) -> Customer:
        pass

    def delete_customer(self, customer: Customer):
        pass


class ProductDAO:
    pass


class ShelfDAO:
    pass
