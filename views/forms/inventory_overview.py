from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QLabel, QScrollArea, QVBoxLayout, QWidget, QScrollArea, QGridLayout)
from PySide6.QtCharts import (QChart, QChartView, QPieSeries, QPieSlice)

from data.orm.schema import Product
from views.items.customer_stock_item import CustomerStockItem
from views.items.product_card_inventory import ProductCardInventory
from views.theme import Theme
from PySide6 import QtCore


class InventoryOverviewView(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.resize(1520, 1080)
        self.setStyleSheet(u"background-color: " + Theme.GHOST_WHITE + ";")

        self.current_customer = None
        self.previous_customer = None

        container1 = QWidget(self)
        container1.setGeometry(100, 219, 464, 762)
        container1.setStyleSheet("background-color: white;"
                                 "border-radius: 25;")

        container2 = QWidget(self)
        container2.setGeometry(628, 219, 835, 792)
        container2.setStyleSheet("background-color: white;"
                                 "border-radius: 25;")

        inventory_overview_label = QLabel("Inventory Overview", self)
        inventory_overview_label.setGeometry(100, 60, 725, 108)
        inventory_overview_label.setStyleSheet(
            "background-color: None; color: " + Theme.DARK_BLUE + ";")
        inventory_overview_label.setFont(Theme.POPPINS_BOLD_72)

        product_list_label = QLabel("Product List", self)
        product_list_label.setGeometry(655, 271, 782, 52)
        product_list_label.setStyleSheet("background-color: None;")
        product_list_label.setAlignment(QtCore.Qt.AlignCenter)
        product_list_label.setFont(Theme.POPPINS_BOLD_36)

        customer_selection_label = QLabel("Customer Selection", self)
        customer_selection_label.setGeometry(150, 266, 364, 54)
        customer_selection_label.setStyleSheet(
            "background-color: None; color: " + Theme.BLUE + "")
        customer_selection_label.setFont(Theme.POPPINS_BOLD_36)

        customer_name_label = QLabel("Customer's name", self)
        customer_name_label.setGeometry(134, 349, 198, 25)
        customer_name_label.setStyleSheet(
            "background-color: None; color: " + Theme.DARK_BLUE + ";")
        customer_name_label.setFont(Theme.POPPINS_BOLD_14)
        customer_name_label.setAlignment(QtCore.Qt.AlignCenter)

        product_stocked_label = QLabel("Product stocked", self)
        product_stocked_label.setGeometry(348, 349, 175, 25)
        product_stocked_label.setStyleSheet(
            "background-color: None; color: " + Theme.DARK_BLUE + ";")
        product_stocked_label.setFont(Theme.POPPINS_BOLD_14)
        product_stocked_label.setAlignment(QtCore.Qt.AlignCenter)

        base_widget_customer = QWidget(self)
        base_widget_customer.setGeometry(134, 383, 416, 235)
        base_widget_customer.setStyleSheet("background-color: transparent;")

        self.scroll_area_customer = QScrollArea(base_widget_customer)
        self.scroll_area_customer.setGeometry(0, 0, 416, 235)
        self.scroll_area_customer.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area_customer.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area_customer.setStyleSheet(
            "background-color: transparent; border: none;")
        self.scroll_area_customer.setWidgetResizable(True)

        self.scroll_area_widget_customer = QWidget()
        self.scroll_area_widget_customer.setGeometry(0, 0, 416, 235)

        self.layout_customer = QVBoxLayout(self)
        self.layout_customer.setSpacing(24)

        self.layout_customer.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_area_widget_customer.setLayout(self.layout_customer)
        self.scroll_area_customer.setWidget(self.scroll_area_widget_customer)

        base_widget_product = QWidget(self)
        base_widget_product.setGeometry(655, 371, 782, 566)
        base_widget_product.setStyleSheet("background-color: transparent;")

        self.scroll_area_product = QScrollArea(base_widget_product)
        self.scroll_area_product.setGeometry(0, 0, 782, 566)
        self.scroll_area_product.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area_product.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area_product.setStyleSheet(
            "background-color: transparent; border: none;")
        self.scroll_area_product.setWidgetResizable(True)

        self.scroll_area_widget_product = QWidget()
        self.scroll_area_widget_product.setGeometry(0, 0, 782, 566)

        self.layout_product = QVBoxLayout(self)
        self.layout_product.setSpacing(30)

        self.layout_product.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_area_widget_product.setLayout(self.layout_product)
        self.scroll_area_product.setWidget(self.scroll_area_widget_product)

        self.pie_chart_widget = QWidget(self)
        self.pie_chart_widget.setGeometry(150, 602, 400, 400)
        self.pie_chart_widget.setStyleSheet("background-color: transparent;")
        self.series = None
        self.chart = QChart()
        self.chart.legend().hide()
        self.chartview = QChartView(self.chart)
        self.gridlayout = QGridLayout()
        self.pie_chart_widget.setLayout(self.gridlayout)

        self.customer_selected_function = None

    # Add Product Item to the product list
    def add_product_item(self, product: Product) -> None:
        card = ProductCardInventory(product)
        self.scroll_area_widget_product.layout().addWidget(card)

    def clear_product_item(self) -> None:
        for i in reversed(range(self.layout_product.count())):
            self.layout_product.itemAt(i).widget().deleteLater()

    # Add Customer Item to the customer list
    def add_customer_item(self, name: str, percent: float, id: int) -> None:
        card = CustomerStockItem(self, name, percent, id)
        self.scroll_area_widget_customer.layout().addWidget(card)

    def get_selected_customer_item(self) -> None:
        return self.current_customer

    def clear_customer_item(self) -> None:
        for i in reversed(range(self.layout_customer.count())):
            self.layout_customer.itemAt(i).widget().deleteLater()

    def set_customer_selected_function(self, function) -> None:
        self.customer_selected_function = function

    def draw_pie_chart_of_selected_customer(self, name: str, percent: float) -> None:
        if not self.gridlayout.isEmpty():
            self.series.clear()
            self.chart.removeAllSeries()
        self.series = QPieSeries()
        slice = QPieSlice(name, percent)
        slice.setBrush(QColor("#2ACAB0"))
        slice.setBorderColor("black")
        slice.setBorderWidth(5)
        self.series.append(slice)
        slice2 = QPieSlice("Blank", 100-percent)
        slice2.setBrush(QColor("#C4C4C4"))
        slice2.setBorderColor("black")
        slice2.setBorderWidth(5)
        self.series.append(slice2)
        self.chart.addSeries(self.series)
        self.gridlayout.addWidget(self.chartview)
