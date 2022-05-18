from views.forms.stack_page import StackPage
from views.theme import Theme
from views.forms.log_activity_view import LogWindowView
from views.forms.product_search_view import ProductSearchView
from data.orm.schema import Log, Product
from data.filter_options import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class HomePageView(StackPage):
    def __init__(self) -> None:
        super().__init__()

        self.set_styleSheet("stack_page_theme.qss")

        log_window_view_container = QWidget(self)
        log_window_view_container.setObjectName("container")
        log_window_view_container.setGeometry(940, 186, 500, 794)

        self.log_window_view = LogWindowView(log_window_view_container)

        product_search_container = QWidget(self)
        product_search_container.setObjectName("container")
        product_search_container.setGeometry(107, 186, 800, 794)

        self.product_search_view = ProductSearchView(product_search_container)

        # title page name
        title = QLabel("Home", self)
        title.setObjectName("page_name")
        title.setFont(Theme.POPPINS_BOLD_64)
        title.setGeometry(100, 60, 195, 96)

    def add_log(self, log: Log):
        self.log_window_view.add_log(log)

    def clear_logs(self):
        self.log_window_view.clear_logs()

    def set_search_bt_listener(self, event):
        self.product_search_view.set_search_bt_listener(event)

    def get_search_input(self) -> str:
        return self.product_search_view.get_search_input()

    def get_filter(self) -> FilterOption:
        filter = self.product_search_view.get_filter()
        match filter:
            case "id":
                return IdFilter()
            case "product_name":
                return NameFilter()
            case "customer_name":
                return CustomerFilter()

    def set_input_changed_listener(self, function):
        self.product_search_view.set_input_changed_listener(function)

    def setEnabled_search_bt(self, status: bool):
        self.product_search_view.setEnabled_search_bt(status)

    def add_product_card(self, product: Product):
        return self.product_search_view.add_product_card(product)

    def clear_product_cards(self):
        self.product_search_view.clear_product_cards()

    def get_card_list(self):
        return self.product_search_view.get_card_list()
