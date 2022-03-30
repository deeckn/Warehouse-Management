from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from data.data_classes import Customer
from views.theme import Theme


class CustomerCard(QWidget):
    def __init__(self, parent, customer: Customer):
        QWidget.__init__(self,  None)
        self.setFixedSize(680, 150)
        self.customer = customer
        self.qparent = parent

        self.bg = QLabel(self)
        self.bg.setGeometry(0, 0, 680, 150)
        self.bg.setStyleSheet(
            f"background-color: {Theme.GHOST_WHITE}; border-radius: 30;")

        customer_info_1 = QLabel(self)
        customer_info_1.setGeometry(44, 20, 316, 108)
        customer_info_1.setFont(Theme.POPPINS_REGULAR_18)
        customer_info_1.setStyleSheet("background-color: none;")

        text = f"""Name: {customer.get_name()}
Phone: {customer.get_phone()}
Email: {customer.get_email()}
Packing Service: {"Applied" if customer.get_packing_service() else "Not Applied"}"""

        customer_info_1.setText(text)

        customer_info_2 = QLabel(self)
        customer_info_2.setGeometry(371, 20, 292, 108)
        customer_info_2.setFont(Theme.POPPINS_REGULAR_18)
        customer_info_2.setStyleSheet("background-color: none;")
        text = f"""Rental Duration: {customer.get_rental_duration()}
Date Joined: {customer.get_date_joined().replace("_","-")}
Expiry Date: {customer.get_expiry_date().replace("_","-")}
Total Payment: {customer.get_total_payment()}"""

        customer_info_2.setText(text)

    def mousePressEvent(self, event) -> None:
        if(self.qparent.current_customer == self):
            self.unclick()
            self.qparent.current_customer = None
            self.qparent.unselect_event()
            return

        if(self.qparent.current_customer != None):
            self.qparent.current_customer.unclick()

        self.qparent.current_customer = self
        self.qparent.select_event()

        self.bg.setStyleSheet(
            f"background-color: {Theme.GHOST_WHITE}; border-radius: 30; border: 3px solid {Theme.YELLOW};")

    def unclick(self):
        self.bg.setStyleSheet(
            f"background-color: {Theme.GHOST_WHITE}; border-radius: 30;")
