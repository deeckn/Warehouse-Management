from itertools import product
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from data.filter_options import *
from data.orm.schema import *
from views.theme import Theme
from views.items.product_list_card import ProductListCard


class ProductInputForm(QWidget):
    def __init__(self, parent=None) -> None:
        QWidget.__init__(self, parent)
        self.current_filter = None
        self.current_modify = None

        bg = QLabel(self)
        bg.setGeometry(0, 0, 500, 794)
        bg.setStyleSheet(f"background-color: white; border-radius: 25px;")

        head_style = f"background-color: transparent; color:{Theme.BLUE};"
        input_form_style = f"background-color: {Theme.GREY}; color:black; border-radius: 0px;"
        line_break_top_style = "border-top: 1px solid black; background-color: none;"
        text_over_line_style = "color:black; background-color:white;"
        radio_bt_style = f"color: {Theme.BLUE};"

        # Input line edit
        self.search_product_le = QLineEdit(self)
        self.search_product_le.setFont(Theme.POPPINS_REGULAR_18)
        self.search_product_le.setGeometry(50, 66, 290, 40)
        self.search_product_le.setStyleSheet(
            f"background-color: {Theme.GREY}; color:black; border-radius: 0px;")

        # Input radio button
        # Search by
        option = QWidget(self)
        option.setGeometry(50, 146, 389, 22)
        option_layout = QHBoxLayout(option)
        option_layout.setContentsMargins(0, 0, 0, 0)

        self.client_name_search_option = QRadioButton("Client name")
        self.client_name_search_option.setFixedWidth(116)

        self.product_id_search_option = QRadioButton("Product ID")
        self.product_id_search_option.setFixedWidth(102)

        self.product_name_search_option = QRadioButton("Product Name")
        self.product_name_search_option.setFixedWidth(131)

        for radioBt in (self.client_name_search_option, self.product_id_search_option, self.product_name_search_option):
            radioBt.setStyleSheet(radio_bt_style)
            radioBt.setFont(Theme.POPPINS_REGULAR_14)
            option_layout.addWidget(radioBt)
            radioBt.clicked.connect(self.update_current_filter)

        # Yellow bt
        self.search_bt = QPushButton(self, text="Search")
        self.search_bt.setFont(Theme.POPPINS_REGULAR_18)
        self.search_bt.setGeometry(350, 66, 100, 40)

        self.product_id_le = QLineEdit(self)
        self.product_id_le.setFont(Theme.POPPINS_REGULAR_18)
        self.product_id_le.setGeometry(50, 271, 187, 40)
        self.product_id_le.setValidator(QIntValidator(0, 999))

        self.product_name_le = QLineEdit(self)
        self.product_name_le.setFont(Theme.POPPINS_REGULAR_18)
        self.product_name_le.setGeometry(263, 271, 187, 40)

        self.batch_id_le = QLineEdit(self)
        self.batch_id_le.setFont(Theme.POPPINS_REGULAR_18)
        self.batch_id_le.setGeometry(50, 348, 90, 40)
        self.batch_id_le.setAlignment(Qt.AlignCenter)
        self.batch_id_le.setValidator(QIntValidator(0, 999))

        self.quantity_le = QLineEdit(self)
        self.quantity_le.setFont(Theme.POPPINS_REGULAR_18)
        self.quantity_le.setGeometry(148, 348, 90, 40)
        self.quantity_le.setAlignment(Qt.AlignCenter)
        self.quantity_le.setValidator(QIntValidator(0, 999))

        self.choose_location_bt = QPushButton(self, text="Choose Location")
        self.choose_location_bt.setFont(Theme.POPPINS_BOLD_18)
        self.choose_location_bt.setGeometry(263, 348, 187, 40)

        self.weight_le = QLineEdit(self)
        self.weight_le.setFont(Theme.POPPINS_REGULAR_18)
        self.weight_le.setGeometry(50, 425, 187, 40)
        self.weight_le.setValidator(QIntValidator(0, 9999999))

        self.length_le = QLineEdit(self)
        self.length_le.setFont(Theme.POPPINS_REGULAR_18)
        self.length_le.setGeometry(265, 425, 60, 40)
        self.length_le.setAlignment(Qt.AlignCenter)
        self.length_le.setValidator(QIntValidator(0, 999))

        self.width_le = QLineEdit(self)
        self.width_le.setFont(Theme.POPPINS_REGULAR_18)
        self.width_le.setGeometry(328, 425, 60, 40)
        self.width_le.setAlignment(Qt.AlignCenter)
        self.width_le.setValidator(QIntValidator(0, 999))

        self.height_le = QLineEdit(self)
        self.height_le.setFont(Theme.POPPINS_REGULAR_18)
        self.height_le.setGeometry(390, 425, 60, 40)
        self.height_le.setAlignment(Qt.AlignCenter)
        self.height_le.setValidator(QIntValidator(0, 999))

        self.low_stock_quantity_le = QLineEdit(self)
        self.low_stock_quantity_le.setFont(Theme.POPPINS_REGULAR_18)
        self.low_stock_quantity_le.setGeometry(50, 502, 187, 40)
        self.low_stock_quantity_le.setValidator(QIntValidator(0, 99999999))

        self.owner_id_le = QLineEdit(self)
        self.owner_id_le.setFont(Theme.POPPINS_REGULAR_18)
        self.owner_id_le.setGeometry(266, 502, 187, 40)
        self.owner_id_le.setStyleSheet(input_form_style)
        self.owner_id_le.setValidator(QIntValidator(0, 99999999))

        # Input radio button
        # Modify
        option = QWidget(self)
        option.setGeometry(50, 213, 369, 22)
        option_layout = QHBoxLayout(option)
        option_layout.setContentsMargins(0, 0, 0, 0)

        self.add_new_option = QRadioButton("Add New")
        self.add_new_option.setFixedWidth(93)

        self.add_batch = QRadioButton("Add Batch")
        self.add_batch.setFixedWidth(104)

        self.edit_option = QRadioButton("Edit")
        self.edit_option.setFixedWidth(56)

        self.delete_option = QRadioButton("Delete")
        self.delete_option.setFixedWidth(75)

        for option in (self.add_new_option, self.add_batch, self.edit_option, self.delete_option):
            option.setStyleSheet(radio_bt_style)
            option.setFont(Theme.POPPINS_REGULAR_14)
            option_layout.addWidget(option)
            option.clicked.connect(self.update_current_modifier)

        # Category
        category_box = QWidget(self)
        category_box.setGeometry(71, 588, 360, 110)
        category_layout = QHBoxLayout()
        category_box.setLayout(category_layout)

        # category 1
        category_parts = QVBoxLayout()
        self.electrical_option = QRadioButton("Electrical")
        self.fashion_option = QRadioButton("Fashion")
        self.utensils_option = QRadioButton("Utensils")
        self.furniture_option = QRadioButton("Furniture")

        for option in (self.electrical_option, self.fashion_option, self.utensils_option, self.furniture_option):
            option.setFont(Theme.POPPINS_REGULAR_14)
            option.setStyleSheet(radio_bt_style)
            option.setAutoExclusive(False)
            category_parts.addWidget(option)

        category_layout.addLayout(category_parts)

        # category 2
        category_parts = QVBoxLayout()
        self.collectibles_option = QRadioButton("Collectibles")
        self.dryFood_option = QRadioButton("Dry Food")
        self.chemicals_option = QRadioButton("Chemicals")
        self.others_option = QRadioButton("Others")

        for option in (self.collectibles_option, self.dryFood_option, self.chemicals_option, self.others_option):
            option.setFont(Theme.POPPINS_REGULAR_14)
            option.setStyleSheet(radio_bt_style)
            option.setAutoExclusive(False)
            category_parts.addWidget(option)

        category_layout.addLayout(category_parts)

        self.clear_bt = QPushButton(self, text="Clear")
        self.clear_bt.setFont(Theme.POPPINS_BOLD_16)
        self.clear_bt.setGeometry(52, 718, 96, 40)
        self.clear_bt.setStyleSheet(
            f"background-color: {Theme.YELLOW}; color:white; border-radius: 5px;")

        self.make_changes_bt = QPushButton(self, text="Make Changes")
        self.make_changes_bt.setFont(Theme.POPPINS_BOLD_16)
        self.make_changes_bt.setGeometry(273, 718, 180, 40)

        self.set_enable_all(False)

        # UI
        ui = QLabel(self, text="Search Products")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(50, 39, 152, 27)
        ui.setStyleSheet(head_style)

        ui = QLabel(self, text="Search by")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(50, 115, 108, 26)
        ui.setStyleSheet(head_style)

        ui = QLabel(self)
        ui.setGeometry(50, 193, 400, 1)
        ui.setStyleSheet(line_break_top_style)

        ui = QLabel(self, text="Modify")
        ui.setFont(Theme.POPPINS_REGULAR_14)
        ui.setAlignment(Qt.AlignCenter)
        ui.setGeometry(216, 182, 68, 21)
        ui.setStyleSheet(text_over_line_style)

        ui = QLabel(self, text="Product ID")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(50, 244, 96, 27)
        ui.setStyleSheet(head_style)

        ui = QLabel(self, text="Product Name")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(263, 244, 133, 27)
        ui.setStyleSheet(head_style)

        ui = QLabel(self, text="Batch #")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(50, 321, 75, 27)
        ui.setStyleSheet(head_style)

        ui = QLabel(self, text="Quantity")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(148, 321, 82, 27)
        ui.setStyleSheet(head_style)

        ui = QLabel(self, text="Weight (Kg)")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(51, 398, 113, 27)
        ui.setStyleSheet(head_style)

        ui = QLabel(self, text="L")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(290, 398, 9, 27)
        ui.setStyleSheet(head_style)

        ui = QLabel(self, text="W")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(348, 399, 19, 27)
        ui.setStyleSheet(head_style)

        ui = QLabel(self, text="H")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(413, 399, 14, 27)
        ui.setStyleSheet(head_style)

        ui = QLabel(self, text="Low Stock Quantity")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(50, 475, 178, 27)
        ui.setStyleSheet(head_style)

        ui = QLabel(self, text="Owner ID")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(265, 475, 83, 27)
        ui.setStyleSheet(head_style)

        ui = QLabel(self, text="Category")
        ui.setFont(Theme.POPPINS_BOLD_18)
        ui.setGeometry(51, 552, 95, 27)
        ui.setStyleSheet(head_style)

    def clear_input(self):
        for le in (self.product_id_le, self.product_name_le, self.batch_id_le, self.quantity_le, self.weight_le, self.length_le, self.width_le, self.height_le, self.low_stock_quantity_le, self.owner_id_le):
            le.setText("")
        for category in (self.electrical_option, self.fashion_option, self.utensils_option, self.furniture_option, self.collectibles_option, self.dryFood_option, self.chemicals_option, self.others_option):
            category.setChecked(False)
        self.choose_location_bt.setText("Choose Location")

    def get_search_input(self) -> str:
        return self.search_product_le.text()

    def get_current_filter(self) -> str:
        return self.current_filter

    def get_modify_option(self) -> str:
        return self.current_modify

    def get_product_id(self) -> int:
        return int(self.product_id_le.text())

    def get_product_name(self) -> str:
        return self.product_name_le.text()

    def get_batch_id(self) -> int:
        return int(self.batch_id_le.text())

    def get_quantity(self) -> int:
        return int(self.quantity_le.text())

    def get_weight(self) -> int:
        return int(self.weight_le.text())

    def get_length(self) -> int:
        return int(self.length_le.text())

    def get_width(self) -> int:
        return int(self.width_le.text())

    def get_height(self) -> int:
        return int(self.height_le.text())

    def get_low_stock_quantity(self) -> int:
        return int(self.quantity_le.text())

    def get_owner_id(self) -> int:
        return int(self.owner_id_le.text())

    def get_location(self) -> str:
        locate = self.choose_location_bt.text()
        if locate == "Choose Location":
            return None
        else:
            return locate

    def set_event_search_button(self, function):
        self.search_bt.clicked.connect(function)

    def set_enable_search_button(self, boolean: bool):
        self.search_bt.setEnabled(boolean)
        self.search_bt.setStyleSheet(
            f"background-color: {Theme.YELLOW if boolean else Theme.DARK_YELLOW}; color:{'white' if bool else Theme.DARK_WHITE}; border-radius: 5px;")

    def set_event_make_change_button(self, function):
        self.make_changes_bt.clicked.connect(function)

    def set_event_clear_button(self, function):
        self.clear_bt.clicked.connect(function)

    def set_enable_make_change_button(self, boolean: bool):
        self.make_changes_bt.setEnabled(boolean)
        self.make_changes_bt.setStyleSheet(
            f"background-color: {Theme.YELLOW if boolean else Theme.DARK_YELLOW}; color:{'white' if bool else Theme.DARK_WHITE}; border-radius: 5px;")

    def set_enable_choose_location_button(self, boolean: bool):
        self.choose_location_bt.setEnabled(boolean)
        self.choose_location_bt.setStyleSheet(
            f"background-color: {Theme.YELLOW if boolean else Theme.DARK_YELLOW}; color:{'white' if bool else Theme.DARK_WHITE}; border-radius: 5px;")

    def set_event_choose_location_button(self, function):
        self.choose_location_bt.clicked.connect(function)

    def set_enable_search_input(self, boolean: bool):
        self.search_product_le.setEnabled(boolean)
        self.search_product_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_product_id(self, boolean: bool):
        self.product_id_le.setEnabled(boolean)
        self.product_id_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_product_name(self, boolean: bool):
        self.product_name_le.setEnabled(boolean)
        self.product_name_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_batch_id(self, boolean: bool):
        self.batch_id_le.setEnabled(boolean)
        self.batch_id_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_quantity(self, boolean: bool):
        self.quantity_le.setEnabled(boolean)
        self.quantity_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_weight(self, boolean: bool):
        self.weight_le.setEnabled(boolean)
        self.weight_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_length(self, boolean: bool):
        self.length_le.setEnabled(boolean)
        self.length_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_width(self, boolean: bool):
        self.width_le.setEnabled(boolean)
        self.width_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_height(self, boolean: bool):
        self.height_le.setEnabled(boolean)
        self.height_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_low_stock(self, boolean: bool):
        self.low_stock_quantity_le.setEnabled(boolean)
        self.low_stock_quantity_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_owner_id(self, boolean: bool):
        self.owner_id_le.setEnabled(boolean)
        self.owner_id_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_product_id(self, boolean: bool):
        self.product_id_le.setEnabled(boolean)
        self.product_id_le.setStyleSheet(
            f"background-color: {Theme.GREY if boolean else Theme.DARK_GREY}; color:black; border-radius: 0px;")

    def set_enable_all(self, boolean: bool):
        self.set_enable_search_input(boolean)
        self.set_enable_search_button(boolean)
        self.set_enable_product_id(boolean)
        self.set_enable_product_name(boolean)
        self.set_enable_batch_id(boolean)
        self.set_enable_quantity(boolean)
        self.set_enable_length(boolean)
        self.set_enable_width(boolean)
        self.set_enable_low_stock(boolean)
        self.set_enable_owner_id(boolean)
        self.set_enable_choose_location_button(boolean)
        self.set_enable_height(boolean)
        self.set_enable_make_change_button(boolean)
        self.set_enable_weight(boolean)

    def set_event_add_new(self, function):
        self.add_new_option.toggled.connect(function)

    def set_event_add_batch(self, function):
        self.add_batch.toggled.connect(function)

    def set_event_edit(self, function):
        self.edit_option.toggled.connect(function)

    def set_event_delete(self, function):
        self.delete_option.toggled.connect(function)

    def set_input_with_card(self, card: ProductListCard):

        product = card.get_product()
        location = card.get_current_location()
        dimension = product.get_dimension()
        owner = product.get_owner()
        categories = product.get_category_list()
        self.clear_input()

        if self.current_modify == "Add New":
            self.product_name_le.setText(str(product.get_name()))
            self.quantity_le.setText(str(location.get_batch_quantity()))
            self.weight_le.setText(str(product.get_weight()))
            self.length_le.setText(str(dimension.get_length()))
            self.width_le.setText(str(dimension.get_width()))
            self.height_le.setText(str(dimension.get_height()))
            self.low_stock_quantity_le.setText(
                str(product.get_low_stock_quantity()))
            self.owner_id_le.setText(str(owner.get_id()))
            return

        if self.current_modify == "Delete":
            self.product_id_le.setText(str(product.get_id()))
            self.batch_id_le.setText(str(location.get_batch_number()))
            return

        if self.current_modify == "Add Batch":
            self.product_id_le.setText(str(product.get_id()))
            self.quantity_le.setText(str(location.get_batch_quantity()))
            self.weight_le.setText(str(product.get_weight()))
            self.length_le.setText(str(dimension.get_length()))
            self.width_le.setText(str(dimension.get_width()))
            self.height_le.setText(str(dimension.get_height()))
            return

        if self.current_modify == "Edit":
            self.product_name_le.setText(str(product.get_name()))
            self.product_id_le.setText(str(product.get_id()))
            self.batch_id_le.setText(str(location.get_batch_number()))
            self.quantity_le.setText(str(location.get_batch_quantity()))
            self.choose_location_bt.setText(location.get_location())
            self.weight_le.setText(str(product.get_weight()))
            self.length_le.setText(str(dimension.get_length()))
            self.width_le.setText(str(dimension.get_width()))
            self.height_le.setText(str(dimension.get_height()))
            self.low_stock_quantity_le.setText(
                str(product.get_low_stock_quantity()))
            self.owner_id_le.setText(str(owner.get_id()))
            for catergory in categories:
                if(isinstance(catergory, Electronics)):
                    self.electrical_option.setChecked(True)
                elif(isinstance(catergory, Fashion)):
                    self.fashion_option.setChecked(True)
                elif(isinstance(catergory, Utensils)):
                    self.utensils_option.setChecked(True)
                elif(isinstance(catergory, Furniture)):
                    self.furniture_option.setChecked(True)
                elif(isinstance(catergory, Collectibles)):
                    self.collectibles_option.setChecked(True)
                elif(isinstance(catergory, DryFood)):
                    self.dryFood_option.setChecked(True)
                elif(isinstance(catergory, Chemicals)):
                    self.chemicals_option.setChecked(True)
                elif(isinstance(catergory, Others)):
                    self.others_option.setChecked(True)
            return

    def set_event_search_input_change(self, function):
        self.search_product_le.textChanged.connect(function)

    def set_event_filters(self, function):
        for radioBt in (self.client_name_search_option, self.product_id_search_option, self.product_name_search_option):
            radioBt.clicked.connect(function)

    def update_current_filter(self):
        self.current_filter = self.sender().text()

    def update_current_modifier(self):
        self.current_modify = self.sender().text()
        self.clear_input()
        if self.current_modify == "Add New":
            self.set_enable_add_new()
        elif self.current_modify == "Add Batch":
            self.set_enable_add_batch()
        elif self.current_modify == "Edit":
            self.set_enable_edit()
        elif self.current_modify == "Delete":
            self.set_enable_delete()

    def get_current_modify(self) -> str:
        return self.current_modify

    def set_enable_add_new(self):
        self.set_enable_product_id(False)
        self.set_enable_product_name(True)
        self.set_enable_batch_id(False)
        self.set_enable_quantity(True)
        self.set_enable_choose_location_button(True)
        self.set_enable_weight(True)
        self.set_enable_length(True)
        self.set_enable_width(True)
        self.set_enable_height(True)
        self.set_enable_low_stock(True)
        self.set_enable_owner_id(True)

    def set_enable_edit(self):
        self.set_enable_product_id(True)
        self.set_enable_product_name(True)
        self.set_enable_batch_id(True)
        self.set_enable_quantity(True)
        self.set_enable_choose_location_button(True)
        self.set_enable_weight(True)
        self.set_enable_length(True)
        self.set_enable_width(True)
        self.set_enable_height(True)
        self.set_enable_low_stock(True)
        self.set_enable_owner_id(True)

    def set_enable_add_batch(self):
        self.set_enable_product_id(True)
        self.set_enable_product_name(False)
        self.set_enable_batch_id(False)
        self.set_enable_quantity(True)
        self.set_enable_choose_location_button(True)
        self.set_enable_weight(True)
        self.set_enable_length(True)
        self.set_enable_width(True)
        self.set_enable_height(True)
        self.set_enable_low_stock(False)
        self.set_enable_owner_id(False)

    def set_enable_delete(self):
        self.set_enable_product_id(True)
        self.set_enable_product_name(False)
        self.set_enable_batch_id(True)
        self.set_enable_quantity(False)
        self.set_enable_choose_location_button(False)
        self.set_enable_weight(False)
        self.set_enable_length(False)
        self.set_enable_width(False)
        self.set_enable_height(False)
        self.set_enable_low_stock(False)
        self.set_enable_owner_id(False)

    def get_categoires(self) -> list[str]:
        categories = []
        for category in (self.electrical_option, self.fashion_option, self.utensils_option, self.furniture_option, self.collectibles_option, self.dryFood_option, self.chemicals_option, self.others_option):
            if category.isChecked():
                categories.append(category.text())
        return categories

    def change_location(self, new_location: str):
        self.choose_location_bt.setText(new_location)
