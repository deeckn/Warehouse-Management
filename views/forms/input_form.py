from PySide6.QtWidgets import QWidget, QPushButton, QLabel
from views.theme import Theme


class InputForm(QWidget):
    def __init__(self, parent=None) -> None:
        QWidget.__init__(self, parent)

        bg = QLabel(self)
        bg.setGeometry(0, 0, 500, 794)
        bg.setStyleSheet(f"background-color: white; border-radius: 25px")

        self.delete_button = QPushButton("DELETE", self)
        self.delete_button.setGeometry(0, 732, 167, 65)
        self.delete_button.setObjectName("delete_btn")

        self.save_button = QPushButton("SAVE", self)
        self.save_button.setGeometry(167, 732, 166, 65)
        self.save_button.setObjectName("save_btn")

        self.add_button = QPushButton("ADD", self)
        self.add_button.setGeometry(333, 732, 167, 65)
        self.add_button.setObjectName("add_btn")

        self.set_delete_button_Enabled(False)
        self.set_save_button_Enabled(False)
        self.set_add_button_Enabled(False)

        for bt in (self.save_button, self.delete_button, self.add_button):
            bt.setFont(Theme.POPPINS_BOLD_24)

    def set_add_button_Enabled(self, boolean):
        style = f"background-color:  {Theme.GREEN}; color: white; border-bottom-right-radius: 23px;" if boolean else f"background-color:  {Theme.LIGHTER_DARK_GREEN}; color: {Theme.DARK_WHITE}; border-bottom-right-radius: 23px;"
        self.add_button.setStyleSheet(style)
        self.add_button.setEnabled(boolean)

    def set_delete_button_Enabled(self, boolean):
        style = f"background-color: {Theme.RED}; color: white;border-bottom-left-radius: 23px;" if boolean else f"background-color: {Theme.DARK_RED}; color: {Theme.DARK_WHITE}; border-bottom-left-radius: 23px;"
        self.delete_button.setStyleSheet(style)
        self.delete_button.setEnabled(boolean)

    def set_save_button_Enabled(self, boolean):
        style = f"background-color:  {Theme.YELLOW}; color: white; border-radius: none;" if boolean else f"background-color: {Theme.DARK_YELLOW}; color: {Theme.DARK_WHITE}; border: none;"
        self.save_button.setStyleSheet(style)
        self.save_button.setEnabled(boolean)
