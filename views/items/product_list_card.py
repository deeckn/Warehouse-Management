from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from data.data_classes import ProductItem


class ProductListCard(QWidget):
    def __init__(self, product : ProductItem):
        QWidget.__init__(self, None)
