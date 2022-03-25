from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QLabel
from views.theme import Theme
import os.path


class StackPage(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self, None)
        self.setFixedSize(1520, 1080)
        bg = QLabel(self)
        bg.setGeometry(0, 0, 1520, 1080)
        bg.setStyleSheet("background-color: #F8F8FF;")

    def set_styleSheet(self, file_name):
        file_path = os.path.dirname(os.path.abspath(__file__))
        real_path = os.path.join(file_path, file_name)
        with open(real_path, 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
        f.close()
