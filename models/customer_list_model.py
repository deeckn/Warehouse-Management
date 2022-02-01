from model import Model
from data_classes.user import User
from data_classes.customer import Customer


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
