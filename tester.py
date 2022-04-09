from data.app_dao import AppDAO, ProductDAO
from views.root_container import RootContainer
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    dao: ProductDAO = AppDAO.get_dao("product")
    product = dao.get_product(1)
    print(product)
    AppDAO.close_db()
