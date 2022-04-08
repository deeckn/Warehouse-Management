from data.data_classes import Customer
from views.forms.item_list import ItemList
from views.items.customer_item import CustomerCard


class CustomerList(ItemList):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.qparent = parent

    def add_card(self, customer: Customer):
        """Add new customer card to the list"""
        card = CustomerCard(self.qparent, customer)
        self.scroll_area_layout.addWidget(card)

    def clear_all_card(self):
        childs = self.scroll_area_widget.children()
        if len(childs) > 1:
            childs = childs[1:]
            for widget in childs:
                widget.close()
