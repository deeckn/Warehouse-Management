from data.orm.schema import Product
from views.forms.item_list import ItemList
from views.items.product_list_card import ProductListCard


class ProductList(ItemList):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.qparent = parent
        self.current_product: ProductListCard = None
        self.select_event = None
        self.unselect_event = None

    def add_card(self, product: Product):
        """Add new proudct card to the list"""
        card = ProductListCard(self.qparent, product)
        self.scroll_area_layout.addWidget(card)
