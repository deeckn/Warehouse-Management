from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from data.orm.schema import Product, ProductLocation
from views.items.product_category_item import ProductCategoryItem
from views.theme import Theme


class ProductListCard(QWidget):
    def __init__(self, parent, product: Product):
        QWidget.__init__(self,  None)
        self.setFixedSize(680, 200)
        self.product = product
        self.qparent = parent
        self.location = product.get_locations()
        self.click_event = None
        self.current_location = self.location[0]

        self.bg = QLabel(self)
        self.bg.setGeometry(0, 0, 680, 200)
        self.bg.setStyleSheet(
            f"background-color: {Theme.GHOST_WHITE}; border-radius: 30px;")

        category_conatiner = QWidget(self)
        category_conatiner.setGeometry(338, 110, 324, 39)
        self.category_layout = QHBoxLayout(category_conatiner)
        self.category_layout.setContentsMargins(5, 0, 5, 0)
        self.category_layout.setAlignment(Qt.AlignLeft)
        category_conatiner.setStyleSheet("background-color: none;")
        for category in product.get_category_list():
            self.category_layout.addWidget(ProductCategoryItem(category))

        self.product_info_1 = QLabel(self)
        self.product_info_1.setGeometry(40, 20, 299, 170)
        self.product_info_1.setFont(Theme.POPPINS_REGULAR_18)
        self.product_info_1.setStyleSheet(
            "background-color: none; color: black;")

        text = f"Customer: {product.get_owner().get_name()}\n" + \
            f"Product ID: {product.get_id()}\n" + \
            f"Product Name: {product.get_name()}\n" + \
            f"Quantity: {product.get_quantity()}\n" + \
            f"Number of Batches: {product.get_num_of_batches()}\n" + \
            f"Location:"

        self.product_info_1.setText(text)

        self.product_info_2 = QLabel(self)
        self.product_info_2.setGeometry(341, 20, 322, 110)
        self.product_info_2.setFont(Theme.POPPINS_REGULAR_18)
        self.product_info_2.setStyleSheet(
            "background-color: none; color: black;")

        text = f"Weight: {product.get_weight()} kg\n" + \
            f"Low stock level: {product.get_low_stock_quantity()}\n" + \
            f"Date Last Stored: {product.get_last_stored()}\n"

        self.product_info_2.setText(text)

        self.location_cb = QComboBox(self)
        self.location_cb.setGeometry(126, 163, 120, 21)
        self.location_cb.setFont(Theme.POPPINS_REGULAR_18)
        for location in self.location:
            self.location_cb.addItem(location.get_location())

        # Testing purpose for Controller
        def test():
            self.qparent.set_input_with_card(self)
        self.click_event = test

        def test2():
            self.update_current_location()
            self.qparent.set_input_with_card(self)
        self.set_event_change_location(test2)

    def mousePressEvent(self, event) -> None:
        self.click_event()

    def clear_category(self):
        for i in reversed(range(self.category_layout.count())):
            self.category_layout.itemAt(i).widget().close()

    def get_current_location(self) -> ProductLocation:
        return self.current_location

    def set_event_click_card(self, function):
        self.click_event = function

    def set_event_change_location(self, function):
        self.location_cb.currentIndexChanged.connect(function)

    def update(self):
        text = f"Customer: {self.product.get_owner().get_name()}\n" + \
            f"Product ID: {self.product.get_id()}\n" + \
            f"Product Name: {self.product.get_name()}\n" + \
            f"Quantity: {self.current_location.get_batch_quantity()}\n" + \
            f"Number of Batches: {self.product.get_num_of_batches()}\n" + \
            f"Location:"

        self.product_info_1.setText(text)

        text = f"Weight: {self.product.get_weight()} kg\n" + \
            f"Low stock level: {self.product.get_low_stock_quantity()}\n" + \
            f"Date Last Stored: {self.product.get_last_stored()}\n"

        self.product_info_2.setText(text)

    def get_product(self) -> Product:
        return self.product

    def get_current_location(self) -> ProductLocation:
        return self.current_location

    def update_current_location(self):
        index = self.location_cb.currentIndex()
        self.current_location = self.location[index]
