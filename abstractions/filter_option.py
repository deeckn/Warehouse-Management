
class FilterOption:
    def __init__(self, option_name: str) -> None:
        self.option = option_name

    def get_option(self) -> str:
        return self.option

    def __str__(self) -> str:
        return f"Option: {self.option}"
