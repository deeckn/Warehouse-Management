from controller import Controller
from models.model import Model
from PySide6.QtWidgets import QWidget


class LoginPage(Controller):
    def __init__(self, view: QWidget, model: Model):
        Controller.__init__(self, view, model)
