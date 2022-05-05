from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from views.theme import Theme


class ProductInputForm(QWidget):
    def __init__(self, parent=None) -> None:
        QWidget.__init__(self, parent)
        bg = QLabel(self)
        bg.setGeometry(0, 0, 500, 794)
        bg.setStyleSheet(f"background-color: white; border-radius: 25px;")

        head_style = f"background-color: transparent; color:{Theme.BLUE};"
        input_form_style = f"background-color: {Theme.GREY}; color:black; border-radius: 0px;"
        yellow_bt_style = f"background-color: {Theme.YELLOW}; color:white; border-radius: 5px;"
        line_break_top_style = "border-top: 1px solid black; background-color: none;"
        text_over_line_style = "color:black; background-color:white;"
        radio_bt_style = f"color: {Theme.BLUE};"
        # Input line edit
        self.search_product_le = QLineEdit(self)
        self.search_product_le.setFont(Theme.POPPINS_REGULAR_18)
        self.search_product_le.setGeometry(50, 66, 290, 40)
        self.search_product_le.setStyleSheet(input_form_style)

        self.product_id_le = QLineEdit(self)
        self.product_id_le.setFont(Theme.POPPINS_REGULAR_18)
        self.product_id_le.setGeometry(50, 271, 187, 40)
        self.product_id_le.setStyleSheet(input_form_style)

        self.product_name_le = QLineEdit(self)
        self.product_name_le.setFont(Theme.POPPINS_REGULAR_18)
        self.product_name_le.setGeometry(263, 271, 187, 40)
        self.product_name_le.setStyleSheet(input_form_style)

        self.batch_id_le = QLineEdit(self)
        self.batch_id_le.setFont(Theme.POPPINS_REGULAR_18)
        self.batch_id_le.setGeometry(50, 348, 90, 40)
        self.batch_id_le.setStyleSheet(input_form_style)
        self.batch_id_le.setAlignment(Qt.AlignCenter)

        self.quantity_le = QLineEdit(self)
        self.quantity_le.setFont(Theme.POPPINS_REGULAR_18)
        self.quantity_le.setGeometry(148, 348, 90, 40)
        self.quantity_le.setStyleSheet(input_form_style)
        self.quantity_le.setAlignment(Qt.AlignCenter)

        self.weight_le = QLineEdit(self)
        self.weight_le.setFont(Theme.POPPINS_REGULAR_18)
        self.weight_le.setGeometry(50, 425, 187, 40)
        self.weight_le.setStyleSheet(input_form_style)

        self.length_le = QLineEdit(self)
        self.length_le.setFont(Theme.POPPINS_REGULAR_18)
        self.length_le.setGeometry(265, 425, 60, 40)
        self.length_le.setStyleSheet(input_form_style)
        self.length_le.setAlignment(Qt.AlignCenter)

        self.width_le = QLineEdit(self)
        self.width_le.setFont(Theme.POPPINS_REGULAR_18)
        self.width_le.setGeometry(328, 425, 60, 40)
        self.width_le.setStyleSheet(input_form_style)
        self.width_le.setAlignment(Qt.AlignCenter)

        self.height_le = QLineEdit(self)
        self.height_le.setFont(Theme.POPPINS_REGULAR_18)
        self.height_le.setGeometry(390, 425, 60, 40)
        self.height_le.setStyleSheet(input_form_style)
        self.height_le.setAlignment(Qt.AlignCenter)

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

        # Modify
        option = QWidget(self)
        option.setGeometry(50, 213, 369, 22)
        option_layout = QHBoxLayout(option)
        option_layout.setContentsMargins(0, 0, 0, 0)

        self.add_new_option = QRadioButton("Add New")
        self.add_new_option.setFixedWidth(93)

        self.add_batch_option = QRadioButton("Add Batch")
        self.add_batch_option.setFixedWidth(104)

        self.edit_option = QRadioButton("Edit")
        self.edit_option.setFixedWidth(56)

        self.delete_option = QRadioButton("Delete")
        self.delete_option.setFixedWidth(75)

        for radioBt in (self.add_new_option, self.add_batch_option, self.edit_option, self.delete_option):
            radioBt.setStyleSheet(radio_bt_style)
            radioBt.setFont(Theme.POPPINS_REGULAR_14)
            option_layout.addWidget(radioBt)

        # Category
        category_box = QWidget(self)
        category_box.setGeometry(71, 588, 360, 110)
        category_layout = QHBoxLayout()
        category_box.setLayout(category_layout)
        # category_box.add

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

        self.low_stock_quantity_le = QLineEdit(self)
        self.low_stock_quantity_le.setFont(Theme.POPPINS_REGULAR_18)
        self.low_stock_quantity_le.setGeometry(50, 502, 187, 40)
        self.low_stock_quantity_le.setStyleSheet(input_form_style)

        self.owner_id_le = QLineEdit(self)
        self.owner_id_le.setFont(Theme.POPPINS_REGULAR_18)
        self.owner_id_le.setGeometry(266, 502, 187, 40)
        self.owner_id_le.setStyleSheet(input_form_style)

        # Yellow bt
        self.search_bt = QPushButton(self, text="Search")
        self.search_bt.setFont(Theme.POPPINS_REGULAR_18)
        self.search_bt.setGeometry(350, 66, 100, 40)
        self.search_bt.setStyleSheet(yellow_bt_style)

        self.choose_location_bt = QPushButton(self, text="Choose Location")
        self.choose_location_bt.setFont(Theme.POPPINS_BOLD_18)
        self.choose_location_bt.setGeometry(263, 348, 187, 40)
        self.choose_location_bt.setStyleSheet(yellow_bt_style)

        self.make_changes_bt = QPushButton(self, text="Make Changes")
        self.make_changes_bt.setFont(Theme.POPPINS_BOLD_16)
        self.make_changes_bt.setGeometry(273, 718, 180, 40)
        self.make_changes_bt.setStyleSheet(yellow_bt_style)

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

        ui = QLabel(self, text="Proudct ID")
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
