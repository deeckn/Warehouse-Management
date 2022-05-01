from abc import ABC

from data.data_classes import *
from data.filter_options import *
from data.app_dao import *
from datetime import date
from dateutil import relativedelta


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

    def set_current_user(self, username: str):
        self.__current_user = self.user_dao.get_user_by_username(username)


class HomeModel(Model):

    __current_user: User
    __product_dao: ProductDAO
    __customer_dao: CustomerDAO
    __log_dao: LogDAO

    def __init__(self, current_user: User):
        self.__current_user = current_user
        self.__product_dao = AppDAO.get_dao("product")
        self.__customer_dao = AppDAO.get_dao("customer")
        self.__log_dao = AppDAO.get_dao("log")

    def search_product(self, search_input: str, filter: FilterOption) -> list[ProductItem]:
        """Returns a list of ProductItem objects based on the search query and filter"""

        if isinstance(filter, IdFilter):
            return [self.__product_dao.get_product(int(search_input))]

        if isinstance(filter, NameFilter):
            return self.__product_dao.get_product_contains_with(search_input)

        if isinstance(filter, CustomerFilter):
            customers = self.__customer_dao.get_customer_contains_with(
                search_input)
            if customers is None:
                return None

            customer_ids = list(map(lambda c: c.get_id(), customers))
            products: list[ProductItem] = list()
            for id in customer_ids:
                temp = self.__product_dao.get_customer_products(id)
                if temp is None:
                    continue
                products.extend(temp)
            return products

        return None

    def get_activity_logs(self) -> list[LogEntry]:
        """Returns a list of all LogEntry objects in the database"""
        return self.__log_dao.get_all_log_entries()

    def add_product_quantity(self, product: ProductItem, quantity: int):
        current_quantity = product.get_quantity()
        self.__product_dao.update_product(
            id=product.get_id(), quantity=current_quantity+quantity)

        # Logging
        log = LogEntry(
            f"{self.__current_user.get_username()} added {quantity} items for Product ID: {product.get_id()}")
        self.__log_dao.add_log_entry(log)

    def export_product(self, product: ProductItem, quantity: int):
        current_quantity = product.get_quantity()
        self.__product_dao.update_product(
            id=product.get_id(), quantity=current_quantity-quantity)

        # Logging
        log = LogEntry(
            f"{self.__current_user.get_username()} exported {quantity} items for Product ID: {product.get_id()}")
        self.__log_dao.add_log_entry(log)


class CustomerListModel(Model):

    __current_user: User
    __customer_dao: CustomerDAO
    __log_dao: LogDAO

    def __init__(self, current_user: User):
        self.__current_user = current_user
        self.__customer_dao = AppDAO.get_dao("customer")
        self.__log_dao = AppDAO.get_dao("log")

    def get_customer_contains_with(self, search: str) -> list[Customer]:
        """Returns a list of Customer objects from database with the name that contains the search string"""
        return self.__customer_dao.get_customer_contains_with(search)

    def get_all_customers(self) -> list[Customer]:
        """Returns a list of all Customers object in the database"""
        return self.__customer_dao.get_all_customers()

    def add_customer(self, customer: Customer):
        """Adds a new customer to the database"""
        if customer is not None:
            self.__customer_dao.add_customer(customer)

            # Logging
            log = LogEntry(
                f"{self.__current_user.get_username()} added {customer.get_name()} to the system")
            self.__log_dao.add_log_entry(log)

    def save_customer_data(self, previous_info: Customer, new_info: Customer):
        """Saves changes made to customer information"""

        name = None if previous_info.get_name(
        ) == new_info.get_name() else new_info.get_name()

        phone = None if previous_info.get_phone(
        ) == new_info.get_phone() else new_info.get_phone()

        email = None if previous_info.get_email(
        ) == new_info.get_email() else new_info.get_email()

        packing_service = None if previous_info.get_packing_service(
        ) == new_info.get_packing_service() else new_info.get_packing_service()

        if packing_service is not None:
            packing_service = 1 if packing_service else 0

        rental_duration = None if previous_info.get_rental_duration(
        ) == new_info.get_rental_duration() else new_info.get_rental_duration()

        date_joined = None if previous_info.get_date_joined(
        ) == new_info.get_date_joined() else new_info.get_date_joined()

        expiry_date = None if previous_info.get_expiry_date(
        ) == new_info.get_expiry_date() else new_info.get_expiry_date()

        total_payment = None if previous_info.get_total_payment(
        ) == new_info.get_total_payment() else new_info.get_total_payment()

        self.__customer_dao.update_customer(
            previous_info.get_id(),
            name=name,
            phone=phone,
            email=email,
            packing_service=packing_service,
            rental_duration=rental_duration,
            date_joined=date_joined,
            expiry_date=expiry_date,
            total_payment=total_payment
        )

        # Logging
        log = LogEntry(
            f"{self.__current_user.get_username()} updated Customer ID: {previous_info.get_id()} information")
        self.__log_dao.add_log_entry(log)

    def delete_customer(self, customer: Customer):
        """Deletes the given customer from the system"""
        self.__customer_dao.delete_customer(customer.get_id())

        # Logging
        log = LogEntry(
            f"{self.__current_user.get_username()} deleted Customer ID: {customer.get_id()} from the system")
        self.__log_dao.add_log_entry(log)

    def calculate_expiry_date(self, starting_date: date, duration: int) -> date:
        """Returns the an ending date string given the starting date and duration"""
        expiry_date = starting_date + \
            relativedelta.relativedelta(months=duration)
        return expiry_date


class ProductListModel(Model):

    __current_user: User
    __product_dao: ProductDAO
    __location_dao: LocationDAO
    __shelf_dao: ShelfDAO
    __log_dao: LogDAO
    __customer_dao: CustomerDAO

    def __init__(self, current_user: User):
        self.__current_user = current_user
        self.__product_dao = AppDAO.get_dao("product")
        self.__location_dao = AppDAO.get_dao("location")
        self.__shelf_dao = AppDAO.get_dao("shelf")
        self.__log_dao = AppDAO.get_dao("log")
        self.__customer_dao = AppDAO.get_dao("customer")

    def get_all_products(self) -> list[ProductItem]:
        """Returns all products as a list of ProductItem objects"""
        return self.__product_dao.get_all_products()

    def get_product(self, product_id: int) -> ProductItem:
        """Returns a product object given the id"""
        return self.__product_dao.get_product(product_id)

    def search_products_by_customer(self, customer_name: str) -> list[ProductItem]:
        """Returns a list of products based on customer name query"""
        customers = self.__customer_dao.get_customer_contains_with(
            customer_name)
        products: list[ProductItem] = list()
        for customer in customers:
            customer_products = self.__product_dao.get_customer_products(
                customer.get_id())
            if customer_products is not None:
                products.extend(customer_products)

        return products

    def search_product_by_id(self, product_id: int) -> ProductItem:
        """Returns a product item given an ID"""
        return self.__product_dao.get_product(product_id)

    def search_products_by_name(self, product_name: str) -> list[ProductItem]:
        """Returns a list of product items that corresonds to the query string"""
        return self.__product_dao.get_product_contains_with(product_name)

    def is_batch_fit(self, product: ProductItem, quantity: int, shelf: StorageShelf) -> bool:
        """Returns True if the batch can fit in the shelf"""

        product_length, product_width, product_height = product.get_dimension().get_dimension()
        shelf_length, shelf_width, shelf_height = shelf.get_dimensions()

        if (product_length > shelf_length) | \
                (product_width > shelf_width) | \
                (product_height > shelf_height):
            return False

        shelf_volume = shelf.get_volume()

        product_data = self.__location_dao.get_products_on_shelf(
            shelf.get_label())
        occupied_volume = 0

        for data in product_data:
            temp_product = self.__product_dao.get_product(data[0])
            product_volume = temp_product.get_volume()
            occupied_volume += product_volume * data[1]

        shelf_volume -= occupied_volume
        batch_volume = product_length * product_width * product_height * quantity

        return batch_volume < shelf_volume

    def add_new_product(self, product: ProductItem, quantity: int, shelf_label: str, shelf_number: int) -> bool:
        """Adds a new product to the system, returns True for successful operation"""
        if self.__product_dao.exist(product):
            return False

        shelf = self.__shelf_dao.get_shelf_by_label(shelf_label)
        if shelf is None:
            return False

        if not self.is_batch_fit(product, quantity, shelf):
            return False

        # Add new product
        self.__product_dao.add_product(product)

        # Add first batch
        data_product = self.__product_dao.get_product_by_name(
            product.get_name(), product.get_owner().get_id())
        location = Location(1, quantity, shelf_label, shelf_number)
        self.__location_dao.add_product_location(
            data_product.get_id(), location)

        # Logging
        log = LogEntry(
            f"{self.__current_user.get_username()} added {product.get_name()} to the system")
        self.__log_dao.add_log_entry(log)

        return True

    def add_new_batch(self, product_id: int, quantity: int, shelf_label: str, shelf_number: int) -> bool:
        """Adds a new product batch, returns True for a successful operation"""
        batch_count = self.__location_dao.get_batch_count(product_id)
        if batch_count == 0:
            return False

        location = Location(batch_count+1, quantity,
                            shelf_label, shelf_number)
        self.__location_dao.add_product_location(product_id, location)

        # Update quantity
        product_quantity = self.__product_dao.get_product(
            product_id).get_quantity()
        product_quantity += quantity
        self.__product_dao.update_product(
            product_id, quantity=product_quantity)

        return True

    def edit_product(self, old_data: ProductItem, new_data: ProductItem):
        """Updates product information based on the difference of objects"""
        name = None if old_data.get_name() == new_data.get_name() else new_data.get_name()

        quantity = None if old_data.get_quantity(
        ) == new_data.get_quantity() else new_data.get_quantity()

        low_stock = None if old_data.get_low_stock_quantity(
        ) == new_data.get_low_stock_quantity() else new_data.get_low_stock_quantity()

        weight = None if old_data.get_weight(
        ) == new_data.get_weight() else new_data.get_weight()

        last_stored = None if old_data.get_last_stored(
        ) == new_data.get_last_stored() else new_data.get_last_stored()

        owner_id = None if old_data.get_owner().get_id(
        ) == new_data.get_owner().get_id() else new_data.get_owner().get_id()

        length = None if old_data.get_dimension().get_length(
        ) == new_data.get_dimension().get_length() else new_data.get_dimension().get_length()

        width = None if old_data.get_dimension().get_width(
        ) == new_data.get_dimension().get_width() else new_data.get_dimension().get_width()

        height = None if old_data.get_dimension().get_height(
        ) == new_data.get_dimension().get_height() else new_data.get_dimension().get_height()

        self.__product_dao.update_product(
            old_data.get_id(),
            name,
            quantity,
            low_stock,
            weight,
            last_stored,
            owner_id,
            length,
            width,
            height
        )

    def delete_product(self, product_id: int):
        """Deletes a product from the system"""
        self.__product_dao.delete_product(product_id)

        log = LogEntry(
            f"{self.__current_user.get_username()} deleted Product ID: {product_id} from the system")
        self.__log_dao.add_log_entry(log)

    def get_occupied_slots(self, shelf_label: str) -> list[int]:
        """Returns a list of shelf numbers (slots) that are occupied"""
        return self.__location_dao.get_occupied_slots(shelf_label)

    def get_available_shelves(self, product: ProductItem) -> list[StorageShelf]:
        """Returns a list of available shelves that the given product can fit"""
        product_volume = product.get_dimension().get_volume()
        shelves = self.__shelf_dao.get_all_shelves()

        available_shelves: list[StorageShelf] = list()
        for shelf in shelves:
            if shelf.get_volume() > product_volume:
                available_shelves.append(shelf)
        return available_shelves


class AccountModel(Model):
    __current_admin: User
    __user_dao: UserDAO
    __log_dao: LogDAO

    def __init__(self, user: User = None):
        self.__current_admin = user
        self.__user_dao = AppDAO.get_dao("user")
        self.__log_dao = AppDAO.get_dao("log")

    def get_employee_accounts(self) -> list[User]:
        """Returns all user objects from the database"""
        return self.__user_dao.get_all_users()

    def create_new_account(self, user: User):
        """Adds a new user object to the database"""
        self.__user_dao.add_user(user)

        # Logging
        log = LogEntry(
            f"ADMIN: {self.__current_admin.get_username()} created a new account for {user.get_username()}")
        self.__log_dao.add_log_entry(log)

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

    def update_user_info(self, previous_info: User, new_user_info: User):
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

        # Logging
        log = LogEntry(
            f"ADMIN: {self.__current_admin.get_username()} updated ID:{previous_info.get_id()} account")
        self.__log_dao.add_log_entry(log)

    def admin_confirmation(self, password: str) -> bool:
        """Returns the status of admin password confirmation"""
        return self.__current_admin.get_password() == password

    def delete_user_account(self, user: User):
        """Deletes a user object from the database"""
        self.__user_dao.delete_user_by_id(user.get_id())

        # Logging
        log = LogEntry(
            f"ADMIN: {self.__current_admin.get_username()} deleted User: {user.get_username()} from the system")
        self.__log_dao.add_log_entry(log)


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
        products = self.__product_dao.get_low_quantity_products()
        products.sort(key=lambda p: p.get_quantity(), reverse=False)
        return products

    def get_contract_ending_customers(self) -> list[Customer]:
        """Returns a list of contract ending Customer objects"""
        customers = self.__customer_dao.get_all_customers()
        if customers is None:
            return None
        customers = list(
            filter(
                lambda c: self.__within_deadline(
                    self.date_difference(c)
                ),
                customers
            )
        )

        # Sorting by ugency
        customers.sort(key=lambda c: self.date_difference(c), reverse=False)

        if len(customers) == 0:
            return None
        return customers

    def date_difference(self, customer) -> int:
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
    __current_admin: User
    __shelf_dao: ShelfDAO
    __log_dao: LogDAO

    def __init__(self, admin: User):
        self.__current_admin = admin
        self.__shelf_dao = AppDAO.get_dao("shelf")
        self.__log_dao = AppDAO.get_dao("log")

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

        # Logging
        log = LogEntry(
            f"ADMIN: {self.__current_admin.get_username()} added a new shelf with the label {label}")
        self.__log_dao.add_log_entry(log)

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

        # Logging
        log = LogEntry(
            f"ADMIN: {self.__current_admin.get_username()} updated {previous_info.get_label()} information")
        self.__log_dao.add_log_entry(log)

    def delete_shelf(self, shelf: StorageShelf):
        """Deletes a shelf from the database"""
        self.__shelf_dao.delete_shelf(shelf.get_label())

        # Logging
        log = LogEntry(
            f"ADMIN: {self.__current_admin.get_username()} deleted {shelf.get_label()} from the system")
        self.__log_dao.add_log_entry(log)

    def calculate_total_slots(self, rows, columns) -> int:
        """Returns the total number of slots"""
        return rows * columns

    def get_shelves_contains_with(self, shelf_search: str) -> list[StorageShelf]:
        """Returns a list of StorageShelf objects given a search query"""
        return self.__shelf_dao.get_shelves_contains_with(shelf_search)

    def get_all_shelves(self) -> list[StorageShelf]:
        """Returns a list of all StorageShelf objects from the database"""
        return self.__shelf_dao.get_all_shelves()


class InventoryOverviewModel(Model):
    __product_dao: ProductDAO
    __customer_dao: CustomerDAO

    def __init__(self):
        self.__product_dao = AppDAO.get_dao("product")
        self.__customer_dao = AppDAO.get_dao("customer")

    def get_customer_selection(self) -> list[Customer]:
        """Returns a list of Customers"""
        return self.__customer_dao.get_all_customers()

    def get_all_product_list(self) -> list[ProductItem]:
        """Returns a list of Products"""
        return self.__product_dao.get_all_products()

    def get_product_list_by_owner_id(self, owner_id: int) -> list[ProductItem]:
        """Returns a list of Owner's Products"""
        return self.__product_dao.get_customer_products(owner_id)

    def get_product_stock(self, owner_id: int) -> float:
        """Returns percent of each Customers"""
        total = len(self.get_all_product_list())
        if self.get_product_list_by_owner_id(owner_id) is None:
            percent = 0
        else:
            item = len(self.get_product_list_by_owner_id(owner_id))
            percent = (item/total)*100
        return percent

    def get_all_product_stock(self, owners: list[Customer]) -> list[float]:
        """Returns percent of all Customers"""
        owner_percent = list()
        for owner in owners:
            owner_percent.append(self.get_product_stock(owner.get_id()))
        return owner_percent


class ReportModel(Model):

    __report_dao: ReportDAO
    __customer_dao: CustomerDAO
    __product_dao: ProductDAO
    __log_dao: LogDAO

    __notification_model: NotificationModel

    def __init__(self, current_user: User):
        self.__current_user = current_user
        self.__report_dao = AppDAO.get_dao("report")
        self.__customer_dao = AppDAO.get_dao("customer")
        self.__product_dao = AppDAO.get_dao("product")
        self.__log_dao = AppDAO.get_dao("log")

        self.__notification_model = NotificationModel()

    def calculate_customer_stock_percentage(self, customer: Customer) -> float:
        customer_count = self.__product_dao.get_customer_product_count(
            customer.get_id())
        total_count = self.__product_dao.get_total_product_count()
        return (customer_count / total_count) * 100

    def get_all_reports(self) -> list[QuarterlyReport]:
        return self.__report_dao.get_all_reports()

    def get_all_customers(self) -> list[Customer]:
        return self.__customer_dao.get_all_customers()

    def generate_csv_report(self, file_path: str):
        with open(file_path, "w") as file:
            # Quarterly Report
            reports = self.__report_dao.get_all_reports()

            if reports is not None:
                file.write(
                    "Quarterly Report,\nYEAR,QUARTER,REVENUE,UTILIZED SPACE,\n")

                for report in reports:
                    file.write(
                        f"{report.get_year()},{report.get_quarter()},{report.get_total_revenue()},{report.get_utilized_space_percentage()}%,\n"
                    )

            # Customer List
            customers = self.__customer_dao.get_all_customers()

            if customers is not None:
                file.write(
                    "\nCustomer List,\nID,NAME,PHONE,EMAIL,PACKING SERVICE,RENTAL DURATION,DATE JOINED,EXPIRY DATE,TOTAL PAYMENT,\n")

                for customer in customers:
                    file.write(
                        f"{customer.get_id()},{customer.get_name()},{customer.get_phone()},{customer.get_email()},{customer.get_packing_service()},{customer.get_rental_duration()},{customer.get_date_joined()},{customer.get_expiry_date()},{customer.get_total_payment()},\n"
                    )

            # Product List
            if customers is not None:
                file.write(
                    "\nProduct List of Customer Products,\nID,NAME,QUANTITY,WEIGHT,LAST STORED,OWNER\n")

                for customer in customers:
                    products = self.__product_dao.get_customer_products(
                        customer.get_id())
                    if products is None:
                        continue

                    for product in products:
                        file.write(
                            f"{product.get_id()},{product.get_name()},{product.get_quantity()},{product.get_weight()},{product.get_last_stored()},{customer.get_name()},\n")

            # Low Stock Products
            low_stock_products = self.__notification_model.get_low_stock_products()

            if low_stock_products is not None:
                file.write(
                    "\nList of Low Quantity Products,\nID,NAME,QUANTITY,WEIGHT,LAST STORED,OWNER\n")

                for product in low_stock_products:
                    file.write(
                        f"{product.get_id()},{product.get_name()},{product.get_quantity()},{product.get_weight()},{product.get_last_stored()},{product.get_owner().get_name()},\n")

            # Contract Ending Customers
            ending_customers = self.__notification_model.get_contract_ending_customers()

            if ending_customers is not None:
                file.write(
                    "\nList of Contract Ending Customers,\nID,NAME,DAYS LEFT\n")

                for customer in ending_customers:
                    file.write(
                        f"{customer.get_id()},{customer.get_name()},{self.__notification_model.date_difference(customer)},\n")

            # Logs
            logs = self.__log_dao.get_all_log_entries()

            if logs is not None:
                file.write(
                    f"\nLog of System Activities ({LogDAO.LOG_LIMIT} recent),\nID,DATE,TIME,DESCRIPTION\n")

                for log in logs:
                    file.write(
                        f"{log.get_id()},{log.get_date()},{log.get_time()},{log.get_description()},\n")

            file.close()

        log = LogEntry(
            f"{self.__current_user.get_username()} exported report CSV file")
        self.__log_dao.add_log_entry(log)
