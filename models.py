from abc import ABC
from data.data_classes import *
from data.filter_options import FilterOption
from data.app_dao import *
from datetime import date


class Model(ABC):
    pass


class LoginModel(Model):
    __current_user: User

    def __init__(self):
        self.__current_user = None
        self.__current_username = str()
        self.__current_password = str()
        self.valid_access = False
        self.user_dao: UserDAO = AppDAO.get_dao("user")

    def get_input(self, username: str, password: str):
        self.__current_username = username
        self.__current_password = password

    def verify_login(self):
        if self.__current_user is None:
            self.valid_access = False
            return

        self.valid_access = (self.__current_username == self.__current_user.get_username()
                             and self.__current_password == self.__current_user.get_password())

    def retrive_user(self, username: str):
        self.__current_user = self.user_dao.get_user_by_username(username)

    def is_valid(self) -> bool:
        return self.valid_access

    def get_current_user(self) -> User:
        return self.__current_user


class HomeModel(Model):

    __current_search_filter: FilterOption
    __search_query: str
    __current_customer: Customer
    __current_products: list[ProductItem]
    __current_activity_logs: list[LogEntry]

    def __init__(self):
        self.__current_customer = None
        self.__current_products = list()
        self.__current_search_filter = None
        self.__current_activity_logs = list()
        self.__search_query = ""

    def set_home_search_filter(self, filter: FilterOption):
        self.__current_search_filter = filter

    def set_home_search_query(self, query: str):
        self.__search_query = query

    def find_product(self):
        "find product depending on search filter"
        pass

    def load_activity_log(self):
        "get activities from database"
        pass

    def get_activity_logs(self):
        return self.__current_activity_logs

    def add_product(self, product: ProductItem, quantity: int):
        "update quantity of product in database"
        pass

    def export_product(self, product: ProductItem, quantity: int):
        "update quantity of product in database"
        pass


class CustomerListModel(Model):

    __current_user: User
    __current_customer: Customer
    __customer_query: list[Customer]

    def __init__(self):
        self.__current_user = None
        self.__current_customer = None
        self.__customer_query = list()

    def query_customers(self, name: str):
        """Search Customers from Database"""
        pass

    def find_customer(self, id: int):
        """Get Customer by ID from Database"""
        pass

    def set_current_customer(self, customer: Customer):
        self.__current_customer = customer

    def get_current_customer(self) -> Customer:
        return self.__current_customer

    def add_customer(self, customer: Customer):
        pass

    def save_customer_data(self):
        pass

    def delete_customer(self):
        pass


class ProductListModel(Model):

    __current_search_filter: FilterOption
    __search_query: str
    __current_customer: Customer
    __current_products: list[ProductItem]

    def __init__(self):
        self.__current_customer = None
        self.__current_products = list()
        self.__current_search_filter = None
        self.__search_query = ""

    def set_product_search_filter(self, filter: FilterOption):
        self.__current_search_filter = filter

    def set_product_search_query(self, query: str):
        self.__search_query = query

    def find_product_information(self):
        "find product depending on search filter"
        pass

    def load_product_information(self):
        "get product information from database"
        pass

    def update_product_information(self, product: ProductItem):
        "add & save product in database"
        pass

    def delete_product_information(self, product: ProductItem):
        "update product in database"
        pass


class AccountModel(Model):
    __current_admin: User
    __user_dao: UserDAO

    def __init__(self, user: User = None):
        self.__current_admin = user
        self.__user_dao = AppDAO.get_dao("user")

    def get_employee_accounts(self) -> list[User]:
        """Returns all user objects from the database"""
        return self.__user_dao.get_all_users()

    def create_new_account(self, user: User):
        """Adds a new user object to the database"""
        self.__user_dao.add_user(user)

    def generate_username(self, first_name: str, last_name: str) -> str:
        """Returns a valid username based on the user's name"""
        username = str()

        first_name = first_name.lower()
        last_name = last_name.lower()
        first_name_length = 4
        last_name_length = 4

        if len(first_name) <= first_name_length:
            username += first_name
        else:
            username += first_name[0:first_name_length]

        username += "."

        if len(last_name) <= last_name_length:
            username += last_name
        else:
            username += last_name[0:last_name_length]

        return username

    def verify_create_password(self, password: str, confirm: str) -> bool:
        """Returns the status of password confirmation"""
        return password == confirm

    def update_user_info(self, previous_info, new_user_info: User):
        """Updates an existing user information"""
        if previous_info is None:
            return

        first_name = None if new_user_info.get_first_name(
        ) == previous_info.get_first_name() else new_user_info.get_first_name()

        last_name = None if new_user_info.get_last_name(
        ) == previous_info.get_last_name() else new_user_info.get_last_name()

        username = self.generate_username(
            new_user_info.get_first_name(),
            new_user_info.get_last_name()
        )
        username = None if username == previous_info.get_username() else username

        password = None if new_user_info.get_password(
        ) == previous_info.get_password() else new_user_info.get_password()

        self.__user_dao.update_user(
            new_user_info.get_id(),
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )

    def admin_confirmation(self, password: str) -> bool:
        """Returns the status of admin password confirmation"""
        return self.__current_admin.get_password() == password

    def delete_user_account(self, user: User):
        """Deletes a user object from the database"""
        self.__user_dao.delete_user_by_id(user.get_id())


class NotificationModel(Model):
    __product_dao: ProductDAO
    __customer_dao: CustomerDAO

    # Customer contract ending warning
    __deadline = 14

    def __init__(self):
        self.__product_dao = AppDAO.get_dao("product")
        self.__customer_dao = AppDAO.get_dao("customer")

    def get_low_stock_products(self) -> list[ProductItem]:
        """Returns a list of low stock ProductItem objects"""
        return self.__product_dao.get_low_quantity_products()

    def get_contract_ending_customers(self) -> list[Customer]:
        """Returns a list of contract ending Customer objects"""
        customers = self.__customer_dao.get_all_customers()
        customers = list(
            filter(
                lambda c: self.__within_deadline(
                    self.__date_difference(c)
                ),
                customers
            )
        )
        return customers

    def __date_difference(self, customer) -> int:
        """Returns the number of days from Today"""
        expiry_date = customer.get_expiry_date()
        day, month, year = tuple(map(int, expiry_date.split("_")))
        day1 = date(year, month, day)
        day2 = date.today()
        delta = day1 - day2
        return delta.days

    def __within_deadline(self, days):
        """Returns True if the days are within the deadline range"""
        if days < 0:
            return False
        return days <= NotificationModel.__deadline


class SiteSettingsModel(Model):
    __shelf_dao: ShelfDAO

    def __init__(self):
        self.__shelf_dao = AppDAO.get_dao("shelf")

    def add_shelf(
        self,
        label: str,
        max_weight: float,
        length: float,
        width: float,
        height: float,
        rows: int,
        columns: int
    ) -> bool:
        """Adds a new shelf unit to the system. Returns True for successful operation else False"""

        if self.__shelf_dao.get_shelf_by_label(label):
            return False

        shelf = StorageShelf(
            label,
            max_weight,
            length,
            width,
            height,
            rows,
            columns
        )
        self.__shelf_dao.add_shelf(shelf)
        return True

    def search_shelf(self, label: str) -> StorageShelf:
        """Returns a StorageShelf object given the label"""
        return self.__shelf_dao.get_shelf_by_label(label)

    def update_shelf(self, previous_info: StorageShelf, new_info: StorageShelf):
        """Updates shelf information based on new data"""
        max_weight = new_info.get_max_weight() if previous_info.get_max_weight(
        ) != new_info.get_max_weight() else None

        length = new_info.get_length() if previous_info.get_length(
        ) != new_info.get_length() else None

        width = new_info.get_width() if previous_info.get_width(
        ) != new_info.get_width() else None

        height = new_info.get_height() if previous_info.get_height(
        ) != new_info.get_height() else None

        rows = new_info.get_rows() if previous_info.get_rows(
        ) != new_info.get_rows() else None

        columns = new_info.get_columns() if previous_info.get_columns(
        ) != new_info.get_columns() else None

        self.__shelf_dao.update_shelf(
            new_info.get_label(),
            max_weight=max_weight,
            length=length,
            width=width,
            height=height,
            rows=rows,
            columns=columns
        )

    def delete_shelf(self, shelf: StorageShelf):
        """Deletes a shelf from the database"""
        self.__shelf_dao.delete_shelf(shelf.get_label())

    def calculate_total_slots(self, rows, columns) -> int:
        """Returns the total number of slots"""
        return rows * columns

    def get_shelves_contains_with(self, shelf_search: str) -> list[StorageShelf]:
        """Returns a list of StorageShelf objects given a search query"""
        return self.__shelf_dao.get_shelves_contains_with(shelf_search)

    def get_all_shelves(self) -> list[StorageShelf]:
        """Returns a list of all StorageShelf objects from the database"""
        return self.__shelf_dao.get_all_shelves()
