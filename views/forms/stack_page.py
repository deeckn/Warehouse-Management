from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget
from views.theme import Theme


class StackPage(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self, None)
        self.setFixedSize(1520, 1080)
        self.setStyleSheet(f"background-color: #{Theme.GHOST_WHITE};")
        self.viewFont = Theme.POPPINS_BOLD_64
