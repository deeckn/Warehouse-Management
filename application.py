import sys
from PySide6.QtWidgets import QApplication
from controllers import *
from models import *
from views.forms.home_view import HomePageView
from views.forms.login_view import LoginView


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.current_user = AppDAO.get_dao("user").get_user_by_id(1)

        self.login_page = LoginPage(
            LoginView(),
            LoginModel()
        )

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

        self.current_controller = self.report_page

    def start(self):
        self.current_controller.open_page()
        sys.exit(self.app.exec())
