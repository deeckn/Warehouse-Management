from typing import Optional
from PySide6.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import Qt
from views.items.log_item import LogItem

class LogWindowView(QWidget):
    def __init__(self, parent) -> None:
        QWidget.__init__(self, parent)
        self.setStyleSheet("background-color: white; border: none; color: black;")
        #self.setStyleSheet("background-color: white; border: 1px solid black; color: black;")
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedSize(400,620)
        self.scroll_area_widget = QWidget()
        self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)
        self.scroll_area_layout.setSpacing(10)
        self.scroll_area_layout.setContentsMargins(0,10,20,10)
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.spacer = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

    def add_log(self, date: str, time:str, txt: str):
        self.scroll_area_layout.removeItem(self.spacer)
        self.scroll_area_layout.addWidget(LogItem(date,time,txt))
        self.scroll_area_layout.addItem(self.spacer)