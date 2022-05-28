from PySide6.QtWidgets import QLabel, QWidget, QGridLayout
from data.orm.schema import Product

from views.theme import Theme
from views.items.product_category_item import ProductCategoryItem


class ProductCardInventory(QWidget):
    def __init__(self, product: Product):
        QWidget.__init__(self, None)
        self.resize(782, 160)
        self.container = QWidget(self)
        self.container.setGeometry(0, 0, 760, 160)
        self.container.setStyleSheet(
            "background-color: " + Theme.GHOST_WHITE + "; border-radius: 30; color: " + Theme.DARK_BLUE + ";")

        self.grid_layout = QGridLayout()

        self.product_id_label = QLabel(self)
        self.product_id_label.setFont(Theme.POPPINS_REGULAR_18)
        self.product_id_label.setText("Product ID: " + str(product.get_id()))

        self.product_name_label = QLabel(self)
        self.product_name_label.setFont(Theme.POPPINS_REGULAR_18)
        self.product_name_label.setText(
            "Product Name: " + str(product.get_name()))

        self.quality_label = QLabel(self)
        self.quality_label.setFont(Theme.POPPINS_REGULAR_18)
        self.quality_label.setText("Quantity: " + str(product.get_quantity()))

        self.weight_label = QLabel(self)
        self.weight_label.setFont(Theme.POPPINS_REGULAR_18)
        self.weight_label.setText(
            "Weight: " + str(product.get_weight()) + " kg")

        self.low_stock_level_label = QLabel(self)
        self.low_stock_level_label.setFont(Theme.POPPINS_REGULAR_18)
        self.low_stock_level_label.setText(
            "Low stock level: " + str(product.get_low_stock_quantity()))

        self.data_last_stored_label = QLabel(self)
        self.data_last_stored_label.setFont(Theme.POPPINS_REGULAR_18)
        self.data_last_stored_label.setText(
            "Date Last Stored: " + str(product.get_last_stored()))
        self.categories = product.get_category_list()
        for i in range(len(self.categories)):
            catergory_item = ProductCategoryItem(self.categories[i])
            catergory_item.change_size(131, 35)
            self.grid_layout.addWidget(catergory_item, i, 2, 1, 1)

        self.grid_layout.addWidget(self.product_id_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.product_name_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.quality_label, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.weight_label, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.low_stock_level_label, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.data_last_stored_label, 2, 1, 1, 1)

        self.grid_layout.setContentsMargins(40, 20, 40, 40)
        self.setLayout(self.grid_layout)
