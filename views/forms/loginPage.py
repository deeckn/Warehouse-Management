import sys
from PySide6.QtCore import (QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,QWidget)


class Login_Page(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setStyleSheet("background-color: #1A374D")


        self.page_label = QLabel(self)
        self.page_label.setGeometry(QRect(192, 108, 1536, 864)) # x, y,  w, h
        font = QFont("Poppins")
        font.setBold(True)
        self.page_label.setStyleSheet(u"background-color: #F8F8FF;border-radius: 50;")

        decor = QLabel(self)
        decor.setGeometry(QRect(242,158,30,30))
        decor.setStyleSheet("background-color: #C4C4C4; border-radius: 15px")

        decor1 = QLabel(self)
        decor1.setGeometry(QRect(1648,158,30,30))
        decor1.setStyleSheet("background-color: #C4C4C4; border-radius: 15px")

        decor2 = QLabel(self)
        decor2.setGeometry(QRect(242,897,30,30))
        decor2.setStyleSheet("background-color: #C4C4C4; border-radius: 15px")

        decor2 = QLabel(self)
        decor2.setGeometry(QRect(1648,897,30,30))
        decor2.setStyleSheet("background-color: #C4C4C4; border-radius: 15px")

        self.login_label = QLabel(self)
        self.login_label.setGeometry(QRect(342, 208, 301, 131))
        font.setPointSize(72)
        self.login_label.setFont(font)
        self.login_label.setText("Log in")
        self.login_label.setStyleSheet(u"background-color: #F8F8FF;color: #1A374D;")
        
        self.username_label = QLabel(self)
        self.username_label.setGeometry(QRect(342, 356, 271, 54))
        font.setPointSize(36)
        self.username_label.setFont(font)
        self.username_label.setText("Username")
        self.username_label.setStyleSheet(u"background-color: #F8F8FF; color: #406882;")

        self.password_label = QLabel(self)
        self.password_label.setText("Password")
        self.password_label.setGeometry(QRect(342, 559, 251, 54))
        self.password_label.setFont(font)
        self.password_label.setStyleSheet(u"background-color: #F8F8FF; color: #406882;")
        
        self.error_label = QLabel(self)
        self.error_label.setText("Wrong Username or Password")
        self.error_label.setGeometry(QRect(352, 770, 711, 51))
        font.setPointSize(18)
        self.error_label.setFont(font)
        self.error_label.hide()
        self.error_label.setStyleSheet(u"background-color: #F8F8FF; color: Red;")

        self.login_button = QPushButton(self)
        self.login_button.setText("Log in")
        self.login_button.setGeometry(QRect(1428, 782, 200, 80))
        font.setBold(False)
        font.setPointSize(28)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("color: white; background-color: #FDCB6E; border-radius: 25;")

        self.username_lineedit = QLineEdit(self)
        self.username_lineedit.setGeometry(QRect(342, 430, 1286, 109))
        font.setPointSize(36)
        self.username_lineedit.setFont(font)
        self.username_lineedit.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"padding-left: 50;\n"
"padding-top: 10;\n"
"border: none;")

        self.password_lineedit = QLineEdit(self)
        self.password_lineedit.setObjectName(u"password_lineedit")
        self.password_lineedit.setGeometry(QRect(342, 633, 1286, 109))
        self.password_lineedit.setFont(font)
        self.password_lineedit.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"padding-left: 50;\n"
"padding-top: 10;\n"
"border: none;")
        self.password_lineedit.setEchoMode(QLineEdit.Password)

        self.login_button.clicked.connect(self.show_error_label)


    # UI
    def clear_info(self) -> None:
        self.username_lineedit.setText("")
        self.password_lineedit.setText("")
        self.hide_error_label()

    def show_error_label(self) -> None:
        self.error_label.show()

    def hide_error_label(self) -> None:
        self.error_label.hide()
    
    # Getter
    def get_username(self) -> str:
        return self.username_lineedit.text()
    
    def get_password(self) -> str:
        return self.password_lineedit.text()

    #Setter
    def set_login_button_listener(self, function) -> None:
        self.login_button.clicked.connect(function)
