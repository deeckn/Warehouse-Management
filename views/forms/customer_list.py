from data.data_classes import Customer
from views.forms.item_list import ItemList
from views.items.customer_item import CustomerCard


class CustomerList(ItemList):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.qparent = parent

        # Testing purpose
        test_customer = Customer(
            1, "Dee Co Ltd", "0875548888", " DeeDee@GAD.com", True, "3 years", "01_01_2022", "16_01_2022", 300)
        self.add_card(test_customer)
        test_customer = Customer(
            1, "Kris Co Ltd", "012354235", " KKK@GAD.com", False, "5 years", "17_01_2022", "18_01_2022", 400)
        self.add_card(test_customer)

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
