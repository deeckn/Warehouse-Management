import sqlite3
import os.path
from data.access_level import *
from data.data_classes import *
from data.categories import *
from abc import ABC


class DAO(ABC):
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor = self.connection.cursor()


class AppDAO:

    __BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    __DB_PATH = os.path.join(__BASE_DIR, "geb_arai_dee.db")
    __connection: sqlite3.Connection = sqlite3.connect(__DB_PATH)

    @staticmethod
    def close_db():
        """Disconnects the connection to the database"""
        AppDAO.__connection.close()

    @staticmethod
    def get_dao(type: str) -> DAO:
        """
        'user' returns UserDAO,
        'customer' returns CustomerDAO,
        'product' returns ProductDAO,
        'shelf' returns ShelfDAO,
        'log' returns LogDAO,
        'category' returns CategoryDAO,
        'location" returns LocationDAO
        """
        if type == "user":
            return UserDAO(AppDAO.__connection)
        elif type == "customer":
            return CustomerDAO(AppDAO.__connection)
        elif type == "product":
            return ProductDAO(AppDAO.__connection)
        elif type == "shelf":
            return ShelfDAO(AppDAO.__connection)
        elif type == "log":
            return LogDAO(AppDAO.__connection)
        elif type == "category":
            return CategoryDAO(AppDAO.__connection)
        elif type == "location":
            return LocationDAO(AppDAO.__connection)
        else:
            return None


class UserDAO(DAO):

    __table_name = "USERS"
    __COLUMN_ID = "user_id"
    __COLUMN_FIRST_NAME = "first_name"
    __COLUMN_LAST_NAME = "last_name"
    __COLUMN_USERNAME = "username"
    __COLUMN_PASSWORD = "password"
    __COLUMN_ACCESS = "access_level"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)
        self.__query_list = list()

    def get_all_users(self) -> list[User]:
        """Retrieves all users from the USERS table"""
        self.cursor.execute(f"SELECT * FROM {UserDAO.__table_name}")
        users = self.cursor.fetchall()
        self.__query_list = users
        self.__convert_to_object()
        return self.__query_list

    def __convert_to_object(self):
        """Converts raw data to User objects"""
        temp = list()
        for data in self.__query_list:
            access = AdminAccess() if data[5] == "admin" else EmployeeAccess()
            user = User(data[0], data[1], data[2], data[3], data[4], access)
            temp.append(user)
        self.__query_list = temp

    def get_user_by_id(self, id: int) -> User:
        """Retreives a User object from an id"""
        self.cursor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_ID}={id}")
        data = self.cursor.fetchone()
        if data is None:
            return None

        access = AdminAccess() if data[5] == "admin" else EmployeeAccess()
        return User(data[0], data[1], data[2], data[3], data[4], access)

    def get_user_by_username(self, username: str) -> User:
        """Retreives a User object from a username"""
        self.cursor.execute(
            f"SELECT * FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_USERNAME}='{username}'")
        data = self.cursor.fetchone()
        if data is None:
            return None

        access = AdminAccess() if data[5] == "admin" else EmployeeAccess()
        return User(data[0], data[1], data[2], data[3], data[4], access)

    def add_user(self, user: User) -> None:
        """Adds a User object to the database"""
        access = "admin" if isinstance(
            user.get_access_level(), AdminAccess) else "employee"
        self.cursor.execute(f"""
            INSERT INTO {UserDAO.__table_name}
            ({UserDAO.__COLUMN_FIRST_NAME},
            {UserDAO.__COLUMN_LAST_NAME},
            {UserDAO.__COLUMN_USERNAME},
            {UserDAO.__COLUMN_PASSWORD},
            {UserDAO.__COLUMN_ACCESS})
            VALUES
            ('{user.get_first_name()}',
            '{user.get_last_name()}',
            '{user.get_username()}',
            '{user.get_password()}',
            '{access}')
        """)
        self.connection.commit()

    def update_user(
        self,
        user_id: int,
        first_name: str = None,
        last_name: str = None,
        username: str = None,
        password: str = None,
        access: AccessLevel = None
    ) -> None:
        """
        Updates user data given an id.
        Example: update_user(4, first_name="John",
                             username="john.tr", access=AdminAccess())
        """
        query = f"UPDATE {UserDAO.__table_name} SET "

        if first_name is not None:
            query += f'{UserDAO.__COLUMN_FIRST_NAME}="{first_name}", '
        if last_name is not None:
            query += f'{UserDAO.__COLUMN_LAST_NAME}="{last_name}", '
        if username is not None:
            query += f'{UserDAO.__COLUMN_USERNAME}="{username}", '
        if password is not None:
            query += f'{UserDAO.__COLUMN_PASSWORD}="{password}", '
        if access is not None:
            value = "admin" if isinstance(access, AdminAccess) else "employee"
            query += f'{UserDAO.__COLUMN_ACCESS} = "{value}"'

        if query[-2] == ",":
            query = query[:-2]

        query += f" WHERE {UserDAO.__COLUMN_ID}={user_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_user_by_id(self, id: int) -> None:
        """Deletes user data given an id"""
        self.cursor.execute(
            f"DELETE FROM {UserDAO.__table_name} WHERE {UserDAO.__COLUMN_ID}={id}")
        self.connection.commit()


class LogDAO(DAO):

    __table_name = "LOG_ENTRIES"
    __COLUMN_ID = "log_id"
    __COLUMN_DATE = "date"
    __COLUMN_TIME = "time"
    __COLUMN_DESCRIPTION = "description"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)
        self.__query_list = list()

    def get_all_log_entries(self) -> list[LogEntry]:
        """Retreives all log entries"""
        self.cursor.execute(f"SELECT * FROM {LogDAO.__table_name}")
        users = self.cursor.fetchall()
        self.__query_list = users
        self.__convert_to_object()
        return self.__query_list

    def __convert_to_object(self):
        """Converts raw data to User objects"""
        temp = list()
        for data in self.__query_list:
            log_entry = LogEntry(data[0], data[1], data[2], data[3])
            temp.append(log_entry)
        self.__query_list = temp

    def add_log_entry(self, log_entry: LogEntry):
        """Appends a log entry to the LOG_ENTRIES table"""
        self.cursor.execute(f"""
            INSERT INTO {LogDAO.__table_name}
            ({LogDAO.__COLUMN_DATE},
             {LogDAO.__COLUMN_TIME},
             {LogDAO.__COLUMN_DESCRIPTION})
            VALUES ('{log_entry.get_date()}', '{log_entry.get_time()}',
                    '{log_entry.get_description()}')
        """)
        self.connection.commit()


class CustomerDAO(DAO):

    __table_name = "CUSTOMERS"
    __COLUMN_ID = "customer_id"
    __COLUMN_NAME = "name"
    __COLUMN_PHONE = "phone"
    __COLUMN_EMAIL = "email"
    __COLUMN_PACKING_SERVICE = "packing_service"
    __COLUMN_RENTAL_DURATION = "rental_duration"
    __COLUMN_DATE_JOINED = "date_joined"
    __COLUMN_EXPIRY_DATE = "expiry_date"
    __COLUMN_TOTAL_PAYMENT = "total_payment"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)
        self.__query_list = list()

    def get_all_customers(self) -> list[Customer]:
        """Retreives all log entries"""
        self.cursor.execute(f"SELECT * FROM {CustomerDAO.__table_name}")
        users = self.cursor.fetchall()
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
        """Adds a Customer object to the database"""
        packing_service = 1 if customer.get_packing_service() else 0

        self.cursor.execute(f"""
            INSERT INTO {CustomerDAO.__table_name}
            ({CustomerDAO.__COLUMN_NAME},
             {CustomerDAO.__COLUMN_PHONE},
             {CustomerDAO.__COLUMN_EMAIL},
             {CustomerDAO.__COLUMN_PACKING_SERVICE},
             {CustomerDAO.__COLUMN_RENTAL_DURATION},
             {CustomerDAO.__COLUMN_DATE_JOINED},
             {CustomerDAO.__COLUMN_EXPIRY_DATE},
             {CustomerDAO.__COLUMN_TOTAL_PAYMENT})
            VALUES ('{customer.get_name()}',
            '{customer.get_phone()}',
            '{customer.get_email()}',
            {packing_service},
            '{customer.get_rental_duration()}',
            '{customer.get_date_joined()}',
            '{customer.get_expiry_date()}',
            {customer.get_total_payment()})
        """)
        self.connection.commit()

    def update_customer(
        self,
        id: int,
        name: str = None,
        phone: str = None,
        email: str = None,
        packing_service: bool = None,
        rental_duration: str = None,
        date_joined: str = None,
        expiry_date: str = None,
        total_payment: float = None
    ) -> None:
        """
        Updates customer data given an id.
        Example: update_customer(5, phone="1357924680", total_payment=12500)
        """
        query = f"UPDATE {CustomerDAO.__table_name} SET "

        if name is not None:
            query += f'{CustomerDAO.__COLUMN_NAME}="{name}", '
        if phone is not None:
            query += f'{CustomerDAO.__COLUMN_PHONE}="{phone}", '
        if email is not None:
            query += f'{CustomerDAO.__COLUMN_EMAIL}="{email}", '
        if packing_service is not None:
            status = 1 if packing_service else 0
            query += f'{CustomerDAO.__COLUMN_PACKING_SERVICE}={status}, '
        if rental_duration is not None:
            query += f'{CustomerDAO.__COLUMN_RENTAL_DURATION}="{rental_duration}", '
        if date_joined is not None:
            query += f'{CustomerDAO.__COLUMN_DATE_JOINED}="{date_joined}", '
        if expiry_date is not None:
            query += f'{CustomerDAO.__COLUMN_EXPIRY_DATE}="{expiry_date}", '
        if total_payment is not None:
            query += f'{CustomerDAO.__COLUMN_TOTAL_PAYMENT}={total_payment}, '

        if query[-2] == ",":
            query = query[:-2]

        query += f" WHERE {CustomerDAO.__COLUMN_ID}={id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_customer(self, customer_id: int) -> Customer:
        """Retreives a Customer object given an id"""
        self.cursor.execute(
            f"SELECT * FROM {CustomerDAO.__table_name} WHERE {CustomerDAO.__COLUMN_ID}={customer_id}")
        data = self.cursor.fetchone()
        if data is None:
            return None

        packing_service = data[4] == 1
        return Customer(data[0], data[1], data[2], data[3], packing_service, data[5], data[6], data[7], data[8])

    def get_customer_by_name(self, name: str) -> Customer:
        """Retreives a Customer object given a name"""
        self.cursor.execute(
            f"SELECT * FROM {CustomerDAO.__table_name} WHERE {CustomerDAO.__COLUMN_NAME}={name}")
        data = self.cursor.fetchone()
        if data is None:
            return None

        packing_service = data[4] == 1
        return Customer(data[0], data[1], data[2], data[3], packing_service, data[5], data[6], data[7], data[8])

    def delete_customer(self, customer_id: int):
        """Deletes customer data given an id"""
        self.cursor.execute(
            f"DELETE FROM {CustomerDAO.__table_name} WHERE {CustomerDAO.__COLUMN_ID}={customer_id}")
        self.connection.commit()


class CategoryDAO(DAO):

    __table_name = "PRODUCT_CATEGORIES"
    __COLUMN_PRODUCT_ID = "product_id"
    __COLUMN_CATEGORY = "category"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)

    def add_product_category(self, product_id: int, category: ProductCategory):
        """Appends a product category to the PRODUCT_CATEGORIES table"""
        self.cursor.execute(f"""
            INSERT INTO {CategoryDAO.__table_name}
            ({CategoryDAO.__COLUMN_PRODUCT_ID},
             {CategoryDAO.__COLUMN_CATEGORY})
            VALUES ('{product_id}',
                    '{category.get_category()}')
        """)
        self.connection.commit()

    def get_product_categories(self, product_id: int) -> list[ProductCategory]:
        """Returns a list of ProductCategory objects"""
        self.cursor.execute(f"""
            SELECT {CategoryDAO.__COLUMN_CATEGORY}
            FROM {CategoryDAO.__table_name}
            WHERE {CategoryDAO.__COLUMN_PRODUCT_ID}={product_id}
        """)

        data = self.cursor.fetchall()
        categories = list()
        for category in data:
            category_name = category[0]
            category_class = CategoryFactory.get_category(category_name)
            categories.append(category_class)
        return categories

    def remove_product_category(self, product_id: int, category: ProductCategory):
        """Removes a category from a product"""
        self.cursor.execute(f"""
            DELETE FROM {CategoryDAO.__table_name}
            WHERE {CategoryDAO.__COLUMN_PRODUCT_ID}={product_id}
            AND {CategoryDAO.__COLUMN_CATEGORY}='{category.get_category()}'""")
        self.connection.commit()

    def remove_all_product_categories(self, product_id: int):
        """Removes all categories of a product"""
        self.cursor.execute(f"""
            DELETE FROM {CategoryDAO.__table_name}
            WHERE {CategoryDAO.__COLUMN_PRODUCT_ID}={product_id}
        """)
        self.connection.commit()


class LocationDAO(DAO):
    __table_name = "PRODUCT_LOCATIONS"
    __COLUMN_PRODUCT_ID = "product_id"
    __COLUMN_SHELF_LABEL = "shelf_label"
    __COLUMN_STARTING_NUMBER = "starting_number"
    __COLUMN_ENDING_NUMBER = "ending_number"

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)

    def add_product_location(self, product_id: int, location: Location):
        """Adds a product and location entry to the PRODUCT_LOCATIONS table"""
        start, end = location.get_range()

        try:
            self.cursor.execute(f"""
                INSERT INTO {LocationDAO.__table_name}
                ({LocationDAO.__COLUMN_PRODUCT_ID},
                {LocationDAO.__COLUMN_SHELF_LABEL},
                {LocationDAO.__COLUMN_STARTING_NUMBER},
                {LocationDAO.__COLUMN_ENDING_NUMBER})
                VALUES
                ({product_id},
                '{location.get_shelf_label()}',
                {start},
                {end})
            """)
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(
                "Unable to insert a location, \
                the there might be a product of the same id stored on this shelf"
            )
            return

    def get_product_location(self, product_id: int) -> list[Location]:
        """Returns list of Location objects given the product id"""
        self.cursor.execute(f"""
            SELECT
            {LocationDAO.__COLUMN_SHELF_LABEL},
            {LocationDAO.__COLUMN_STARTING_NUMBER},
            {LocationDAO.__COLUMN_ENDING_NUMBER}
            FROM {LocationDAO.__table_name}
            WHERE {LocationDAO.__COLUMN_PRODUCT_ID}={product_id}
        """)

        data = self.cursor.fetchall()
        locations = list()
        for location in data:
            shelf_label = location[0]
            start = location[1]
            end = location[2]
            location_object = Location(shelf_label, start, end)
            locations.append(location_object)

        return locations

    def remove_product_location(self, product_id: int, shelf_label: str):
        """Removes a shelf location of a product in the PRODUCT_LOCATIONS table"""
        self.cursor.execute(f"""
            DELETE FROM {LocationDAO.__table_name}
            WHERE {LocationDAO.__COLUMN_PRODUCT_ID}={product_id}
            AND {LocationDAO.__COLUMN_SHELF_LABEL}='{shelf_label}'""")
        self.connection.commit()

    def remove_all_product_locations(self, product_id: int):
        """Removes the locations of a product"""
        self.cursor.execute(f"""
            DELETE FROM {LocationDAO.__table_name}
            WHERE {LocationDAO.__COLUMN_PRODUCT_ID}={product_id}
        """)
        self.connection.commit()


class ProductDAO(DAO):

    __table_name = "PRODUCTS"
    __COLUMN_PRODUCT_ID = "product_id"
    __COLUMN_NAME = "name"
    __COLUMN_QUANTITY = "quantity"
    __COLUMN_LOW_STOCK = "low_stock"
    __COLUMN_IS_LOW_STOCK = "is_low_stock"
    __COLUMN_WEIGHT = "weight"
    __COLUMN_LAST_STORED = "last_stored"
    __COLUMN_OWNER = "owner"

    __category_dao: CategoryDAO
    __location_dao: LocationDAO
    __customer_dao: CustomerDAO

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection)
        self.__category_dao = AppDAO.get_dao("category")
        self.__location_dao = AppDAO.get_dao("location")
        self.__customer_dao = AppDAO.get_dao("customer")

    def add_product(self, product: ProductItem):
        """Adds a Product object to the PRODUCTS table"""
        is_low_stock = 1 if product.is_low_stock() else 0

        try:
            self.cursor.execute(f"""
                INSERT INTO {ProductDAO.__table_name}
                ({ProductDAO.__COLUMN_NAME},
                {ProductDAO.__COLUMN_QUANTITY},
                {ProductDAO.__COLUMN_LOW_STOCK},
                {ProductDAO.__COLUMN_WEIGHT},
                {ProductDAO.__COLUMN_LAST_STORED},
                {ProductDAO.__COLUMN_OWNER},
                {ProductDAO.__COLUMN_IS_LOW_STOCK})
                VALUES
                ('{product.get_name()}',
                {product.get_quantity()},
                {product.get_low_stock_quantity()},
                {product.get_weight()},
                '{product.get_last_stored()}',
                {product.get_owner().get_id()},
                {is_low_stock})
            """)
            self.connection.commit()

            current_product: ProductItem = self.get_product_by_name(
                product.get_name(),
                product.get_owner().get_id()
            )

            for category in product.get_category_list():
                self.__category_dao.add_product_category(
                    current_product.get_id(),
                    category
                )

            for location in product.get_locations():
                self.__location_dao.add_product_location(
                    current_product.get_id(),
                    location
                )

        except sqlite3.IntegrityError:
            print(
                "Unable to insert the product, \
                the there might be a product with same id"
            )
            return

    def get_product(self, product_id: int) -> ProductItem:
        """Returns a ProductItem object given an id"""
        self.cursor.execute(f"""
            SELECT *
            FROM {ProductDAO.__table_name}
            WHERE {ProductDAO.__COLUMN_PRODUCT_ID}={product_id}
        """)

        data = self.cursor.fetchone()
        categories = self.__category_dao.get_product_categories(product_id)
        locations = self.__location_dao.get_product_location(product_id)
        owner = self.__customer_dao.get_customer(data[6])
        product = ProductItem(
            data[0],
            data[1],
            data[2],
            data[3],
            data[7],
            locations,
            data[4],
            data[5],
            owner,
            categories
        )
        return product

    def get_product_by_name(self, product_name: str, owner_id: int) -> ProductItem:
        """Returns a ProductItem object given the name and owner id"""
        self.cursor.execute(f"""
            SELECT *
            FROM {ProductDAO.__table_name}
            WHERE {ProductDAO.__COLUMN_NAME}='{product_name}'
            AND {ProductDAO.__COLUMN_OWNER}={owner_id}
        """)

        data = self.cursor.fetchone()
        categories = self.__category_dao.get_product_categories(data[0])
        locations = self.__location_dao.get_product_location(data[0])
        owner = self.__customer_dao.get_customer(data[6])
        product = ProductItem(
            data[0],
            data[1],
            data[2],
            data[3],
            data[7],
            locations,
            data[4],
            data[5],
            owner,
            categories
        )
        return product

    def get_all_products(self) -> list[ProductItem]:
        """Returns all products as a list of ProductItem objects"""
        self.cursor.execute(f"""
            SELECT *
            FROM {ProductDAO.__table_name}
        """)

        data = self.cursor.fetchall()
        all_products: list[ProductItem] = list()
        for product in data:
            categories = self.__category_dao.get_product_categories(product[0])
            locations = self.__location_dao.get_product_location(product[0])
            owner = self.__customer_dao.get_customer(product[6])
            product_object = ProductItem(
                product[0],
                product[1],
                product[2],
                product[3],
                product[7],
                locations,
                product[4],
                product[5],
                owner,
                categories
            )
            all_products.append(product_object)

        return all_products

    def update_product(
        self,
        id: int,
        name: str = None,
        quantity: int = None,
        low_stock: bool = None,
        weight: float = None,
        last_stored: str = None,
        owner_id: int = None
    ):
        query = f"UPDATE {ProductDAO.__table_name} SET "

        if name is not None:
            query += f'{ProductDAO.__COLUMN_NAME}="{name}", '
        if quantity is not None:
            query += f'{ProductDAO.__COLUMN_QUANTITY}={quantity}, '
        if low_stock is not None:
            status = 1 if low_stock else 0
            query += f'{ProductDAO.__COLUMN_LOW_STOCK}={status}, '
        if weight is not None:
            query += f'{ProductDAO.__COLUMN_WEIGHT}={weight}, '
        if last_stored is not None:
            query += f'{ProductDAO.__COLUMN_LAST_STORED}="{last_stored}", '
        if owner_id is not None:
            query += f'{ProductDAO.__COLUMN_OWNER}={owner_id}, '

        if query[-2] == ",":
            query = query[:-2]

        query += f" WHERE {CustomerDAO.__COLUMN_ID}={id}"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product(self, product_id: int):
        """Removes a product from the database"""
        self.cursor.execute(f"""
            DELETE FROM {ProductDAO.__table_name}
            WHERE {ProductDAO.__COLUMN_PRODUCT_ID}={product_id}
        """)
        self.connection.commit()

        self.__category_dao.remove_all_product_categories(product_id)
        self.__location_dao.remove_all_product_locations(product_id)


class ShelfDAO(DAO):
    pass
