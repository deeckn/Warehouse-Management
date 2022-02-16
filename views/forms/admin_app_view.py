from views.forms.base_view import BaseView
from views.forms.account_view import AccountView
from views.items.side_menu_item import SideMenuItem

class AdminAppView(BaseView):
    def __init__(self):
        super().__init__()
        self.account_bt = SideMenuItem("user","ACCOUNT SETTINGS")
        self.site_bt = SideMenuItem("fix", "SITE SETTINGS")
        self.overview_bt = SideMenuItem("files", "INVENTORY OVERVIEW")
        self.report_bt = SideMenuItem("docs", "VIEW REPORT")
        self.main_bt = SideMenuItem("goto", "ENTER MAIN APP")
        

        for bt in (self.account_bt, self.site_bt, self.overview_bt, self.report_bt, self.main_bt):
            self.add_side_menu_bt(bt)
        self.add_spacer_side_menu()

        self.current_bt = self.account_bt
        self.account_bt.click()      

        # Set method
        self.account_bt.set_function(self.move_account)
        self.site_bt.set_function(self.move_site)
        self.overview_bt.set_function(self.move_overview)
        self.report_bt.set_function(self.move_report)

        self.account_page = AccountView()
        self.add_page(self.account_page)

    # Setter
    def set_main_button_listener(self, function):
        self.main_bt.set_function(function)
      
    # UI
    def reset(self):
        super().reset()
        self.current_bt = self.account_bt
        self.account_bt.click()      

    # Move
    def move_account(self):
        self.stack.setCurrentIndex(0)
        self.unclick_current_bt()
        self.current_bt = self.account_bt
        self.account_bt.click()
        
    def move_site(self):
        self.stack.setCurrentIndex(1)
        self.unclick_current_bt()
        self.current_bt = self.site_bt
        self.site_bt.click()

    def move_overview(self):
        self.stack.setCurrentIndex(2)
        self.unclick_current_bt()
        self.current_bt = self.overview_bt
        self.overview_bt.click()

    def move_report(self):
        self.stack.setCurrentIndex(3)
        self.unclick_current_bt()
        self.current_bt = self.report_bt
        self.report_bt.click()