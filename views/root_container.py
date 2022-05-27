from views.forms.main_app_view import MainAppView
from views.forms.admin_app_view import AdminAppView
from views.forms.login_view import LoginView
from PySide6.QtWidgets import QStackedWidget, QWidget

import views.rc_icons


class RootContainer(QStackedWidget):
    def __init__(self):
        QStackedWidget.__init__(self, None)
        self.setFixedSize(1920, 1080)
        self.setWindowTitle("GEB-ARAI-DEE")
        self.login_Page = LoginView()
        self.main_app_view = MainAppView()
        self.admin_app_view = AdminAppView()

        self.main_app_view.set_logout_bt_listener(self.move_to_login)
        self.main_app_view.set_admin_bt_listener(self.move_main_to_admin)
        self.admin_app_view.set_logout_bt_listener(self.move_to_login)
        self.admin_app_view.set_main_button_listener(self.move_admin_to_main)

        self.addWidget(self.login_Page)
        self.addWidget(self.main_app_view)
        self.addWidget(self.admin_app_view)

    # Move

    def reset_admin_and_main(self):
        self.main_app_view.reset()
        self.admin_app_view.reset()

    def move_to_login(self):
        self.reset_admin_and_main()
        self.setCurrentIndex(0)

    def move_login_to_main(self):
        self.setCurrentIndex(1)

    def move_login_to_admin(self):
        self.setCurrentIndex(2)

    def move_admin_to_main(self):
        self.setCurrentIndex(1)

    def move_main_to_admin(self):
        self.setCurrentIndex(2)
