from abc import ABC, abstractmethod


class ProductCategory(ABC):
    def __init__(self, category_name: str):
        self.category_name = category_name

    @abstractmethod
    def get_category(self) -> str:
        return self.category_name
