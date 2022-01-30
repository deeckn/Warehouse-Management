from dataclasses import dataclass
from customer import Customer


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
