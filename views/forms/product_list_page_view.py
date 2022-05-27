from data.orm.schema import Product, ProductCategory, Shelf
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
        self.product_form.set_enable_search_button(bool)

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

    def add_card(self, product: Product) -> ProductListCard:
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

    def get_weight(self) -> float:
        return self.product_form.get_weight()

    def get_length(self) -> float:
        return self.product_form.get_length()

    def get_width(self) -> float:
        return self.product_form.get_width()

    def get_height(self) -> float:
        return self.product_form.get_height()

    def get_low_stock_quantity(self) -> int:
        return self.product_form.get_low_stock_quantity()

    def get_owner_id(self) -> int:
        return self.product_form.get_owner_id()

    def get_location(self) -> str:
        return self.product_form.get_location()

    def get_categoires(self, product_id: int) -> list[ProductCategory]:
        temp = []
        for category in self.product_form.get_categoires():
            temp.append(ProductCategory(product_id, category))
        return temp

    def change_location(self, new_location: str):
        self.product_form.change_location(new_location)

    def set_event_clear_button(self, function):
        self.product_form.set_event_clear_button(function)

    def set_event_choose_location(self, function):
        self.product_form.set_event_choose_location_button(function)

    def get_product_volume(self) -> float:
        return self.product_form.get_product_volume()

    def set_event_change_length(self, function):
        self.product_form.set_event_change_length(function)

    def set_event_change_width(self, function):
        self.product_form.set_event_change_width(function)

    def set_event_change_height(self, function):
        self.product_form.set_event_change_height(function)

    def check_dimension(self) -> bool:
        return self.product_form.check_dimension()

    def set_enable_choose_location(self, bool: bool):
        self.product_form.set_enable_choose_location_button(bool)

    def rerender_page(self, new_shelves: list[Shelf]):
        self.location_page.rerender_page(new_shelves)

    def set_event_back_button(self, function):
        self.location_page.set_event_back_bt(function)

    def set_event_change_shelf(self, function):
        self.location_page.set_event_change_shelf(function)

    def update_shelf(self):
        self.location_page.update_shelf()

    def update_table(self):
        self.location_page.update_table()

    def set_current_location(self, location: int):
        self.location_page.set_current_location(location)

    def get_current_location(self) -> str:
        return self.product_form.get_location()

    def get_selected(self) -> str:
        return self.location_page.get_current_location()

    def set_event_confirm_button(self, function):
        self.location_page.set_event_confirm_bt(function)

    def set_text_choose_location(self, text: str):
        self.product_form.set_text_choose_location(text)

    def set_current_shelf(self, label: str):
        self.location_page.set_current_shelf(label)

    def fill_occupied(self, occupied_slots: list[int]):
        self.location_page.fill_occupied(occupied_slots)

    def get_current_shelf(self) -> str:
        return self.location_page.get_current_shelf()

    def check_add_new(self) -> bool:
        return self.product_form.check_add_new()

    def get_current_filter(self) -> str:
        return self.product_form.get_current_filter()

    def clear_all_card(self):
        self.product_list.clear_all_card()

    def add_card(self, product: Product):
        self.product_list.add_card(product)

    def set_enable_make_change_button(self, boolean: bool):
        self.product_form.set_enable_make_change_button(boolean)

    def set_event_all_le(self, function):
        self.product_form.set_event_all_le(function)
