from abc import ABC
from models.model import Model
from PySide6.QtWidgets import QWidget


class Controller(ABC):
    def __init__(self, view: QWidget, model: Model):
        self.view = view
        self.model = model
