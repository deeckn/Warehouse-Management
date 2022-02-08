from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel, QWidget, QSpacerItem, QSizePolicy,
    QVBoxLayout, QHBoxLayout, QStackedWidget)

from views.items.sideMenuItem import SideMenuItem


class BaseView(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self, None)
        self.setStyleSheet("background-color: #F8F8FF")
        font = QFont("Poppins", 18)
        font.setBold(True)
        self.count_bt = 0
        self.current_bt = None
        self.bt_bar_spacer = QSpacerItem(
            0, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Side menu
        self.side_menu_widgets = QWidget()
        self.side_menu_widgets.setFixedSize(400, 1080)
        self.side_menu_widgets.setStyleSheet("background-color: #1A374D;")
        self.main_layout.addWidget(self.side_menu_widgets)

        self.side_menu_layout = QVBoxLayout(self.side_menu_widgets)
        self.side_menu_layout.setContentsMargins(0, 9, 0, 56)
        self.side_menu_layout.setSpacing(7)

        # Side menu -> User label
        self.user_label = QLabel()
        self.user_label.setFixedSize(400, 183)
        self.user_label.setAlignment(Qt.AlignCenter)
        self.user_label.setStyleSheet("color: #F8F8FF")
        self.user_label.setFont(font)
        self.side_menu_layout.addWidget(self.user_label)

        # Side bt bar widget
        self.side_menu_bt_bar = QWidget()
        self.side_menu_bt_bar.setFixedSize(400, 689)
        self.side_menu_layout.addWidget(self.side_menu_bt_bar)
        # Side bt bar layout
        self.side_menu_bt_bar_layout = QVBoxLayout(self.side_menu_bt_bar)

        self.logout_bt = SideMenuItem("out", "Log out")
        self.side_menu_layout.addWidget(self.logout_bt)

        # Stack widget
        self.stack = QStackedWidget()
        self.main_layout.addWidget(self.stack)

    # Getter
    def get_amount_bar_bt(self):
        return self.count_bt

    # Setter
    def set_user_label(self, username: str):
        self.user_label.setText(f"Logged in as {username}")

    def set_logout_bt_events(self, function):
        self.logout_bt.set_function(function)

    def set_function_bar_bt(self, index, function):
        amount = self.side_menu_bt_bar_layout.count()-1
        if index > amount or index < 0:
            print("Button Not exist")
        else:
            bt = self.side_menu_bt_bar_layout.itemAt(index).widget()
            bt.set_function(function)

    def set_up_admin(self):
        self.add_side_menu_bt("user", "ACCOUNT SETTINGS")
        self.add_side_menu_bt("fix", "SITE SETTINGS")
        self.add_side_menu_bt("files", "INVENTORY SETTINGS")
        self.add_side_menu_bt("docs", "VIEW REPORT")
        self.add_side_menu_bt("goto", "ENTER MAIN APP")
        self.click_side_bt(0)
        self.add_function_all_bt(self.unclick_all_side_bt, "insert")

    def set_up_main(self, user_type: str = "normal"):
        self.add_side_menu_bt("home", "HOME")
        self.add_side_menu_bt("user", "CUSTOMER LIST")
        self.add_side_menu_bt("product", "PRODUCT LIST")
        self.add_side_menu_bt("notification", "NOTIFICATIONS")
        if user_type == "admin":
            self.add_side_menu_bt("goto", "ENTER ADMIN APP")
        self.click_side_bt(0)
        self.add_function_all_bt(self.unclick_all_side_bt, "insert")

    def set_function_all_bt(self, function):
        for i in range(self.count_bt):
            bt = self.side_menu_bt_bar_layout.itemAt(i).widget()
            bt.set_function(function)

    # Add
    def add_side_menu_bt(self, bt_img: str, bt_text: str):
        new_bt = SideMenuItem(bt_img, bt_text)
        new_bt.set_click()
        self.count_bt += 1
        self.side_menu_bt_bar_layout.removeItem(self.bt_bar_spacer)
        self.side_menu_bt_bar_layout.addWidget(new_bt)
        self.side_menu_bt_bar_layout.addItem(self.bt_bar_spacer)

    def add_function_bt(self, index, function):
        amount = self.side_menu_bt_bar_layout.count()-1
        if index > amount or index < 0:
            print("Button Not exist")
        else:
            bt = self.side_menu_bt_bar_layout.itemAt(index).widget()
            bt.add_function(function)

    def add_function_all_bt(self, function, add_type: str = "append"):
        for i in range(self.count_bt):
            bt = self.side_menu_bt_bar_layout.itemAt(i).widget()
            bt.add_function(function, add_type)

    # UI
    def clear_side_menu(self):
        amount = self.count_bt
        for i in range(amount):
            bt = self.side_menu_bt_bar_layout.itemAt(0).widget()
            bt.close()
            self.side_menu_bt_bar_layout.removeWidget(bt)
        self.count_bt = 0

    def click_side_bt(self, index):
        bt = self.side_menu_bt_bar_layout.itemAt(index).widget()
        bt.click()

    def unclick_side_bt(self, index):
        bt = self.side_menu_bt_bar_layout.itemAt(index).widget()
        bt.unclick()

    def unclick_all_side_bt(self):
        for i in range(self.count_bt):
            bt = self.side_menu_bt_bar_layout.itemAt(i).widget()
            bt.unclick()
