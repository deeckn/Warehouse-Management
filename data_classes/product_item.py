from dataclasses import dataclass
from customer import Customer
from abstractions.category import ProductCategory


@dataclass
class ProductItem:
    owner: Customer
    id: int
    name: str
    quantity: int
    low_stock: int
    location: str
    weight: float
    last_stored: str
    categories: list[ProductCategory]

    def get_owner(self) -> Customer:
        return self.owner

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_quantity(self) -> int:
        return self.quantity

    def get_low_stock(self) -> int:
        return self.low_stock

    def get_location(self) -> str:
        return self.location

    def get_weight(self) -> float:
        return self.weight

    def get_last_stored(self) -> str:
        return self.last_stored

    def get_category_list(self) -> list[ProductCategory]:
        return self.categories
