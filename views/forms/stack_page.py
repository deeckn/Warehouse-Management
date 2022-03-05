from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget
from views.theme import Theme
import os.path


class StackPage(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self, None)
        self.setFixedSize(1520, 1080)
        self.setStyleSheet(f"background-color: #{Theme.GHOST_WHITE};")

    def set_styleSheet(self, file_name) -> None:
        file_path = os.path.dirname(os.path.abspath(__file__))
        real_path = os.path.join(file_path, file_name)
        with open(real_path, 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
        f.close()
