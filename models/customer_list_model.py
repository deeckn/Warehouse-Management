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
        pass

    def find_customer(self, id: int):
        pass

    def get_current_customer(self) -> Customer:
        pass

    def add_customer(self, customer: Customer):
        pass

    def save_customer_data(self):
        pass

    def delete_customer(self):
        pass
