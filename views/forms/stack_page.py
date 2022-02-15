from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel, QWidget, QSpacerItem, QSizePolicy,
    QVBoxLayout, QHBoxLayout, QStackedWidget)

class Stack_Page(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self, None)
        self.setFixedSize(1520,1080)
