from model import Model
from data_classes.customer import Customer
from data_classes.product_item import ProductItem
from abstractions.filter_options import FilterOption

class ProductListModel(Model):

    __current_search_filter: FilterOption
    __search_query: str
    __current_customer: Customer
    __current_products: list[ProductItem]

    def __init__(self):
        self.__current_customer = None
        self.__current_products =  list()
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

    def update_product_information(self, product: ProductItem, quantity: int):
        "add & save product in database"
        pass

    def delete_product_information(self, product: ProductItem, quantity: int):
        "update product in database"
        pass