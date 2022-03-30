from views.forms.stack_page import StackPage
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from views.theme import Theme


class ProductListPageView(StackPage):
    def __init__(self) -> None:
        super().__init__()

        # title page name
        title = QLabel("Product List", self)
        title.setObjectName("page_name")
        title.setFont(Theme.POPPINS_BOLD_64)
        title.setGeometry(100, 60, 384, 96)
