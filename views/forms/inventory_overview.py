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
        self.setStyleSheet(u"background-color: " + Theme.GHOST_WHITE + ";")

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
        inventory_overview_label.setStyleSheet("background-color: None; color: " + Theme.DARK_BLUE + ";")
        inventory_overview_label.setFont(Theme.POPPINS_BOLD_72)

        product_list_label = QLabel("Product List",self)
        product_list_label.setGeometry(655,271,782,52)
        product_list_label.setStyleSheet("background-color: None;")
        product_list_label.setAlignment(Qt.AlignCenter)
        product_list_label.setFont(Theme.POPPINS_BOLD_36)

        customer_selection_label = QLabel("Customer Selection", self)
        customer_selection_label.setGeometry(150,266,364,54)
        customer_selection_label.setStyleSheet("background-color: None; color: " + Theme.BLUE + "")
        customer_selection_label.setFont(Theme.POPPINS_BOLD_36)

        customer_name_label = QLabel("Customer's name", self)
        customer_name_label.setGeometry(134,349,198,25)
        customer_name_label.setStyleSheet("background-color: None; color: " + Theme.DARK_BLUE + ";")
        customer_name_label.setFont(Theme.POPPINS_BOLD_14)
        customer_name_label.setAlignment(Qt.AlignCenter)

        product_stocked_label = QLabel("Product stocked", self)
        product_stocked_label.setGeometry(348,349,175,25)
        product_stocked_label.setStyleSheet("background-color: None; color: " + Theme.DARK_BLUE + ";")
        product_stocked_label.setFont(Theme.POPPINS_BOLD_14)
        product_stocked_label.setAlignment(Qt.AlignCenter)

        base_widget_customer = QWidget(self)
        base_widget_customer.setGeometry(134,383,422,235)
        base_widget_customer.setStyleSheet("background-color: transparent;")
        
        self.scroll_area_customer = QScrollArea(base_widget_customer)
        self.scroll_area_customer.setGeometry(0,0,422,235)
        self.scroll_area_customer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_customer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_customer.setStyleSheet("background-color: transparent; border: none;")
        self.scroll_area_customer.setWidgetResizable(True)

        self.scroll_area_widget_customer = QWidget()
        self.scroll_area_widget_customer.setGeometry(0, 0, 422, 235)

        self.layout_customer = QVBoxLayout(self)
        self.layout_customer.setSpacing(24)

        self.layout_customer.setAlignment(Qt.AlignTop)
        self.scroll_area_widget_customer.setLayout(self.layout_customer)
        self.scroll_area_customer.setWidget(self.scroll_area_widget_customer)

        base_widget_product = QWidget(self)
        base_widget_product.setGeometry(655,371,782,566)
        base_widget_product.setStyleSheet("background-color: transparent;")
        
        self.scroll_area_product = QScrollArea(base_widget_product)
        self.scroll_area_product.setGeometry(0,0,422,235)
        self.scroll_area_product.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_product.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_product.setStyleSheet("background-color: transparent; border: none;")
        self.scroll_area_product.setWidgetResizable(True)

        self.scroll_area_widget_product = QWidget()
        self.scroll_area_widget_product.setGeometry(0, 0, 782, 566)

        self.layout_product = QVBoxLayout(self)
        self.layout_product.setSpacing(43)

        self.layout_product.setAlignment(Qt.AlignTop)
        self.scroll_area_widget_product.setLayout(self.layout_product)
        self.scroll_area_product.setWidget(self.scroll_area_widget_product)

    # Add Product Item to the product list
    def add_product_item(self):
        pass

    def clear_product_item(self):
        pass

    # Add Customer Item to the customer list
    def add_customer_item(self):
        pass

    def get_selected_customer_item(self):
        pass

    def clear_customer_item(self):
        pass