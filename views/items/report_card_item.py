import datetime
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont
from data.orm.schema import Customer
from views.theme import Theme


class ReportCardItem(QWidget):
    def __init__(self, parent, customer: Customer, percent: int):
        QWidget.__init__(self, parent)
        self.parent_widget = parent
        self.current_customer = customer
        self.percent_stock = percent

        self.setFixedSize(540, 130)
        self.setStyleSheet(f"""
            color: black;
            background-color: {Theme.GHOST_WHITE};
            padding-left: 20px;
            margin: 0px 20px 15px 35px;
            border-radius: 10px;
        """)

        font = QFont("Poppins")
        font.setPixelSize(18)

        self.card = QLabel(self)
        self.card.setFixedSize(540, 130)
        self.card.setFont(font)
        self.__set_card_info()

    def __set_card_info(self):
        text = f"""
    Customer Name: {self.current_customer.get_name()}
    Stock: {self.percent_stock:.2f}%
    Contract End: {self.current_customer.get_expiry_date().replace("_", "/")}
        """
        self.card.setText(text)
