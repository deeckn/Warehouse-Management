import sqlite3
import os.path
from user_dao import UserDAO
from customer_dao import CustomerDAO
from product_dao import ProductDAO
from shelf_dao import ShelfDAO
from log_dao import LogDAO
from user import User
from log_entry import LogEntry


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
