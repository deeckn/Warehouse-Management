from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Boolean, Float, create_engine
import os
from datetime import datetime

# Setup
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'data.db')
Base = declarative_base()
engine = create_engine(connection_string)
Session = sessionmaker()


class User(Base):
    # Schema
    __tablename__ = "USERS"
    user_id = Column("user_id", Integer(), primary_key=True)
    first_name = Column("first_name", String(255))
    last_name = Column("last_name", String(255))
    username = Column("username", String(255))
    password = Column("password", String(255))
    access_level = Column("access_level", String(10))

    def __init__(self, first_name: str, last_name: str, username: str, password: str, access_level: str):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.access_level = access_level

    def get_id(self) -> int:
        return self.user_id

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password

    def get_access_level(self) -> str:
        return self.access_level

    def __str__(self) -> str:
        return f"<User first_name={self.first_name} last_name={self.last_name} username={self.username} password={self.password} access={self.access_level} />"


class Customer(Base):
    # Schema
    __tablename__ = "CUSTOMERS"
    customer_id = Column("customer_id", Integer(), primary_key=True)
    name = Column("name", String(255))
    phone = Column("phone", String(255))
    email = Column("email", String(255))
    packing_service = Column("packing_service", Boolean())
    rental_duration = Column("rental_duration", Integer())
    date_joined = Column("date_joined", String(20))
    expiry_date = Column("expiry_date", String(20))
    total_payment = Column("total_payment", Float())

    def __init__(self, name: str, phone: str, email: str, packing_service: bool, rental_duration: int, date_joined: str, expiry_date: str, total_payment: float):
        super().__init__()
        self.name = name
        self.phone = phone
        self.email = email
        self.packing_service = packing_service
        self.rental_duration = rental_duration
        self.date_joined = date_joined
        self.expiry_date = expiry_date
        self.total_payment = total_payment

    def get_id(self) -> int:
        return self.customer_id

    def get_name(self) -> str:
        return self.name

    def get_phone(self) -> str:
        return self.phone

    def get_email(self) -> str:
        return self.email

    def get_packing_service(self) -> bool:
        return self.packing_service

    def get_rental_duration(self) -> int:
        return self.rental_duration

    def get_date_joined(self) -> str:
        return self.date_joined

    def get_expiry_date(self) -> str:
        return self.expiry_date

    def get_total_payment(self) -> float:
        return self.total_payment


class ProductCategory(Base):
    # Schema
    __tablename__ = "PRODUCT_CATEGORIES"
    product_id = Column("product_id", Integer(), primary_key=True)
    category = Column("category", String(255), primary_key=True)

    def __init__(self, product_id: int, category: str):
        super().__init__()
        self.product_id = product_id
        self.category = category

    def get_category(self) -> str:
        return self.category

    def __str__(self) -> str:
        return self.category


class ProductLocation(Base):
    # Schema
    __tablename__ = "PRODUCT_LOCATIONS"
    product_id = Column("product_id", Integer(), primary_key=True)
    batch_number = Column("batch_number", Integer(), primary_key=True)
    quantity = Column("quantity", Integer())
    shelf_label = Column("shelf_label", String(255))
    shelf_number = Column("shelf_number", Integer())

    def __init__(self, product_id: int, batch_number: int, quantity: int, shelf_label: str, shelf_number: int):
        super().__init__()
        self.product_id = product_id
        self.batch_number = batch_number
        self.quantity = quantity
        self.shelf_label = shelf_label
        self.shelf_number = shelf_number

    def get_batch_number(self) -> int:
        return self.batch_number

    def get_batch_quantity(self) -> int:
        return self.quantity

    def get_shelf_label(self) -> str:
        return self.shelf_label

    def get_shelf_number(self) -> int:
        return self.shelf_number

    def get_location(self) -> str:
        return f"{self.shelf_label}{self.shelf_number:03d}"

    def __str__(self):
        return self.shelf_label


class Product(Base):
    # Table Name
    __tablename__ = "PRODUCTS"

    # Schema
    product_id = Column("product_id", Integer(), primary_key=True)
    name = Column("name", String(255))
    quantity = Column("quantity", Integer())
    low_stock = Column("low_stock", Integer())
    weight = Column("weight", Float())
    last_stored = Column("last_stored", String(20))
    owner = Column("owner", Integer())
    length = Column("length", Float())
    width = Column("width", Float())
    height = Column("height", Float())

    def __init__(
        self,
        name: str,
        quantity: int,
        low_stock: int,
        weight: float,
        last_stored: str,
        owner: int,
        length: float,
        width: float,
        height: float
    ):
        super().__init__()
        self.name = name
        self.quantity = quantity
        self.low_stock = low_stock
        self.weight = weight
        self.last_stored = last_stored
        self.owner = owner
        self.length = length
        self.width = width
        self.height = height
        self.__owner_object = None

    def insert_categories(self, categories: list[ProductCategory]):
        self.categories = categories

    def insert_locations(self, locations: list[ProductLocation]):
        self.locations = locations

    def set_owner_object(self, owner: Customer):
        self.__owner_object = owner

    def get_owner(self) -> Customer:
        return self.__owner_object

    def get_id(self) -> int:
        return self.product_id

    def get_name(self) -> str:
        return self.name

    def get_quantity(self) -> int:
        return self.quantity

    def get_low_stock_quantity(self) -> int:
        return self.low_stock

    def is_low_stock(self) -> bool:
        return self.quantity <= self.low_stock

    def get_locations(self) -> list[ProductLocation]:
        return self.locations

    def get_weight(self) -> float:
        return self.weight

    def get_last_stored(self) -> str:
        return self.last_stored

    def get_category_list(self) -> list[ProductCategory]:
        return self.categories

    def get_num_of_batches(self) -> int:
        return len(self.locations)

    def add_quantity(self, new_quantity: int):
        self.quantity += new_quantity

    def export_quantity(self, exported_quantity: int):
        self.quantity -= exported_quantity

    def get_dimensions(self) -> tuple[float, float, float]:
        return self.length, self.width, self.height

    def get_volume(self) -> float:
        return self.length * self.width * self.height


class Shelf(Base):
    # Schema
    __tablename__ = "SHELVES"
    label = Column("label", String(255), primary_key=True)
    max_weight = Column("max_weight", Float())
    length = Column("length", Float())
    width = Column("width", Float())
    height = Column("height", Float())
    rows = Column("rows", Integer())
    columns = Column("columns", Integer())

    def __init__(self, label: str, max_weight: float, length: float, width: float, height: float, rows: int, columns: int):
        super().__init__()
        self.label = label
        self.max_weight = max_weight
        self.length = length
        self.width = width
        self.height = height
        self.rows = rows
        self.columns = columns

    def get_label(self) -> str:
        return self.label

    def get_max_weight(self) -> float:
        return self.max_weight

    def get_length(self) -> float:
        return self.length

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height

    def get_rows(self) -> int:
        return self.rows

    def get_columns(self) -> int:
        return self.columns

    def get_dimensions(self) -> tuple[float, float, float]:
        return self.length, self.width, self.height

    def get_volume(self) -> float:
        return self.length * self.width * self.height

    def get_entire_volume(self) -> float:
        return self.get_volume() * self.rows * self.columns


class Log(Base):
    # Schema
    __tablename__ = "LOGS"
    log_id = Column("log_id", Integer(), primary_key=True)
    date = Column("date", String(20))
    time = Column("time", String(20))
    description = Column("description", String(1024))

    def __init__(self, description: str, id: int = None, date: str = None, time: str = None):
        super().__init__()

        self.id = id
        self.date = date
        self.time = time
        self.description = description

        if None in [self.date, self.time]:
            today = datetime.now()
            self.date = f"{today.day:02d}_{today.month:02d}_{today.year}"
            self.time = f"{today.hour:02d}_{today.minute:02d}"

    def get_id(self) -> int:
        return self.log_id

    def get_date(self) -> str:
        return self.date

    def get_time(self) -> str:
        return self.time

    def get_description(self) -> str:
        return self.description

    def get_data(self) -> tuple:
        return self.date, self.time, self.description

    def __str__(self) -> str:
        return f"Date: {self.date}, Time: {self.time}, Description: {self.description}"


class QuarterlyReport(Base):
    # Schema
    __tablename__ = "QUARTERLY_REPORTS"
    year = Column("year", Integer(), primary_key=True)
    quarter = Column("quarter", Integer(), primary_key=True)
    utilized_space = Column("utilized_space", Float())
    total_revenue = Column("total_revenue", Float())

    def __init__(self, year: int, quarter: int, utilized_space: float, total_revenue: float):
        super().__init__()
        self.year = year
        self.quarter = quarter
        self.utilized_space = utilized_space
        self.total_revenue = total_revenue

    def get_year(self) -> int:
        return self.year

    def get_quarter(self) -> int:
        return self.quarter

    def get_utilized_space_percentage(self) -> float:
        return self.utilized_space * 100

    def get_unutilized_space_percentage(self) -> float:
        return 1 - self.utilized_space * 100

    def get_total_revenue(self) -> float:
        return self.total_revenue

    def get_monthly_revenue(self) -> float:
        return self.total_revenue / 12
