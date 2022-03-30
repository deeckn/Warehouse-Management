from data.data_classes import ProductItem, Customer
from views.forms.item_list import ItemList
from views.items.product_list_card import ProductListCard


class ProductList(ItemList):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.qparent = parent
        self.current_product:ProductListCard = None
        self.select_event = None
        self.unselect_event = None

        # Testing purpose
        test_customer = Customer(
            1, "Dee Co Ltd", "0875548888", " DeeDee@GAD.com", True, "3 years", "01_01_2022", "16_01_2022", 300)
        test_product = ProductItem(1,"Test1",1,0,[],10,"",test_customer,[])
        self.add_card(test_product)

    def add_card(self, product: ProductItem):
        """Add new proudct card to the list"""
        card = ProductListCard(self.qparent, product)
        self.scroll_area_layout.addWidget(card)
