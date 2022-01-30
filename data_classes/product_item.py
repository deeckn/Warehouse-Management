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
