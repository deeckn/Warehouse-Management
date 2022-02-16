import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
# from views.forms.account_ui import AccountUI # for real testing
from account_ui import AccountUI # for local testing
# from data_classes import User


class AccountView(QWidget):

    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = AccountUI()
        self.ui.setupUi(self)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.ui.scrollArea_widget.setLayout(self.layout)

    # Create new account
    def get_first_name_input(self) -> str:
        return self.ui.usin_create_first_name.text()

    def get_last_name_input(self) -> str:
        return self.ui.usin_create_last_name.text()

    def set_username_label(self, username: str) -> None:
        self.ui.create_username.setText(username)

    def get_password_input(self) -> str:
        return self.ui.usin_create_password.text()

    def get_password_confirm_input(self) -> str:
        return self.ui.usin_create_confirm.text()

    def get_create_admin_status(self) -> bool:
        return self.ui.btn_create_admin.isChecked()

    # Edit employee account
    def set_first_name_edit(self, first_name: str) -> None:
        self.ui.edit_first_name_label.setText(first_name)

    def set_last_name_edit(self, last_name: str) -> None:
        self.ui.edit_last_name_label.setText(last_name)

    def set_username_edit(self, username: str) -> None:
        self.ui.edit_username.setText(username)

    def get_change_password(self) -> str:
        return self.ui.usin_edit_change_password.text()

    def get_admin_password(self) -> str:
        return self.ui.usin_edit_password.text()

    def get_delete_status(self) -> bool:
        return self.ui.btn_delete.isChecked()

    def get_save_changes_status(self) -> bool:
        return self.ui.btn_save_changes.isChecked()

    # Employee Account List
    # def add_employee_card(self, employee: User) -> None:
    #     card = QLabel()
    #     txt = "First Name: " + employee.get_first_name()
    #     + "\nLast Name: " + employee.get_last_name()
    #     + "\nUsername: " + employee.get_username()

    #     card.setText(txt)
    #     self.ui.employee_acc_list_widget.layout().addWidget(card)

    # def get_selected_account() -> User:
    #     return

    def add_employee_card(self, fName: str, lName: str, user: str) -> None:
        card = QPushButton()
        txt = "First Name: " + fName + "\nLast Name: " + lName + "\nUsername: " + user
        card.setText(txt)
        card.setFixedSize(355, 500)
        card.setStyleSheet(
            "color:#000000; background-color:#980000; margin-top:0px; margin-bottom:10px;")
        self.layout.addWidget(card)

    def clear_employee_list() -> None:
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AccountView()
    w.add_employee_card("Chakrin", "Deesit", "Deeckn")
    w.add_employee_card("Natcha", "Teekayu", "Faynch")
    w.add_employee_card("Tawan", "Lekngam", "Tawancraft")
    w.show()
    sys.exit(app.exec())
