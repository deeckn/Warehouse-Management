from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtGui import Qt, QIntValidator
from views.theme import Theme
from data.data_classes import ProductItem


class ProductCardItem(QWidget):
    def __init__(self, parent, item: ProductItem) -> None:
        QWidget.__init__(self, parent)
        self.setFixedSize(680, 150)

        self.item = item

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.info = QLabel()
        self.info.setFixedWidth(412)
        self.info.setFont(Theme.POPPINS_REGULAR_18)
        self.info.setStyleSheet(
            "padding-top: 21px; padding-bottom: 21px; padding-left: 41px;")
        self.info.setText(
            f"Customer Name: {item.get_owner()}\nProduct ID: {item.get_id()}\nProduct Name: {item.get_name()}\nQuantity: {item.get_quantity()}""")
        main_layout.addWidget(self.info)
        quantity_box = QWidget()
        quantity_box.setFixedWidth(107)
        main_layout.addWidget(quantity_box)
        quantity_box_layout = QVBoxLayout(quantity_box)
        ui_text = QLabel("Quantity")
        ui_text.setFont(Theme.POPPINS_BOLD_18)
        ui_text.setFixedHeight(34)
        ui_text.setStyleSheet("border: none; color: #406882;")
        quantity_box_layout.addWidget(ui_text)
        self.quantity_LE = QLineEdit()
        self.quantity_LE.setValidator(QIntValidator(0, 9999999))
        self.quantity_LE.setFont(Theme.POPPINS_REGULAR_18)
        self.quantity_LE.setAlignment(Qt.AlignCenter)
        self.quantity_LE.setStyleSheet(
            "background-color: #F8F8FF; border-bottom: 1px solid black;")
        quantity_box_layout.addWidget(self.quantity_LE)
        self.bt_box = QWidget()
        self.bt_box.setFixedWidth(163)
        main_layout.addWidget(self.bt_box)
        bt_box_layout = QVBoxLayout(self.bt_box)
        bt_box_layout.setAlignment(Qt.AlignCenter)
        self.add_bt = QPushButton("ADD")
        self.add_bt.setFixedSize(100, 40)
        self.add_bt.setStyleSheet(
            "background-color: #99E997; border: none; border-radius:10px; color:#F8F8FF;")
        self.add_bt.setFont(Theme.POPPINS_BOLD_18)
        bt_box_layout.addWidget(self.add_bt)
        self.export_bt = QPushButton("EXPORT")
        self.export_bt.setFixedSize(100, 40)
        self.export_bt.setStyleSheet(
            "background-color: #FF7474; border: none; border-radius:10px; color:#F8F8FF;")
        self.export_bt.setFont(Theme.POPPINS_BOLD_18)
        bt_box_layout.addWidget(self.export_bt)
