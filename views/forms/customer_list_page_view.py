from data.data_classes import Customer
from views.forms.stack_page import StackPage
from views.forms.customer_input_form import CustomerInputForm
from views.forms.customer_list import CustomerList
from views.items.customer_item import CustomerCard
from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QLabel
from views.theme import Theme


class CustomerListPageView(StackPage):
    def __init__(self) -> None:
        super().__init__()
        self.current_customer: CustomerCard = None

        self.select_event = None
        self.unselect_event = None

        self.customer_form = CustomerInputForm(self)
        self.customer_form.move(100, 176)

        self.customer_list = CustomerList(self)
        self.customer_list.move(640, 176)

        # title page name
        title = QLabel("Customer List", self)
        title.setStyleSheet(f"color: {Theme.DARK_BLUE}")
        title.setFont(Theme.POPPINS_BOLD_64)
        title.setGeometry(100, 60, 454, 96)

        # Controller
        # self.set_unselect_event(lambda: self.reset_form())

        # self.set_select_event(lambda: self.set_form(
        #     self.current_customer.customer))

    def set_form(self, customer: Customer):
        self.customer_form.customer_name_le.setText(customer.get_name())
        self.customer_form.customer_phone_le.setText(customer.get_phone())
        self.customer_form.customer_email_le.setText(customer.get_email())
        self.customer_form.applied_option.setChecked(
            customer.get_packing_service())
        self.customer_form.not_applied_option.setChecked(
            not customer.get_packing_service())
        self.customer_form.rental_duration_le.setText(
            customer.get_rental_duration())

        self.customer_form.date_joined_picker.setDateTime(
            QDateTime.fromString(customer.get_date_joined().replace("_", "-"), "dd-MM-yyyy"))

    def reset_form(self):
        self.customer_form.customer_name_le.setText("")
        self.customer_form.customer_phone_le.setText("")
        self.customer_form.customer_email_le.setText("")
        self.customer_form.applied_option.setAutoExclusive(False)
        self.customer_form.applied_option.setChecked(False)
        self.customer_form.not_applied_option.setChecked(False)
        self.customer_form.applied_option.setAutoExclusive(True)
        self.customer_form.rental_duration_le.setText("")
        self.customer_form.date_joined_picker.setDateTime(
            QDateTime.currentDateTime())
    
    def update_current_card(self, new_customer: Customer):
        self.current_customer.set_customer(new_customer)
        self.current_customer.update()

    def reset_list(self):
        self.current_customer.unclick()
        self.current_customer = None

    def set_select_event(self, event):
        self.select_event = event

    def set_unselect_event(self, event):
        self.unselect_event = event

    def isFormEmpty(self):
        return self.customer_form.customer_name_le.text() == "" and \
            self.customer_form.customer_phone_le.text() == "" and \
            self.customer_form.customer_email_le.text() == "" and \
            self.customer_form.rental_duration_le.text() == ""

    def reset_card(self):
        self.customer_list.clear_all_card()
        self.current_customer = None
        self.reset_form()

    def isCardSelected(self):
        return self.current_customer != None

    def get_name(self) -> str:
        return self.customer_form.customer_name_le.text()

    def get_phone(self) -> str:
        return self.customer_form.customer_name_le.text()

    def get_email(self) -> str:
        return self.customer_form.customer_email_le.text()

    def get_rental_duration(self) -> str:
        return self.customer_form.rental_duration_le.text()

    def get_packing_service(self) -> bool:
        return self.customer_form.applied_option.isCheckable()

    def get_joined_date(self) -> str:
        return self.customer_form.date_joined_picker.dateTime().toString("dd_MM_yyyy")
