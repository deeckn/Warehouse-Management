
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QFont, QIntValidator
from PySide6.QtWidgets import (
    QFrame, QLabel, QLineEdit, QPushButton, QScrollArea, QVBoxLayout, QWidget, QScrollArea)

from views.items.shelf_item import ShelfItem
from data.orm.schema import Shelf
from views.theme import Theme


class SiteSettingView(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setFixedSize(1520, 1080)

        bg = QLabel(self)
        bg.setGeometry(0, 0, 1520, 1080)
        bg.setStyleSheet("background-color: #F8F8FF;")

        self.current_shelf: ShelfItem = None
        self.previous_shelf = None

        self.select_event = None
        self.unselect_event = None

        # font
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPixelSize(72)
        font.setBold(True)

        site_setting_label = QLabel("Site Settings", self)
        site_setting_label.setGeometry(100, 50, 461, 108)
        site_setting_label.setFont(font)
        site_setting_label.setStyleSheet(u"color: #1A374D;")

        space_1 = QLabel(self)
        space_1.setGeometry(100, 219, 500, 794)
        space_1.setStyleSheet(u"background-color: #FFFFFF;\n"
                              "border-radius: 25;")

        space_2 = QLabel(self)
        space_2.setGeometry(640, 219, 800, 794)
        space_2.setStyleSheet(u"background-color: white;\n"
                              "border-radius: 25;")

        font.setFamilies([u"Poppins"])
        font.setPixelSize(18)
        font.setBold(True)

        shelf_label_seach_label = QLabel("Shelf Label", self)
        shelf_label_seach_label.setGeometry(150, 296, 131, 28)
        shelf_label_seach_label.setFont(font)
        shelf_label_seach_label.setStyleSheet(u"color: #406882;\n"
                                              "background-color: transparent;")

        max_weight_label = QLabel("Max Weight (Kg)", self)
        max_weight_label.setGeometry(311, 488, 201, 28)
        max_weight_label.setFont(font)
        max_weight_label.setStyleSheet(u"background-color: transparent;\n"
                                       "color: #406882;")

        shelf_label_information_label = QLabel("Shelf Label", self)
        shelf_label_information_label.setGeometry(151, 488, 141, 28)
        shelf_label_information_label.setFont(font)
        shelf_label_information_label.setStyleSheet(u"background-color: transparent;\n"
                                                    "color: #406882;")

        per_slot_max_weight_label = QLabel("per slot", self)
        per_slot_max_weight_label.setGeometry(476, 523, 69, 28)
        per_slot_max_weight_label.setFont(font)
        per_slot_max_weight_label.setStyleSheet(u"color: #406882; \n"
                                                "background-color: transparent;")

        dimension_label = QLabel("Dimensions", self)
        dimension_label.setGeometry(151, 568, 110, 28)
        dimension_label.setFont(font)
        dimension_label.setStyleSheet(u"background-color: transparent; \n"
                                      "color: #406882;")

        length_label = QLabel("Length (m)", self)
        length_label.setGeometry(169, 607, 104, 28)
        length_label.setFont(font)
        length_label.setStyleSheet(u"background-color: transparent; \n"
                                   "color: #406882; ")

        width_label = QLabel("Width (m)", self)
        width_label.setGeometry(169, 656, 108, 28)
        width_label.setFont(font)
        width_label.setStyleSheet(u"background-color: transparent;\n"
                                  "color: #406882;")

        height_label = QLabel("Height (m)", self)
        height_label.setGeometry(169, 705, 102, 28)
        height_label.setFont(font)
        height_label.setStyleSheet(u"background-color: transparent; \n"
                                   "color: #406882;")

        slot_label = QLabel("Slot", self)
        slot_label.setGeometry(151, 751, 137, 28)
        slot_label.setFont(font)
        slot_label.setStyleSheet(u"background-color: transparent; \n"
                                 "color: #406882;")

        weight_per_slot_label = QLabel("per slot", self)
        weight_per_slot_label.setGeometry(462, 657, 69, 28)
        weight_per_slot_label.setFont(font)
        weight_per_slot_label.setStyleSheet(u"background-color: transparent;\n"
                                            "color: #406882;")

        row_label = QLabel("Row", self)
        row_label.setGeometry(QRect(170, 793, 39, 28))
        row_label.setFont(font)
        row_label.setStyleSheet(u"background-color: transparent;\n"
                                "color: #406882;")

        column_label = QLabel("Column", self)
        column_label.setGeometry(351, 793, 75, 28)
        column_label.setFont(font)
        column_label.setStyleSheet(u"background-color: transparent;\n"
                                   "color: #406882;")

        self.total_label = QLabel(self)
        self.total_label.setGeometry(169, 848, 200, 27)
        self.total_label.setFont(font)
        self.total_label.setStyleSheet(u"background-color: transparent;\n"
                                       "color: #406882;")

        font.setFamilies([u"Poppins"])
        font.setPixelSize(18)
        font.setBold(False)

        self.search_button = QPushButton("Search", self)
        self.search_button.setGeometry(374, 387, 176, 41)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet(u"background-color: #FDCB6E;\n "
                                         "border-radius: 10;\n"
                                         "color: white")

        self.search_lineEdit = QLineEdit(self)
        self.search_lineEdit.setGeometry(150, 324, 400, 42)
        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setStyleSheet(u"border-radius: 0;\n"
                                           "background-color: #DDDDDD;"
                                           "padding-left: 14;\n"
                                           "padding-top: 5;")

        self.shelf_label_lineEdit = QLineEdit(self)
        self.shelf_label_lineEdit.setGeometry(151, 516, 150, 42)
        self.shelf_label_lineEdit.setFont(font)
        self.shelf_label_lineEdit.setStyleSheet(u"border-radius: 0;\n"
                                                "background-color: #DDDDDD;"
                                                "padding-left: 14;\n"
                                                "padding-top: 5;")

        self.max_weight_lineEdit = QLineEdit(self)
        self.max_weight_lineEdit.setGeometry(311, 516, 150, 42)
        self.max_weight_lineEdit.setValidator(QIntValidator(0, 9999999))
        self.max_weight_lineEdit.setFont(font)
        self.max_weight_lineEdit.setStyleSheet(u"border-radius: 0; \n"
                                               "background-color: #DDDDDD;"
                                               "padding-left: 14;\n"
                                               "padding-top: 5;")

        self.length_lineEdit = QLineEdit(self)
        self.length_lineEdit.setGeometry(307, 601, 125, 42)
        self.length_lineEdit.setFont(font)
        self.length_lineEdit.setValidator(QIntValidator(0, 9999999))
        self.length_lineEdit.setStyleSheet(u"border-radius: 0;\n"
                                           "background-color: #DDDDDD;"
                                           "padding-left: 14;\n"
                                           "padding-top: 5;")

        self.width_lineEdit = QLineEdit(self)
        self.width_lineEdit.setGeometry(307, 650, 125, 42)
        self.width_lineEdit.setFont(font)
        self.width_lineEdit.setValidator(QIntValidator(0, 9999999))
        self.width_lineEdit.setStyleSheet(u"border-radius: 0;\n"
                                          "background-color: #DDDDDD;"
                                          "padding-left: 14;\n"
                                          "padding-top: 5;")

        self.height_lineEdit = QLineEdit(self)
        self.height_lineEdit.setGeometry(307, 699, 125, 42)
        self.height_lineEdit.setFont(font)
        self.height_lineEdit.setValidator(QIntValidator(0, 9999999))
        self.height_lineEdit.setStyleSheet(u"border-radius: 0; \n"
                                           "background-color: #DDDDDD;"
                                           "padding-left: 14;\n"
                                           "padding-top: 5;")

        self.row_lineEdit = QLineEdit(self)
        self.row_lineEdit.setGeometry(219, 786, 120, 42)
        self.row_lineEdit.setFont(font)
        self.row_lineEdit.setValidator(QIntValidator(0, 9999999))
        self.row_lineEdit.setStyleSheet(u"border-radius: 0; \n"
                                        "background-color: #DDDDDD;"
                                        "padding-left: 14; \n"
                                        "padding-top: 5;")

        self.column_lineEdit = QLineEdit(self)
        self.column_lineEdit.setGeometry(434, 786, 120, 42)
        self.column_lineEdit.setFont(font)
        self.column_lineEdit.setValidator(QIntValidator(0, 9999999))
        self.column_lineEdit.setStyleSheet(u"border-radius: 0; \n"
                                           "background-color: #DDDDDD;"
                                           "padding-left: 14; \n"
                                           "padding-top: 5;")

        font.setFamilies([u"Poppins"])
        font.setPixelSize(24)
        font.setBold(True)

        self.save_button = QPushButton("SAVE", self)
        self.save_button.setGeometry(267, 948, 166, 65)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet(u"background-color: #FDCB6E;\n"
                                       "color: white;\n"
                                       "border-radius: 0;")

        self.delete_button = QPushButton("DELETE", self)
        self.delete_button.setGeometry(100, 948, 167, 65)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet(u"background-color: #FF7474;\n "
                                         "color: white; \n"
                                         "border-bottom-left-radius: 25px;")

        self.add_button = QPushButton("ADD", self)
        self.add_button.setGeometry(433, 948, 167, 65)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet(u"background-color: #2ACAB0;\n"
                                      "color: white;\n"
                                      "border-bottom-right-radius: 25;")

        font.setFamilies([u"Poppins"])
        font.setPixelSize(14)
        font.setBold(False)

        search_label = QLabel("Search", self)
        search_label.setGeometry(325, 264, 50, 22)
        search_label.setFont(font)
        search_label.setStyleSheet(u"background-color: transparent;")

        information_label = QLabel("Information", self)
        information_label.setGeometry(310, 460, 82, 22)
        information_label.setFont(font)
        information_label.setStyleSheet(u"background-color: transparent;")

        line = QFrame(self)
        line.setGeometry(151, 471, 145, 1)
        line.setStyleSheet(u"background-color:black;")
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        line_2 = QFrame(self)
        line_2.setGeometry(406, 471, 145, 1)
        line_2.setStyleSheet(u"background-color: black;")
        line_2.setFrameShape(QFrame.HLine)
        line_2.setFrameShadow(QFrame.Sunken)

        line_3 = QFrame(self)
        line_3.setGeometry(150, 275, 170, 1)
        line_3.setStyleSheet(u"background-color: black;")
        line_3.setFrameShape(QFrame.HLine)
        line_3.setFrameShadow(QFrame.Sunken)

        line_4 = QFrame(self)
        line_4.setGeometry(380, 275, 170, 1)
        line_4.setStyleSheet(u"background-color: black;")
        line_4.setFrameShape(QFrame.HLine)
        line_4.setFrameShadow(QFrame.Sunken)

        base_widget = QWidget(self)
        base_widget.setGeometry(694, 273, 700, 686)
        base_widget.setStyleSheet("background-color: transparent;")

        self.scroll_area = QScrollArea(base_widget)
        self.scroll_area.setGeometry(0, 0, 700, 686)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setStyleSheet(
            "background-color: transparent; border: none;")
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area_widget = QWidget()
        self.scroll_area_widget.setGeometry(0, 0, 700, 686)

        self.layout_ = QVBoxLayout(self)
        self.layout_.setSpacing(15)

        self.layout_.setAlignment(Qt.AlignTop)
        self.scroll_area_widget.setLayout(self.layout_)
        self.scroll_area.setWidget(self.scroll_area_widget)

    # Get data from current selected shelf
    def get_shelf_current_shelf_item(self) -> str:
        return self.current_shelf.get_shelf()

    def get_max_weight_current_shelf_item(self) -> str:
        return self.current_shelf.get_max_weight()

    def get_length_current_shelf_item(self) -> str:
        return self.current_shelf.get_length()

    def get_width_current_shelf_item(self) -> str:
        return self.current_shelf.get_width()

    def get_height_current_shelf_item(self) -> str:
        return self.current_shelf.get_height()

    def get_row_current_shelf_item(self) -> str:
        return self.current_shelf.get_row()

    def get_column_current_shelf_item(self) -> str:
        return self.current_shelf.get_column()

    # Set LineEdits

    def set_shelf_LineEdit(self, text: str) -> None:
        self.shelf_label_lineEdit.setText(text)

    def set_max_weight_LineEdit(self, text: str) -> None:
        self.max_weight_lineEdit.setText(text)

    def set_length_LineEdit(self, text: str) -> None:
        self.length_lineEdit.setText(text)

    def set_width_LineEdit(self, text: str) -> None:
        self.width_lineEdit.setText(text)

    def set_height_LineEdit(self, text: str) -> None:
        self.height_lineEdit.setText(text)

    def set_row_LineEdit(self, text: str) -> None:
        self.row_lineEdit.setText(text)

    def set_column_LineEdit(self, text: str) -> None:
        self.column_lineEdit.setText(text)

    # Set Total Labels
    def set_total_label(self, text: str) -> None:
        self.total_label.setText("Total : " + text)

    # Get LineEdits
    def get_search_LineEdit(self) -> str:
        return self.search_lineEdit.text()

    def get_shelf_LineEdit(self) -> str:
        return self.shelf_label_lineEdit.text()

    def get_max_weight_LineEdit(self) -> str:
        return self.max_weight_lineEdit.text()

    def get_length_LineEdit(self) -> str:
        return self.length_lineEdit.text()

    def get_width_LineEdit(self) -> str:
        return self.width_lineEdit.text()

    def get_height_LineEdit(self) -> str:
        return self.height_lineEdit.text()

    def get_row_LineEdit(self) -> str:
        return self.row_lineEdit.text()

    def get_column_LineEdit(self) -> str:
        return self.column_lineEdit.text()

    # Set Buttons Listener
    def set_delete_button_listener(self, function) -> None:
        self.delete_button.clicked.connect(function)

    def set_save_button_listener(self, function) -> None:
        self.save_button.clicked.connect(function)

    def set_add_button_listener(self, function) -> None:
        self.add_button.clicked.connect(function)

    def set_search_listener(self, function) -> None:
        self.search_button.clicked.connect(function)

    # set Event

    def set_select_event(self, event):
        self.select_event = event

    def set_unselect_event(self, event):
        self.unselect_event = event

    # Set Enable Buttons
    def set_add_button_enabled(self, boolean):
        style = f"background-color:  {Theme.GREEN}; color: white; border-bottom-right-radius: 23px;" if boolean else f"background-color:  {Theme.LIGHTER_DARK_GREEN}; color: {Theme.DARK_WHITE}; border-bottom-right-radius: 23px;"
        self.add_button.setStyleSheet(style)
        self.add_button.setEnabled(boolean)

    def set_delete_button_enabled(self, boolean):
        style = f"background-color: {Theme.RED}; color: white;border-bottom-left-radius: 23px;" if boolean else f"background-color: {Theme.DARK_RED}; color: {Theme.DARK_WHITE}; border-bottom-left-radius: 23px;"
        self.delete_button.setStyleSheet(style)
        self.delete_button.setEnabled(boolean)

    def set_save_button_enabled(self, boolean):
        style = f"background-color:  {Theme.YELLOW}; color: white; border-radius: none;" if boolean else f"background-color: {Theme.DARK_YELLOW}; color: {Theme.DARK_WHITE}; border: none;"
        self.save_button.setStyleSheet(style)
        self.save_button.setEnabled(boolean)

    # Set LineEdit from Shelf
    def set_lineEdit_from_shelf(self, shelf: Shelf):
        self.shelf_label_lineEdit.setText(shelf.get_label())
        self.max_weight_lineEdit.setText(str(shelf.get_max_weight()))
        self.length_lineEdit.setText(str(shelf.get_length()))
        self.width_lineEdit.setText(str(shelf.get_width()))
        self.height_lineEdit.setText(str(shelf.get_height()))
        self.row_lineEdit.setText(str(shelf.get_rows()))
        self.column_lineEdit.setText(str(shelf.get_columns()))

    # Employee Account List
    def add_shelf(self, shelf: Shelf):
        """Inserts a new ShelfItem object to the list"""
        card = ShelfItem(self, shelf)
        self.scroll_area_widget.layout().addWidget(card)
        # self.layout_.addWidget(card)

    def get_selected_shelf(self) -> Shelf:
        """Returns the selected ShelfItem object on the UI"""
        return self.current_shelf.get_current_shelf()

    def clear_shelf_list(self):
        """Clears the list represented in the scrollarea"""
        for i in reversed(range(self.layout_.count())):
            self.layout_.itemAt(i).widget().setParent(None)

    # Reset Shelves List and LineEdit
    def reset_site_setting_view(self):
        """Clears all of View components"""
        self.clear_shelf_list()
        self.current_shelf = None

    def reset_input(self):
        self.search_lineEdit.setText("")
        self.shelf_label_lineEdit.setText("")
        self.max_weight_lineEdit.setText("")
        self.length_lineEdit.setText("")
        self.width_lineEdit.setText("")
        self.height_lineEdit.setText("")
        self.row_lineEdit.setText("")
        self.column_lineEdit.setText("")

    # Check Boolean
    def is_no_empty_lineEdit(self):
        """Check if form is valid for add submission"""
        return not \
            (
                self.shelf_label_lineEdit.text() == "" or
                self.max_weight_lineEdit.text() == "" or
                self.length_lineEdit.text() == "" or
                self.width_lineEdit.text() == "" or
                self.height_lineEdit.text() == "" or
                self.row_lineEdit.text() == "" or
                self.column_lineEdit.text() == ""
            )

    # Check LineEdit Change
    def set_input_on_change_listener(self, function):
        self.shelf_label_lineEdit.textChanged.connect(function)
        self.max_weight_lineEdit.textChanged.connect(function)
        self.length_lineEdit.textChanged.connect(function)
        self.width_lineEdit.textChanged.connect(function)
        self.height_lineEdit.textChanged.connect(function)
        self.row_lineEdit.textChanged.connect(function)
        self.column_lineEdit.textChanged.connect(function)

    def is_current_edited(self):
        """Check if the current selected customer is edited"""
        label = self.shelf_label_lineEdit.text()
        max_weight = self.max_weight_lineEdit.text()
        length = self.length_lineEdit.text()
        width = self.width_lineEdit.text()
        height = self.height_lineEdit.text()
        row = self.row_lineEdit.text()
        column = self.column_lineEdit.text()

        current_shelf = self.current_shelf
        if label != current_shelf.get_shelf_label:
            return True

        if max_weight != str(current_shelf.get_max_weight()):
            return True

        if length != str(current_shelf.get_length()):
            return True

        if width != str(current_shelf.get_width()):
            return True

        if height != str(current_shelf.get_height()):
            return True

        if row != str(current_shelf.get_row()):
            return True

        if column != str(current_shelf.get_column()):
            return True

        return False

    def is_search_lineEdit_filled(self):
        return self.search_lineEdit != ""

    def is_card_selected(self):
        return self.current_shelf != None
