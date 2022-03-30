from views.forms.stack_page import StackPage
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from views.forms.product_list import ProductList
from views.forms.product_input_form import ProductInputForm
from views.items.product_list_card import ProductListCard
from views.theme import Theme


class ProductListPageView(StackPage):
    def __init__(self) -> None:
        super().__init__()
        self.current_product: ProductListCard = None

        self.select_event = None
        self.unselect_event = None

        self.product_form = ProductInputForm(self)
        self.product_form.move(100, 176)

        self.product_list = ProductList(self)
        self.product_list.move(640, 176)


        # title page name
        title = QLabel("Product List", self)
        title.setObjectName("page_name")
        title.setStyleSheet(f"color: {Theme.DARK_BLUE}")
        title.setFont(Theme.POPPINS_BOLD_64)
        title.setGeometry(100, 60, 384, 96)

    def set_select_event(self, event):
        self.select_event = event

    def set_unselect_event(self, event):
        self.unselect_event = event
