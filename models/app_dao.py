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

    def get_all_users(self) -> list[User]:
        return self.user_dao.get_all_users()

    def get_user_by_id(self, id: int) -> User:
        return self.user_dao.get_user_by_id(id)

    def get_user_by_username(self, username: str) -> User:
        return self.user_dao.get_user_by_username(username)

    def insert_log_entry(self, log_entry: LogEntry):
        self.log_dao.add_log_entry(log_entry)

    def close_db(self):
        self.connection.close()
