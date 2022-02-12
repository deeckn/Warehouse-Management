import sys
from PySide6.QtWidgets import QApplication
from controllers import *
from views.forms.login_view import LoginView
from models import LoginModel


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.current_controller = LoginPage(LoginView(), LoginModel())

    def start(self):
        self.current_controller.open_page()
        sys.exit(self.app.exec())
