from controllers.controller import Controller
from models.model import Model
from PySide6.QtWidgets import QWidget
from views.forms.login_view import LoginView
from models.login_model import LoginModel


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
            pass
        else:
            self.view.show_error_label()
