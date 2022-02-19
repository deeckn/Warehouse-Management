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

class ShelfItem(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.resize(680, 120)
        self.setStyleSheet(u"background-color: #FFFFFF;\n"
        "border-radius: 30")

        self.font = QFont()
        self.font.setFamilies([u"Poppins"])
        self.font.setPixelSize(18)
        self.font.setBold(False)

        self.shelf_label = QLabel(self)
        self.shelf_label.setGeometry(QRect(44, 17, 245, 27))
        self.shelf_label.setFont(self.font)
        self.shelf_label.setStyleSheet(u"background-color: transparent; \n"
        "color: black;")

        self.max_weight_label = QLabel(self)
        self.max_weight_label.setGeometry(QRect(44, 44, 245, 27))
        self.max_weight_label.setFont(self.font)
        self.max_weight_label.setStyleSheet(u"background-color: transparent; \n"
        "color: black;")

        self.dimensions_label = QLabel(self)
        self.dimensions_label.setGeometry(QRect(44, 71, 245, 27))
        self.dimensions_label.setFont(self.font)
        self.dimensions_label.setStyleSheet(u"background-color: transparent; \n"
        "color: black;")

        self.total_slot_label = QLabel(self)
        self.total_slot_label.setGeometry(QRect(371, 17, 245, 27))
        self.total_slot_label.setFont(self.font)
        self.total_slot_label.setStyleSheet(u"background-color: transparent; \n"
        "color: black;")

        self.row_label = QLabel(self)
        self.row_label.setGeometry(QRect(371, 44, 245, 27))
        self.row_label.setFont(self.font)
        self.row_label.setStyleSheet(u"background-color: transparent; \n"
        "color: black;")

        self.column_label = QLabel(self)
        self.column_label.setGeometry(QRect(371, 71, 245, 27))
        self.column_label.setFont(self.font)
        self.column_label.setStyleSheet(u"background-color: transparent; \n"
        "color: black;")


    
    # Set Functions
    def set_shelf_label(self, text:str) -> None:
        self.shelf_label.setText("Shelf: " + text)

    def set_max_weight_label(self, text:str) -> None:
        self.max_weight_label.setText("Max Weight: " + text + " Kg")
    
    def set_dimensions_label(self, text:str) -> None:
        self.dimensions_label.setText("Dimensions: " + text)

    def set_total_slot_label(self, text:str) -> None:
        self.total_slot_label.setText("Total Slot: " + text)

    def set_row_label(self, text:str) -> None:
        self.row_label.setText("Row: " + text)

    def set_column_label(self, text:str) -> None:
        self.column_label.setText("Column: " + text)

    def stroke_shelf(self)-> None:
        self.setStyleSheet(u"background-color: #FFFFFF;\n"
        "border-radius: 30\n"
        "stroke: black\n"
        "stroke-width: 3")