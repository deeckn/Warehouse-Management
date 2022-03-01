from views.forms.stack_page import StackPage  # For real test
from views.theme import Theme
from views.forms.log_activity_view import LogWindowView
from views.forms.product_search_view import ProductSearchView
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class HomeView(StackPage):
    def __init__(self) -> None:
        super().__init__()
        self.set_styleSheet("home_view_theme.qss")
        self.current_filter = "ID"

        log_window_view_container = QWidget(self)
        log_window_view_container.setObjectName("page_widget")
        log_window_view_container.setGeometry(940, 186, 500, 794)

        self.log_window_view = LogWindowView(log_window_view_container)

        product_search_container = QWidget(self)
        product_search_container.setObjectName("page_widget")
        product_search_container.setGeometry(107, 186, 800, 794)

        self.product_search_view = ProductSearchView(product_search_container)

        # Header
        header = QLabel("Home", self)
        header.setObjectName("h1")
        header.setFont(Theme.POPPINS_BOLD_64)
        header.setGeometry(100, 60, 195, 96)
