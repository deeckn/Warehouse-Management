#from stack_page import StackPage # for local user
from views.forms.stack_page import StackPage # For real test
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class HomePage(StackPage):
    def __init__(self) -> None:
        super().__init__()

        self.header = QLabel("Home",self)
        self.header.setFont(self.viewFont)
        self.header.setGeometry(100,60,195,96)
        self.header.setStyleSheet("color: #1A374D;")

        self.activity_log_bg = QLabel(self)
        self.activity_log_bg.setGeometry(940,186,500,794)
        self.activity_log_bg.setStyleSheet("background-color: white; border-radius: 25px;")

        self.product_search_bg = QLabel(self)
        self.product_search_bg.setGeometry(103,186,800,794)
        self.product_search_bg.setStyleSheet("background-color: white; border-radius: 25px;")

        self.viewFont.setPointSize(24)

        self.header_activity_log = QLabel("Activity Log",self)
        self.header_activity_log.setFont(self.viewFont)
        self.header_activity_log.setGeometry(1000,226,145,36)
        self.header_activity_log.setStyleSheet("color: #406882; background-color: none;")

        self.header_product_search = QLabel("Product Search",self)
        self.header_product_search.setFont(self.viewFont)
        self.header_product_search.setStyleSheet("color: #406882; background-color: none;")
        self.header_product_search.setGeometry(160, 218, 190,36)

        self.viewFont.setPointSize(18)

        self.product_search_button = QPushButton(self)
        self.product_search_button.setText("SEARCH")
        self.product_search_button.setFont(self.viewFont)
        self.product_search_button.setStyleSheet("color: white; background-color: #FDCB6E; border-radius: 10px;")
        self.product_search_button.setGeometry(720,313,120,40)

        self.viewFont.setBold(False)

        self.viewFont.setPointSize(14)
        self.product_search_input = QLineEdit(self)
        self.product_search_input.setGeometry(160,262,680,40)
        self.product_search_input.setFont(self.viewFont)
        self.product_search_input.setStyleSheet("padding-left: 15px; color: black; background-color: #EAEAEA;")

        # Decor
        self.decor_linebreak_activity = QLabel(self)
        self.decor_linebreak_activity.setGeometry(1000,271, 381,47)
        self.decor_linebreak_activity.setStyleSheet("border-top: 1px solid black; border-bottom: 1px solid black; background-color: none;")

        self.decor_linebreak_product_search = QLabel(self)
        self.decor_linebreak_product_search.setGeometry(160, 384, 680, 1)
        self.decor_linebreak_product_search.setStyleSheet("border-top: 1px solid black; border-bottom: 1px solid black; background-color: none;")

        self.viewFont.setPointSize(18)
        self.decor_legend_activity_Date = QLabel("Date",self)
        self.decor_legend_activity_Time = QLabel("Time",self)
        self.decor_legend_activity_Event = QLabel("Event",self)
        self.decor_legend_activity_Date.setFont(self.viewFont)
        self.decor_legend_activity_Time.setFont(self.viewFont)
        self.decor_legend_activity_Event.setFont(self.viewFont)
        self.decor_legend_activity_Date.setStyleSheet("background-color: none; color: black")
        self.decor_legend_activity_Time.setStyleSheet("background-color: none; color: black")
        self.decor_legend_activity_Event.setStyleSheet("background-color: none; color: black")
        self.decor_legend_activity_Date.setGeometry(1000,281,43,27)
        self.decor_legend_activity_Time.setGeometry(1105,281,44,27)
        self.decor_legend_activity_Event.setGeometry(1200,281,49,27)

        self.viewFont.setPointSize(14)
        self.decor_guide_product_search = QLabel("Enter quantity to add or export products",self)
        self.decor_guide_product_search.setAlignment(Qt.AlignCenter)
        self.decor_guide_product_search.setGeometry(350,373,300,21)
        self.decor_guide_product_search.setStyleSheet("background-color: white; color: black")



