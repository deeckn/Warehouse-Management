from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from data.categories import ProductCategory
from views.theme import Theme

class ProductCategoryItem(QLabel):
    def __init__(self, catergory : ProductCategory):
        QLabel.__init__(self,str(catergory))
        self.setFixedSize(100, 35)
        self.setFont(Theme.POPPINS_BOLD_14)
        self.setAlignment(Qt.AlignCenter)
        color = self.get_color(str(catergory))
        border_color = self.get_border_color(str(catergory))
        self.setStyleSheet(f"background-color: {color}; border-radius: 17; border: 4px solid {border_color}; ")

    @staticmethod
    def get_color(category: str):
        if(category == "Electronics"):
            return Theme.YELLOW
        if(category == "Fashion"):
            return Theme.VIOLET
        if(category == "Utensils"):
            return Theme.CREAM
        if(category == "Furniture"):
            return Theme.LIGHT_BLUE
        if(category == "Collectibles"):
            return Theme.LIGHT_BROWN
        if(category == "Dry Food"):
            return Theme.RED_ORANGE
        if(category == "Chemicals"):
            return Theme.GREEN
        if(category == "Others"):
            return Theme.LIGHT_GREY

    @staticmethod  
    def get_border_color(category: str):
        if(category == "Electronics"):
            return Theme.DARK_YELLOW
        if(category == "Fashion"):
            return Theme.DARK_VIOLET
        if(category == "Utensils"):
            return Theme.DARK_CREAM
        if(category == "Furniture"):
            return Theme.BLUE
        if(category == "Collectibles"):
            return Theme.BROWN
        if(category == "Dry Food"):
            return Theme.DARK_RED_ORANGE
        if(category == "Chemicals"):
            return Theme.DARK_GREEN
        if(category == "Others"):
            return Theme.DARK_GREY