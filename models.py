from abc import ABC
from data.data_classes import *
from data.filter_options import FilterOption
from data.app_dao import AppDAO


class Model(ABC):
    pass


class LoginModel(Model):
    __current_user: User

    def __init__(self):
        self.__current_user = None
        self.__current_username = str()
        self.__current_password = str()
        self.valid_access = False
        self.app_dao = AppDAO()

    def get_input(self, username: str, password: str):
        self.__current_username = username
        self.__current_password = password

    def verify_login(self):
        if self.__current_user is None:
            self.valid_access = False
            return

        if (self.__current_username == self.__current_user.get_username()
                and self.__current_password == self.__current_user.get_password()):
            self.valid_access = True

    def retrive_user(self, username: str):
        self.__current_user = self.app_dao.get_user_by_username(username)

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
