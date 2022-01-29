
class ProductCategory:
    def __init__(self, category_name: str) -> None:
        super().__init__()
        self.category_name = category_name

    def get_category_name(self) -> str:
        return self.category_name
