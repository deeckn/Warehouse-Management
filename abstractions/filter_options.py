
class FilterOption:
    def __init__(self, option_name: str) -> None:
        self.option = option_name

    def get_option(self) -> str:
        return self.option

    def __str__(self) -> str:
        return f"Option: {self.option}"


class NameFilter(FilterOption):
    def __init__(self) -> None:
        self.option = "name"


class IdFilter(FilterOption):
    def __init__(self) -> None:
        self.option = "id"


class CustomerFilter(FilterOption):
    def __init__(self) -> None:
        self.option = "customer"


class DateFilter(FilterOption):
    def __init__(self) -> None:
        self.option = "date"


class QuantityFilter(FilterOption):
    def __init__(self) -> None:
        self.option = "quantity"


class WeightFilter(FilterOption):
    def __init__(self) -> None:
        self.option = "weight"
