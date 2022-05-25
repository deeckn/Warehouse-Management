from cgitb import reset
from PySide6.QtWidgets import QComboBox, QPushButton, QLabel, QWidget, QGridLayout
from data.orm.schema import Shelf
from views.theme import Theme
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QPixmap


class LocationPageView(QWidget):
    def __init__(self, parent=None) -> None:
        QWidget.__init__(self, parent)
        self.current_position = None
        self.avail_shelfs = None
        self.current_shelf = None

        bg = QLabel(self)
        bg.setStyleSheet(f"background-color:{Theme.GHOST_WHITE};")
        bg.setFixedSize(1520, 1080)

        self.shelf_select_cb = QComboBox(self)
        self.shelf_select_cb.setGeometry(QRect(610, 65, 300, 50))
        self.shelf_select_cb.setFont(Theme.POPPINS_BOLD_24)

        self.next_shelf_bt = QPushButton(parent=self)
        self.next_shelf_bt.move(1310, 65)
        self.next_shelf_bt.setIcon(QPixmap(f":/icons/next_btn.png"))
        self.next_shelf_bt.setIconSize(QSize(40, 40))
        self.next_shelf_bt.setStyleSheet("background-color: transparent;")

        self.back_shelf_bt = QPushButton(parent=self)
        self.back_shelf_bt.move(165, 65)
        self.back_shelf_bt.setIcon(QPixmap(f":/icons/back_btn.png"))
        self.back_shelf_bt.setIconSize(QSize(40, 40))
        self.back_shelf_bt.setStyleSheet("background-color: transparent;")

        self.back_bt = QPushButton(parent=self, text="Back")
        self.back_bt.setGeometry(160, 950, 111, 52)
        self.back_bt.setFont(Theme.POPPINS_BOLD_24)
        self.back_bt.setStyleSheet(
            f"background-color:{Theme.BLUE};color:white;border-radius:18px")

        self.confirm_bt = QPushButton(parent=self, text="CONFIRM")
        self.confirm_bt.setGeometry(1187, 950, 173, 53)
        self.confirm_bt.setFont(Theme.POPPINS_BOLD_24)
        self.confirm_bt.setStyleSheet(
            f"background-color:{Theme.YELLOW};color:white;border-radius:15px")

        table_bg = QLabel(self)
        table_bg.setGeometry(160, 210, 1200, 700)
        table_bg.setStyleSheet("background-color: white;")

        self.table_widget = QWidget(self)
        self.table_widget.setGeometry(160, 210, 1200, 700)
        self.grid = QGridLayout()
        self.table_widget.setLayout(self.grid)

        # UI
        ui_green_color = QLabel(self)
        ui_green_color.setGeometry(160, 159, 30, 30)
        ui_green_color.setStyleSheet(
            f"background-color: {Theme.GREEN}; border-radius:15px;")

        ui_green_indicator = QLabel(text="Available", parent=self)
        ui_green_indicator.setFont(Theme.POPPINS_REGULAR_18)
        ui_green_indicator.move(200, 159)

        ui_red_color = QLabel(self)
        ui_red_color.setGeometry(300, 159, 30, 30)
        ui_red_color.setStyleSheet(
            f"background-color: {Theme.RED}; border-radius:15px;")

        ui_red_indicator = QLabel(text="Occupied", parent=self)
        ui_red_indicator.setFont(Theme.POPPINS_REGULAR_18)
        ui_red_indicator.move(340, 159)

        ui_yellow_color = QLabel(self)
        ui_yellow_color.setGeometry(450, 159, 30, 30)
        ui_yellow_color.setStyleSheet(
            f"background-color: {Theme.YELLOW}; border-radius:15px;")

        ui_yellow_indicator = QLabel(text="Selected", parent=self)
        ui_yellow_indicator.setFont(Theme.POPPINS_REGULAR_18)
        ui_yellow_indicator.move(490, 159)

    def set_up(self, available_shelfs: list[Shelf]):
        self.avail_shelfs = available_shelfs

        for storage_shelf in available_shelfs:
            self.shelf_select_cb.addItem(storage_shelf.get_label())
        self.current_shelf = available_shelfs[0]
        self.update_table()

    def fill_occupied(self, occupied_slots: list[int]):
        buttons = self.table_widget.children()
        for i in occupied_slots:
            if buttons[i] != self.current_position:
                buttons[i].setStyleSheet(
                    f"background-color: {Theme.RED}; color: {Theme.GHOST_WHITE}; border:none;")
                buttons[i].setEnabled(False)

    def reset_table(self):
        self.current_position = None
        childs = self.table_widget.children()
        if len(childs) > 1:
            childs = childs[1:]
            for widget in childs:
                widget.setParent(None)
                widget.close()

    def reset_shelf(self):
        self.shelf_select_cb.clear()
        self.current_shelf = None

    def select_position(self):
        bt = self.sender()
        if(self.current_position == bt):
            self.clear_current_pos()
            self.current_position = None
            return

        if(self.current_position != None):
            self.clear_current_pos()
        self.current_position = bt
        bt.setStyleSheet(
            f"background-color: {Theme.YELLOW}; color: {Theme.GHOST_WHITE}; border:none;")

    def clear_current_pos(self):
        self.current_position.setStyleSheet(
            f"background-color: {Theme.GREEN}; color: {Theme.GHOST_WHITE}; border:none;")
        self.current_position.setEnabled(True)

    def set_event_back_bt(self, function):
        self.back_bt.clicked.connect(function)

    def set_event_confirm_bt(self, function):
        self.confirm_bt.clicked.connect(function)

    def get_current_location(self) -> str:
        return f"{self.current_shelf.get_label()}{self.current_position.text()}"

    def set_current_location(self, location: int):
        childs = self.table_widget.children()
        self.current_position = childs[location]
        self.current_position.setStyleSheet(
            f"background-color: {Theme.YELLOW}; color: {Theme.GHOST_WHITE}; border:none;")

    def get_current_shelf(self) -> int:
        return self.shelf_select_cb.currentIndex()

    def set_event_change_shelf(self, function):
        self.shelf_select_cb.currentIndexChanged.connect(function)

    def get_current_shelf(self) -> str:
        return self.shelf_select_cb.currentText()

    def update_shelf(self):
        self.current_shelf = self.avail_shelfs[self.shelf_select_cb.currentIndex(
        )]

    def update_table(self):
        self.reset_table()
        rows = self.current_shelf.get_rows()
        cols = self.current_shelf.get_columns()

        positions = [(i, j) for i in range(rows)
                     for j in range(cols)]
        datas = [f"{i:03d}" for i in range(1, rows*cols+1)]

        for position, data in zip(positions, datas):
            button = QPushButton(data)
            button.setFixedHeight((700//rows)-10)
            button.setStyleSheet(
                f"background-color: {Theme.GREEN}; color: {Theme.GHOST_WHITE}; border:none;")
            button.setFont(Theme.POPPINS_BOLD_16)
            button.clicked.connect(self.select_position)
            self.grid.addWidget(button, *position)
