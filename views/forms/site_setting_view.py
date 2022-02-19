# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'site_setting_view.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class SiteSettingView(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.resize(1552, 1080)
        self.setStyleSheet(u"background-color: #E5E5E5;")
        
        # font
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPixelSize(72)
        font1.setBold(True)

        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPixelSize(18)
        font2.setBold(True)

        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPixelSize(18)
        font3.setBold(False)

        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setPixelSize(24)
        font5.setBold(True)

        font6 = QFont()
        font6.setFamilies([u"Poppins"])
        font6.setPixelSize(14)
        font6.setBold(False)

        self.site_setting_label = QLabel("Site Settings", self)
        self.site_setting_label.setGeometry(QRect(100, 60, 641, 121))
        self.site_setting_label.setFont(font1)
        self.site_setting_label.setStyleSheet(u"color: #1A374D;")

        self.space_1 = QLabel(self)
        self.space_1.setGeometry(QRect(100, 219, 500, 794))
        self.space_1.setStyleSheet(u"background-color: #FFFFFF;\n"
        "border-radius: 25;")
        
        self.Shelf_label_seach_label = QLabel("Shelf Label", self)
        self.Shelf_label_seach_label.setGeometry(QRect(150, 296, 131, 28))
        self.Shelf_label_seach_label.setFont(font2)
        self.Shelf_label_seach_label.setStyleSheet(u"color: #406882;\n"
        "background-color: transparent;")

        self.Search_LineEdit = QLineEdit(self)
        self.Search_LineEdit.setGeometry(QRect(150, 324, 400, 42))
        self.Search_LineEdit.setFont(font3)
        self.Search_LineEdit.setStyleSheet(u"border-radius: 0;\n"
        "padding-left: 14;\n"
        "padding-top: 5;")

        self.search_button = QPushButton("Search", self)
        self.search_button.setGeometry(QRect(374, 387, 176, 41))
        self.search_button.setFont(font3)
        self.search_button.setStyleSheet(u"background-color: #FDCB6E;\n "
        "border-radius: 10;\n"
        "color: white")

        self.shelf_label_information_label = QLabel("Shelf Label", self)
        self.shelf_label_information_label.setGeometry(QRect(151, 488, 141, 28))
        self.shelf_label_information_label.setFont(font2)
        self.shelf_label_information_label.setStyleSheet(u"background-color: transparent;\n"
        "color: #406882;")

        self.max_weight_label = QLabel("Max Weight (Kg)",self)
        self.max_weight_label.setGeometry(QRect(311, 488, 201, 28))
        self.max_weight_label.setFont(font2)
        self.max_weight_label.setStyleSheet(u"background-color: transparent;\n"
        "color: #406882;")

        self.shelf_label_informtion_lineEdit = QLineEdit(self)
        self.shelf_label_informtion_lineEdit.setGeometry(QRect(151, 516, 150, 42))
        self.shelf_label_informtion_lineEdit.setFont(font3)
        self.shelf_label_informtion_lineEdit.setStyleSheet(u"border-radius: 0;\n"
        "padding-left: 14;\n"
        "padding-top: 5;")

        self.max_weight_LineEdit = QLineEdit(self)
        self.max_weight_LineEdit.setGeometry(QRect(311, 516, 150, 42))
        self.max_weight_LineEdit.setFont(font3)
        self.max_weight_LineEdit.setStyleSheet(u"border-radius: 0; \n"
        "padding-left: 14;\n"
        "padding-top: 5;")

        self.per_slot_max_weight_label = QLabel("per slot", self)
        self.per_slot_max_weight_label.setGeometry(QRect(476, 523, 69, 28))
        self.per_slot_max_weight_label.setFont(font2)
        self.per_slot_max_weight_label.setStyleSheet(u"color: #406882; \n"
        "background-color: transparent;")

        self.Dimension_label = QLabel("Dimensions",self)
        self.Dimension_label.setGeometry(QRect(151, 568, 110, 28))
        self.Dimension_label.setFont(font2)
        self.Dimension_label.setStyleSheet(u"background-color: transparent; \n"
        "color: #406882;")

        self.Length_label = QLabel("Length (m)", self)
        self.Length_label.setGeometry(QRect(169, 607, 104, 28))
        self.Length_label.setFont(font2)
        self.Length_label.setStyleSheet(u"background-color: transparent; \n"
        "color: #406882; ")

        self.weight_label = QLabel("Weight (m)", self)
        self.weight_label.setGeometry(QRect(169, 656, 108, 28))
        self.weight_label.setFont(font2)
        self.weight_label.setStyleSheet(u"background-color: transparent;\n"
        "color: #406882;")

        self.height_label = QLabel("Height (m)", self)
        self.height_label.setGeometry(QRect(169, 705, 102, 28))
        self.height_label.setFont(font2)
        self.height_label.setStyleSheet(u"background-color: transparent; \n"
        "color: #406882;")

        self.Length_LineEdit = QLineEdit(self)
        self.Length_LineEdit.setGeometry(QRect(307, 601, 125, 42))
        self.Length_LineEdit.setFont(font3)
        self.Length_LineEdit.setStyleSheet(u"border-radius: 0;\n"
        "padding-left: 14;\n"
        "padding-top: 5;")

        self.Weight_LineEdit = QLineEdit(self)
        self.Weight_LineEdit.setGeometry(QRect(307, 650, 125, 42))
        self.Weight_LineEdit.setFont(font3)
        self.Weight_LineEdit.setStyleSheet(u"border-radius: 0;\n"
        "padding-left: 14;\n"
        "padding-top: 5;")

        self.Height_LineEdit = QLineEdit(self)
        self.Height_LineEdit.setGeometry(QRect(307, 699, 125, 42))
        self.Height_LineEdit.setFont(font3)
        self.Height_LineEdit.setStyleSheet(u"border-radius: 0; \n"
        "padding-left: 14;\n"
        "padding-top: 5;")

        self.slot_label = QLabel("Slot", self)
        self.slot_label.setGeometry(QRect(151, 751, 137, 28))
        self.slot_label.setFont(font2)
        self.slot_label.setStyleSheet(u"background-color: transparent; \n"
        "color: #406882;")

        self.weight_per_slot_label = QLabel("per slot", self)
        self.weight_per_slot_label.setGeometry(QRect(462, 657, 69, 28))
        self.weight_per_slot_label.setFont(font2)
        self.weight_per_slot_label.setStyleSheet(u"background-color: transparent;\n"
        "color: #406882;")

        self.row_label = QLabel("Row", self)
        self.row_label.setGeometry(QRect(170, 793, 39, 28))
        self.row_label.setFont(font2)
        self.row_label.setStyleSheet(u"background-color: transparent;\n"
        "color: #406882;")

        self.column_label = QLabel("Column", self)
        self.column_label.setGeometry(QRect(351, 793, 75, 28))
        self.column_label.setFont(font2)
        self.column_label.setStyleSheet(u"background-color: transparent;\n"
        "color: #406882;")

        self.Row_LineEdit = QLineEdit(self)
        self.Row_LineEdit.setGeometry(QRect(219, 786, 120, 42))
        self.Row_LineEdit.setFont(font3)
        self.Row_LineEdit.setStyleSheet(u"border-radius: 0; \n"
        "padding-left: 14; \n"
        "padding-top: 5;")

        self.column_LineEdit = QLineEdit(self)
        self.column_LineEdit.setGeometry(QRect(434, 786, 120, 42))
        self.column_LineEdit.setFont(font3)
        self.column_LineEdit.setStyleSheet(u"border-radius: 0; \n"
        "padding-left: 14; \n"
        "padding-top: 5;")

        self.Total_label = QLabel(self)
        self.Total_label.setGeometry(QRect(169, 848, 200, 27))
        self.Total_label.setFont(font2)
        self.Total_label.setStyleSheet(u"background-color: transparent;\n"
        "color: #406882;")

        self.save_button = QPushButton("SAVE", self)
        self.save_button.setGeometry(QRect(267, 948, 166, 65))
        self.save_button.setFont(font5)
        self.save_button.setStyleSheet(u"background-color: #FDCB6E;\n"
        "color: white;\n"
        "border-radius: 0;")

        self.delete_button = QPushButton("DELETE", self)
        self.delete_button.setGeometry(QRect(100, 948, 167, 64))
        self.delete_button.setFont(font5)
        self.delete_button.setStyleSheet(u"background-color: #FF7474;\n "
        "color: white; \n"
        "border-bottom-left-radius: 25px;")

        self.add_button = QPushButton("ADD", self)
        self.add_button.setGeometry(QRect(433, 948, 167, 65))
        self.add_button.setFont(font5)
        self.add_button.setStyleSheet(u"background-color: #2ACAB0;\n"
        "color: white;\n"
        "border-bottom-right-radius: 25;")

        self.space_2 = QLabel(self)
        self.space_2.setGeometry(QRect(640, 219, 800, 794))
        self.space_2.setStyleSheet(u"background-color: white;\n"
        "border-radius: 25;")

        self.search_label = QLabel("Search",self)
        self.search_label.setGeometry(QRect(325, 264, 50, 22))
        self.search_label.setFont(font6)
        self.search_label.setStyleSheet(u"background-color: transparent;")

        self.information_label = QLabel("Information", self)
        self.information_label.setGeometry(QRect(310, 460, 82, 22))
        self.information_label.setFont(font6)
        self.information_label.setStyleSheet(u"background-color: transparent;")

        self.line = QFrame(self)
        self.line.setGeometry(QRect(151, 471, 145, 1))
        self.line.setStyleSheet(u"background-color:black;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.line_2 = QFrame(self)
        self.line_2.setGeometry(QRect(406, 471, 145, 1))
        self.line_2.setStyleSheet(u"background-color: black;")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.line_3 = QFrame(self)
        self.line_3.setGeometry(QRect(150, 275, 170, 1))
        self.line_3.setStyleSheet(u"background-color: black;")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.line_4 = QFrame(self)
        self.line_4.setGeometry(QRect(380, 275, 170, 1))
        self.line_4.setStyleSheet(u"background-color: black;")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
    
    # Set LineEdits
    def set_shelf_LineEdit(self, text: str) -> None:
        self.shelf_label_informtion_lineEdit.setText(text)
    
    def set_max_weight_LineEdit(self, text: str) -> None:
        self.max_weight_LineEdit.setText(text)
    
    def set_length_LineEdit(self, text:str) -> None:
        self.Length_LineEdit.setText(text)

    def set_weight_LineEdit(self, text:str) -> None:
        self.weight_label.setText(text)
    
    def set_height_LineEdit(self, text:str) -> None:
        self.Height_LineEdit.setText(text)
    
    def set_row_LineEdit(self, text:str) -> None:
        self.Row_LineEdit.setText(text)

    def set_column_LineEdit(self, text:str) -> None:
        self.column_LineEdit.setText(text)

    # Set Labels
    def set_total_label(self, text:str) -> None:
        self.Total_label.setText("Total : " + text)

    # Get LineEdits
    def get_search(self) -> str:
        return self.Search_LineEdit.text()

    def get_shelf_LineEdit(self) -> str:
        return self.shelf_label_informtion_lineEdit.text()
    
    def get_max_weight_LineEdit(self) -> str:
        return self.max_weight_LineEdit.text()
    
    def get_length_LineEdit(self) -> str:
        return self.Length_LineEdit.text()

    def get_weight_LineEdit(self) -> str:
        return self.weight_label.text()
    
    def get_height_LineEdit(self) -> str:
        return self.Height_LineEdit.text()
    
    def get_row_LineEdit(self) -> str:
        return self.Row_LineEdit.text()

    def get_column_LineEdit(self) -> str:
        return self.column_LineEdit.text()

    # Set Buttons Listener
    def set_delete_button_listener(self, function) -> None:
        self.delete_button.clicked.connect(function)
    
    def set_save_button_listener(self, function) -> None:
        self.save_button.clicked.connect(function)

    def set_add_button_listener(self, function) -> None:
        self.add_button.clicked.connect(function)

    def set_search_listener(self, function) -> None:
        self.search_button.clicked.connect(function)