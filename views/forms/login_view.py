from PySide6.QtCore import QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget
from views.theme import Theme


class LoginView(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        bg_label = QLabel(self)
        bg_label.setGeometry(0, 0, 1920, 1080)
        bg_label.setStyleSheet("background-color: #1A374D;")

        self.page_label = QLabel(self)
        self.page_label.setGeometry(QRect(192, 108, 1536, 864))
        self.page_label.setStyleSheet(f"""
            background-color: {Theme.GHOST_WHITE}; 
            border-radius: 50;
        """)

        decor = QLabel(self)
        decor.setGeometry(QRect(242, 158, 30, 30))
        decor.setStyleSheet("background-color: #C4C4C4; border-radius: 15px")

        decor1 = QLabel(self)
        decor1.setGeometry(QRect(1648, 158, 30, 30))
        decor1.setStyleSheet("background-color: #C4C4C4; border-radius: 15px")

        decor2 = QLabel(self)
        decor2.setGeometry(QRect(242, 897, 30, 30))
        decor2.setStyleSheet("background-color: #C4C4C4; border-radius: 15px")

        decor2 = QLabel(self)
        decor2.setGeometry(QRect(1648, 897, 30, 30))
        decor2.setStyleSheet("background-color: #C4C4C4; border-radius: 15px")

        self.login_label = QLabel(self)
        self.login_label.setGeometry(QRect(342, 208, 301, 131))
        self.login_label.setFont(Theme.POPPINS_BOLD_72)
        self.login_label.setText("Log in")
        self.login_label.setStyleSheet(f"""
            background-color: {Theme.GHOST_WHITE}; 
            color: {Theme.DARK_BLUE};
        """)

        self.username_label = QLabel(self)
        self.username_label.setGeometry(QRect(342, 356, 271, 54))
        self.username_label.setFont(Theme.POPPINS_BOLD_36)
        self.username_label.setText("Username")
        self.username_label.setStyleSheet(f"""
            background-color: {Theme.GHOST_WHITE}; 
            color: {Theme.BLUE};
        """)

        self.password_label = QLabel(self)
        self.password_label.setText("Password")
        self.password_label.setGeometry(QRect(342, 559, 251, 54))
        self.password_label.setFont(Theme.POPPINS_BOLD_36)
        self.password_label.setStyleSheet(f"""
            background-color: {Theme.GHOST_WHITE}; 
            color: {Theme.BLUE};
        """)

        self.error_label = QLabel(self)
        self.error_label.setText("Wrong Username or Password")
        self.error_label.setGeometry(QRect(352, 770, 711, 51))
        self.error_label.setFont(Theme.POPPINS_BOLD_18)
        self.error_label.hide()
        self.error_label.setStyleSheet(f"""
            background-color: {Theme.GHOST_WHITE}; 
            color: {Theme.RED};
        """)

        self.login_button = QPushButton(self)
        self.login_button.setText("Log in")
        self.login_button.setGeometry(QRect(1428, 782, 200, 80))
        self.login_button.setFont(Theme.POPPINS_REGULAR_28)
        self.login_button.setStyleSheet(f"""
            color: white; 
            background-color: #FDCB6E; 
            border-radius: 25;
        """)

        self.username_lineedit = QLineEdit(self)
        self.username_lineedit.setGeometry(QRect(342, 430, 1286, 109))
        self.username_lineedit.setFont(Theme.POPPINS_REGULAR_36)
        self.username_lineedit.setStyleSheet(f"""
            background-color: rgb(221, 221, 221);
            padding-left: 50; 
            padding-top: 10; 
            border: none; 
            color: black;
        """)

        self.password_lineedit = QLineEdit(self)
        self.password_lineedit.setObjectName(u"password_lineedit")
        self.password_lineedit.setGeometry(QRect(342, 633, 1286, 109))
        self.password_lineedit.setFont(Theme.POPPINS_REGULAR_36)
        self.password_lineedit.setStyleSheet(f"""
            background-color: rgb(221, 221, 221);
            padding-left: 50; 
            padding-top: 10; 
            border: none; 
            color: black;
        """)
        self.password_lineedit.setEchoMode(QLineEdit.Password)

    # UI
    def reset(self):
        """Resets the line edit fields and hides error label"""
        self.clear_info()
        self.hide_error_label()

    def clear_info(self) -> None:
        """Clears line edit inputs"""
        self.username_lineedit.setText("")
        self.password_lineedit.setText("")

    def show_error_label(self):
        self.error_label.show()

    def hide_error_label(self):
        self.error_label.hide()

    def get_username(self) -> str:
        return self.username_lineedit.text()

    def get_password(self) -> str:
        return self.password_lineedit.text()

    def set_login_button_listener(self, function):
        """Sets a function to the login button event"""
        self.login_button.clicked.connect(function)
