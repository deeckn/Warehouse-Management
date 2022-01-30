from category import ProductCategory


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
