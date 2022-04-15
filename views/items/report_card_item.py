import datetime
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont, QMouseEvent
from data.data_classes import Customer
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
        text = "Company Name: " + self.current_customer.get_name() + "\nStock: " + \
            str(self.percent_stock) + " %\nExpired: " + self.current_customer.get_expiry_date().replace("_", "/")

        self.card.setText(text)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.parent_widget.previous_card.setStyleSheet(f"""
            color: black; 
            background-color: {Theme.GHOST_WHITE}; 
            padding-left: 20px; 
            margin: 0px 20px 15px 35px; 
            border-radius: 10px;
        """)

        self.parent_widget.current_card = self
        self.setStyleSheet(f"""
            color: black; 
            background-color: #FDCB6E; 
            padding-left: 20px; 
            margin: 0px 20px 15px 35px; 
            border-radius: 10px; 
        """)
        self.parent_widget.previous_card = self.parent_widget.current_card
        self.parent_widget.card_selected_function()
