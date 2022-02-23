import PySide6
from PySide6.QtWidgets import QWidget, QLabel,QPushButton
from PySide6.QtGui import QFont


class EmployeeCardItem(QWidget):
    def __init__(self, parent) -> None:
        QWidget.__init__(self, parent)
        self.parent_widget = parent

        self.setFixedSize(340, 170)
        self.setStyleSheet(
            "color:#000000; background-color:#F8F8FF; padding-left:20px; margin:0px 20px 15px 35px; border-radius:10px;")

        font = QFont("Poppins")
        font.setPixelSize(18)

        self.card = QLabel(self)
        self.card.setFixedSize(340, 170)
        self.card.setFont(font)

    def set_employee_card(self, text: str) -> None:
        self.card.setText(text)

    def get_text(self) -> str:
        return self.card.text()

    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self.parent_widget.previous_card.setStyleSheet(
            "color:#000000; background-color:#F8F8FF; padding-left:20px; margin:0px 20px 15px 35px; border-radius:10px;")
        self.parent_widget.current_card = self
        self.setStyleSheet(
            "color:#000000; background-color:#F8F8FF; padding-left:20px; margin:0px 20px 15px 35px; border-radius:10px; border:3px solid #FDCB6E;")
        self.parent_widget.previous_card = self.parent_widget.current_card