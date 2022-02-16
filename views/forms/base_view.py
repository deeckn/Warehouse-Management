from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel, QWidget, QSpacerItem, QSizePolicy,
    QVBoxLayout, QHBoxLayout, QStackedWidget)

from views.items.side_menu_item import SideMenuItem


class BaseView(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self, None)
        self.setStyleSheet("background-color: #F8F8FF")
        font = QFont("Poppins", 24)
        font.setBold(True)
        self.current_bt = None
        self.spacer = QSpacerItem(
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

        self.logout_bt =SideMenuItem("out", "Log out")
        self.logout_bt.add_function(self.logout_bt.unclick)
        self.side_menu_layout.addWidget(self.logout_bt)

        # Stack widget
        self.stack = QStackedWidget()
        self.main_layout.addWidget(self.stack)

        self.set_user_label("USER00") # Testing purpose


    # Setter
    def set_current_bt(self, bt:SideMenuItem):
        self.current_bt = bt

    def set_user_label(self, username: str):
        self.user_label.setText(f"Logged in as {username}")

    def set_logout_bt_listener(self, function):
        self.logout_bt.set_function(function)



    def set_function_all_bt(self, function):
        for i in range(self.count_bt):
            bt = self.side_menu_bt_bar_layout.itemAt(i).widget()
            bt.set_function(function)

    # Add
    def add_side_menu_bt(self, new_bt:SideMenuItem) -> None:
        self.side_menu_bt_bar_layout.addWidget(new_bt)
       

    def add_function_all_bt(self, function, add_type: str = "append"):
        for i in range(self.count_bt):
            bt = self.side_menu_bt_bar_layout.itemAt(i).widget()
            bt.add_function(function, add_type)

    def add_spacer_side_menu(self):
        self.side_menu_bt_bar_layout.addItem(self.spacer)

    def add_page(self, new_page: QWidget):
        self.stack.addWidget(new_page)

    def unclick_current_bt(self):
        self.current_bt.unclick()

    def reset(self):
        self.unclick_current_bt()
        self.stack.setCurrentIndex(0)