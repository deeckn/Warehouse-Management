from forms.baseView import Base_View
from forms.loginPage import Login_Page
from PySide6.QtWidgets import (QStackedWidget)

class MyView(QStackedWidget):
    def __init__(self):
        QStackedWidget.__init__(self ,None)
        self.setFixedSize(1920,1080)
        self.setStyleSheet("background-color: #1A374D")
        self.setWindowTitle("GEB-ARAI-DEE")
        self.login_Page = Login_Page()
        self.addWidget(self.login_Page) 
        self.login_Page.set_login_button_listener(self.move_to_admin) # Tester
        self.base_View = Base_View() # Base View
        self.base_View.set_logout_bt_events(self.move_to_login_page)
        self.addWidget(self.base_View) 

    # Move
    def move_to_login_page(self):
        self.login_Page.clear_info()
        self.base_View.clear_side_menu()
        self.setCurrentIndex(0)

    def move_to_main(self):
        self.setCurrentIndex(1)
        self.base_View.clear_side_menu()
        self.base_View.set_up_main() 
    
    def move_to_admin(self):
        self.setCurrentIndex(1)
        self.base_View.clear_side_menu()
        self.base_View.set_up_admin()
        self.base_View.set_function_bar_bt(4,self.move_to_main_admin)

    def move_to_main_admin(self):
        self.base_View.clear_side_menu()
        self.setCurrentIndex(1)
        self.base_View.set_up_main("admin")
        self.base_View.set_function_bar_bt(4,self.move_to_admin)

    # Setter
    def set_user_label(self, username:str):
        self.base_View.set_user_label(username)
    
    def set_function_login_bt(self, function):
        self.login_Page.set_login_button_listener(function)
