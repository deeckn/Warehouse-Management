from abc import ABC, abstractmethod


class ProductCategory(ABC):
    def __init__(self, category_name: str):
        self.category_name = category_name

    @abstractmethod
    def get_category(self) -> str:
        return self.category_name


class Electronics(ProductCategory):
    def __init__(self):
        super().__init__("Electronics")


class Fashion(ProductCategory):
    def __init__(self):
        super().__init__("Fashion")


class Utensils(ProductCategory):
    def __init__(self):
        super().__init__("Utensils")


class Furniture(ProductCategory):
    def __init__(self):
        super().__init__("Furniture")


class Collectibles(ProductCategory):
    def __init__(self):
        super().__init__("Collectibles")


class DryFood(ProductCategory):
    def __init__(self):
        super().__init__("DryFood")


class Chemicals(ProductCategory):
    def __init__(self):
        super().__init__("Chemicals")


class Others(ProductCategory):
    def __init__(self):
        super().__init__("Others")
