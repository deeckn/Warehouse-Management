import sqlite3
from customer import Customer


class CustomerDAO:

    __table_name = "CUSTOMERS"
    __COLUMN_ID = "id"
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
        pass

    def update_customer(self, customer: Customer):
        pass

    def get_customer_by_name(self, name: str) -> Customer:
        pass

    def delete_customer(self, customer: Customer):
        pass
