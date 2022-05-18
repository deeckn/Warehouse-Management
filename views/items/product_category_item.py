from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from views.theme import Theme


class ProductCategoryItem(QLabel):
    def __init__(self, catergory: str):
        QLabel.__init__(self, str(catergory))
        self.setFixedSize(100, 35)
        self.setFont(Theme.POPPINS_BOLD_14)
        self.setAlignment(Qt.AlignCenter)
        color = self.get_color(str(catergory))
        border_color = self.get_border_color(str(catergory))
        self.setStyleSheet(
            f"background-color: {color}; border-radius: 17; border: 4px solid {border_color}; color: white;")

    @staticmethod
    def get_color(category: str):
        if category == "electronics":
            return Theme.YELLOW
        if category == "fashion":
            return Theme.VIOLET
        if category == "utensils":
            return Theme.CREAM
        if category == "furniture":
            return Theme.LIGHT_BLUE
        if category == "collectibles":
            return Theme.LIGHT_BROWN
        if category == "dry_food":
            return Theme.RED_ORANGE
        if category == "chemicals":
            return Theme.GREEN
        if category == "others":
            return Theme.LIGHT_GREY

    @staticmethod
    def get_border_color(category: str):
        if category == "electronics":
            return Theme.DARK_YELLOW
        if category == "fashion":
            return Theme.DARK_VIOLET
        if category == "utensils":
            return Theme.DARK_CREAM
        if category == "furniture":
            return Theme.BLUE
        if category == "collectibles":
            return Theme.BROWN
        if category == "dry_food":
            return Theme.DARK_RED_ORANGE
        if category == "chemicals":
            return Theme.DARK_GREEN
        if category == "others":
            return Theme.DARK_GREY

    def change_size(self, weight: int, height: int):
        self.setFixedSize(weight, height)
