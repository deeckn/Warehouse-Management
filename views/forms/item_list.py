from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class ItemList(QWidget):
    def __init__(self, parent=None) -> None:
        QWidget.__init__(self, parent)

        bg = QLabel(self)
        bg.setGeometry(0, 0, 800, 794)
        bg.setStyleSheet("background-color: white; border-radius: 25;")

        scroll_area = QScrollArea(self)
        scroll_area.setGeometry(64, 54, 688, 618)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("background-color: white; border:none;")
        scroll_area.setWidgetResizable(True)

        self.scroll_area_widget = QWidget()

        self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)
        self.scroll_area_layout.setSpacing(40)
        self.scroll_area_layout.setAlignment(Qt.AlignTop)
        scroll_area.setWidget(self.scroll_area_widget)
