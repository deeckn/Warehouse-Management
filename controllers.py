from abc import ABC
from data.access_level import AdminAccess
from views.forms.login_view import LoginView
from models import *
from PySide6.QtWidgets import QWidget


class Controller(ABC):
    view: QWidget
    model: Model

    def __init__(self, view: QWidget, model: Model):
        self.view = view
        self.model = model

    def open_page(self):
        self.view.showFullScreen()


class LoginPage(Controller):
    view: LoginView
    model: LoginModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
        self.view.set_login_button_listener(self.verify_login)

    def verify_login(self):
        username = self.view.get_username()
        password = self.view.get_password()
        self.model.get_input(username, password)
        self.model.retrive_user(username)
        self.model.verify_login()

        if self.model.is_valid():
            self.view.hide_error_label()
            user_access = self.model.get_current_user().get_access_level()
            if isinstance(user_access, AdminAccess):
                print("Open Admin Page")
            else:
                print("Open Employee Page")
        else:
            self.view.show_error_label()


class HomePage(Controller):
    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
