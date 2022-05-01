from views.forms.input_form import InputForm
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget, QHBoxLayout, QRadioButton, QDateEdit
from PySide6.QtGui import Qt
from PySide6.QtCore import QDateTime
from views.theme import Theme


class CustomerInputForm(InputForm):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        # Style
        default_le = f"background-color: {Theme.GREY};border-radius: 0px;color: black;padding-left: 10px;"
        h1 = f"color: {Theme.BLUE}; background-color: none;"
        line_break_top = "border-top: 1px solid black; background-color: none;"
        guide = "background-color: white; color: black;"
        radio_bt_style = f"color: {Theme.BLUE};"

        # Customer Search Input
        self.customer_search_le = QLineEdit(self)
        self.customer_search_le.setGeometry(50, 101, 400, 40)
        self.customer_search_le.setFont(Theme.POPPINS_REGULAR_18)
        self.customer_search_le.setStyleSheet(default_le)

        # Search Button
        self.search_bt = QPushButton("SEARCH", self)
        self.search_bt.setGeometry(274, 161, 176, 40)
        self.search_bt.setFont(Theme.POPPINS_BOLD_18)
        self.search_bt.setStyleSheet(
            f"color: white;background-color: {Theme.YELLOW};border-radius: 10px;")

        # Customer Name Input
        self.customer_name_le = QLineEdit(self)
        self.customer_name_le.setGeometry(50, 285, 400, 40)
        self.customer_name_le.setFont(Theme.POPPINS_REGULAR_18)
        self.customer_name_le.setStyleSheet(
            default_le)

        # Customer Phone Input
        self.customer_phone_le = QLineEdit(self)
        self.customer_phone_le.setGeometry(50, 363, 400, 40)
        self.customer_phone_le.setFont(Theme.POPPINS_REGULAR_18)
        self.customer_phone_le.setStyleSheet(
            default_le)

        # Customer Email Input
        self.customer_email_le = QLineEdit(self)
        self.customer_email_le.setGeometry(50, 440, 400, 40)
        self.customer_email_le.setFont(Theme.POPPINS_REGULAR_18)
        self.customer_email_le.setStyleSheet(
            default_le)

        self.rental_duration_le = QLineEdit(self)
        self.rental_duration_le.setGeometry(264, 581, 187, 40)
        self.rental_duration_le.setFont(Theme.POPPINS_REGULAR_18)
        self.rental_duration_le.setStyleSheet(
            default_le)

        # Packaging Service Radio Buttons
        option = QWidget(self)
        option.setGeometry(65, 523, 235, 22)
        option_layout = QHBoxLayout(option)
        option_layout.setContentsMargins(0, 0, 0, 0)

        self.applied_option = QRadioButton("Applied")
        self.applied_option.setFixedWidth(82)

        self.not_applied_option = QRadioButton("Not Applied")
        self.not_applied_option.setFixedWidth(110)

        for radio_bt in (self.applied_option, self.not_applied_option):
            radio_bt.setFont(Theme.POPPINS_REGULAR_14)
            radio_bt.setObjectName("packing_option")
            radio_bt.setStyleSheet(radio_bt_style)
            option_layout.addWidget(radio_bt)

        self.date_joined_picker = QDateEdit(self)
        self.date_joined_picker.setGeometry(51, 581, 187, 40)
        self.date_joined_picker.setDisplayFormat("dd-MM-yyyy")
        self.date_joined_picker.setFont(Theme.POPPINS_REGULAR_14)

        self.date_joined_picker.setDateTime(QDateTime.currentDateTime())
        self.date_joined_picker.setCalendarPopup(True)

        # Labels
        ui_line_break = QLabel(self)
        ui_line_break.setStyleSheet(line_break_top)
        ui_line_break.setGeometry(50, 54, 400, 1)

        ui_guide_label = QLabel("Search", self)
        ui_guide_label.setAlignment(Qt.AlignCenter)
        ui_guide_label.setFont(Theme.POPPINS_REGULAR_14)
        ui_guide_label.setStyleSheet(guide)
        ui_guide_label.setGeometry(220, 43, 60, 21)

        ui_guide_label = QLabel("Customer Name", self)
        ui_guide_label.setFont(Theme.POPPINS_BOLD_18)
        ui_guide_label.setStyleSheet(h1)
        ui_guide_label.setGeometry(50, 74, 153, 27)

        ui_guide_label = QLabel("Customer Name", self)
        ui_guide_label.setFont(Theme.POPPINS_BOLD_18)
        ui_guide_label.setStyleSheet(h1)
        ui_guide_label.setGeometry(50, 258, 153, 27)

        ui_guide_label = QLabel("Phone", self)
        ui_guide_label.setFont(Theme.POPPINS_BOLD_18)
        ui_guide_label.setStyleSheet(h1)
        ui_guide_label.setGeometry(50, 336, 59, 27)

        ui_guide_label = QLabel("Email", self)
        ui_guide_label.setFont(Theme.POPPINS_BOLD_18)
        ui_guide_label.setStyleSheet(h1)
        ui_guide_label.setGeometry(50, 413, 52, 27)

        ui_guide_label = QLabel("Packing Service", self)
        ui_guide_label.setFont(Theme.POPPINS_BOLD_18)
        ui_guide_label.setStyleSheet(h1)
        ui_guide_label.setGeometry(50, 490, 148, 27)

        ui_guide_label = QLabel("Date Joined", self)
        ui_guide_label.setFont(Theme.POPPINS_BOLD_18)
        ui_guide_label.setStyleSheet(h1)
        ui_guide_label.setGeometry(50, 555, 117, 27)

        ui_guide_label = QLabel("Date Joined", self)
        ui_guide_label.setFont(Theme.POPPINS_BOLD_18)
        ui_guide_label.setStyleSheet(h1)
        ui_guide_label.setGeometry(50, 555, 117, 27)

        ui_guide_label = QLabel("Rental Duration", self)
        ui_guide_label.setFont(Theme.POPPINS_BOLD_18)
        ui_guide_label.setStyleSheet(h1)
        ui_guide_label.setGeometry(264, 555, 150, 27)

        ui_line_break = QLabel(self)
        ui_line_break.setStyleSheet(line_break_top)
        ui_line_break.setGeometry(51, 242, 400, 1)

        ui_guide_label = QLabel("Information", self)
        ui_guide_label.setAlignment(Qt.AlignCenter)
        ui_guide_label.setFont(Theme.POPPINS_REGULAR_14)
        ui_guide_label.setStyleSheet(guide)
        ui_guide_label.setGeometry(196, 231, 110, 21)

    # Clear

    def clear_search_le(self):
        self.customer_search_le.setText("")

    # Search Functionality

    def set_search_button_listener(self, function):
        self.search_bt.clicked.connect(function)

    def get_search_input(self) -> str:
        return self.customer_search_le.text()

    # Add new customer

    def set_add_button_listener(self, function):
        self.add_button.clicked.connect(function)

    def set_input_on_change_listener(self, function):
        self.customer_name_le.textChanged.connect(function)
        self.customer_phone_le.textChanged.connect(function)
        self.customer_email_le.textChanged.connect(function)
        self.rental_duration_le.textChanged.connect(function)
        self.applied_option.clicked.connect(function)
        self.not_applied_option.clicked.connect(function)

    # Save edited data

    def set_save_button_listener(self, function):
        self.save_button.clicked.connect(function)

    # Delete customer

    def set_delete_button_listener(self, function):
        self.delete_button.clicked.connect(function)
