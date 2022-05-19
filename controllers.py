from abc import ABC
from data.access_level import AdminAccess, EmployeeAccess
from models import *
from PySide6.QtWidgets import QWidget
from datetime import date
from views.forms.account_view import AccountView
from views.forms.customer_list_page_view import CustomerListPageView
from views.forms.inventory_overview import InventoryOverviewView
from views.forms.login_view import LoginView
from views.forms.notifications_view import NotificationView
from views.forms.report_view import ReportView
from views.forms.site_setting_view import SiteSettingView
import views.rc_icons


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

    def __init__(self, view: QWidget, model: Model, root):
        super().__init__(view, model)
        self.view.set_login_button_listener(self.verify_login)
        self.root = root

    def verify_login(self):
        username = self.view.get_username()
        password = self.view.get_password()
        self.model.get_input(username, password)
        self.model.retrive_user(username)
        self.model.verify_login()

        if self.model.is_valid():
            self.view.hide_error_label()
            self.model.set_current_user(username)
            self.set_current_user(self.get_current_user())
            self.root.initialize_pages()
        else:
            self.view.show_error_label()

    def get_current_user(self) -> User:
        return self.model.get_current_user()

    def set_current_user(self, user: User):
        self.root.set_current_user(user)

    def clear_input_fields(self):
        self.view.clear_info()


class HomePage(Controller):
    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
        self.update_activity_logs()
        self.view.set_search_bt_listener(self.search)
        self.view.set_input_changed_listener(self.input_check)

    def search(self):
        input = self.view.get_search_input()
        filter_option = self.view.get_filter()
        self.view.clear_product_cards()
        products = self.model.search_product(input, filter_option)  # [None]
        if None not in products:
            for product in products:
                card = self.view.add_product_card(product)

                def generate(temp):
                    def quantity_check():
                        new_quantity = temp.get_new_quantity()
                        add_state = True
                        export_state = True
                        if new_quantity == 0:
                            add_state = False
                            export_state = False
                        elif new_quantity > temp.get_product().get_quantity():
                            export_state = False
                        temp.set_enable_add_bt(add_state)
                        temp.set_enable_export_bt(export_state)

                    def add():
                        new_quantity = temp.get_new_quantity()
                        self.model.add_product_quantity(
                            temp.get_product(), new_quantity)
                        temp.add_quantity(new_quantity)
                        temp.update_card()
                        temp.clear_quantity_input()
                        self.update_activity_logs()

                    def export():
                        new_quantity = temp.get_new_quantity()
                        if new_quantity == 0:
                            return
                        self.model.export_product(
                            temp.get_product(), new_quantity)
                        temp.export_quantity(new_quantity)
                        temp.update_card()
                        temp.clear_quantity_input()
                        self.update_activity_logs()
                    return (quantity_check, add, export)

                events = generate(card)
                card.set_quantity_changed_listener(events[0])
                card.set_add_bt_listener(events[1])
                card.set_export_bt_listener(events[2])

    def update_activity_logs(self):
        self.view.clear_logs()
        for log in self.model.get_activity_logs():
            self.view.add_log(log)

    def input_check(self):
        input = self.view.get_search_input()
        self.view.setEnabled_search_bt(input != "")


class CustomerPage(Controller):
    view: CustomerListPageView
    model: CustomerListModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)

        # Initial List Data
        self.__fill_customer_cards(self.model.get_all_customers())

        # Card select/unselect events
        self.view.set_unselect_event(lambda: self.view.reset_form())

        self.view.set_select_event(lambda: self.view.set_form(
            self.view.current_customer.get_customer())
        )

        # Search Button Event
        self.view.customer_form.set_search_button_listener(
            self.search_users
        )

        # Form Buttons Event
        self.view.set_add_button_listenter(self.add_customer)
        self.view.set_save_button_listener(self.edit_customer)
        self.view.set_delete_button_listener(self.delete_customer)

        # Form OnChange Event
        self.view.set_input_on_change_listener(self.validate_buttons)

    def __fill_customer_cards(self, customers: list[Customer]):
        if customers is None:
            return

        for customer in customers:
            self.view.customer_list.add_card(customer)

    def search_users(self):
        search_string = self.view.get_search_input()
        if len(search_string) == 0:
            self.view.reset_card_list()
            self.__fill_customer_cards(self.model.get_all_customers())
            return

        customers = self.model.get_customer_contains_with(search_string)
        if customers is None:
            return

        self.view.reset_card_list()
        self.__fill_customer_cards(customers)

    def add_customer(self):
        if self.view.is_card_selected() or not self.view.is_form_valid():
            return

        # Retreive user inputs
        name = self.view.get_name()
        phone = self.view.get_phone()
        email = self.view.get_email()
        packing_service = self.view.get_packing_service()
        date_joined = self.view.get_joined_date()
        duration = int(self.view.get_rental_duration())

        # Calculate Expiry Date
        day, month, year = list(map(int, date_joined.split("_")))
        date_start = date(year, month, day)
        expiry_date = self.model.calculate_expiry_date(
            date_start, duration)
        expiring_day = f"{expiry_date.day:02d}_{expiry_date.month:02d}_{expiry_date.year:02d}"

        # Initialize new customer
        new_customer = Customer(
            None,
            name,
            phone,
            email,
            packing_service,
            duration,
            date_joined,
            expiring_day,
            0
        )

        # Update page
        self.model.add_customer(new_customer)
        self.view.reset_card_list()
        self.view.reset_form()
        self.view.reset_search_input()
        self.__fill_customer_cards(self.model.get_all_customers())

    def validate_buttons(self):
        # Add Button
        if self.view.is_card_selected() or not self.view.is_form_valid():
            self.view.customer_form.set_add_button_enabled(False)
        else:
            self.view.customer_form.set_add_button_enabled(True)

        # Save Button
        if self.view.is_card_selected() and self.view.is_current_edited():
            self.view.customer_form.set_save_button_enabled(True)
        else:
            self.view.customer_form.set_save_button_enabled(False)

        # Delete Button
        if self.view.is_card_selected() and not self.view.is_current_edited():
            self.view.customer_form.set_delete_button_enabled(True)
        else:
            self.view.customer_form.set_delete_button_enabled(False)

    def edit_customer(self):
        if not (self.view.is_card_selected() and self.view.is_current_edited()):
            return

        prev_info = self.view.get_current_customer()

        date_joined = self.view.get_joined_date()
        duration = int(self.view.get_rental_duration())

        day, month, year = list(
            map(int, date_joined.split("_")))
        date_start = date(year, month, day)
        expiry_date = self.model.calculate_expiry_date(
            date_start, duration)
        expiring_day = f"{expiry_date.day:02d}_{expiry_date.month:02d}_{expiry_date.year:02d}"

        new_info = Customer(
            prev_info.get_id(),
            self.view.get_name(),
            self.view.get_phone(),
            self.view.get_email(),
            self.view.get_packing_service(),
            duration,
            date_joined,
            expiring_day,
            prev_info.get_total_payment()
        )

        self.model.save_customer_data(prev_info, new_info)
        self.__update_list()

    def delete_customer(self):
        if not self.view.is_card_selected() or self.view.is_current_edited():
            return

        current_customer = self.view.get_current_customer()
        self.model.delete_customer(current_customer)

        self.__update_list()

    def __update_list(self):
        # Update List
        self.view.reset_card_list()
        self.__fill_customer_cards(self.model.get_all_customers())


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

        if employees is None:
            return

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

        if customers is None:
            return

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
        self.view.set_customer_selected_function(
            self.fill_selected_customer_products)

    def __fill_customer_list(self):
        customers = self.model.get_customer_selection()
        for customer in customers:
            self.view.add_customer_item(
                customer.get_name(),
                self.get_customer_percent_stocked(customer.get_id()),
                customer.get_id()
            )

    def get_customer_percent_stocked(self, id: int) -> float:
        return self.model.get_product_stock(id)

    def get_products_of_customer(self, id: int) -> list[ProductItem]:
        return self.model.get_product_list_by_owner_id(id)

    def fill_selected_customer_products(self):
        self.view.clear_product_item()

        if self.view.current_customer is None:
            return

        id = self.view.current_customer.get_customer_id()
        products = self.get_products_of_customer(id)
        if products is not None:
            for product in products:
                self.view.add_product_item(product)


class ReportPage(Controller):
    view: ReportView
    model: ReportModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)
        self.quarter_reports = self.model.get_all_reports()
        self.index_limit = len(self.quarter_reports)-1
        self.report_index = 0
        self.update_dashboard(self.quarter_reports[self.report_index])
        self.load_cards()

        self.view.set_next_button_listener(self.next_quarter)
        self.view.set_back_button_listener(self.previous_quarter)
        self.view.set_export_button_listener(self.export_report)

    def update_dashboard(self, report: QuarterlyReport):
        # Update Quarter Label
        self.view.set_quarter_label(report.get_year(), report.get_quarter())

        # Update Pie Chart
        self.view.draw_pie_chart_of_selected_customer(
            "", report.get_utilized_space_percentage())

        # Update Revenue
        self.view.set_total_show_label(report.get_total_revenue())
        self.view.set_monthly_show_label(report.get_monthly_revenue())

        # Capacity Utilization
        self.view.set_capacity_show_label(
            report.get_utilized_space_percentage())

    def next_quarter(self):
        if not self.is_right_end():
            self.report_index += 1

        self.update_dashboard(self.quarter_reports[self.report_index])

    def previous_quarter(self):
        if not self.is_left_end():
            self.report_index -= 1

        self.update_dashboard(self.quarter_reports[self.report_index])

    def is_right_end(self) -> bool:
        return self.report_index == self.index_limit

    def is_left_end(self) -> bool:
        return self.report_index == 0

    def load_cards(self):
        customers = self.model.get_all_customers()
        for customer in customers:
            percentage = self.model.calculate_customer_stock_percentage(
                customer)
            self.view.add_report_card(customer, percentage)

    def export_report(self):
        file_path = self.view.save_file_to()
        self.model.generate_csv_report(file_path)


class SiteSettingPage(Controller):
    view: SiteSettingView
    model: SiteSettingsModel

    def __init__(self, view: QWidget, model: Model):
        super().__init__(view, model)

        # fill all of Shelves
        self.__fill_strorage_shelf(self.model.get_all_shelves())

        # Set all buttons to disable
        self.set_all_button_disable()

        # Set every buttons
        self.view.set_add_button_listener(self.add_shelf)
        self.view.set_delete_button_listener(self.delete_shelf)
        self.view.set_save_button_listener(self.edit_shelf)
        self.view.set_search_listener(self.search_shelf)

        # Set change on Input
        self.view.set_input_on_change_listener(self.validate_buttons)

        # Set select and unselect Shelves
        self.view.set_unselect_event(lambda: self.view.reset_input())

        self.view.set_select_event(lambda: self.view.set_lineEdit_from_shelf(
            self.view.get_selected_shelf())
        )

        # Thank to Kris Code many of them he was implement it krub :)

    def set_all_button_disable(self):
        self.view.set_add_button_enabled(False)
        self.view.set_delete_button_enabled(False)
        self.view.set_save_button_enabled(False)

    def __fill_strorage_shelf(self, shelves: list[StorageShelf]):
        if shelves is None:
            return

        for shelf in shelves:
            self.view.add_shelf(shelf)

    def search_shelf(self):
        if not self.view.is_search_lineEdit_filled():
            return
        search_shelves = self.model.get_shelves_contains_with(
            self.view.get_search_LineEdit())
        self.view.reset_site_setting_view()
        self.view.reset_input()
        self.__fill_strorage_shelf(search_shelves)

    def add_shelf(self):
        if self.view.is_card_selected() or not self.view.is_no_empty_lineEdit():
            return

        label = self.view.get_shelf_LineEdit()
        max_weight = self.view.get_max_weight_LineEdit()
        length = self.view.get_length_LineEdit()
        width = self.view.get_width_LineEdit()
        height = self.view.get_height_LineEdit()
        row = self.view.get_row_LineEdit()
        column = self.view.get_column_LineEdit()

        self.model.add_shelf(label, max_weight, length,
                             width, height, row, column)

        self.__update_list()

    def delete_shelf(self):
        if not self.view.is_card_selected():
            return

        self.model.delete_shelf(self.view.get_selected_shelf())
        self.view.reset_input()

        self.__update_list()

    def edit_shelf(self):
        if not self.view.is_card_selected() or not self.view.is_current_edited():
            return

        label = self.view.get_shelf_LineEdit()
        max_weight = self.view.get_max_weight_LineEdit()
        length = self.view.get_length_LineEdit()
        width = self.view.get_width_LineEdit()
        height = self.view.get_height_LineEdit()
        row = self.view.get_row_LineEdit()
        column = self.view.get_column_LineEdit()

        edited_shelf = StorageShelf(
            label, max_weight, length, width, height, row, column)
        self.model.update_shelf(self.view.get_selected_shelf(), edited_shelf)
        self.view.reset_input()
        self.__update_list()

    def validate_buttons(self):
        # Add Button
        if self.view.is_card_selected() or not self.view.is_no_empty_lineEdit():
            self.view.set_add_button_enabled(False)
        else:
            self.view.set_add_button_enabled(True)

        # Save Button
        if self.view.is_card_selected() and self.view.is_current_edited():
            self.view.set_save_button_enabled(True)
        else:
            self.view.set_save_button_enabled(False)

        # Delete Button
        if self.view.is_card_selected():
            self.view.set_delete_button_enabled(True)
        else:
            self.view.set_delete_button_enabled(False)

    def __update_list(self):
        self.view.reset_site_setting_view()
        self.__fill_strorage_shelf(self.model.get_all_shelves())
