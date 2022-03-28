from views.forms.stack_page import StackPage
from views.theme import Theme
from views.forms.log_activity_view import LogWindowView
from views.forms.product_search_view import ProductSearchView
from views.items.product_card_home_item import ProductCardHomeItem
from data.data_classes import Customer, ProductItem
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import copy


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

        self.product_search_view = ProductSearchView(
            self, product_search_container)

        # title page name
        title = QLabel("Home", self)
        title.setObjectName("page_name")
        title.setFont(Theme.POPPINS_BOLD_64)
        title.setGeometry(100, 60, 195, 96)

    # Example for controller
    # def set_add_event(self):
    #     cards = self.product_search_view.get_card_list()
    #     for card in cards:
    #         def generate(temp):
    #             def test():
    #                 print(temp.item.get_id())
    #             return test
    #         card.add_bt.clicked.connect(generate(card))
