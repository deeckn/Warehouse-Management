from dataclasses import dataclass
from customer import Customer
from abstractions.categories import ProductCategory


@dataclass
class ProductItem:
    __owner: Customer
    __id: int
    __name: str
    __quantity: int
    __low_stock: int
    __location: str
    __weight: float
    __last_stored: str
    __categories: list[ProductCategory]

    def get_owner(self) -> Customer:
        return self.__owner

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_quantity(self) -> int:
        return self.__quantity

    def get_low_stock(self) -> int:
        return self.__low_stock

    def get_location(self) -> str:
        return self.__location

    def get_weight(self) -> float:
        return self.__weight

    def get_last_stored(self) -> str:
        return self.__last_stored

    def get_category_list(self) -> list[ProductCategory]:
        return self.__categories
