from tkinter import LEFT, RIGHT
from turtle import left
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform,QMouseEvent)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget, QGridLayout)



from views.theme import Theme

class CustomerStockItem(QWidget):
    def __init__(self, parent, name:str, percent:float):
        QWidget.__init__(self, None)
        self.container = QWidget(self)
        self.container.resize(380,60)
        self.container.setStyleSheet("background-color: " + Theme.GHOST_WHITE + "; border-radius: 15")

        self.name = name
        self.percent = percent

        self.parent_widget = parent
        self.grid_layout = QGridLayout()

        self.customer_label = QLabel(self)
        self.customer_label.setFont(Theme.POPPINS_BOLD_14)
        self.customer_label.setStyleSheet("color: " + Theme.DARK_BLUE)
        self.customer_label.resize(152, 35)
        self.customer_label.setText(name)

        self.product_stocked_label = QLabel(self)
        self.product_stocked_label.setFont(Theme.POPPINS_BOLD_14)
        self.product_stocked_label.setStyleSheet("color: " + Theme.DARK_BLUE)
        self.product_stocked_label.resize(143, 29)
        self.product_stocked_label.setText(str(percent) + "%")

        self.grid_layout.addWidget(self.customer_label, 0,0,1,1)
        self.grid_layout.addWidget(self.product_stocked_label, 0,1,1,1)
        self.grid_layout.setContentsMargins(23,21,0,19)

        self.setLayout(self.grid_layout)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        # Draw Pie Chart
        self.parent_widget.draw_pie_chart_of_selected_customer(self.name, self.percent)
        if(self.parent_widget.previous_customer != None):
            self.parent_widget.previous_customer.container.setStyleSheet("background-color: " + Theme.GHOST_WHITE + "; border-radius: 15;")
        self.parent_widget.current_customer = self
        self.container.setStyleSheet("background-color: #EAEAEA; border-radius: 15;")
        self.parent_widget.previous_customer = self.parent_widget.current_customer
        
