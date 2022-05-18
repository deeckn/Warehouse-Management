from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont, QMouseEvent
from data.orm.schema import User
from views.theme import Theme


class EmployeeCardItem(QWidget):
    def __init__(self, parent, employee: User):
        QWidget.__init__(self, parent)
        self.parent_widget = parent
        self.current_employee = employee

        self.setFixedSize(340, 170)
        self.setStyleSheet(f"""
            color: black;
            background-color: {Theme.GHOST_WHITE};
            padding-left: 20px;
            margin: 0px 20px 15px 35px;
            border-radius: 10px;
        """)

        font = QFont("Poppins")
        font.setPixelSize(18)

        self.card = QLabel(self)
        self.card.setFixedSize(340, 170)
        self.card.setFont(font)
        self.__set_card_info()

    def __set_card_info(self):
        accessLevel = ""
        if self.current_employee.get_access_level() == "a":
            accessLevel = "Admin"
        else:
            accessLevel = "Employee"

        text = "First Name: " + self.current_employee.get_first_name() + "\nLast Name: " + \
            self.current_employee.get_last_name() + "\nUsername: " + self.current_employee.get_username() + \
            "\nAccess Level: " + accessLevel

        self.card.setText(text)

    def get_current_employee(self) -> User:
        """Returns the User data represented by this Card UI"""
        return self.current_employee

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.parent_widget.previous_card.setStyleSheet(f"""
            color: black; 
            background-color: {Theme.GHOST_WHITE}; 
            padding-left: 20px; 
            margin: 0px 20px 15px 35px; 
            border-radius: 10px;
        """)

        self.parent_widget.current_card = self
        self.setStyleSheet(f"""
            color: black; 
            background-color: {Theme.GHOST_WHITE}; 
            padding-left: 20px; 
            margin: 0px 20px 15px 35px; 
            border-radius: 10px; 
            border: 3px solid #FDCB6E;
        """)
        self.parent_widget.previous_card = self.parent_widget.current_card
        self.parent_widget.card_selected_function()
