from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    phone: str
    email: str
    packing_service: bool
    rental_duration: str
    date_joined: str
    expiry_date: str
    total_payment: float
