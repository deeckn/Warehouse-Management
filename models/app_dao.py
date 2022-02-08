import sqlite3
import os.path
from user_dao import UserDAO
from customer_dao import CustomerDAO
from room_dao import RoomDAO
from shelf_dao import ShelfDAO
from log_dao import LogDAO
from user import User


class AppDAO:

    __BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    __db_path = os.path.join(__BASE_DIR, "geb_arai_dee.db")

    def __init__(self):
        self.connection = sqlite3.connect(AppDAO.__db_path)
        self.user_dao = UserDAO(self.connection)
        self.customer_dao = CustomerDAO()
        self.room_dao = RoomDAO()
        self.shelf_dao = ShelfDAO()
        self.log_dao = LogDAO()

    def get_all_users(self) -> list[User]:
        return self.user_dao.get_all_users()

    def get_user_by_id(self, id: int) -> User:
        return self.user_dao.get_user_by_id(id)

    def get_user_by_username(self, username: str) -> User:
        return self.user_dao.get_user_by_username(username)

    def close_db(self):
        self.connection.close()


if __name__ == "__main__":
    app_dao = AppDAO()
    user = app_dao.get_user_by_username("test")
    print(
        f"ID: {user.get_id()}, USERNAME: {user.get_username()}, PASS: {user.get_password()}")
    app_dao.close_db()
