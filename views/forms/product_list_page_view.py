from data.data_classes import ProductItem
from views.forms.stack_page import StackPage
from PySide6.QtWidgets import QLabel
from views.forms.product_list import ProductList
from views.forms.product_input_form import ProductInputForm
from views.forms.location_page_view import LocationPageView
from views.items.product_list_card import ProductListCard
from views.theme import Theme


class ProductListPageView(StackPage):
    def __init__(self) -> None:
        super().__init__()
        self.current_product: ProductListCard = None

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
        # Location Page
        self.location_page = LocationPageView(self)
        self.hide_location_page()

    def set_event_search_input_change(self, function):
        """Set event when search input is changed"""
        self.product_form.set_event_search_input_change(function)

    def set_event_filters(self, function):
        """Set event when filter is selected"""
        self.product_form.set_event_filters(function)

    def set_enable_search_input(self, bool: bool):
        """Set enable stat for search line edit in form"""
        self.product_form.set_enable_search_input(bool)

    def set_enable_search_button(self, bool: bool):
        """Set enable stat for search button in form"""
        self.product_form.set_enable_search_button

    def set_current_location(self, current_location: int):
        """Set the current location of LocationPage (Input only location number)"""
        self.location_page.set_current_location(current_location)

    def set_input_with_card(self, card: ProductListCard):
        """Fill form with card"""
        if (self.product_form.get_current_modify() != None):
            self.product_form.set_input_with_card(card)

    def show_location_page(self):
        """Unhide LocationPage"""
        self.location_page.show()

    def hide_location_page(self):
        self.location_page.hide()

    def clear_form(self):
        self.product_form.clear_input()

    def set_event_search_bt(self, function):
        self.product_form.set_event_search_button(function)

    def get_search_input(self) -> str:
        return self.product_form.get_search_input()

    def add_card(self, product: ProductItem) -> ProductListCard:
        return self.product_list.add_card(product)

    def set_event_make_change_bt(self, function):
        self.product_form.set_event_make_change_button(function)

    def get_filter(self) -> str:
        return self.product_form.get_current_filter()

    def get_current_modify(self) -> str:
        return self.product_form.get_current_modify()

    def get_product_id(self) -> int:
        return self.product_form.get_product_id()

    def get_product_name(self) -> str:
        return self.product_form.get_product_name()

    def get_batch_id(self) -> int:
        return self.product_form.get_batch_id()

    def get_quantity(self) -> int:
        return self.product_form.get_quantity()

    def get_weight(self) -> int:
        return self.product_form.get_weight()

    def get_length(self) -> int:
        return self.product_form.get_length()

    def get_width(self) -> int:
        return self.product_form.get_width()

    def get_height(self) -> int:
        return self.product_form.get_height()

    def get_low_stock_quantity(self) -> int:
        return self.product_form.get_low_stock_quantity()

    def get_owner_id(self) -> int:
        return self.product_form.get_owner_id()

    def get_location(self) -> str:
        return self.product_form.get_location()

    def get_categoires(self) -> list[str]:
        return self.product_form.get_categoires()

    def change_location(self, new_location: str):
        self.product_form.change_location(new_location)
