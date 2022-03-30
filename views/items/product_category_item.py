from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from data.data_classes import ProductCategory
from views.theme import Theme


class ProductCategory(QWidget):
    def __init__(self, category: ProductCategory):
        self.setFixedSize(100, 35)
        bg = QLabel(self)
        bg.setGeometry(0, 0, 100, 35)
        bg.setStyleSheet(
            f"background-color: {Theme.YELLOW}; border: 4px solid {Theme.DARK_GREEN};")
