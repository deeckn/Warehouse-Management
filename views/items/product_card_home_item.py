from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import Qt, QIntValidator
from views.theme import Theme
from data.data_classes import ProductItem


class ProductCardHomeItem(QWidget):
    def __init__(self,  item: ProductItem) -> None:
        QWidget.__init__(self, None)
        self.setFixedSize(680, 150)

        bg = QLabel(self)
        bg.setGeometry(0, 0, 680, 150)
        bg.setStyleSheet(
            f"background-color: {Theme.GHOST_WHITE}; border-radius:25px")

        self.enable_add_style = f"background-color: {Theme.GREEN}; border: none; border-radius:10px; color:{Theme.GHOST_WHITE};"
        self.enable_export_style =  f"background-color: {Theme.RED}; border: none; border-radius:10px; color:{Theme.GHOST_WHITE};"
       
        self.disable_add_style = f"background-color: {Theme.DARK_GREEN}; border: none; border-radius:10px; color:{Theme.DARK_WHITE};"
        self.disable_export_style =  f"background-color: {Theme.DARK_RED}; border: none; border-radius:10px; color:{Theme.DARK_WHITE};"

        self.product = item

        self.info = QLabel(self)
        self.info.setGeometry(40, 20, 361, 108)
        self.info.setFont(Theme.POPPINS_REGULAR_18)
        self.info.setStyleSheet("background-color: none"
                                )
        self.info.setText(
            f"Customer Name: {item.get_owner().get_name()}\nProduct ID: {item.get_id()}\nProduct Name: {item.get_name()}\nQuantity: {item.get_quantity()}""")

        ui_text = QLabel("Quantity", self)
        ui_text.setFont(Theme.POPPINS_BOLD_18)
        ui_text.setGeometry(424, 32, 82, 34)
        ui_text.setStyleSheet(f"color: {Theme.BLUE};background-color: none")

        ui_line = QLabel(self)
        ui_line.setGeometry(411, 114, 107, 1)
        ui_line.setStyleSheet("border-bottom: 1px solid black;")

        self.quantity_LE = QLineEdit(self)
        self.quantity_LE.setValidator(QIntValidator(0, 99999999))
        self.quantity_LE.setFont(Theme.POPPINS_REGULAR_18)
        self.quantity_LE.setAlignment(Qt.AlignCenter)
        self.quantity_LE.setStyleSheet(
            f"background-color: {Theme.GHOST_WHITE}; ")
        self.quantity_LE.setGeometry(408, 80, 107, 34)

        self.add_bt = QPushButton("ADD", self)
        self.add_bt.setGeometry(540, 22, 100, 40)
        self.add_bt.setFont(Theme.POPPINS_BOLD_18)

        self.export_bt = QPushButton("EXPORT", self)
        self.export_bt.setGeometry(540, 74, 100, 40)
        self.export_bt.setFont(Theme.POPPINS_BOLD_18)

        self.set_enable_add_bt(False)
        self.set_enable_export_bt(False)

    def set_add_bt_listener(self, event):
        self.add_bt.clicked.connect(event)

    def set_export_bt_listener(self, event):
        self.export_bt.clicked.connect(event)

    def set_quantity_changed_listener(self, event):
        self.quantity_LE.textChanged.connect(event)

    def get_new_quantity(self):
        try:
            return int(self.quantity_LE.text())
        except Exception:
            return 0

    def clear_quantity_input(self):
        self.quantity_LE.setText("")

    def get_product(self):
        return self.product

    def add_quantity(self, new_quantity:int):
        self.product.add_quantity(new_quantity)

    def export_quantity(self, new_quantity:int):
        self.product.export_quantity(new_quantity)

    def set_enable_add_bt(self, state:bool):
        self.add_bt.setEnabled(state)
        self.add_bt.setStyleSheet(self.enable_add_style if state else self.disable_add_style)

    def set_enable_export_bt(self, state:bool):
        self.export_bt.setEnabled(state)
        self.export_bt.setStyleSheet(self.enable_export_style if state else self.disable_export_style)

    def update_card(self):
         self.info.setText(
            f"Customer Name: {self.product.get_owner().get_name()}\nProduct ID: {self.product.get_id()}\nProduct Name: {self.product.get_name()}\nQuantity: {self.product.get_quantity()}""")