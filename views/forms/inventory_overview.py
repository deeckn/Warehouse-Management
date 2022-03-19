from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform,QIntValidator)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QPushButton, QScrollArea, QSizePolicy,
                               QVBoxLayout, QWidget,QScrollArea, )

from views.theme import Theme

class InventoryOverviewView(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.resize(1520, 1080)
        self.setStyleSheet(u"background-color: #F8F8FF;")

        container1 = QWidget(self)
        container1.setGeometry(100,219,464,762)
        container1.setStyleSheet("background-color: white;"
        "border-radius: 25;")

        container2 = QWidget(self)
        container2.setGeometry(628,219,835,792)
        container2.setStyleSheet("background-color: white;"
        "border-radius: 25;")

        inventory_overview_label = QLabel("Inventory Overview", self)
        inventory_overview_label.setGeometry(100,60,725,108)
        inventory_overview_label.setStyleSheet("background-color: None; color: #1A374D;")
        inventory_overview_label.setFont(Theme.POPPINS_BOLD_72)

        product_list_label = QLabel("Product List",self)
        product_list_label.setGeometry(655,271,782,52)
        product_list_label.setStyleSheet("background-color: None;")
        product_list_label.setAlignment(Qt.AlignCenter)
        product_list_label.setFont(Theme.POPPINS_BOLD_36)

        customer_selection_label = QLabel("Customer Selection", self)
        customer_selection_label.setGeometry(150,266,364,54)
        customer_selection_label.setStyleSheet("background-color: None; color: #406882")
        customer_selection_label.setFont(Theme.POPPINS_BOLD_36)

        customer_name_label = QLabel("Customer's name", self)
        customer_name_label.setGeometry(134,349,198,25)
        customer_name_label.setStyleSheet("background-color: None; color: #1A374D;")
        customer_name_label.setFont(Theme.POPPINS_BOLD_14)
        customer_name_label.setAlignment(Qt.AlignCenter)

        product_stocked_label = QLabel("Product stocked", self)
        product_stocked_label.setGeometry(348,349,175,25)
        product_stocked_label.setStyleSheet("background-color: None; color: #1A374D;")
        product_stocked_label.setFont(Theme.POPPINS_BOLD_14)
        product_stocked_label.setAlignment(Qt.AlignCenter)