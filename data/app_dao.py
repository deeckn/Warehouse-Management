import sqlite3
import os.path
from data.access_level import *
from data.data_classes import *
from abc import ABC


class DAO(ABC):
    pass


class AppDAO:

    __BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    __DB_PATH = os.path.join(__BASE_DIR, "geb_arai_dee.db")
    __connection: sqlite3.Connection = sqlite3.connect(__DB_PATH)

    @staticmethod
    def close_db():
        """Disconnects the connection to the database"""
        AppDAO.__connection.close()

    @staticmethod
    def get_dao(type: str) -> DAO:
        """
        'user' returns UserDAO,
        'customer' returns CustomerDAO,
        'product' returns ProductDAO,
        'shelf' returns ShelfDAO,
        'log' returns LogDAO
        """
        if type == "user":
            return UserDAO(AppDAO.__connection)
        elif type == "customer":
            return CustomerDAO(AppDAO.__connection)
        elif type == "product":
            return ProductDAO()
        elif type == "shelf":
            return ShelfDAO()
        elif type == "log":
            return LogDAO(AppDAO.__connection)
        else:
            return None


class UserDAO(DAO):

    __table_name = "USERS"
    __COLUMN_ID = "user_id"
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
        """Adds a User object to the database"""
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

    def update_user(
        self,
        user_id: int,
        first_name: str = None,
        last_name: str = None,
        username: str = None,
        password: str = None,
        access: AccessLevel = None
    ) -> None:
        """
        Updates user data given an id.
        Example: update_user(4, first_name="John", username="john.tr", access=AdminAccess())
        """
        query = f"UPDATE {UserDAO.__table_name} SET "

        if first_name is not None:
            query += f'{UserDAO.__COLUMN_FIRST_NAME}="{first_name}", '
        if last_name is not None:
            query += f'{UserDAO.__COLUMN_LAST_NAME}="{last_name}", '
        if username is not None:
            query += f'{UserDAO.__COLUMN_USERNAME}="{username}", '
        if password is not None:
            query += f'{UserDAO.__COLUMN_PASSWORD}="{password}", '
        if access is not None:
            value = "admin" if isinstance(access, AdminAccess) else "employee"
            query += f'{UserDAO.__COLUMN_ACCESS} = "{value}"'

        if query[-2] == ",":
            query = query[:-2]

        query += f" WHERE {UserDAO.__COLUMN_ID}={user_id}"
        self.__cursor.execute(query)
        self.__connection.commit()

    def delete_user_by_id(self, id: int) -> None:
        """Deletes user data given an id"""
        self.__cursor.execute(
            f"DELETE FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_ID}={id}")
        self.__connection.commit()


class LogDAO(DAO):

    __table_name = "LOG_ENTRIES"
    __COLUMN_ID = "log_id"
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
            ({LogDAO.__COLUMN_DATE}, 
             {LogDAO.__COLUMN_TIME}, 
             {LogDAO.__COLUMN_DESCRIPTION})
            VALUES ('{log_entry.get_date()}', '{log_entry.get_time()}',
                    '{log_entry.get_description()}')
        """)
        self.__connection.commit()


class CustomerDAO(DAO):

    __table_name = "CUSTOMERS"
    __COLUMN_ID = "customer_id"
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
        """Adds a Customer object to the database"""
        packing_service = 1 if customer.get_packing_service() else 0

        self.__cursor.execute(f"""
            INSERT INTO {CustomerDAO.__table_name}
            ({CustomerDAO.__COLUMN_NAME}, 
             {CustomerDAO.__COLUMN_PHONE}, 
             {CustomerDAO.__COLUMN_EMAIL}, 
             {CustomerDAO.__COLUMN_PACKING_SERVICE}, 
             {CustomerDAO.__COLUMN_RENTAL_DURATION}, 
             {CustomerDAO.__COLUMN_DATE_JOINED}, 
             {CustomerDAO.__COLUMN_EXPIRY_DATE}, 
             {CustomerDAO.__COLUMN_TOTAL_PAYMENT})
            VALUES ('{customer.get_name()}', 
            '{customer.get_phone()}', 
            '{customer.get_email()}', 
            {packing_service}, 
            '{customer.get_rental_duration()}', 
            '{customer.get_date_joined()}', 
            '{customer.get_expiry_date()}', 
            {customer.get_total_payment()})
        """)
        self.__connection.commit()

    def update_customer(
        self,
        id: int,
        name: str = None,
        phone: str = None,
        email: str = None,
        packing_service: bool = None,
        rental_duration: str = None,
        date_joined: str = None,
        expiry_date: str = None,
        total_payment: float = None
    ) -> None:
        """
        Updates customer data given an id.
        Example: update_customer(5, phone="1357924680", total_payment=12500)
        """
        query = f"UPDATE {CustomerDAO.__table_name} SET "

        if name is not None:
            query += f'{CustomerDAO.__COLUMN_NAME}="{name}", '
        if phone is not None:
            query += f'{CustomerDAO.__COLUMN_PHONE}="{phone}", '
        if email is not None:
            query += f'{CustomerDAO.__COLUMN_EMAIL}="{email}", '
        if packing_service is not None:
            status = 1 if packing_service else 0
            query += f'{CustomerDAO.__COLUMN_PACKING_SERVICE}={status}, '
        if rental_duration is not None:
            query += f'{CustomerDAO.__COLUMN_RENTAL_DURATION}="{rental_duration}", '
        if date_joined is not None:
            query += f'{CustomerDAO.__COLUMN_DATE_JOINED}="{date_joined}", '
        if expiry_date is not None:
            query += f'{CustomerDAO.__COLUMN_EXPIRY_DATE}="{expiry_date}", '
        if total_payment is not None:
            query += f'{CustomerDAO.__COLUMN_TOTAL_PAYMENT}={total_payment}, '

        if query[-2] == ",":
            query = query[:-2]

        query += f" WHERE {CustomerDAO.__COLUMN_ID}={id}"
        self.__cursor.execute(query)
        self.__connection.commit()

    def get_customer(self, customer_id: int) -> Customer:
        """Retreives a Customer object given an id"""
        self.__cursor.execute(
            f"SELECT * FROM {CustomerDAO.__table_name} WHERE {CustomerDAO.__COLUMN_ID}={customer_id}")
        data = self.__cursor.fetchone()
        if data is None:
            return None

        packing_service = data[4] == 1
        return Customer(data[0], data[1], data[2], data[3], packing_service, data[5], data[6], data[7], data[8])

    def get_customer_by_name(self, name: str) -> Customer:
        """Retreives a Customer object given a name"""
        self.__cursor.execute(
            f"SELECT * FROM {CustomerDAO.__table_name} WHERE {CustomerDAO.__COLUMN_NAME}={name}")
        data = self.__cursor.fetchone()
        if data is None:
            return None

        packing_service = data[4] == 1
        return Customer(data[0], data[1], data[2], data[3], packing_service, data[5], data[6], data[7], data[8])

    def delete_customer(self, customer_id: int):
        """Deletes customer data given an id"""
        self.__cursor.execute(
            f"DELETE FROM {CustomerDAO.__table_name} WHERE {CustomerDAO.__COLUMN_ID}={customer_id}")
        self.__connection.commit()


class ProductDAO(DAO):

    __table_name = "PRODUCTS"
    __COLUMN_ID = "product_id"
    __COLUMN_NAME = "name"
    __COLUMN_QUANTITY = "quantity"
    __COLUMN_LOW_STOCK = "low_stock"
    __COLUMN_WEIGHT = "weight"
    __COLUMN_LAST_STORED = "last_stored"
    __COLUMN_LOCATION = "location"
    __COLUMN_OWNER = "owner"
    __COLUMN_CATEGORY = "category"

    def __init__(self, connection: sqlite3.Connection):
        self.__connection = connection
        self.__cursor = self.__connection.cursor()
        self.__query_list = list()

    def add_product(self, product: ProductItem):
        pass

    def get_product(self, product_id: int) -> ProductItem:
        pass

    def get_all_products(self) -> list[ProductItem]:
        pass

    def update_product(
        self,
        id: int,
        name: str = None,
        quantity: int = None,
        low_stock: int = None,
        weight: float = None,
        last_stored: str = None,
        location: int = None,
        owner_id: int = None
    ):
        pass

    def delete_product(self, product_id: int):
        pass


class ShelfDAO(DAO):
    pass
