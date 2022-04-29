import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform,QMouseEvent)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget, QGridLayout)

from data.data_classes import StorageShelf


class ShelfItem(QWidget):
    def __init__(self, parent, shelf: StorageShelf):
        QWidget.__init__(self,  None)

        self.container = QWidget(self)
        self.container.setGeometry(0, 0, 680, 120)
        self.container.setStyleSheet("background-color: #F8F8FF; border-radius: 30;")

        self.parent_widget = parent
        self.__shelf = shelf
        self.grid_layout = QGridLayout()

        self.font = QFont()
        self.font.setFamilies([u"Poppins"])
        self.font.setPixelSize(18)
        self.font.setBold(False)

        self.shelf_label = QLabel()
        self.shelf_label.resize(245, 27)
        self.shelf_label.setFont(self.font)

        self.max_weight_label = QLabel()
        self.max_weight_label.resize(245, 27)
        self.max_weight_label.setFont(self.font)
    
        self.dimensions_label = QLabel()
        self.dimensions_label.resize(245, 27)
        self.dimensions_label.setFont(self.font)
    
        self.total_slot_label = QLabel()
        self.total_slot_label.resize(245, 27)
        self.total_slot_label.setFont(self.font)

        self.row_label = QLabel()
        self.row_label.resize(245, 27)
        self.row_label.setFont(self.font)

        self.column_label = QLabel()
        self.column_label.resize(245, 27)
        self.column_label.setFont(self.font)
       
        self.grid_layout.addWidget(self.shelf_label, 0,0,1,1)
        self.grid_layout.addWidget(self.max_weight_label, 1,0,1,1)
        self.grid_layout.addWidget(self.dimensions_label, 2,0,1,1)
        self.grid_layout.addWidget(self.total_slot_label, 0,1,1,1)
        self.grid_layout.addWidget(self.row_label, 1,1,1,1)
        self.grid_layout.addWidget(self.column_label, 2,1,1,1)
        self.grid_layout.setContentsMargins(44,17,40,17)
        
        self.setLayout(self.grid_layout)

        self.set_shelf_label()
        self.set_max_weight_label()
        self.set_dimensions_label()
        self.set_total_slot_label()
        self.set_row_label()
        self.set_column_label()

    def calculate_total_slot(self) -> int:
        return self.__shelf.get_rows() * self.__shelf.get_columns()

    # Get Function
    def get_current_shelf(self) -> StorageShelf:
        """"get Shelf Database"""
        return self.__shelf

    def get_shelf_label(self) -> str:
        """get Shelf of Shelf"""
        return self.__shelf.get_label()

    def get_max_weight(self) -> int:
        """get Max Weight of Shelf"""
        return self.__shelf.get_max_weight()
    
    def get_length(self) -> int:
        """get Length of Shelf"""
        return self.__shelf.get_length()

    def get_width(self) -> int:
        """get Length of Shelf"""
        return self.__shelf.get_width()

    def get_height(self) -> int:
        """get Height of Shelf"""
        return self.__shelf.get_height()

    def get_total_slot(self) -> int:
        """get Total Slot of Shelf"""
        return self.calculate_total_slot()

    def get_row(self) -> int:
        """get Row of Shelf"""
        return self.__shelf.get_rows()

    def get_column(self) -> int:
        """get Column of Shelf"""
        return self.__shelf.get_columns()
    
    # Set Functions
    def set_shelf_label(self) -> None:
        """Set Shelf Label in Widget"""
        self.shelf_label.setText("Shelf: " + str(self.get_shelf_label()))

    def set_max_weight_label(self) -> None:
        """Set Max Weight Label in Widget"""
        self.max_weight_label.setText("Max Weight: " + str(self.get_max_weight()))

    def set_dimensions_label(self) -> None:
        """Set Dimension Label in Widget"""
        self.dimensions_label.setText("Dimensions: " + str(self.get_length()) + " x " + str(self.get_width()) + " x " + str(self.get_height()))

    def set_total_slot_label(self) -> None:
        """Set Total Slot Label in Widget"""
        self.total_slot_label.setText("Total Slot: " + str(self.get_total_slot()))
        
    def set_row_label(self) -> None:
        """Set Row Label in Widget"""
        self.row_label.setText("Row: " + str(self.get_row()))

    def set_column_label(self) -> None:
        """Set Column Label in Widget"""
        self.column_label.setText("Column: " + str(self.get_column()))

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if(self.parent_widget.previous_shelf != None):
            self.parent_widget.previous_shelf.container.setStyleSheet("background-color: #F8F8FF; border-radius: 30;")
        self.parent_widget.current_shelf = self
        self.container.setStyleSheet("background-color: #F8F8FF; border-radius: 30; border: 3px solid #FDCB6E;")
        self.shelf_label.setStyleSheet("background-color: transparent;\n"
        "border: 0px")
        self.max_weight_label.setStyleSheet("background-color: transparent;\n"
        "border: 0px")
        self.dimensions_label.setStyleSheet("background-color: transparent;\n"
        "border: 0px")
        self.total_slot_label.setStyleSheet("background-color: transparent;\n"
        "border: 0px")
        self.row_label.setStyleSheet("background-color: transparent;\n"
        "border: 0px")
        self.column_label.setStyleSheet("background-color: transparent;\n"
        "border: 0px")
        self.parent_widget.previous_shelf = self.parent_widget.current_shelf