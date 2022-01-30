from controller import Controller
from models.model import Model
from PySide6.QtWidgets import QWidget


class HomePage(Controller):
    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
