from model import Model
from customer import Customer
from product_item import ProductItem
from log_entry import LogEntry
from filter_options import FilterOption


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
