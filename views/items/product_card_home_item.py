from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QComboBox
from PySide6.QtGui import Qt, QIntValidator
from views.theme import Theme
from data.orm.schema import Product, ProductLocation


class ProductCardHomeItem(QWidget):
    def __init__(self,  item: Product) -> None:
        QWidget.__init__(self, None)
        self.setFixedSize(680, 150)

        bg = QLabel(self)
        bg.setGeometry(0, 0, 680, 150)
        bg.setStyleSheet(
            f"background-color: {Theme.GHOST_WHITE}; border-radius:25px")

        self.enable_add_style = f"background-color: {Theme.GREEN}; border: none; border-radius:10px; color:{Theme.GHOST_WHITE};"
        self.enable_export_style = f"background-color: {Theme.RED}; border: none; border-radius:10px; color:{Theme.GHOST_WHITE};"

        self.disable_add_style = f"background-color: {Theme.DARK_GREEN}; border: none; border-radius:10px; color:{Theme.DARK_WHITE};"
        self.disable_export_style = f"background-color: {Theme.DARK_RED}; border: none; border-radius:10px; color:{Theme.DARK_WHITE};"

        self.product = item

        self.info = QLabel(self)
        self.info.setGeometry(40, 20, 361, 108)
        self.info.setFont(Theme.POPPINS_REGULAR_18)
        self.info.setStyleSheet("background-color: none")

        ui_text = QLabel("Batch", self)
        ui_text.setFont(Theme.POPPINS_BOLD_18)
        ui_text.setGeometry(330, 32, 60, 34)
        ui_text.setStyleSheet(f"color: {Theme.BLUE};background-color: none")

        self.batch_cb = QComboBox(self)
        self.batch_cb.setGeometry(305, 100, 94, 25)
        self.batch_cb.setFont(Theme.POPPINS_REGULAR_18)
        for num in range(1, self.product.get_num_of_batches()+1):
            self.batch_cb.addItem(str(num))

        ui_text = QLabel("Quantity", self)
        ui_text.setFont(Theme.POPPINS_BOLD_18)
        ui_text.setGeometry(429, 32, 82, 34)
        ui_text.setStyleSheet(f"color: {Theme.BLUE};background-color: none")

        self.quantity_LE = QLineEdit(self)
        self.quantity_LE.setValidator(QIntValidator(0, 99999999))
        self.quantity_LE.setFont(Theme.POPPINS_REGULAR_18)
        self.quantity_LE.setAlignment(Qt.AlignCenter)
        self.quantity_LE.setStyleSheet(
            f"background-color: None; ")
        self.quantity_LE.setGeometry(420, 100, 100, 25)

        self.add_bt = QPushButton("ADD", self)
        self.add_bt.setGeometry(545, 22, 100, 40)
        self.add_bt.setFont(Theme.POPPINS_BOLD_18)

        self.export_bt = QPushButton("EXPORT", self)
        self.export_bt.setGeometry(545, 74, 100, 40)
        self.export_bt.setFont(Theme.POPPINS_BOLD_18)

        self.update_card()
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

    def add_quantity(self, new_quantity: int):
        self.product.add_quantity(new_quantity)

    def export_quantity(self, new_quantity: int):
        self.product.export_quantity(new_quantity)

    def set_enable_add_bt(self, state: bool):
        self.add_bt.setEnabled(state)
        self.add_bt.setStyleSheet(
            self.enable_add_style if state else self.disable_add_style)

    def set_enable_export_bt(self, state: bool):
        self.export_bt.setEnabled(state)
        self.export_bt.setStyleSheet(
            self.enable_export_style if state else self.disable_export_style)

    def update_card(self):
        locations = self.product.get_locations()
        current_batch = self.batch_cb.currentIndex()
        self.info.setText(
            f"Customer Name: {self.product.get_owner().get_name()}\nProduct ID: {self.product.get_id()}\nProduct Name: {self.product.get_name()}\nQuantity: {str(self.get_current_quantity())}")

    def get_product_id(self) -> int:
        return self.product.get_id()

    def get_current_batch(self) -> int:
        return int(self.batch_cb.currentText())

    def set_event_batch_cb(self, function):
        self.batch_cb.currentIndexChanged.connect(function)

    def get_current_quantity(self) -> int:
        locations = self.product.get_locations()
        current_batch = self.batch_cb.currentIndex()
        return locations[current_batch].get_batch_quantity()
