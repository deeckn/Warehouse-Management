from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from data.orm.schema import Product
from views.items.product_category_item import ProductCategoryItem
from views.theme import Theme


class ProductListCard(QWidget):
    def __init__(self, parent, product: Product):
        QWidget.__init__(self,  None)
        self.setFixedSize(680, 177)
        self.product = product
        self.qparent = parent

        self.bg = QLabel(self)
        self.bg.setGeometry(0, 0, 680, 177)
        self.bg.setStyleSheet(
            f"background-color: {Theme.GHOST_WHITE}; border-radius: 30;")

        category_conatiner = QWidget(self)
        category_conatiner.setGeometry(338, 110, 324, 39)
        self.category_layout = QHBoxLayout(category_conatiner)
        self.category_layout.setContentsMargins(5, 0, 5, 0)
        self.category_layout.setAlignment(Qt.AlignLeft)
        category_conatiner.setStyleSheet("background-color: none;")

        self.product_info_1 = QLabel(self)
        self.product_info_1.setGeometry(39, 20, 299, 135)
        self.product_info_1.setFont(Theme.POPPINS_REGULAR_18)
        self.product_info_1.setStyleSheet(
            "background-color: none; color: black;")

        text = f"Customer: {product.get_owner().get_name()}\n" + \
            f"Product ID: {product.get_id()}\n" + \
            f"Product Name: {product.get_name()}\n" + \
            f"Quantity: {product.get_quantity()}\n" + \
            f"Location "

        self.product_info_1.setText(text)

        self.product_info_2 = QLabel(self)
        self.product_info_2.setGeometry(340, 20, 322, 80)
        self.product_info_2.setFont(Theme.POPPINS_REGULAR_18)
        self.product_info_2.setStyleSheet(
            "background-color: none; color: black;")

        text = f"Weight: {product.get_weight()}\n" + \
            f"Low stock level: {product.get_low_stock_quantity()}\n" + \
            f"Date Last Stored: {product.get_last_stored()}\n"

        self.product_info_2.setText(text)

    def mousePressEvent(self, event) -> None:
        if(self.qparent.current_product == self):
            self.unclick()
            self.qparent.current_product = None
            self.qparent.unselect_event()
            return

        if(self.qparent.current_product != None):
            self.qparent.current_product.unclick()

        self.qparent.current_product = self
        self.qparent.select_event()

        self.bg.setStyleSheet(
            f"background-color: {Theme.GHOST_WHITE}; border-radius: 30; border: 3px solid {Theme.YELLOW};")

    def unclick(self):
        self.bg.setStyleSheet(
            f"background-color: {Theme.GHOST_WHITE}; border-radius: 30;")

    def clear_category(self):
        for i in reversed(range(self.category_layout.count())):
            self.category_layout.itemAt(i).widget().close()
