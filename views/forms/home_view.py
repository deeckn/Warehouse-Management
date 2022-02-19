#from stack_page import StackPage # for local user
from views.forms.stack_page import StackPage # For real test
from views.forms.log_activity_view import LogWindowView
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class HomeView(StackPage):
    def __init__(self) -> None:
        super().__init__()
        # BG
        activity_log_bg = QLabel(self)
        activity_log_bg.setGeometry(940,186,500,794)
        activity_log_bg.setStyleSheet("background-color: white; border-radius: 25px;")

        product_search_bg = QLabel(self)
        product_search_bg.setGeometry(103,186,800,794)
        product_search_bg.setStyleSheet("background-color: white; border-radius: 25px;")

        # Header
        header = QLabel("Home",self)
        header.setFont(self.viewFont)
        header.setGeometry(100,60,195,96)
        header.setStyleSheet("color: #1A374D;")
    
        self.viewFont.setPixelSize(24)

        header_activity_log = QLabel("Activity Log",self)
        header_activity_log.setFont(self.viewFont)
        header_activity_log.setGeometry(1000,226,145,36)
        header_activity_log.setStyleSheet("color: #406882; background-color: none;")

        header_product_search = QLabel("Product Search",self)
        header_product_search.setFont(self.viewFont)
        header_product_search.setStyleSheet("color: #406882; background-color: none;")
        header_product_search.setGeometry(160, 218, 190,36)

        # Input Widget
        self.viewFont.setPixelSize(18)

        self.product_search_button = QPushButton(self)
        self.product_search_button.setText("SEARCH")
        self.product_search_button.setFont(self.viewFont)
        self.product_search_button.setStyleSheet("color: white; background-color: #FDCB6E; border-radius: 10px;")
        self.product_search_button.setGeometry(720,313,120,40)

        self.viewFont.setBold(False)
        self.viewFont.setPixelSize(14)

        self.product_search_input = QLineEdit(self)
        self.product_search_input.setGeometry(160,262,680,40)
        self.product_search_input.setFont(self.viewFont)
        self.product_search_input.setStyleSheet("padding-left: 15px; color: black; border: none; background-color: #EAEAEA;")

        # Output Widget
        self.activity_log_window = LogWindowView(self)
        self.activity_log_window.move(1000, 320)
        
        # Testing purpose
        self.activity_log_window.add_log("01/06/2022","10.00 am","John added 20 Black Shirts to Mr. Tawan’s product list")
        self.activity_log_window.add_log("01/04/2022","12.45 am","Mary logged into the system")
        self.activity_log_window.add_log("01/03/2022","07.15 am","Mike logged out from the system")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")
        self.activity_log_window.add_log("01/01/2022","16.00 pm","Mike updated Mark’s last name from “Urkman” to “Smith”")

        # Decor
        decor_linebreak_activity = QLabel(self)
        decor_linebreak_activity.setGeometry(1000,271, 381,47)
        decor_linebreak_activity.setStyleSheet("border-top: 1px solid black; border-bottom: 1px solid black; background-color: none;")

        decor_linebreak_product_search = QLabel(self)
        decor_linebreak_product_search.setGeometry(160, 384, 680, 1)
        decor_linebreak_product_search.setStyleSheet("border-top: 1px solid black; border-bottom: 1px solid black; background-color: none;")

        self.viewFont.setBold(False)
        self.viewFont.setPixelSize(18)

        decor_legend_activity_Date = QLabel("Date",self)
        decor_legend_activity_Time = QLabel("Time",self)
        decor_legend_activity_Event = QLabel("Event",self)
        decor_legend_activity_Date.setFont(self.viewFont)
        decor_legend_activity_Time.setFont(self.viewFont)
        decor_legend_activity_Event.setFont(self.viewFont)
        decor_legend_activity_Date.setStyleSheet("background-color: none; color: black")
        decor_legend_activity_Time.setStyleSheet("background-color: none; color: black")
        decor_legend_activity_Event.setStyleSheet("background-color: none; color: black")
        decor_legend_activity_Date.setGeometry(1000,281,43,27)
        decor_legend_activity_Time.setGeometry(1105,281,44,27)
        decor_legend_activity_Event.setGeometry(1200,281,49,27)

        self.viewFont.setPixelSize(14)
        decor_guide_product_search = QLabel("Enter quantity to add or export products",self)
        decor_guide_product_search.setFont(self.viewFont)
        decor_guide_product_search.setAlignment(Qt.AlignCenter)
        decor_guide_product_search.setGeometry(350,373,300,21)
        decor_guide_product_search.setStyleSheet("background-color: white; color: black")

        decor_img_product_search =  QLabel(self)
        decor_img_product_search.setGeometry(353,218,30,30)
        decor_img_product_search.setStyleSheet("background-color: none;")
        img = QPixmap(f":/icons/search.svg").scaled(30, 30)
        img = img.transformed(QTransform().scale(-1, 1))
        painter = QPainter(img)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(img.rect(), QColor("#406882"))
        painter.end()
        decor_img_product_search.setPixmap(img)



