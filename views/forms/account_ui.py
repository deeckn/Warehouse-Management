import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class AccountAdminUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.setFixedSize(1520, 1080)

        font = QFont("Poppins")
        font.setPixelSize(72)
        font.setBold(True)
        account_setting_label = QLabel("Account Settings", self)
        account_setting_label.setObjectName("account_setting_label")
        account_setting_label.setGeometry(QRect(100, 60, 700, 90))
        account_setting_label.setFont(font)

        employee_acc_list_widget = QWidget(self)
        employee_acc_list_widget.setObjectName("employee_acc_list_widget")
        employee_acc_list_widget.setGeometry(QRect(100, 222, 380, 765))

        font.setPixelSize(24)
        employee_acc_list_label = QLabel(
            "Employee Account List", employee_acc_list_widget)
        employee_acc_list_label.setObjectName("employee_acc_list_label")
        employee_acc_list_label.setAlignment(Qt.AlignCenter)
        employee_acc_list_label.setGeometry(QRect(0, 0, 380, 80))
        employee_acc_list_label.setFont(font)

        scrollArea = QScrollArea(employee_acc_list_widget)
        scrollArea.setObjectName("scrollArea")
        scrollArea.setGeometry(QRect(0, 80, 380, 685))
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scrollArea_widget = QWidget()
        scrollArea_widget.setObjectName("scrollArea_widget")
        scrollArea_widget.setGeometry(QRect(0, 0, 380, 685))
        scrollArea.setWidget(scrollArea_widget)

        # Create new account
        create_new_acc_widget = QWidget(self)
        create_new_acc_widget.setObjectName("create_new_acc_widget")
        create_new_acc_widget.setGeometry(QRect(560, 220, 850, 350))

        create_new_acc_label = QLabel(
            "Create New Account", create_new_acc_widget)
        create_new_acc_label.setObjectName("create_new_acc_label")
        create_new_acc_label.setGeometry(QRect(50, 30, 271, 41))
        create_new_acc_label.setFont(font)

        font.setPixelSize(18)
        font.setBold(False)
        create_first_name_label = QLabel("First Name :", create_new_acc_widget)
        create_first_name_label.setObjectName("create_first_name_label")
        create_first_name_label.setGeometry(QRect(50, 90, 120, 30))
        create_first_name_label.setFont(font)

        create_last_name_label = QLabel("Last Name :", create_new_acc_widget)
        create_last_name_label.setObjectName("create_last_name_label")
        create_last_name_label.setGeometry(QRect(50, 140, 120, 30))
        create_last_name_label.setFont(font)

        create_username_label = QLabel("Username :", create_new_acc_widget)
        create_username_label.setObjectName("create_username_label")
        create_username_label.setGeometry(QRect(50, 190, 120, 30))
        create_username_label.setFont(font)

        create_password_label = QLabel("Password :", create_new_acc_widget)
        create_password_label.setObjectName("create_password_label")
        create_password_label.setGeometry(QRect(50, 240, 120, 30))
        create_password_label.setFont(font)

        create_confirm_label = QLabel("Confirm :", create_new_acc_widget)
        create_confirm_label.setObjectName("create_confirm_label")
        create_confirm_label.setGeometry(QRect(480, 240, 81, 30))
        create_confirm_label.setFont(font)

        usin_create_first_name = QLineEdit(create_new_acc_widget)
        usin_create_first_name.setObjectName("usin_create_first_name")
        usin_create_first_name.setGeometry(QRect(170, 90, 620, 30))
        usin_create_first_name.setFont(font)

        usin_create_last_name = QLineEdit(create_new_acc_widget)
        usin_create_last_name.setObjectName("usin_create_last_name")
        usin_create_last_name.setGeometry(QRect(170, 140, 620, 30))
        usin_create_last_name.setFont(font)

        create_username = QLabel(create_new_acc_widget)
        create_username.setObjectName("create_username")
        create_username.setGeometry(QRect(170, 190, 281, 30))
        create_username.setFont(font)

        usin_create_password = QLineEdit(create_new_acc_widget)
        usin_create_password.setObjectName("usin_create_password")
        usin_create_password.setGeometry(QRect(170, 240, 280, 30))
        usin_create_password.setFont(font)

        usin_create_confirm = QLineEdit(create_new_acc_widget)
        usin_create_confirm.setObjectName("usin_create_confirm")
        usin_create_confirm.setGeometry(QRect(580, 240, 210, 30))
        usin_create_confirm.setFont(font)

        font.setPixelSize(14)
        font.setBold(True)
        btn_create_admin = QRadioButton(
            "Create as admin account ", create_new_acc_widget)
        btn_create_admin.setObjectName("btn_create_admin")
        btn_create_admin.setEnabled(True)
        btn_create_admin.setGeometry(QRect(50, 290, 211, 20))
        btn_create_admin.setFont(font)
        btn_create_admin.setLayoutDirection(Qt.RightToLeft)

        font.setPixelSize(18)
        font.setBold(False)
        btn_create_account = QPushButton(
            "Create Account", create_new_acc_widget)
        btn_create_account.setObjectName("btn_create_account")
        btn_create_account.setGeometry(QRect(590, 290, 200, 30))
        btn_create_account.setFont(font)

        #Edit employee account
        edit_employee_acc_widget = QWidget(self)
        edit_employee_acc_widget.setObjectName("edit_employee_acc_widget")
        edit_employee_acc_widget.setGeometry(QRect(560, 638, 850, 350))

        font.setPixelSize(24)
        font.setBold(True)
        edit_employee_acc_label = QLabel("Edit Employee Account",edit_employee_acc_widget)
        edit_employee_acc_label.setObjectName("edit_employee_acc_label")
        edit_employee_acc_label.setGeometry(QRect(50, 30, 301, 41))
        edit_employee_acc_label.setFont(font)

        font.setPixelSize(14)
        font.setBold(False)
        edit_description_label = QLabel("Click on an employee card on the left to select an employee account", edit_employee_acc_widget)
        edit_description_label.setObjectName("edit_description_label")
        edit_description_label.setGeometry(QRect(50, 70, 501, 16))
        edit_description_label.setFont(font)

        font.setPixelSize(18)
        edit_first_name_label = QLabel("First Name :", edit_employee_acc_widget)
        edit_first_name_label.setObjectName("edit_first_name_label")
        edit_first_name_label.setGeometry(QRect(50, 100, 120, 30))
        edit_first_name_label.setFont(font)

        edit_last_name_label = QLabel("Last Name :", edit_employee_acc_widget)
        edit_last_name_label.setObjectName("edit_last_name_label")
        edit_last_name_label.setGeometry(QRect(50, 150, 120, 30))
        edit_last_name_label.setFont(font)

        edit_username_label = QLabel("Username :", edit_employee_acc_widget)
        edit_username_label.setObjectName("edit_username_label")
        edit_username_label.setGeometry(QRect(50, 200, 120, 30))
        edit_username_label.setFont(font)

        edit_change_password_label = QLabel("Change Password :", edit_employee_acc_widget)
        edit_change_password_label.setObjectName("edit_change_password_label")
        edit_change_password_label.setGeometry(QRect(330, 200, 181, 30))
        edit_change_password_label.setFont(font)

        usin_edit_first_name = QLineEdit(edit_employee_acc_widget)
        usin_edit_first_name.setObjectName("usin_edit_first_name")
        usin_edit_first_name.setGeometry(QRect(170, 100, 620, 30))
        usin_edit_first_name.setFont(font)

        usin_edit_last_name = QLineEdit(edit_employee_acc_widget)
        usin_edit_last_name.setObjectName("usin_edit_last_name")
        usin_edit_last_name.setGeometry(QRect(170, 150, 620, 30))
        usin_edit_last_name.setFont(font)

        edit_username = QLabel(edit_employee_acc_widget)
        edit_username.setObjectName("edit_username")
        edit_username.setGeometry(QRect(170, 200, 141, 30))
        edit_username.setFont(font)

        usin_edit_change_password = QLineEdit(edit_employee_acc_widget)
        usin_edit_change_password.setObjectName("usin_edit_change_password")
        usin_edit_change_password.setGeometry(QRect(525, 200, 265, 30))
        usin_edit_change_password.setFont(font)

        font.setPixelSize(14)
        edit_admin_confirm_label = QLabel("Admin Confirmation :", edit_employee_acc_widget)
        edit_admin_confirm_label.setObjectName("edit_admin_confirm_label")
        edit_admin_confirm_label.setGeometry(QRect(50, 255, 501, 16))
        edit_admin_confirm_label.setFont(font)

        font.setPixelSize(18)
        edit_password_label = QLabel("Password :", edit_employee_acc_widget)
        edit_password_label.setObjectName("edit_password_label")
        edit_password_label.setGeometry(QRect(50, 280, 101, 30))
        edit_password_label.setFont(font)

        usin_edit_password = QLineEdit(edit_employee_acc_widget)
        usin_edit_password.setObjectName("usin_edit_password")
        usin_edit_password.setGeometry(QRect(170, 280, 265, 30))
        usin_edit_password.setFont(font)

        btn_delete = QPushButton("delete", edit_employee_acc_widget)
        btn_delete.setObjectName("btn_delete")
        btn_delete.setGeometry(QRect(470, 280, 140, 30))
        btn_delete.setFont(font)

        btn_save_changes = QPushButton("Save Changes", edit_employee_acc_widget)
        btn_save_changes.setObjectName("btn_save_changes")
        btn_save_changes.setGeometry(QRect(620, 280, 170, 30))
        btn_save_changes.setFont(font)

    def set_styleSheet(self, file_name: str) -> None:
        with open(file_name, 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
        f.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AccountAdminUI()
    w.set_styleSheet("account_view_theme.qss")
    w.show()
    sys.exit(app.exec())
