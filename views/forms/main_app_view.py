from views.forms.base_view import BaseView
from views.forms.product_list_page_view import ProductListPageView
from views.items.side_menu_item import SideMenuItem


class MainAppView(BaseView):
    def __init__(self, pages: dict):
        super().__init__()
        self.home_bt = SideMenuItem("home", "HOME")
        self.customer_bt = SideMenuItem("user", "CUSTOMER LIST")
        self.product_bt = SideMenuItem("product", "PRODUCT LIST")
        self.notifications_bt = SideMenuItem("notification", "NOTIFICATIONS")
        self.admin_bt = SideMenuItem("goto", "ENTER ADMIN APP")

        for bt in (self.home_bt, self.customer_bt, self.product_bt, self.notifications_bt, self.admin_bt):
            self.add_side_menu_bt(bt)
        self.add_spacer_side_menu()

        self.current_bt = self.home_bt
        self.home_bt.click()
        self.hide_admin_bt()

        self.home_page = pages["home"]
        self.add_page(self.home_page.view)

        self.customer_list_page = pages["customer"]
        self.add_page(self.customer_list_page.view)

        self.product_list_page = pages["product"]
        self.add_page(self.product_list_page.view)

        self.noti_page = pages["notification"]
        self.add_page(self.noti_page.view)

        # Controller
        self.home_bt.set_function(self.move_home)
        self.customer_bt.set_function(self.move_customer)
        self.product_bt.set_function(self.move_product)
        self.notifications_bt.set_function(self.move_notifications)

    # UI

    def hide_admin_bt(self):
        self.admin_bt.hide()

    def show_admin_bt(self):
        self.admin_bt.show()

    def reset(self):
        super().reset()
        self.current_bt = self.home_bt
        self.home_bt.click()
        self.hide_admin_bt()

    # Move
    def move_home(self):
        self.home_page.update_activity_logs()
        self.stack.setCurrentIndex(0)
        self.unclick_current_bt()
        self.current_bt = self.home_bt
        self.home_bt.click()

    def move_customer(self):
        self.stack.setCurrentIndex(1)
        self.unclick_current_bt()
        self.current_bt = self.customer_bt
        self.customer_bt.click()

    def move_product(self):
        self.stack.setCurrentIndex(2)
        self.unclick_current_bt()
        self.current_bt = self.product_bt
        self.product_bt.click()

    def move_notifications(self):
        self.stack.setCurrentIndex(3)
        self.unclick_current_bt()
        self.current_bt = self.notifications_bt
        self.notifications_bt.click()

    # Setter
    def set_admin_bt_listener(self, function):
        self.admin_bt.set_function(function)
