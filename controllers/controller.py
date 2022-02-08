from abc import ABC
from models.model import Model
from PySide6.QtWidgets import QWidget


class Controller(ABC):
    view: QWidget
    model: Model

    def __init__(self, view: QWidget, model: Model):
        self.view = view
        self.model = model

    def open_page(self):
        self.view.showFullScreen()
