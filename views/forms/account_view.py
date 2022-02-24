import os.path
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QScrollArea, QVBoxLayout
from data.data_classes import User
from views.items.employee_card_item import EmployeeCardItem


class AccountView(QWidget):

    def __init__(self):
        QWidget.__init__(self, None)
        self.set_styleSheet()

        self.setFixedSize(1520, 1080)

        self.current_card: EmployeeCardItem = None
        self.previous_card = QWidget()

        font = QFont("Poppins")
        font.setPixelSize(72)
        font.setBold(True)
        account_setting_label = QLabel("Account Settings", self)
        account_setting_label.setObjectName("page_name")
        account_setting_label.setGeometry(100, 60, 700, 90)
        account_setting_label.setFont(font)

        employee_acc_list_widget = QWidget(self)
        employee_acc_list_widget.setObjectName("sub_widget")
        employee_acc_list_widget.setGeometry(100, 222, 380, 765)

        font.setPixelSize(24)
        employee_acc_list_label = QLabel(
            "Employee Account List", employee_acc_list_widget)
        employee_acc_list_label.setObjectName("employee_acc_list_label")
        employee_acc_list_label.setAlignment(Qt.AlignCenter)
        employee_acc_list_label.setGeometry(0, 0, 380, 80)
        employee_acc_list_label.setFont(font)

        self.scrollArea = QScrollArea(employee_acc_list_widget)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(0, 80, 380, 685)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)

        self.scrollArea_widget = QWidget()
        self.scrollArea_widget.setObjectName("sub_widget")
        self.scrollArea_widget.setGeometry(0, 0, 380, 685)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignTop)
        self.scrollArea_widget.setLayout(self.layout)
        self.scrollArea.setWidget(self.scrollArea_widget)

        # Create new account
        create_new_acc_widget = QWidget(self)
        create_new_acc_widget.setObjectName("sub_widget")
        create_new_acc_widget.setGeometry(560, 220, 850, 350)

        create_new_acc_label = QLabel(
            "Create New Account", create_new_acc_widget)
        create_new_acc_label.setGeometry(50, 30, 271, 41)
        create_new_acc_label.setFont(font)

        font.setPixelSize(18)
        font.setBold(False)
        create_first_name_label = QLabel("First Name :", create_new_acc_widget)
        create_first_name_label.setGeometry(50, 90, 120, 30)
        create_first_name_label.setFont(font)

        create_last_name_label = QLabel("Last Name :", create_new_acc_widget)
        create_last_name_label.setGeometry(50, 140, 120, 30)
        create_last_name_label.setFont(font)

        create_username_label = QLabel("Username :", create_new_acc_widget)
        create_username_label.setGeometry(50, 190, 120, 30)
        create_username_label.setFont(font)

        create_password_label = QLabel("Password :", create_new_acc_widget)
        create_password_label.setGeometry(50, 240, 120, 30)
        create_password_label.setFont(font)

        create_confirm_label = QLabel("Confirm :", create_new_acc_widget)
        create_confirm_label.setGeometry(480, 240, 81, 30)
        create_confirm_label.setFont(font)

        self.usin_create_first_name = QLineEdit(create_new_acc_widget)
        self.usin_create_first_name.setGeometry(170, 90, 620, 30)
        self.usin_create_first_name.setFont(font)

        self.usin_create_last_name = QLineEdit(create_new_acc_widget)
        self.usin_create_last_name.setGeometry(170, 140, 620, 30)
        self.usin_create_last_name.setFont(font)

        self.create_username = QLabel(create_new_acc_widget)
        self.create_username.setGeometry(170, 190, 281, 30)
        self.create_username.setFont(font)

        self.usin_create_password = QLineEdit(create_new_acc_widget)
        self.usin_create_password.setGeometry(170, 240, 280, 30)
        self.usin_create_password.setFont(font)

        self.usin_create_confirm = QLineEdit(create_new_acc_widget)
        self.usin_create_confirm.setGeometry(580, 240, 210, 30)
        self.usin_create_confirm.setFont(font)

        font.setPixelSize(14)
        font.setBold(True)
        self.btn_create_admin = QRadioButton(
            "Create as admin account ", create_new_acc_widget)
        self.btn_create_admin.setObjectName("btn_create_admin")
        self.btn_create_admin.setEnabled(True)
        self.btn_create_admin.setGeometry(50, 290, 211, 20)
        self.btn_create_admin.setFont(font)
        self.btn_create_admin.setLayoutDirection(Qt.RightToLeft)

        font.setPixelSize(18)
        font.setBold(False)
        self.btn_create_account = QPushButton(
            "Create Account", create_new_acc_widget)
        self.btn_create_account.setObjectName("yellow_btn")
        self.btn_create_account.setGeometry(590, 290, 200, 30)
        self.btn_create_account.setFont(font)
        # self.btn_create_account.clicked.connect(self.add_employee_card)

        # Edit employee account
        edit_employee_acc_widget = QWidget(self)
        edit_employee_acc_widget.setObjectName("sub_widget")
        edit_employee_acc_widget.setGeometry(560, 638, 850, 350)

        font.setPixelSize(24)
        font.setBold(True)
        edit_employee_acc_label = QLabel(
            "Edit Employee Account", edit_employee_acc_widget)
        edit_employee_acc_label.setGeometry(50, 30, 301, 41)
        edit_employee_acc_label.setFont(font)

        font.setPixelSize(14)
        font.setBold(False)
        edit_description_label = QLabel(
            "Click on an employee card on the left to select an employee account", edit_employee_acc_widget)
        edit_description_label.setGeometry(50, 70, 501, 16)
        edit_description_label.setFont(font)

        font.setPixelSize(18)
        edit_first_name_label = QLabel(
            "First Name :", edit_employee_acc_widget)
        edit_first_name_label.setGeometry(50, 100, 120, 30)
        edit_first_name_label.setFont(font)

        edit_last_name_label = QLabel("Last Name :", edit_employee_acc_widget)
        edit_last_name_label.setGeometry(50, 150, 120, 30)
        edit_last_name_label.setFont(font)

        edit_username_label = QLabel("Username :", edit_employee_acc_widget)
        edit_username_label.setGeometry(50, 200, 120, 30)
        edit_username_label.setFont(font)

        edit_change_password_label = QLabel(
            "Change Password :", edit_employee_acc_widget)
        edit_change_password_label.setGeometry(330, 200, 181, 30)
        edit_change_password_label.setFont(font)

        self.usin_edit_first_name = QLineEdit(edit_employee_acc_widget)
        self.usin_edit_first_name.setGeometry(170, 100, 620, 30)
        self.usin_edit_first_name.setFont(font)

        self.usin_edit_last_name = QLineEdit(edit_employee_acc_widget)
        self.usin_edit_last_name.setGeometry(170, 150, 620, 30)
        self.usin_edit_last_name.setFont(font)

        self.edit_username = QLabel(edit_employee_acc_widget)
        self.edit_username.setGeometry(170, 200, 141, 30)
        self.edit_username.setFont(font)

        self.usin_edit_change_password = QLineEdit(edit_employee_acc_widget)
        self.usin_edit_change_password.setGeometry(525, 200, 265, 30)
        self.usin_edit_change_password.setFont(font)

        font.setPixelSize(14)
        edit_admin_confirm_label = QLabel(
            "Admin Confirmation :", edit_employee_acc_widget)
        edit_admin_confirm_label.setGeometry(50, 255, 501, 16)
        edit_admin_confirm_label.setFont(font)

        font.setPixelSize(18)
        edit_password_label = QLabel("Password :", edit_employee_acc_widget)
        edit_password_label.setGeometry(50, 280, 101, 30)
        edit_password_label.setFont(font)

        self.usin_edit_password = QLineEdit(edit_employee_acc_widget)
        self.usin_edit_password.setGeometry(170, 280, 265, 30)
        self.usin_edit_password.setFont(font)

        self.btn_delete = QPushButton("Delete", edit_employee_acc_widget)
        self.btn_delete.setObjectName("yellow_btn")
        self.btn_delete.setGeometry(470, 280, 140, 30)
        self.btn_delete.setFont(font)

        self.btn_save_changes = QPushButton(
            "Save Changes", edit_employee_acc_widget)
        self.btn_save_changes.setObjectName("yellow_btn")
        self.btn_save_changes.setGeometry(620, 280, 170, 30)
        self.btn_save_changes.setFont(font)

    def set_styleSheet(self) -> None:
        file_path = os.path.dirname(os.path.abspath(__file__))
        real_path = os.path.join(file_path, "account_view_theme.qss")
        with open(real_path, 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
        f.close()

    # Create new account
    def get_first_name_input(self) -> str:
        """Returns the first name (create new account) input as a string"""
        return self.usin_create_first_name.text()

    def get_last_name_input(self) -> str:
        """Returns the last name (create new account) input as a string"""
        return self.usin_create_last_name.text()

    def set_username_label(self, username: str):
        """Sets the (create new account) username label to a given string"""
        self.create_username.setText(username)

    def get_password_input(self) -> str:
        """Returns the password (create new account) input as a string"""
        return self.usin_create_password.text()

    def get_password_confirm_input(self) -> str:
        """Returns the confirm password (create new account) input as a string"""
        return self.usin_create_confirm.text()

    def get_create_admin_status(self) -> bool:
        """Returns the state of create admin radio button"""
        return self.btn_create_admin.isChecked()

    # Edit employee account
    def set_first_name_edit(self, first_name: str):
        """Sets the (edit employee account) first name line edit to a given string"""
        self.edit_first_name_label.setText(first_name)

    def set_last_name_edit(self, last_name: str):
        """Sets the (edit employee account) last name line edit to a given string"""
        self.edit_last_name_label.setText(last_name)

    def set_username_edit(self, username: str):
        """Sets the (edit employee account) username label to a given string"""
        self.edit_username.setText(username)

    def get_change_password(self) -> str:
        """Returns a string of the password line edit in edit employee account"""
        return self.usin_edit_change_password.text()

    def get_admin_password(self) -> str:
        """Returns the admin password confirmation as a string"""
        return self.usin_edit_password.text()

    def get_delete_status(self) -> bool:
        """Returns True if the delete button is pressed else False"""
        return self.btn_delete.isChecked()

    def get_save_changes_status(self) -> bool:
        """Returns True if the save changes button is pressed else False"""
        return self.btn_save_changes.isChecked()

    # Employee Account List
    def add_employee_card(self, employee: User):
        """Inserts a new EmployeeCardItem object to the list given an User object"""
        card = EmployeeCardItem(self, employee)
        self.scrollArea_widget.layout().addWidget(card)

    def get_selected_account(self) -> User:
        """Returns the selected EmployeeCardItem object on the UI"""
        return self.current_card.get_current_employee()

    def clear_employee_list(self):
        """Clears the list represented in the scrollarea"""
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

    # Set Button Listeners

    def set_create_account_button_listener(self, function):
        self.btn_create_account.clicked.connect(function)

    def set_delete_button_listener(self, function):
        self.btn_delete.clicked.connect(function)

    def set_save_changes_button_listener(self, function):
        self.btn_save_changes.clicked.connect(function)
