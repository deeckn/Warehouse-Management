from abc import ABC


class ProductCategory(ABC):
    def __init__(self, category_name: str):
        self.category_name = category_name

    def get_category(self) -> str:
        return self.category_name

    def __str__(self) -> str:
        return self.category_name.capitalize()


class Electronics(ProductCategory):
    def __init__(self):
        super().__init__("electronics")


class Fashion(ProductCategory):
    def __init__(self):
        super().__init__("fashion")


class Utensils(ProductCategory):
    def __init__(self):
        super().__init__("utensils")


class Furniture(ProductCategory):
    def __init__(self):
        super().__init__("furniture")


class Collectibles(ProductCategory):
    def __init__(self):
        super().__init__("collectibles")


class DryFood(ProductCategory):
    def __init__(self):
        super().__init__("dry_food")

    def __str__(self) -> str:
        return "Dry Food"


class Chemicals(ProductCategory):
    def __init__(self):
        super().__init__("chemicals")


class Others(ProductCategory):
    def __init__(self):
        super().__init__("others")


class CategoryFactory:
    @staticmethod
    def get_category(category: str) -> ProductCategory:
        """Returns a ProductCategory object [
            "electronics",
            "fashion",
            "utensils",
            "furniture",
            "collectibles",
            "dry_food",
            "chemicals",
            "others"
        ]. Eg. get_category("fashion") -> Fashion()"""
        if category == "electronics":
            return Electronics()
        elif category == "fashion":
            return Fashion()
        elif category == "utensils":
            return Utensils()
        elif category == "furniture":
            return Furniture()
        elif category == "collectibles":
            return Collectibles()
        elif category == "dry_food":
            return DryFood()
        elif category == "chemicals":
            return Chemicals()
        elif category == "others":
            return Others()
        else:
            return None
