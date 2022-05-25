from controllers import *
from models import *
from views.forms.admin_app_view import AdminAppView
from views.forms.home_view import HomePageView
from views.forms.login_view import LoginView
from views.forms.main_app_view import MainAppView
from PySide6.QtWidgets import QStackedWidget


class Application(QStackedWidget):
    def __init__(self):
        QStackedWidget.__init__(self, None)
        self.setFixedSize(1920, 1080)
        self.setWindowTitle("GEB-ARAI-DEE")

        # Current User
        self.current_user = None

        # Login Page
        self.login_page = LoginPage(
            LoginView(),
            LoginModel(),
            self
        )
        self.addWidget(self.login_page.view)

        # Employee main application
        self.main_app_view = None

        # Administrative functionalities
        self.admin_app_view = None

        # User pages
        self.home_page = None
        self.customer_page = None
        self.notification_page = None
        self.product_page = None

        # Admin Pages
        self.account_page = None
        self.inventory_page = None
        self.report_page = None

    def initialize_pages(self):
        """Initial pages triggered by the login page"""
        if self.current_user is None:
            return

        self.home_page = HomePage(
            HomePageView(),
            HomeModel(self.current_user)
        )

        self.customer_page = CustomerPage(
            CustomerListPageView(),
            CustomerListModel(self.current_user)
        )

        self.notification_page = NotificationPage(
            NotificationView(),
            NotificationModel()
        )

        self.product_page = ProductPage(
            ProductListPageView(),
            ProductListModel(self.current_user)
        )

        if self.current_user.get_access_level() == "admin":
            self.account_page = AccountPage(
                AccountView(),
                AccountModel(self.current_user)
            )

            self.site_setting_page = SiteSettingPage(
                SiteSettingView(),
                SiteSettingsModel(self.current_user)
            )

            self.inventory_page = InventoryOverviewPage(
                InventoryOverviewView(),
                InventoryOverviewModel()
            )

            self.report_page = ReportPage(
                ReportView(),
                ReportModel(self.current_user)
            )

        # Application Path based on AccessLevel
        if self.main_app_view is None:
            self.main_app_setup()

        if self.current_user.get_access_level() == "admin":
            if self.admin_app_view is None:
                self.admin_app_setup()
            self.move_login_to_admin()
        else:
            self.move_admin_to_main()

    def main_app_setup(self):
        """Set up the main application"""
        self.main_app_view = MainAppView({
            "home": self.home_page,
            "customer": self.customer_page,
            "product": self.product_page,
            "notification": self.notification_page,
        })

        self.main_app_view.set_admin_bt_listener(self.move_main_to_admin)

        if self.current_user.get_access_level() == "admin":
            self.main_app_view.show_admin_bt()
        else:
            self.main_app_view.hide_admin_bt()

        self.main_app_view.set_user_label(self.current_user.get_username())
        self.main_app_view.set_logout_bt_listener(self.move_to_login)
        self.addWidget(self.main_app_view)

    def admin_app_setup(self):
        """Set up the admin section of the application"""
        self.admin_app_view = AdminAppView({
            "account": self.account_page,
            "site": self.site_setting_page,
            "inventory": self.inventory_page,
            "report": self.report_page
        })
        self.admin_app_view.set_user_label(self.current_user.get_username())
        self.admin_app_view.set_main_button_listener(self.move_admin_to_main)
        self.admin_app_view.set_logout_bt_listener(self.move_to_login)
        self.addWidget(self.admin_app_view)

    def update_user_label(self, username: str):
        if self.main_app_view is not None:
            self.main_app_view.set_user_label(username)

        if self.admin_app_view is not None:
            self.admin_app_view.set_user_label(username)

    # Move Methods
    def reset_admin_and_main(self):
        self.main_app_view.reset()
        if self.admin_app_view is not None:
            self.admin_app_view.reset()

    def move_to_login(self):
        self.current_user = None
        self.login_page.clear_input_fields()
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

    # Driver Method
    def start(self):
        self.showFullScreen()

    def set_current_user(self, user: User):
        """Set current user by the login page"""
        self.current_user = user
