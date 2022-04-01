from abc import ABC
from data.access_level import AdminAccess, EmployeeAccess
from views.forms.account_view import AccountView
from views.forms.inventory_overview import InventoryOverviewView
from views.forms.login_view import LoginView
from models import *
from PySide6.QtWidgets import QWidget
from views.forms.notifications_view import NotificationView


class Controller(ABC):
    view: QWidget
    model: Model

    def __init__(self, view: QWidget, model: Model):
        self.view = view
        self.model = model

    def open_page(self):
        self.view.show()


class LoginPage(Controller):
    view: LoginView
    model: LoginModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
        self.view.set_login_button_listener(self.verify_login)

    def verify_login(self):
        username = self.view.get_username()
        password = self.view.get_password()
        self.model.get_input(username, password)
        self.model.retrive_user(username)
        self.model.verify_login()

        if self.model.is_valid():
            self.view.hide_error_label()
            user_access = self.model.get_current_user().get_access_level()
            if isinstance(user_access, AdminAccess):
                print("Open Admin Page")
            else:
                print("Open Employee Page")
            self.model.set_current_user(username)
        else:
            self.view.show_error_label()

    def get_current_user(self) -> User:
        return self.model.get_current_user()


class HomePage(Controller):
    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)


class AccountPage(Controller):
    view: AccountView
    model: AccountModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
        self.fill_user_cards()

        self.view.set_create_account_button_listener(self.create_account)

        self.view.set_create_text_changed_listener(lambda:
                                                   self.update_create_username_field("create"))

        self.view.set_edit_text_change_listener(lambda:
                                                self.update_create_username_field("edit"))

        self.view.set_card_selected_listener(self.fill_user_info)

        self.view.set_save_changes_button_listener(self.update_user_info)

        self.view.set_delete_button_listener(self.delete_account)

    def fill_user_cards(self):
        """Retreives a list of user and display as cards"""
        employees = self.model.get_employee_accounts()
        for user in employees:
            self.view.add_employee_card(user)

    def update_user_cards(self):
        self.view.clear_employee_list()
        self.fill_user_cards()

    def create_account(self):
        """Creates a new account based on the user input"""
        first_name = self.view.get_first_name_input()
        last_name = self.view.get_last_name_input()
        username = self.model.generate_username(first_name, last_name)
        password = self.view.get_password_input()
        pass_confirm = self.view.get_password_confirm_input()
        access = AdminAccess() if self.view.get_create_admin_status() else EmployeeAccess()

        new_user = User(
            None,
            first_name,
            last_name,
            username,
            password,
            access
        )

        if self.model.verify_create_password(password, pass_confirm):
            self.model.create_new_account(new_user)
            self.view.reset_create_account_inputs()
            self.update_user_cards()
            self.view.reset_admin_password()
        else:
            print("Invalid password confirmation")

    def update_create_username_field(self, section: str):
        """Automatically updates the username label in the create account section"""
        if section == "create":
            first_name = self.view.get_first_name_input()
            last_name = self.view.get_last_name_input()
            username = self.model.generate_username(first_name, last_name)

            if username != ".":
                self.view.set_username_label(username)
            else:
                self.view.set_username_label("")

        elif section == "edit":
            first_name = self.view.get_first_name_edit()
            last_name = self.view.get_last_name_edit()
            username = self.model.generate_username(first_name, last_name)

            if username != ".":
                self.view.set_username_edit(username)
            else:
                self.view.set_username_edit("")
        else:
            return

    def fill_user_info(self):
        """Fills the edit user section with information based on the selected card"""
        current_user: User = self.view.get_selected_account()
        self.view.set_first_name_edit(current_user.get_first_name())
        self.view.set_last_name_edit(current_user.get_last_name())
        self.view.set_username_edit(current_user.get_username())

    def update_user_info(self):
        """Updates user data if changes occur"""
        current_user = self.view.get_selected_account()
        first_name = self.view.get_first_name_edit()
        last_name = self.view.get_last_name_edit()
        username = self.model.generate_username(first_name, last_name)
        password = self.view.get_change_password()

        new_info = User(
            current_user.get_id(),
            first_name,
            last_name,
            username,
            password,
            current_user.get_access_level()
        )

        admin_confirmation = self.view.get_admin_password()
        if self.model.admin_confirmation(admin_confirmation):
            self.model.update_user_info(current_user, new_info)
            self.update_user_cards()
            self.view.reset_admin_password()
        else:
            print("Invalid admin password")

    def delete_account(self):
        """Deletes the selected account"""
        current_user: User = self.view.get_selected_account()
        admin_confirmation = self.view.get_admin_password()
        if self.model.admin_confirmation(admin_confirmation):
            self.model.delete_user_account(current_user)
            self.update_user_cards()
            self.view.reset_edit_account_inputs()
        else:
            print("Invalid admin password")


class NotificationPage(Controller):
    view: NotificationView
    model: NotificationModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
        self.__load_data()

    def __load_data(self):
        products = self.model.get_low_stock_products()
        for product in products:
            self.view.add_event_card(
                "low_stock",
                f"Product ID: {product.get_id()} | Quantity: {product.get_quantity()}",
                product.get_owner().get_name(),
                str(product.get_owner().get_id())
            )

        customers = self.model.get_contract_ending_customers()
        for customer in customers:
            ending_days = self.model.date_difference(customer)
            self.view.add_event_card(
                "contract_end",
                f"Contract over in {ending_days} days",
                customer.get_name(),
                str(customer.get_id())
            )

class InventoryOverviewPage(Controller):
    view: InventoryOverviewView
    model: InventoryOverviewModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
        self.__fill_customer_list()
        self.view.set_customer_selected_function(self.fill_selected_customer_products)
        
    def __fill_customer_list(self):
        self.customer = self.model.get_customer_selection()
        for i in self.customer:
            self.view.add_customer_item(i.get_name(), self.get_customer_percent_stocked(i.get_id()), i.get_id())
    
    def get_customer_percent_stocked(self, id: int)->float:
        return self.model.get_product_stock(id)

    def get_products_of_customer(self, id: int) -> list[ProductItem]:
        return self.model.get_product_list_by_owner_id(id)

    def fill_selected_customer_products(self):
        self.view.clear_product_item()
        if(self.view.current_customer != None):
            id = self.view.current_customer.get_customer_id()
            products = self.get_products_of_customer(id)
            if(products is not None):
                for product in products:
                    self.view.add_product_item(product)