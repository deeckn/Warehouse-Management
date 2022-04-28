import sys
from PySide6.QtWidgets import QApplication
from controllers import *
from models import *
from views.forms.home_view import HomePageView
from views.forms.login_view import LoginView


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.current_user = None

        # Login Page
        self.login_page = LoginPage(
            LoginView(),
            LoginModel(),
            self
        )

        # User pages
        self.home_page = None
        self.customer_page = None
        self.notification_page = None

        # Admin Pages
        self.account_page = None
        self.inventory_page = None
        self.report_page = None

    def initialize_pages(self):
        """Initial pages triggered by the login page"""
        if self.current_user is None:
            return

        self.customer_page = CustomerPage(
            CustomerListPageView(),
            CustomerListModel(self.current_user)
        )

        self.account_page = AccountPage(
            AccountView(),
            AccountModel(self.current_user)
        )

        self.home_page = HomePage(
            HomePageView(),
            HomeModel(self.current_user)
        )

        self.notification_page = NotificationPage(
            NotificationView(),
            NotificationModel()
        )

        self.inventory_page = InventoryOverviewPage(
            InventoryOverviewView(),
            InventoryOverviewModel()
        )

        self.report_page = ReportPage(
            ReportView(),
            ReportModel(self.current_user)
        )

    def start(self):
        self.login_page.open_page()
        sys.exit(self.app.exec())

    def set_current_user(self, user: User):
        self.current_user = user
