from dataclasses import dataclass
from datetime import datetime
from data.access_level import AccessLevel
from data.categories import ProductCategory


@dataclass
class User:
    __id: int
    __first_name: str
    __last_name: str
    __username: str
    __password: str
    __access: AccessLevel

    def get_id(self) -> int:
        return self.__id

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_access_level(self) -> AccessLevel:
        return self.__access


@dataclass
class Customer:

    __id: int
    __name: str
    __phone: str
    __email: str
    __packing_service: bool
    __rental_duration: int
    __date_joined: str
    __expiry_date: str
    __total_payment: float

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_phone(self) -> str:
        return self.__phone

    def get_email(self) -> str:
        return self.__email

    def get_packing_service(self) -> bool:
        return self.__packing_service

    def get_rental_duration(self) -> int:
        return self.__rental_duration

    def get_date_joined(self) -> str:
        return self.__date_joined

    def get_expiry_date(self) -> str:
        return self.__expiry_date

    def get_total_payment(self) -> float:
        return self.__total_payment


@dataclass
class StorageShelf:
    __label: str
    __max_weight: float
    __length: float
    __width: float
    __height: float
    __rows: int
    __columns: int

    def get_label(self) -> str:
        return self.__label

    def get_max_weight(self) -> float:
        return self.__max_weight

    def get_length(self) -> float:
        return self.__length

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.__height

    def get_rows(self) -> int:
        return self.__rows

    def get_columns(self) -> int:
        return self.__columns


@dataclass
class LogEntry:
    __id: int
    __date: str
    __time: str
    __description: str

    def __init__(self, description: str, id: int = None, date: str = None, time: str = None):
        self.__id = id
        self.__date = date
        self.__time = time
        self.__description = description

        if None in [self.__date, self.__time]:
            today = datetime.now()
            self.__date = f"{today.day:02d}_{today.month:02d}_{today.year}"
            self.__time = f"{today.hour:02d}_{today.minute:02d}"

    def get_id(self) -> int:
        return self.__id

    def get_date(self) -> str:
        return self.__date

    def get_time(self) -> str:
        return self.__time

    def get_description(self) -> str:
        return self.__description

    def get_data(self) -> tuple:
        return self.__date, self.__time, self.__description

    def __str__(self) -> str:
        return f"Date: {self.__date}, Time: {self.__time}, Description: {self.__description}"


@dataclass
class Location:
    batch_number: int
    quantity: int
    shelf_label: str

    def __str__(self):
        return self.shelf_label

    def get_batch_number(self) -> int:
        return self.batch_number

    def get_batch_quantity(self) -> int:
        return self.quantity

    def get_shelf_label(self) -> str:
        return self.shelf_label


@dataclass
class Dimension:
    __length: float
    __width: float
    __height: float

    def get_dimension(self) -> tuple[float, float, float]:
        return self.__length, self.__width, self.__height


@dataclass
class ProductItem:
    __id: int
    __name: str
    __quantity: int
    __low_stock: int
    __locations: list[Location]
    __weight: float
    __last_stored: str
    __owner: Customer
    __categories: list[ProductCategory]
    __dimension: Dimension

    def get_owner(self) -> Customer:
        return self.__owner

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_quantity(self) -> int:
        return self.__quantity

    def get_low_stock_quantity(self) -> int:
        return self.__low_stock

    def is_low_stock(self) -> bool:
        return self.__quantity <= self.__low_stock

    def get_locations(self) -> list[Location]:
        return self.__locations

    def get_weight(self) -> float:
        return self.__weight

    def get_last_stored(self) -> str:
        return self.__last_stored

    def get_category_list(self) -> list[ProductCategory]:
        return self.__categories

    def add_quantity(self, new_quantity: int):
        self.__quantity += new_quantity

    def export_quantity(self, exported_quantity: int):
        self.__quantity -= exported_quantity

    def get_dimension(self) -> Dimension:
        return self.__dimension


@dataclass
class QuarterlyReport:
    __year: int
    __quarter: int
    __utilized_space: float
    __total_revenue: float

    def get_year(self) -> int:
        return self.__year

    def get_quarter(self) -> int:
        return self.__quarter

    def get_utilized_space(self) -> float:
        return self.__utilized_space

    def get_unutilized_space(self) -> float:
        return 1 - self.__utilized_space

    def get_total_revenue(self) -> float:
        return self.__total_revenue

    def get_monthly_revenue(self) -> float:
        return self.__total_revenue / 12
