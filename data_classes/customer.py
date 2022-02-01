from dataclasses import dataclass


@dataclass
class Customer:
    __name: str
    __phone: str
    __email: str
    __packing_service: bool
    __rental_duration: str
    __date_joined: str
    __expiry_date: str
    __total_payment: float

    def get_name(self) -> str:
        return self.__name

    def get_phone(self) -> str:
        return self.__phone

    def get_email(self) -> str:
        return self.__email

    def get_packing_service(self) -> bool:
        return self.__packing_service

    def get_rental_duration(self) -> str:
        return self.__rental_duration

    def get_date_joined(self) -> str:
        return self.__date_joined

    def get_expiry_date(self) -> str:
        return self.__expiry_date

    def get_total_payment(self) -> float:
        return self.__total_payment
