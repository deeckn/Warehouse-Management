from data.data_classes import ProductItem
from views.forms.item_list import ItemList
from views.items.product_card import PRod


class ProductList(ItemList):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
