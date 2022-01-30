from filter_option import FilterOption


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
