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

        self.customer_info_1 = QLabel(self)
        self.customer_info_1.setGeometry(44, 20, 316, 108)
        self.customer_info_1.setFont(Theme.POPPINS_REGULAR_18)
        self.customer_info_1.setStyleSheet(
            "background-color: none; color: black;")

        text = f"Name: {customer.get_name()}\n" + \
            f"Phone: {customer.get_phone()}\n" + \
            f"Email: {customer.get_email()}\n" + \
            f"Packing Service: {'Applied' if customer.get_packing_service() else 'Not Applied'}"

        self.customer_info_1.setText(text)

        self.customer_info_2 = QLabel(self)
        self.customer_info_2.setGeometry(371, 20, 292, 108)
        self.customer_info_2.setFont(Theme.POPPINS_REGULAR_18)
        self.customer_info_2.setStyleSheet(
            "background-color: none; color: black;")
        text = f"Rental Duration: {customer.get_rental_duration()}\n" + \
            f"Date Joined: {customer.get_date_joined().replace('_','-')}\n" + \
            f"Expiry Date: {customer.get_expiry_date().replace('_','-')}\n" + \
            f"Total Payment: {customer.get_total_payment()}"

        self.customer_info_2.setText(text)

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

    def update(self):
        text = f"Name: {self.customer.get_name()}\n" + \
            f"Phone: {self.customer.get_phone()}\n" + \
            f"Email: {self.customer.get_email()}\n" + \
            f"Packing Service: {'Applied' if self.customer.get_packing_service() else 'Not Applied'}"

        self.customer_info_1.setText(text)

        text = f"Rental Duration: {self.customer.get_rental_duration()}\n" + \
            f"Date Joined: {self.customer.get_date_joined().replace('_','-')}\n" + \
            f"Expiry Date: {self.customer.get_expiry_date().replace('_','-')}\n" + \
            f"Total Payment: {self.customer.get_total_payment()}"

        self.customer_info_2.setText(text)

    def set_customer(self, new_customer: Customer):
        self.customer = new_customer

    def get_customer(self) -> Customer:
        return self.customer
